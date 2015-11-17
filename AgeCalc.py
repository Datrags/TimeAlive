age = float(raw_input('what is your age? '))

if age < 0:
    print "This is definitely not possible"
    
else:
    print "You have been alive",age,"."
    
    days = age * 356
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    
    
    print "You been alive",days,"days."
    print "You been alive",hours,"hours."
    print "You been alive",minutes,"minutes."
    print "You been alive",seconds,"seconds."
