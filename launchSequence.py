def launchSequenceChecker(systemNames, stepNumbers):
    
    #import time
    #start_time = time.time()
    
    
    uniqueSystems = set(systemNames)
    
    #print ("Set took", time.time() - start_time, "to run")
    
    
    sequenceCorrect = True;
    
    for system in uniqueSystems:
        if sequenceCorrect == False:
            break;
        
        #import time
        #start_time = time.time()
        
        indices = [i for i, x in enumerate(systemNames) if x == system]
        
        #print ("Indices", time.time() - start_time, "to run")

        curStepNum = 0
        
        for index in indices:
            if sequenceCorrect == False:
                break
            if stepNumbers[index] > curStepNum:
                curStepNum = stepNumbers[index]
            else:
                sequenceCorrect = False
        
    return sequenceCorrect