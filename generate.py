import json

def thermostate_mdp(goal, ratio):



    costs = {"on":0.5,"off":0.5}
    actions = ["on","off"]
    states_names=[]

    states = {}

    State16 = { "on": {16.5 :0.5, 17 :0.2, 16 :0.3},
                "off":{16.5 :0.1, 17 :0  , 16 :0.9},
                "initial_value":0}
    
    State245 = { "on":{25 :0.7, 24.5 :0.2, 24 :0.1},
                "off":{25 :0.1, 24.5 :0.2, 24 :0.7},
                "initial_value":0}
    
    State25 = { "on": {25 :0.9, 24.5 :0.1},
                "off":{25 :0.3, 24.5 :0.7},
                "initial_value":0}
    


    count = 15.5
    while count < 24.5:
        count += 0.5
        states_names.append(count)
        if count == 16:
            states[count] = State16
        elif count == 24.5:
            states[count] = State245
        elif count == 25:
            states[count] = State25
        else:
            states[count] = { "on": {count + 0.5 :0.5, count + 1 :0.2, count:0.2, count - 0.5 : 0.1},
                             "off": {count + 0.5 :0.1, count + 1 :0, count:0.2, count - 0.5 : 0},
                             "initial_value":0}
    with open('Values.json', 'w') as f:
        json.dump({
            "states": states,
            "costs": costs,
            "actions": actions,
            "states_names": states_names,
            "goal_state": goal,
            "difference ratio" : ratio
        }, f, indent=4)
thermostate_mdp(22, 0.001)