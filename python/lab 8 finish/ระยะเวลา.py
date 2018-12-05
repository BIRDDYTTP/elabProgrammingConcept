def read_hour():
    hour = int(input("Enter hour: "))
    if hour <= 23 and hour >= 0:
        hour = hour
    return hour
def read_minute():
    minute = int(input("Enter minute: "))
    if minute >= 0 and minute <= 59:
        minute = minute
    return minute
def read_second():
    sec = int(input("Enter second: "))
    if sec >= 0 and sec <= 59:
        sec = sec
    return sec
def to_seconds(h,m,s):
    a = (h*3600)+(m*60)+s
    return a
def time_elapsed(start,finish):
    time = finish - start
    hour = time//3600
    minute = (time-(hour*3600))//60
    sec = time-((hour*3600)+(minute*60))
    ans = "%d hours %d minutes %d seconds."%(hour,minute,sec)
    return ans

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))