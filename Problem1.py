#Problem 1
from datetime import time

time_input1 = input('')
time_input2 = input('')

h1, m1, s_am_pm1 = map(str.strip, time_input1.split(':'))
s1, am_pm1 = s_am_pm1.split()

h2, m2, s_am_pm2 = map(str.strip, time_input2.split(':'))
s2, am_pm2 = s_am_pm2.split()

if am_pm1 not in ('am', 'pm') or am_pm2 not in ('am', 'pm'):
    print("Invalid time format. Use 'am' or 'pm'")
else:
    h1 = int(h1)
    m1 = int(m1)
    s1 = int(s1)
    h2 = int(h2)
    m2 = int(m2)
    s2 = int(s2)

    if am_pm1 == 'pm' and h1 != 12:
        h1 += 12
    elif am_pm1 == 'am' and h1 == 12:
        h1 = 0

    if am_pm2 == 'pm' and h2 != 12:
        h2 += 12
    elif am_pm2 == 'am' and h2 == 12:
        h2 = 0
    
    difference = (60 * h2 + m2 + s2/60) - (60 * h1 + m1 + s1/60) 

    if am_pm1 == "pm":
        difference *= -1
        difference /= 2

    if am_pm1 == am_pm2 and h2 < h1:
        difference += 24*60

    print(int(difference))