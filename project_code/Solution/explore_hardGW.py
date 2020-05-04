'''
Created on Apr 9, 2017

@author: Jon
'''
import sys

sys.path.append('./burlap.jar')
import java
from collections import defaultdict
from time import clock
from burlap.behavior.policy import Policy;
from burlap.behavior.policy import RandomPolicy;
from burlap.behavior.policy import BoltzmannQPolicy;
from burlap.behavior.policy import EpsilonGreedy;
from burlap.behavior.policy import GreedyQPolicy;
from burlap.assignment4 import BasicGridWorld;
from burlap.behavior.singleagent import EpisodeAnalysis;
from burlap.behavior.singleagent.auxiliary import StateReachability;
from burlap.behavior.singleagent.auxiliary.valuefunctionvis import ValueFunctionVisualizerGUI;
from burlap.behavior.singleagent.learning.tdmethods import QLearning;
from burlap.behavior.singleagent.planning.stochastic.policyiteration import PolicyIteration;
from burlap.behavior.singleagent.planning.stochastic.valueiteration import ValueIteration;
from burlap.behavior.valuefunction import ValueFunction;
from burlap.domain.singleagent.gridworld import GridWorldDomain;
from burlap.oomdp.core import Domain;
from burlap.oomdp.core import TerminalFunction;
from burlap.oomdp.core.states import State;
from burlap.oomdp.singleagent import RewardFunction;
from burlap.oomdp.singleagent import SADomain;
from burlap.oomdp.singleagent.environment import SimulatedEnvironment;
from burlap.oomdp.statehashing import HashableStateFactory;
from burlap.oomdp.statehashing import SimpleHashableStateFactory;
from burlap.assignment4.util import MapPrinter;
from burlap.oomdp.core import TerminalFunction;
from burlap.oomdp.core.states import State;
from burlap.oomdp.singleagent import RewardFunction;
from burlap.oomdp.singleagent.explorer import VisualExplorer;
from burlap.oomdp.visualizer import Visualizer;
from burlap.assignment4.util import BasicRewardFunction;
from burlap.assignment4.util import BasicTerminalFunction;
from burlap.assignment4.util import MapPrinter;
from burlap.oomdp.core import TerminalFunction;
from burlap.assignment4.EasyGridWorldLauncher import visualizeInitialGridWorld
from burlap.assignment4.util.AnalysisRunner import calcRewardInEpisode, simpleValueFunctionVis, getAllStates
import csv
from collections import deque
import pickle


def dumpCSV(nIter, times, rewards, steps, convergence, world, method):
    fname = 'Exploration_HardMDP{} {}.csv'.format(world, method)
    iters = range(1, nIter + 1)
    assert len(iters) == len(times)
    assert len(iters) == len(rewards)
    assert len(iters) == len(steps)
    assert len(iters) == len(convergence)
    with open(fname, 'wb') as f:
        f.write('iter,time,reward,steps,convergence\n')
        writer = csv.writer(f, delimiter=',')
        writer.writerows(zip(iters, times, rewards, steps, convergence))


def runEvals(initialState, plan, rewardL, stepL):
    r = []
    s = []
    for trial in range(evalTrials):
        ea = plan.evaluateBehavior(initialState, rf, tf, 300);
        r.append(calcRewardInEpisode(ea))
        s.append(ea.numTimeSteps())
    rewardL.append(sum(r) / float(len(r)))
    stepL.append(sum(s) / float(len(s)))


def comparePolicies(policy1, policy2):
    assert len(policy1) == len(policy1)
    diffs = 0
    for k in policy1.keys():
        if policy1[k] != policy2[k]:
            diffs += 1
    return diffs


def mapPicture(javaStrArr):
    out = []
    for row in javaStrArr:
        out.append([])
        for element in row:
            out[-1].append(str(element))
    return out


def dumpPolicyMap(javaStrArr, fname):
    pic = mapPicture(javaStrArr)
    with open(fname, 'wb') as f:
        pickle.dump(pic, f)


