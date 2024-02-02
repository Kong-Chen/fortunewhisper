from datetime import datetime, time

current_time = datetime.now().time()
midnight = time(0, 0)
eight_am = time(8, 0)

print(current_time)
print(midnight)
print(eight_am)

if midnight <= current_time <= eight_am:
    print('1')
else:
    print('2')
