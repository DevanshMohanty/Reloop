def daily_check(threshold,current_days_left,prod_type):
    notification = ''
    if(current_days_left <0 ):
        if(current_days_left == -1):
            notification = f'{prod_type} expired yesterday'
        else: notification = f'It has been {-1*current_days_left} days since {prod_type} has expired'
    

    elif(current_days_left == 0):
        notification = f'!!! {prod_type} expires today'

    else:
        if(current_days_left < threshold):
            if(current_days_left == 1):
                notification = f'!!{prod_type} expires tomorrow'
            else:
                notification = f'!There are {current_days_left} days left until {prod_type} expires'

    return notification,current_days_left   


           