if __name__ == '__main__':
    world = 'Hard'
    discount = 0.99
    MAX_ITERATIONS = 500;
    NUM_INTERVALS = 500;
    evalTrials = 100;
    userMap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 0, 0, -1, -1, -1, -1, -1, -1],
               [0, 0, 0, 0, 0, 0, 0, 0, -5, -5, 0, -5, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -5, 0, 0, 0, 0, 1, 0, 0],
               [-3, -3, -5, -1, -5, -3, 0, 0, 0, 0, 0, -5, 0, -5, 0, 0, 1, 0, 0, 0],
               [0, -3, -3, -1, -3, -3, 1, 1, 0, 0, -5, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, -5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, -5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, -5, 0, 0, 1, 0, 0, 0, 0, 0, 1, -5, 0, 1, 0, 0, 0, 0, 0],
               [0, 1, -5, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, -1, -1],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, -1, -1],
               [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, -1],
               [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    n = len(userMap)
    tmp = java.lang.reflect.Array.newInstance(java.lang.Integer.TYPE, [n, n])
    for i in range(n):
        for j in range(n):
            tmp[i][j] = userMap[i][j]
    userMap = MapPrinter().mapToMatrix(tmp)
    maxX = maxY = n - 1

    gen = BasicGridWorld(userMap, maxX, maxY)
    domain = gen.generateDomain()
    initialState = gen.getExampleState(domain);

    rf = BasicRewardFunction(maxX, maxY, userMap)
    tf = BasicTerminalFunction(maxX, maxY)
    env = SimulatedEnvironment(domain, rf, tf, initialState);
    # shows starting and ending positions
    #visualizeInitialGridWorld(domain, gen, env)
    #    Print the map that is being analyzed
    print("/////{} Grid World Analysis/////\n".format(world))
    MapPrinter().printMap(MapPrinter.matrixToMap(userMap));

    hashingFactory = SimpleHashableStateFactory()
    increment = MAX_ITERATIONS / NUM_INTERVALS
    timing = defaultdict(list)
    rewards = defaultdict(list)
    steps = defaultdict(list)
    convergence = defaultdict(list)
    allStates = getAllStates(domain, rf, tf, initialState)
    # Value Iteration
    iterations = range(1, MAX_ITERATIONS + 1)

    MAX_ITERATIONS = NUM_INTERVALS = MAX_ITERATIONS * 10;
    increment = MAX_ITERATIONS / NUM_INTERVALS
    iterations = range(1, MAX_ITERATIONS + 1)
    for lr in [0.1, 0.9]:
        for qInit in [-100, 0, 100]:
            epsilon =0.1
            #for epsilon in [0.1, 0.3, 0.5]:
            last10Chg = deque([99] * 10, maxlen=10)
            Qname = 'Q-Learning L{:0.1f} q{:0.1f} E{:0.1f}'.format(lr, qInit, epsilon)
            agent = QLearning(domain, discount, hashingFactory, qInit, lr, epsilon, 300)
            # agent.setLearningRateFunction(SoftTimeInverseDecayLR(1.,0.))
            #agent.setLearningPolicy(RandomPolicy(domain))
            #agent.setLearningPolicy(GreedyQPolicy(agent))
            #agent.setLearningPolicy(BoltzmannQPolicy(agent,1E10))
            #agent.setLearningPolicy(EpsilonGreedy(agent, epsilon))
            agent.setDebugCode(0)
            print("//{} {} Iteration Analysis//".format(world, Qname))
            for nIter in iterations:
                if nIter % 50 == 0: print(nIter)
                startTime = clock()
                ea = agent.runLearningEpisode(env, 300)
                if len(timing[Qname]) > 0:
                    timing[Qname].append(timing[Qname][-1] + clock() - startTime)
                else:
                    timing[Qname].append(clock() - startTime)
                env.resetEnvironment()
                agent.initializeForPlanning(rf, tf, 1)
                p = agent.planFromState(initialState)  # run planning from our initial state
                last10Chg.append(agent.maxQChangeInLastEpisode)
                convergence[Qname].append(sum(last10Chg) / 10.)
                # evaluate the policy with one roll out visualize the trajectory
                runEvals(initialState, p, rewards[Qname], steps[Qname])
                if convergence[Qname][-1] <0.5:
                    #dumpPolicyMap(MapPrinter.printPolicyMap(allStates, p, gen.getMap()),'QL {} {} Iter {} Policy Map.pkl'.format(Qname,world,nIter))
                    break
            print("\n\n\n")
            dumpCSV(nIter, timing[Qname], rewards[Qname], steps[Qname], convergence[Qname], world, Qname)
