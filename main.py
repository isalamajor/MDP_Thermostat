import json
import sys

def main():
    fp = open('Values.json', 'r')
    data = json.load(fp)
    fp.close()
    
    
    #temperature=int(temperature)
    cost_on=int(data["costs"]["on"])
    cost_off=int(data["costs"]["off"])
    states_enumertion=data["states"]
    previous_values={}
    # we store values with margins so we dont have problems when we iterate in state 16, 24.5 and 25
    count = 15
    while count < 26:
        count=count + 0.5
        previous_values[count] = 0

    print(previous_values)
    count = 15.5
    while count < 25:
        
        count = count + 0.5
        
        if count == 16:
        
            sumatory_on=cost_on
            
            for state_to_go in states_enumertion["State16"]["on"]:
                
                #1+float(state_to_go)  important change to float if you want to add to the count
                sumatory_on = sumatory_on + (float(states_enumertion["State16"]["on"][state_to_go])*previous_values[count+float(state_to_go)])
            
            sumatory_off=cost_off   
            for state_to_go in states_enumertion["State16"]["off"]:
                #1+float(state_to_go)  important change to float if you want to add to the count
                sumatory_off = sumatory_off + (float(states_enumertion["State16"]["off"][state_to_go])*previous_values[count+float(state_to_go)])
           
            previous_values[count] = min(sumatory_on,sumatory_off)

        elif count == 24.5:
            
            sumatory_on=cost_on
            for state_to_go in states_enumertion["State24,5"]["on"]:
                
                #1+float(state_to_go)  important change to float if you want to add to the count
                sumatory_on = sumatory_on + (float(states_enumertion["State24,5"]["on"][state_to_go])*previous_values[count+float(state_to_go)])
            
            sumatory_off=cost_off   
            for state_to_go in states_enumertion["State24,5"]["off"]:
                #1+float(state_to_go)  important change to float if you want to add to the count
                sumatory_off = sumatory_off + (float(states_enumertion["State24,5"]["off"][state_to_go])*previous_values[count+float(state_to_go)])
           
            previous_values[count] = min(sumatory_on,sumatory_off)
        elif count == 25:

            sumatory_on=cost_on
            for state_to_go in states_enumertion["State25"]["on"]:
                
                #1+float(state_to_go)  important change to float if you want to add to the count
                sumatory_on = sumatory_on + (float(states_enumertion["State25"]["on"][state_to_go])*previous_values[count+float(state_to_go)])
            
            sumatory_off=cost_off   
            for state_to_go in states_enumertion["State25"]["off"]:
                #1+float(state_to_go)  important change to float if you want to add to the count
                sumatory_off = sumatory_off + (float(states_enumertion["State25"]["off"][state_to_go])*previous_values[count+float(state_to_go)])
           
            previous_values[count] = min(sumatory_on,sumatory_off)
        else:
            
            sumatory_on=cost_on
            for state_to_go in states_enumertion["State"]["on"]:
                
                #1+float(state_to_go)  important change to float if you want to add to the count
                sumatory_on = sumatory_on + (float(states_enumertion["State"]["on"][state_to_go])*previous_values[count+float(state_to_go)])
            
            sumatory_off=cost_off   
            for state_to_go in states_enumertion["State"]["off"]:
                #1+float(state_to_go)  important change to float if you want to add to the count
                sumatory_off = sumatory_off + (float(states_enumertion["State"]["off"][state_to_go])*previous_values[count+float(state_to_go)])
           
            previous_values[count] = min(sumatory_on,sumatory_off)
        

    
    print(previous_values)
    return None
    






if __name__ == "__main__":
   main()