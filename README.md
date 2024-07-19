
# Activity Selection Problem

## Overview
This repository contains the solution to the Activity Selection Problem using both Greedy and Dynamic Programming approaches. The Activity Selection Problem is a classic optimization problem that involves selecting the maximum number of non-overlapping activities from a given set.

## Table of Contents
- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [Greedy Algorithm](#greedy-algorithm)
  - [Dynamic Programming Algorithm](#dynamic-programming-algorithm)
- [Implementation](#implementation)
- [Performance Analysis](#performance-analysis)
- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Code](#running-the-code)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Activity Selection Problem requires selecting the maximum number of non-overlapping activities. Each activity is defined by a start time and an end time, and the objective is to maximize the number of activities that can be attended without overlap.

## Algorithms

### Greedy Algorithm
The greedy algorithm selects the next activity that finishes the earliest and is compatible with the previously selected activities.

**Steps:**
1. Sort activities by their finish times in ascending order.
2. Select the first activity.
3. For each subsequent activity, if its start time is greater than or equal to the finish time of the last selected activity, select it.

### Dynamic Programming Algorithm
The dynamic programming approach considers all possible combinations of activities to ensure that the maximum number of non-overlapping activities is selected.

**Steps:**
1. Sort activities by their finish times in ascending order.
2. Create a table to store solutions to subproblems.
3. Use a recursive relation to fill the table by including or excluding each activity.

## Implementation
This repository includes the implementation of both the Greedy and Dynamic Programming algorithms in Python.

- **greedy_activity_selection.py**: Contains the Greedy Algorithm.
- **dp_activity_selection.py**: Contains the Dynamic Programming Algorithm.

## Performance Analysis
The performance of both algorithms is compared based on time and space complexity:
- **Greedy Algorithm**: \(O(n \log n)\) time complexity due to sorting, \(O(n)\) space complexity.
- **Dynamic Programming Algorithm**: \(O(n^2)\) time complexity due to nested loops, \(O(n)\) space complexity.

## Usage

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/bonifeso/GREEDY-ALGORITHM-FOR-ACTIVITY-SELECTION-PROBLEM.git
   cd activity-selection-problem
   ```

### Running the Code

#### Greedy Algorithm
Run the greedy algorithm script:
```bash
python greedy_activity_selection.py
```

#### Dynamic Programming Algorithm
Run the dynamic programming script:
```bash
python dp_activity_selection.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.


