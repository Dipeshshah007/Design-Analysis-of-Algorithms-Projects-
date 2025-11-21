# Design-Analysis-of-Algorithms-Projects-
Project 3 - Dynamic Programming and DFS/BFS Problems

Problem Statement:

Pseudo-polynomial Partition
Given a set consisting of n integers [a1, a2, … an], you want to partition into two parts so that the sum of the two parts is equal.  Suppose s =  a1 + a2 … + an. The time complexity of your algorithm should be O(ns) or better.  [Note: Due to the presence of the term s in the time complexity, such an algorithm is called pseudo polynomial algorithm.]

# 📊 Theoretical Analysis

Final Time Complexity: T(n) = O(nS)

# ⚙️ How to Run the Program

1. Clone the Repository

   git clone https://github.com/Dipeshshah007/Design-Analysis-of-Algorithms-Projects-.git
   cd Design-Analysis-of-Algorithms-Projects-

2. Install Dependencies

   Make sure you have Python installed (>=3.8). Install required libraries:
   pip install numpy
   pip install pandas
   pip install matplotlib

3. Run the Program

   python project3.py

4. Output

a. Prints a table of experimental runtime vs theoretical runtime.
b. Plots a graph comparing experimental and theoretical results.

5. 📄 Files Included

project3.py → Python code for running experiments.
README.md → Instructions to set up and run the project.


________________________________________________________________________________________________________________________________________________________


# Design-Analysis-of-Algorithms-Projects-
Project 2 - Divide & Conquer, Greedy

Problem Statement:

Option 0: Quick select, deterministic (median of medians method)

# 📊 Theoretical Analysis

Final Time Complexity: T(n) = O(n)

# ⚙️ How to Run the Program

1. Clone the Repository

   git clone https://github.com/Dipeshshah007/Design-Analysis-of-Algorithms-Projects-.git
   cd Design-Analysis-of-Algorithms-Projects-

2. Install Dependencies

   Make sure you have Python installed (>=3.8). Install required libraries:
   pip install numpy
   pip install matplotlib

3. Run the Program

   python Deterministic Quickselect.py

4. Output

a. Prints a table of experimental runtime vs theoretical runtime.
b. Plots a graph comparing experimental and theoretical results.

5. 📄 Files Included

Deterministic Quickselect.py → Python code for running experiments.
README.md → Instructions to set up and run the project.


________________________________________________________________________________________________________________________________________________________


# Design-Analysis-of-Algorithms-Projects-
Project 1 - Asymptotic Analysis

Analyze the following pseudocode to determine its time complexity and validate it experimentally:

int j = 2;
while (j < n) {
    int k = j;
    while (k < n) {
        Sum += a[j] * b[k];
        k = k * k;
    }
    j = 2 * j;
}

# 📊 Theoretical Analysis

Outer loop executes O(log n) times.

Inner loop executes O(log log n) times.

Final Time Complexity: T(n) = O(log n * log log n)

# ⚙️ How to Run the Program

1. Clone the Repository

   git clone https://github.com/Dipeshshah007/Design-Analysis-of-Algorithms-Projects-.git
   cd Design-Analysis-of-Algorithms-Projects-

2. Install Dependencies

   Make sure you have Python installed (>=3.8). Install required libraries:
   pip install numpy
   pip install matplotlib

3. Run the Program

   python Solution 1.py

4. Output

a. Prints a table of experimental runtime vs theoretical runtime.
b. Plots a graph comparing experimental and theoretical results.

5. 📄 Files Included

Solution 1.py → Python code for running experiments.
README.md → Instructions to set up and run the project.

