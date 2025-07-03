
try:
    print(x)
except NameError:
    print("variables is not defined")
finally:
    print("everything went wrong")
    
    
    x = -1
    
    if x <0:
        raise Exception("sorry, no numbers below zerp")