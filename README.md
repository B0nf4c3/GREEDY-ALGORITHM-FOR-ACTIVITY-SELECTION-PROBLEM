
# Activity Selection Problem

## Problem Statement
- The Activity Selection Problem is a classic optimization problem in computer science and operations research.   
- The goal is to select the maximum number of non-overlapping activities from a given set.  
- Each activity has a start time and an end time, and it is assumed that a person can only work on one activity at a time.

## Greedy Algorithm Approach

### Definition
- The greedy algorithm for the Activity Selection Problem is an efficient method that makes a sequence of choices, each of which looks best at the moment, to achieve an optimal solution.  
- The idea is to always pick the next activity that finishes the earliest and is compatible with the previously selected activities.

### Steps to Solve
1. **Sort activities by their finish times** in ascending order.
2. **Select the first activity** from the sorted list as it has the earliest finish time.
3. **Iterate through the remaining activities** and select an activity if its start time is greater than or equal to the finish time of the last selected activity.

### Implementation in Python

```python
def greedy_activity_selection(activities):
    # Sort activities based on finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    # The first activity always gets selected
    selected_activities = [sorted_activities[0]]
    last_finish_time = sorted_activities[0][1]
    
    for i in range(1, len(sorted_activities)):
        if sorted_activities[i][0] >= last_finish_time:
            selected_activities.append(sorted_activities[i])
            last_finish_time = sorted_activities[i][1]
    
    return selected_activities

# Example usage
activities = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9), (8, 10)]
selected = greedy_activity_selection(activities)
print("Selected activities (Greedy):", selected)
```

## Dynamic Programming Approach

### Definition
- The dynamic programming approach to the Activity Selection Problem involves considering all possible combinations of activities to ensure that the maximum number of non-overlapping activities is selected.

### Steps to Solve
1. **Sort activities by their finish times** in ascending order.
2. **Create a table** to store solutions to subproblems.
3. **Use a recursive relation** to fill the table by including or excluding each activity.

### Implementation in Python

```python
def dp_activity_selection(activities):
    n = len(activities)
    
    # Sort activities by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    # Initialize a table to store solutions of subproblems
    dp = [0] * (n + 1)
    
    # Base case: no activities selected
    dp[0] = 0
    
    for i in range(1, n + 1):
        # Find the latest activity that doesn't conflict with the current activity
        for j in range(i - 1, -1, -1):
            if sorted_activities[j][1] <= sorted_activities[i - 1][0]:
                dp[i] = max(dp[i - 1], dp[j + 1] + 1)
                break
        else:
            dp[i] = dp[i - 1]
    
    return dp[n]

# Example usage
activities = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9), (8, 10)]
max_activities = dp_activity_selection(activities)
print("Maximum number of activities (DP):", max_activities)
```

## Performance Analysis

### Time Complexity
- **Greedy Approach**: \(O(n \log n)\) due to the sorting step, and \(O(n)\) for the selection, making it \(O(n \log n)\) overall.
- **Dynamic Programming Approach**: \(O(n^2)\) due to the nested loops to find the latest non-conflicting activity and to fill the DP table.

### Space Complexity
- **Greedy Approach**: \(O(n)\) for storing the sorted activities and selected activities.
- **Dynamic Programming Approach**: \(O(n)\) for the DP table.

## Experimental Results
Run both algorithms on various sets of activities and compare their performances. The results should be visualized using tables and graphs.

## Summary
- The greedy approach is more efficient with a time complexity of \(O(n \log n)\).
- The dynamic programming approach, while having a higher time complexity of \(O(n^2)\), ensures all possible combinations are considered.

