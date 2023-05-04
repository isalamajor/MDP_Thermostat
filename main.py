import json


def main():
    fp = open('Values.json', 'r')
    data = json.load(fp)
    fp.close()

    #Format for printing
    key_format = "\033[1;35m"
    value_format = "\033[1;36m"
    separator_format = "\033[1;37m"


    # temperature = int(temperature)
    cost_on = int(data["costs"]["on"])
    cost_off = int(data["costs"]["off"])
    states_enumeration = data["states"]
    print(states_enumeration)
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

    #print(previous_values)
    count = 15.5
    iteration=0
    while count > 0:
        # la resta hay que ver que hacemos mal pero siempre es el valor del menor coste mas que la vez anterior
        if ((new_values[24] - previous_values[24]) > 0.01) or iteration<1:
            print(new_values[24])
            print(previous_values[24])


            print(new_values[24] - previous_values[24])
            print("------------------------------------------------------")

            """print(key_format, 24, separator_format, "->", value_format, previous_values[24])
            print("-----------------------------------------")
            print(key_format, 24, separator_format, "->", value_format, new_values[24])
            print("00000000000000000000000000000000000000000")"""

            iteration += 1
            count = 15
            while count < 26:
                count = count + 0.5
                previous_values[count] = new_values[count]
            #for key in previous_values:

            
            count = 15.5
            while count < 25:
                count += 0.5
                state_type = "State"
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
                    summation_on += (float(states_enumeration[state_type][action][state_to_go]) * previous_values[
                        count + float(state_to_go)])
                
                summation_off = cost_off
                action = "off"
                
                for state_to_go in states_enumeration[state_type][action]:
                    # 1+float(state_to_go)  important change to float if you want to add to the count
                    summation_off += (float(states_enumeration[state_type][action][state_to_go]) * previous_values[
                        count + float(state_to_go)])
                
                new_values[count] = min(summation_on, summation_off)
                """if iteration ==2:
                    print(summation_off)
                    print(summation_on)
                    break"""
        else:
            """print(key_format, 20, separator_format, "->", value_format, previous_values[20])
            print(key_format, 20, separator_format, "->", value_format, new_values[20])"""
            break
        


    # print(previous_values)
    print(key_format, 16, separator_format, "->", value_format, new_values[16])
    print(key_format, 16.5, separator_format, "->", value_format, new_values[16.5])
    print(cost_on)

    #for key in previous_values:
    """ print(key_format, 20, separator_format, "->", value_format, previous_values[20])
    #for key in previous_values:
    print(key_format, 20, separator_format, "->", value_format, new_values[20])"""
    print(iteration)
    return None

if __name__ == "__main__":
    main()