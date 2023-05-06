import json

def thermostate_mdp(goal, ratio):



    costs = {"on":0.5,"off":0.5}
    actions = ["on","off"]
    states_names=[]

    states = {}

    

    State16 = { "on": {16.5 :0.5, 17.0 :0.2, 16.0 :0.3},
                "off":{16.5 :0.1, 17.0 :0  , 16.0 :0.9},
                "initial_value":0}
    
    State245 = { "on":{25.0 :0.7, 24.5 :0.2, 24.0 :0.1},
                "off":{25.0 :0.1, 24.5 :0.2, 24.0 :0.7},
                "initial_value":0}
    
    State25 = { "on": {25.0 :0.9, 24.5 :0.1},
                "off":{25.0 :0.3, 24.5 :0.7},
                "initial_value":0}
    


    count = 15.5
    while count < 25:
        count += 0.5
        states_names.append(str(count))
        if count==goal:
            states[count] = { "on": {count + 0.5 :0.0, count + 1 :0.0, count:0.0, count - 0.5 : 0.0},
                             "off": {count + 0.5 :0.0, count + 1 :0.0, count:0.0, count - 0.5 : 0.0},
                             "initial_value":0}
        elif count == 16:
            states[count] = State16
        elif count == 24.5:
            states[count] = State245
        elif count == 25:
            states[count] = State25
        else:
            states[count] = { "on": {count + 0.5 :0.5, count + 1 :0.2, count:0.2, count - 0.5 : 0.1},
                             "off": {count + 0.5 :0.1, count + 1 :0, count:0.2, count - 0.5 : 0.7},
                             "initial_value":0}
    count=15.5
    while count < 25:
        count += 0.5
        for key in states_names:
            if not (float(key) == count or float(key) == count-0.5 or float(key) == count+0.5 or float(key) == count + 1): 
                states[count]["on"][key] = 0.0
                states[count]["off"][key] = 0.0

    with open('Values.json', 'w') as f:
        json.dump({
            "states": states,
            "costs": costs,
            "actions": actions,
            "states names": states_names,
            "goal state": goal,
            "difference ratio" : ratio
        }, f, indent=4, ensure_ascii=False)
thermostate_mdp(22, 0.001)