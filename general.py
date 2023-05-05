import json


def MDP(json_file):

    fp = open(json_file, 'r')
    data = json.load(fp)
    fp.close()

    states = data['states']
    actions = data['states'][0]
    print(actions)


