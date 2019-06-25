def launchSequenceChecker(systemNames, stepNumbers):
    
    
    uniqueSystems = set(systemNames)
    
    
    sequenceCorrect = True;
    
    for system in uniqueSystems:
        if sequenceCorrect == False:
            break;
        
        indices = [i for i, x in enumerate(systemNames) if x == system]
        

        curStepNum = 0
        
        for index in indices:
            if sequenceCorrect == False:
                break
            if stepNumbers[index] > curStepNum:
                curStepNum = stepNumbers[index]
            else:
                sequenceCorrect = False
        
    return sequenceCorrect
