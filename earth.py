from datetime import datetime, timedelta
from datetime import datetime, time

current_time = datetime.now().time()
midnight = time(0, 0)
eight_am = time(8, 0)



if midnight <= current_time <= eight_am:
    print ('凌晨')
else :
    print ('非凌晨')
    print(current_time)
    print (midnight)
    print (eight_am)