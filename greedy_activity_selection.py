def greedy_activity_selection(activities):
    sorted_activities = sorted(activities, key=lambda x: x[1])
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


#Expect this output
'''
Selected activities (Greedy): [(1, 3), (4, 7), (8, 10)]
'''