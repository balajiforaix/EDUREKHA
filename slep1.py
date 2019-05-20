def sleep_in(weekday, vacation):
    if not weekday and  vacation :
        print("Vacation")	    
        return True	    
    else:
        print("Weekday")
        return False
sleep_in(True, True)
