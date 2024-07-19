def dp_activity_selection(activities):
    n = len(activities)
    sorted_activities = sorted(activities, key=lambda x: x[1])
    dp = [0] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
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
