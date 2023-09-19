"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""
def timeConversion(s):
    # Write your code here
    split1 = s.split(':')
    split2=[0,1,2]
    if 'AM' in split1[2]:
        if split1[0]=='12':
            split2[0]='00'
            split2[1]=split1[1]
            split2[2]=split1[2][:2]
        else:
            a=int(split1[0])
            my_dict={1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09', 10:'10', 11:'11'}
            split2[0]=my_dict[a]
            split2[1]=split1[1]
            split2[2]=split1[2][:2]            
    else:
        if split1[0]=='12':
            split2[0]='12'
            split2[1]=split1[1]
            split2[2]=split1[2][:2]
        else:
            a=int(split1[0])
            split2[0]=a+12
            split2[1]=split1[1]
            split2[2]=split1[2][:2]
    op_str=''
    for i in split2:
        op_str=op_str+str(i)+':'
    op_str = op_str.strip(':')
    print(op_str)
    return op_str

import datetime
import random
date_list = ['12:00:12PM', '02:30:59PM', '05:14:07PM','12:30:05AM']
print(f'Input list in 12 hr format is {date_list}.')
op_list=[]
for i in date_list:
    a=timeConversion(i)
    op_list.append(a)
print(f'Output list in 24 hours format is {op_list}.')