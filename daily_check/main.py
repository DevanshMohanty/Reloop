from db import prod_type,days_left,desc

def daily_check(threshold):
    notification = ''
    days_left = days_left - 1 
    if(days_left <0 ):
        notification = f'It has been {-1*days_left} days since {prod_type} has expired'

    elif(days_left == 0):
        notification = f'!!! {prod_type} expires today'

    else:
        if(days_left < threshold):
            if(days_left == 1):
                notification = f'!!{prod_type} expires tomorrow'
            else:
                notification = f'!There are {days_left} days left until {prod_type} expires'

    return notification       
           