def dp_activity_selection(activities):
    n = len(activities)

    # Sort activities by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])

    # Table to store the maximum number of activities
    dp = [0] * (n + 1)
    
    # Base case: no activities selected
    dp[0] = 0

    # Fill the dp table
    for i in range(1, n + 1):
        # Find the latest activity that doesn't conflict with the current activity
        include = 1  # Include the current activity
        for j in range(i - 1, -1, -1):
            if sorted_activities[j][1] <= sorted_activities[i - 1][0]:
                include += dp[j + 1]
                break
        
        dp[i] = max(dp[i - 1], include)

    return dp[n]

# Example usage
activities = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9), (8, 10)]
max_activities = dp_activity_selection(activities)
print("Maximum number of activities (DP):", max_activities)


'''
Epected output 
    Maximum number of activities (DP): 3
The output is the maximum number of non-overlapping activities that can be selected.
'''