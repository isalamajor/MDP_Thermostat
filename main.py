import json
from generate import thermostate_mdp


def main(json_file):

    # Open the json file where the data of the problem is entered
    fp = open(json_file, 'r')
    data = json.load(fp)
    fp.close()

    # Store the necessary data in local arrays and variables
    states_dic = data['states']
    cost_dic = data['costs']
    actions_list = data['actions']
    states_list = data['states names']
    goal_state = data['goal state']
    diff = data['difference ratio']

    # Create dictionaries to store the Bellman's Equation Values
    current_values = {}
    next_values = {}
    optimal_policies = {}
    for i in states_list:
        current_values[i] = 0
        next_values[i] = 0
        optimal_policies[i] = 0

    # Create a list to store whether each State has reached its peak value (0 or 1)
    states_reached = [0]*len(states_dic)

    # Variable to keep track of the number of iterations used by the MDP
    iterations = 0

    # The loop keeps going until every state has reached its peak, so the minimum value in
    # the states_reached list must be a 1 (no zeros in the list)
    while min(states_reached) < 1:

        # This can be uncommented, we can use it to keep track of what is happening in each iteration
        # print("Iteration number", iterations, "->", current_values)
        # iterations += 1

        # We use and index to identify the state we are working with at the moment and store in its
        # place of the states_reached list if it has reached its peak
        state_index = 0

        # We use Bellman's Equation to calculate the new values for each state
        for state in states_list:
            if state != goal_state:
                actions_costs = []

                for action in actions_list:
                    action_cost = cost_dic[action]
                    for state_to_go in states_list:
                        action_cost += states_dic[state][action][state_to_go] * current_values[state_to_go]
                    actions_costs.append(action_cost)

                    # We store the optimal policy for the current state
                    if action_cost <= min(actions_costs):
                        optimal_policies[state] = action

                next_values[state] = min(actions_costs)

                # If the state has reached its peak value we put a 0 in its states_reached list place
                if (next_values[state] - current_values[state]) < diff:
                    states_reached[state_index] = 1

            # The goal state does not have an optimal policy, and we do not need to calculate values for it
            else:
                states_reached[state_index] = 1
                optimal_policies[state] = "goal state"

            state_index += 1

        # The next values of the current operation will be the current values of the next one
        current_values = next_values.copy()

    # We print the optimal policy of each state with a format that is visually easy to understand
    for key in optimal_policies:
        print("\033[1;35m", key, "\033[1;37m", "->", "\033[1;36m", optimal_policies[key])


if __name__ == "__main__":
    # thermostate_mdp("22.0", 0.001) # Run this line if the json is modified
    main('Values.json')
