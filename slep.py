def sleep_in(weekday, vacation):
    if weekday is True and vacation is False:
	    print("today is weekday")
    elif weekday is False and vacation is True:
		print("today is vacation")
	
    else:
        if weekday is True and vacation is True:
	    print("today is weekday")
		
sleep_in(False, True)
