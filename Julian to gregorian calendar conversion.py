"""
Given a year, , find the date of the 256th day of that year according to the official Russian calendar during that year. 
Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is .

For example, the given year = 1984. 1984 is divisible by 4, so it is a leap year. 
The 256th day of a leap year after 1918 is September 12, so the answer is 12.09.1984.
"""

def dayOfProgrammer(year):
    # Write your code here
    day=''
    month='09'
    if 1700<=year<=1917:
        if year%4==0:
            day='12'
        else:
            day='13'
    elif year==1918:
        day='26'
    elif 1918<year<=2700:
        if year%400==0 or (year%4==0 and year%100!=0):
            day='12'
        else:
            day='13'        
    date=f'{day}.{month}.{year}'
    return date

ip = 2000
result = dayOfProgrammer(ip)
print(result)