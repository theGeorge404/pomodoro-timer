import time

time_on = 0
time_off = 0

def countdown():
   print('3..')
   time.sleep(1)
   print('2..')
   time.sleep(1)
   print('1..')
   time.sleep(1)
   print('start')


while True:
    userchoice = input('choose an option [1]start default   [2]set time off  [3]start timer  [4]start default timer ')
    if userchoice == '0':
        break
    elif userchoice == '1':
        time_on = int(input('Set time on in minutes: ')) * 60
    elif userchoice == '2':
        time_off = int(input('Set time off in minutes: ')) * 60
    elif userchoice == '3':
        if time_on <= 0:
          if time_off <= 0:
           print('error 101')
          else:
           print('error 102')
        elif time_off <= 0:
           if time_on <= 0:
              print('error 101')
           else:
              print('error 103')
        else:
         print('ready for work ',time_off // 60 , 'minutes')
         countdown()
         time.sleep(time_on)
         print('time out, rest ',time_off // 60 , 'minutes')
         time.sleep(time_off)
         print('time out, lets repeat!!')
    elif userchoice == '4':
        time.sleep(1500)
        print('time out, rest 5 minutes')
        countdown()
        time.sleep(300)
        print('time out, lets repeat!!')
    elif userchoice == '5':
       print('time on = ', time_on)
       print('time off = ', time_off)
       print('US = ' + userchoice)
    else:
        print('error 404')
        time.sleep(2)



