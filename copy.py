import json
import copy


def main(temperature):
    fp = open('Values.json', 'r')
    data = json.load(fp)
    fp.close()

    # Format for printing
    key_format = "\033[1;35m"
    value_format = "\033[1;36m"
    separator_format = "\033[1;37m"

    # temperature = int(temperature)
    cost_on = float(data["costs"]["on"])
    cost_off = float(data["costs"]["off"])
    states_enumeration = data["states"]
    previous_values = {}
    new_values = {}

    # we store values with margins so that we do not have problems when we iterate in state 16, 24.5 and 25
    count = 15
    while count < 26:
        count = count + 0.5
        previous_values[count] = 0

    count = 15
    while count < 26:
        count = count + 0.5
        new_values[count] = 0

    # print(previous_values)
    count = 15.5
    iteration = 0
    while iteration < 1 or (new_values[24] - previous_values[24]) > 0.001:

        iteration += 1
        previous_values = copy.deepcopy(new_values)

        count = 15.5
        while count < 25:
            count += 0.5
            state_type = "State"
            if count == temperature:
                if count == 25:
                    break
                else:
                    count += 0.5

            if count == 16:
                state_type = "State16"
            elif count == 24.5:
                state_type = "State24,5"
            elif count == 25:
                state_type = "State25"

            summation_on = cost_on
            action = "on"
            for state_to_go in states_enumeration[state_type][action]:
                # 1+float(state_to_go)  important change to float if you want to add to the count
                summation_on += (float(states_enumeration[state_type][action][state_to_go]) * float(previous_values[
                                                                                                        count + float(
                                                                                                            state_to_go)]))

            summation_off = cost_off
            action = "off"
            for state_to_go in states_enumeration[state_type][action]:
                # 1+float(state_to_go)  important change to float if you want to add to the count
                summation_off += (float(states_enumeration[state_type][action][state_to_go]) * float(previous_values[
                                                                                                         count + float(
                                                                                                             state_to_go)]))

            new_values[count] = min(summation_on, summation_off)

    count = 15.5
    while count < 25:
        count += 0.5
        state_type = "State"
        if count == temperature:
            if count == 25:
                break
            else:
                count += 0.5

        if count == 16:
            state_type = "State16"
        elif count == 24.5:
            state_type = "State24,5"
        elif count == 25:
            state_type = "State25"

        summation_on = cost_on
        action = "on"
        for state_to_go in states_enumeration[state_type][action]:
            # 1+float(state_to_go)  important change to float if you want to add to the count
            summation_on += (float(states_enumeration[state_type][action][state_to_go]) * float(previous_values[
                                                                                                    count + float(
                                                                                                        state_to_go)]))

        summation_off = cost_off
        action = "off"
        for state_to_go in states_enumeration[state_type][action]:
            # 1+float(state_to_go)  important change to float if you want to add to the count
            summation_off += (float(states_enumeration[state_type][action][state_to_go]) * float(previous_values[
                                                                                                     count + float(
                                                                                                         state_to_go)]))

        new_values[count] = min(summation_on, summation_off)
    print(iteration)

    """print(key_format, 16, separator_format, "->", value_format, new_values[16])
    print(key_format, 16.5, separator_format, "->", value_format, new_values[16.5])
    print(cost_on)
"""
    """for key in previous_values:
        print(key_format, 20, separator_format, "->", value_format, previous_values[20])
    for key in previous_values:
        print(key_format, 20, separator_format, "->", value_format, new_values[20])
    return None"""


if __name__ == "__main__":
    main(24)