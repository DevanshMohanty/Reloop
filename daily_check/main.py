import db

def daily_check(threshold,days_left,prod_type):
    notification = ''
    current_days_left = days_left - 1 
    if(current_days_left <0 ):
        notification = f'It has been {-1*current_days_left} days since {prod_type} has expired'

    elif(current_days_left == 0):
        notification = f'!!! {prod_type} expires today'

    else:
        if(current_days_left < threshold):
            if(days_left == 1):
                notification = f'!!{prod_type} expires tomorrow'
            else:
                notification = f'!There are {days_left} days left until {prod_type} expires'

    return notification,current_days_left   

def update_file(current_days_left):
    lines=[]
    with open("db.py","r")as f:
        lines=f.readlines()
    with open("db.py","w") as f:
        for line in lines:
            if line.strip().startswith("days_left"):
                    f.write(f'days_left={current_days_left}\n')
            else:
                f.write(line)

def main():
    message,days_left=daily_check(3,db.days_left,db.prod_type)
    update_file(days_left)
    print(message)

if __name__=="__main__":
    main()
           