import time

def alarm():

    day = time.asctime()
    day = day[0:3]
    if day == 'Mon':
        day = 0
    elif day == 'Tue':
        day = 1
    elif day == 'Wed':
        day = 2
    elif day == 'Thu':
        day = 3
    elif day == 'Fri':
        day = 4
    elif day == 'Sat':
        day = 5
    elif day == 'Sun':
        day = 6

    while True:
        try:
            time_input1 = input('Enter time in HH:MM:SS format : ')
            #date_input1 = input('Enter date in DD/MM/YYYY format : ')

            time_input = time_input1.split(':')
            #date_input = date_input1.split('/')

            hours=int(time_input[0])
            minute=int(time_input[1])
            sec=int(time_input[2])
            if 0 <= hours <= 23 and 0 <= minute <= 59 and 0 <=sec <=59:
                break
            else:
                sec = int('seconds')
            break
        except:
            print("Please enter the value in correct format or within the range")


    date = time.asctime()
    date = int(date[8:10])

    month = time.asctime()
    month = month[4:7]

    if month == 'Jan':
        month = 1
    elif month == 'Feb':
        month = 2
    elif month == 'Mar':
        month = 3
    elif month == 'Apr':
        month = 4
    elif month == 'May':
        month = 5
    elif month == 'Jun':
        month = 6
    elif month == 'Jul':
        month = 7
    elif month == 'Aug':
        month = 8
    elif month == 'Sep':
        month = 9
    elif month == 'Oct':
        month = 10
    elif month == 'Nov':
        month = 11
    elif month == 'Dec':
        month = 12

    year = time.asctime()
    year = int(year[20:])

    value = time.struct_time((year, month, date, hours, minute, sec, day, 362,1))
    #print(value) To get the 'value' in struct_time type
    return value
