# find landa closure in every state
def landaClosure(values,state):
    if not (state in recursion):
        recursion.append(state)
        for i1 in range(4, len(data)):
            if (state + " l") in data[i1]:
                values.append(data[i1].split()[2])
                landaClosure( values,data[i1].split()[2])


# list for data , inputs , closures , states and transitions
recursion = list()
data = list()
transitions = dict()
closures = dict()
newEndStates = list()


def main():
    # reading inputs from file and adding transitions
    inputFile = open("NFA_Input_2.txt", "r")
    inputs = inputFile.readlines()
    terminals = inputs[0].split()
    for i1 in terminals:
        transitions[tuple(inputs[2].split() + list(i1))] = []
    allStates = inputs[1].split()
    for i1 in allStates:
        closures[i1] = []
        landaClosure(closures[i1],i1)
    endStates = inputs[3].split()
    inputFile.close()
    # finding another transitions
    while True:
        check = 0
        for newState in transitions.keys():
            rangeLoop = len(newState) - 1
            for i1 in range(rangeLoop):
                checkState = newState[i1] + ' ' + newState[len(newState) - 1]
                rangeInput = len(inputs)
                for i2 in range(4, rangeInput):
                    if (newState[i1] + " خ»") in inputs[i2]:
                        landaTransition(newState, inputs[i2].split()[2])
                    if checkState in inputs[i2] and not (inputs[i2].split()[2] in transitions[newState]):
                        transitions[newState].append(inputs[i2].split()[2])
                        check = 1
            # lambda closures for all available transition
            for i1 in transitions[newState]:
                for i2 in closures.keys():
                    if i1 == i2:
                        for i3 in closures[i2]:
                            if not (i3 in transitions[newState]):
                                transitions[newState].append(i3)
        if check == 0:
            break
        # add created transition to another states
        for i1 in transitions.copy().values():
            if i1:
                for i2 in terminals:
                    count = 0
                    for i3 in transitions.keys():
                        if sorted(tuple(i1 + list(i2))) == sorted(i3):
                            count = 1
                            break
                    if count == 0:
                        transitions[tuple(i1 + list(i2))] = []
    # finding new transition
    newState = []
    for i in transitions.keys():
        tmp = list(i)
        del tmp[len(i) - 1]
        if not (sorted(tmp) in newState):
            newState.append(sorted(tmp))
    if [] in transitions.values():
        newState.append([])
    # finding new final states
    for i in transitions.keys():
        for i1 in range(len(i) - 1):
            if i[i1] in endStates:
                tmp = list(i)
                del tmp[len(i) - 1]
                if not (sorted(tmp) in newEndStates):
                    newEndStates.append(sorted(tmp))

    # we create output
    OutputFile = open("DFA_Output_2.txt", "w")
    # here we put terminals in string
    DFATerminals = ""
    for i3 in terminals:
        DFATerminals = DFATerminals + i3 + ' '

    # put all states
    statesStr = ""
    for i1 in newState:
        if i1:
            for i2 in i1:
                statesStr = statesStr + i2
            statesStr = statesStr + ' '

    # reformat all transitions

    listOfTransition = list(transitions.items())
    range2 = len(listOfTransition)
    for i1 in range(range2):
        listOfTransition[i1] = list(listOfTransition[i1])
        listOfTransition[i1][1] = sorted(listOfTransition[i1][1])
        listOfTransition[i1][0] = list(listOfTransition[i1][0])
        tmp = listOfTransition[i1][0][-1]
        del listOfTransition[i1][0][-1]
        listOfTransition[i1][0] = sorted(listOfTransition[i1][0])
        listOfTransition[i1][0].append(tmp)

    # reformat all transitions and put all in a string
    transitionStr = "".join([str(item1) for item1 in listOfTransition])
    for i1 in terminals:
        transitionStr = transitionStr.replace("'" + i1 + "'", ' ' + i1 + ' ')
    transitionStr = transitionStr.replace("[]", "trap_State")
    transitionStr = transitionStr.replace("trap_State]", "trap_State\n")
    transitionStr = transitionStr.replace("]]", "\n")
    transitionStr = transitionStr.replace("[", "")
    transitionStr = transitionStr.replace(", ", "")
    transitionStr = transitionStr.replace("]", "")
    transitionStr = transitionStr.replace("'", "")

    # put final States
    endStr = ""
    for i1 in newEndStates:
        for i2 in i1:
            endStr = endStr + i2
        endStr = endStr + ' '

    finalOutput = DFATerminals + "\n" + statesStr + "\n" + inputs[2] + endStr + "\n" + transitionStr
    OutputFile.write(finalOutput)
    OutputFile.close()

# run main function
if __name__ == '__main__':
   main()

# find transition that has landa
def landaTransition(key, transitionState):
    if not (transitionState in recursion):
        recursion.append(transitionState)
        range1 = len(data)
        for i1 in range(4, range1):
            check = transitionState + ' ' + key[len(key) - 1]
            if check in data[i1] and not (data[i1].split()[2] in transitions[key]):
                transitions[key].append(data[i1].split()[2])
            if (transitionState + "l") in data[i1]:
                landaTransition(key, data[i1].split()[2])