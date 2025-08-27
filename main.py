import time

time_on = 0
time_off = 0

while True:
    userchoice = input('choose an option [1]set time on  [2]set time off  [3]start timer  [4]start default timer ')
    if userchoice == '1':
        time_on = int(input('Set time on in minutes: ')) * 60
    elif userchoice == '2':
        time_off = int(input('Set time off in minutes: ')) * 60
    elif userchoice == '3':
        print('lets start' {time_on // 60} + 'minutes')
        time.sleep(time_on)
        print('time out, rest ' + {time_off // 60} +  'minutes')
        time.sleep(time_off)
        print('time on, lets repeat!!')
    elif userchoice == '4':
        time.sleep(1500)
        print('time out, rest 5 minutes')
        time.sleep(300)
        print('time on, lets repeat!!')
    else:
        print('error:')