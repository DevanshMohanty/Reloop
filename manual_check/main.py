from db import prod_type,days_left,desc
from expired import repurposes
from present import uses


print(f"\nPRODUCT NAME: {prod_type}")
status = 'USABLE'
if(days_left <= 0 ):
    status = 'EXPIRED'
    print(f"\nPRODUCT STATUS: {status}")
    days_passed = -1 * days_left
    print(f"\nDays Passed Since Expiry: {days_passed}")
    rep = repurposes()
    print(f"\n{rep}")
else:
    print(f"\nPRODUCT STATUS: {status}")
    print(f"\nDays Left Until Expiry: {days_left}")
    use = uses()
    print(f"\n{use}")
    


