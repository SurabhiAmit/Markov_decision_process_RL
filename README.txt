Project description:

Application of planning algorithms of Value Iteration, Policy Iteration and Reinforcement Learning algorithm of Q-Learning on Markov Decision Processes and comparison of the performances. The variation in VI and PI performances with the size of the MDP is also analyzed.Various exploration strategies are also tried on Q-learning.

The following methodology and steps were used for both MDPs in Jython 2.7 and Windows 10 machine. 
BURLAP was used for implementation and the MDPs used are 4*4 and 20*20 grid-worlds.

Code:-
The parent folder is project_code and it consists of the following folders:
1. Solution folder that contains the python files for this assignment and the csv files used for plotting
2. BURLAP that contains the source code of BURLAP
3. gridworld.html which can be used to create grid-worlds with varying shapes and reward structures using an internet browser.
4. .project and .pydevproject files used for assignment implementation

Solution folder has the following python files:
1. easyGW.py that applies Policy Iteration, Value Iteration and Q-learning on MDP-1 and saves the results in csv files generated inside Solution directory.
2. hardGW.py that applies Policy Iteration, Value Iteration and Q-learning on MDP-2 and saves the results in csv files generated inside Solution directory.
3. explore_easyGW.py that uses various exploration strategies for Q-learning on MDP-1. The different strategies are commented and the required strategy can be uncommented and code run to obtain relevant results in the form of .csv files inside Solution directory. 
4. explore_hardGW.py that uses various exploration strategies for Q-learning on MDP-2. The different strategies are commented and the required strategy can be uncommented and code run to obtain relevant results in the form of .csv files inside Solution directory. 
5. hard_Q_convergence.py runs the Q-learning code for 501000 iterations on MDP-1 to check for convergence. The results are stored in .csv files inside Solution folder.
6. easy_Q_convergence.py runs the Q-learning code for 501000 iterations on MDP-1 to check for convergence. The results are stored in .csv files inside Solution folder.
7. varysize.py applies Policy Iteration, Value Iteration and Q-learning on MDP gridworlds of different shapes from 2*2 to 50*50 and the results are stored in .csv files in Solution directory.

The above python files also generate visualizations and .pkl files that can be used to plot the policy later, if needed. The code generating those files are commented. Please uncomment the corresponding code lines if visualization is needed. Also if .pkl files are to be stored(within Solution folder), please uncomment those code lines also. These code lines were commented so as not to populate the Solution folder with several .pkl files and not to cause memory error with several visualizations.

Other than the above mentioned python files, the Solution directory has burlap.jar which is compiled form of BURLAP library.

Other folders inside the parent directory are:
1.Easy_plot that has the .csv files used to plot the policy iteration, value iteration and Q-learning results for MDP-1.
2.Hard_plot that has the .csv files used to plot the policy iteration, value iteration and Q-learning results for MDP-2.
3.explore_easy that has sub-folders of Boltzmann, epsilon-greedy, greedy and randomPolicy, each populated with results of Q-learning for MDP-1 with different hyperparameters, used for plotting in report.
4.explore_hard that has sub-folders of Boltzmann, epsilon-greedy, greedy and randomPolicy, each populated with results of Q-learning for MDP-2 with different hyperparameters used for plotting in report.
5.varysize_plot that has the results of applying Policy Iteration, Value Iteration and Q-learning on MDP gridworlds of different shapes from 2*2 to 50*50.
6.Q_convergence that has the results of Q-learning applied on MDP-1 and MDP-2 for 501K iterations.
7.low_gamma that has the results of applying Policy Iteration, Value Iteration and Q-learning on both MDPs, using low discount factor of 0.6, instead of 0.99 used earlier.
8.other_experiments folder has 
	a. burlap jar used to run the .py files, 
	b. python files of easy2.py which applies all three algorithms on another easy MDP of size 4*4, easy3.py which applies those algorithms on another 4*4 MDP with different reward structure. 
	c. It also has hard2.py, hard3.py and hard4.py that applies the three algorithms on different large MDPs of different reward structures, in order to explore how reward structure affects the algorithmic performance.

The above  mentioned .csv files were used to plot the charts in report. The data from these files were exported to a pivot table in MS excel to create required charts and plots.

Detailed steps and instructions to run the code:

