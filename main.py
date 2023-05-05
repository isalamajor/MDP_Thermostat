import json


def main(json_file):

    # Open the json file where the data of the problem is entered
    fp = open(json_file, 'r')
    data = json.load(fp)
    fp.close()

    # Store the necessary data in local dictionaries and variables
    states_dic = data['states']
    actions_list = data['actions']
    cost_dic = data['costs']
    states_list = data['states names']
    goal_state = data['goal state']
    diff = data['difference ratio']

    # Create dictionaries to store the Bellman's Equation Values
    current_values = {}
    next_values = {}
    cheaper_actions = {}
    for i in states_list:
        current_values[i] = 0
        next_values[i] = 0
        cheaper_actions[i] = 0

    print("current_values:", current_values)
    print("actions_list:", actions_list)
    print("next_values:", next_values)
    print("cost_dic:", cost_dic)
    print("states_dic:", states_dic)
    print("states_list", states_list)

    # Create a list to store whether each State has reached its peak value (0 or 1)
    states_reached = [0]*len(states_dic)

    # Variable to keep track of the number of iterations used by the MDP
    iterations = 0

    while min(states_reached) < 1:

        print("Iteration number", iterations, "->", current_values)
        iterations += 1
        state_index = 0

        for state in states_list:
            if state != goal_state:
                actions_costs = []

                for action in actions_list:
                    action_cost = cost_dic[action]
                    for state_to_go in states_list:
                        action_cost += states_dic[state][action][state_to_go] * current_values[state_to_go]
                    actions_costs.append(action_cost)

                    if action_cost <= min(actions_costs):
                        cheaper_actions[state] = action

                next_values[state] = min(actions_costs)

                if (next_values[state] - current_values[state]) < diff:
                    states_reached[state_index] = 1
            else:
                states_reached[state_index] = 1
            state_index += 1

        current_values = next_values.copy()
        print(states_reached)
    print("Optimal Policy for each State:", cheaper_actions)


if __name__ == "__main__":
    main('excel.json')
