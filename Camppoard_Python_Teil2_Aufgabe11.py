for counterUp in range(11):
    print("     " + str(counterUp))
    for counterDown in range(counterUp, 0, -1):
        print("           " + str(counterDown))
        #counterDown -= 1
    counterUp += 1    