The steps are:
1. Run easyGW.py to obtain the results of Policy Iteration, Value Iteration and Q-learning on MDP-1 in .csv file. The file format is <Type_of_MDP><Algorithm Used>.csv, where type of MDP is easy and the algorithm used is Policy Iteration, Value Iteration or Q-learning. In the case of Q-learning, the hyperparameters used are also mentioned in the file name.
2. Run hardGW.py to obtain the results of Policy Iteration, Value Iteration and Q-learning on MDP-2 in .csv file. The format for the .csv file is same as that for results of easyGW.py but the type of MDP is hard. 
3. Run explore_easy.py to obtain the results for MDP-1 with Q-learning exploration strategies of Greedy-Q policy, Boltzmann-Q Policy, Epsilon greedy-Q policy and Random Policy. The results are stored in .csv files with file names beginning with "Exploration_EasyMDP".
4. Run explore_hard.py to obtain the results for MDP-2 with Q-learning exploration strategies of Greedy-Q policy, Boltzmann-Q Policy, Epsilon greedy-Q policy and Random Policy. The results are stored in .csv files with file names beginning with "Exploration_HardMDP".
5. Run varysize.py to obtain the results of applying Policy Iteration, Value Iteration and Q-learning on simple MDPs of different sizes and the results are stored in .csv files with names "size <Algorithm used>.csv".
6. Run hard_Q_convergence.py to obtain results till 501K iterations for MDP-2 in .csv files with file name "QL_convergence<Type of MDP><Algorithm used>.csv" where type of MDP is "Hard" and Algorithm used is "Q-learning with used hyperparameters".
7. Run easy_Q_convergence.py to obtain results till 501K iterations for MDP-1 in .csv files with file name as "QL_convergence<Type of MDP><Algorithm used>.csv" where type of MDP is "Easy" and Algorithm used is "Q-learning with used hyperparameters".

NB: All the above python files will generate visualizations and .pkl files of policy maps if the appropriate code lines are uncommented.

The following python files in other_experiments folder inside Solution directory can be run as follows:
1. Run easy2.py to obtain the results of applying Policy Iteration, Value iteration and Q-learning on a 4*4 MDP with reward structure different from MDP-1. The results will be stored within the "other_experiments" folder as .csv files with the file_name "<type of MDP>_2 <method used>.csv" where type of MDP is easy and method used can be any of the three algorithms.
2. Run easy3.py to obtain the results of applying Policy Iteration, Value iteration and Q-learning on a 4*4 MDP with reward structure different from MDP-1 and the MDP in easy2.py. The results will be stored within the "other_experiments" folder as .csv files with the file_name "<type of MDP>_3 <method used>.csv" where type of MDP is easy and method used can be any of the three algorithms.
3.Run hard2.py to obtain the results of applying Policy Iteration, Value iteration and Q-learning on a 19*20 MDP with reward structure different from MDP-2. The results will be stored within the "other_experiments" folder as .csv files with the file_name "<type of MDP>_3 <method used>.csv" where type of MDP is hard and method used can be any of the three algorithms.
4.Run hard3.py to obtain the results of applying Policy Iteration, Value iteration and Q-learning on a 20*20 MDP with reward structure different from MDP-2. The results will be stored within the "other_experiments" folder as .csv files with the file_name "<type of MDP>_4 <method used>.csv" where type of MDP is hard and method used can be any of the three algorithms.
5.Run hard4.py to obtain the results of applying Policy Iteration, Value iteration and Q-learning on a 18*20 MDP with reward structure different from MDP-2. The results will be stored within the "other_experiments" folder as .csv files with the file_name "<type of MDP>_5 <method used>.csv" where type of MDP is hard and method used can be any of the three algorithms.

NB: Similar to the python files inside the Solution folder, the python files inside "other-experiments" folder also can generate visulizations and .pkl files if the corresponding code lines are uncommented.

The .csv files have the iteration count, convergence delta, reward and runtime for each iteration for the corresponding MDP and algorithm used.

The folder structure is given below for easy reference:
	project_code(parent folder)
		1. BURLAP
		2. Solution
			a. Easy_plot
			b. explore_easy
			c. explore_hard
			d. hard_plot
			e. low_gamma
			f. other_experiments
			g. Q_convergence
			h. varysize_plot
			i. burlap.jar
			j. easy_Q_convergence.py
			k. easyGW.py
			l. explore_easyGW.py
			m. explore_hardGW.py
			n. hard_Q_convergence.py
			o. hardGW.py
			p. varysize.py		
		3. .project
		4. .pydevproject
		5. gridworld.html

		
Notes:
		
1. The .csv files in low_gamma folder are generated by running easyGW.py and hardGW.py files after changing the discount factor in those files to 0.6 from 0.99.

2. The MDPs are formulated using gridworld.html. The block-colors of MDP visualizations in report Fig.1 are set using gridworld.html. Though there is no positive reward other than the terminal reward for the used MDPs, gridworld.html has provision to allot positive rewards(in figure) for states other than the terminal state also.

3. The Q-learning for MDP2 did not show convergence within the iterations used in hardGW.py. This is the reason why hard_Q_convergence.py was created so that Q-learning can alone be run for multiple times without running value iteration and policy iteration, to check for convergence. Similarly, easy_Q_convergence.py was created for MDP-1 to run Q-learning multiple times to study its characteristics.

4. The .csv data files used to plot the graphs in report are included inside the Solution folder.