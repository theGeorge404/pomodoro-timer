import time
import sys

time_on = 0
time_off = 0

#I used a `time.sleep()` to slow down the softwere and avoid over saturing the user

def countdown():
   time.sleep(1)
   print('3..')
   time.sleep(1)
   print('2..')
   time.sleep(1)
   print('1..')
   time.sleep(1)
   print('start')

def bar(duration=10): #I see it on internet
    total = 100  
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = '█' * i + '-' * (total - i)
        sys.stdout.write(f'\r|{bar}| {percent:.1f}%')
        sys.stdout.flush()
        time.sleep(duration / total)
    print()


def personaliced():
    choice2 = input('choose an option [0]go back  [1]set time on   [2]set time off  [3]start personaliced timer:  ')
    if choice2 == '0':
        pass
    elif choice2 == '1':
        ontimeon = input('Set time to work in minutes:  ') * 60 #why does this not work??
        time.sleep(1)
    elif choice2 == '2':
        ontimeoff =  input('Set time to break in minutes:  ') * 60 #other hand this doesn't work
        time.sleep(1)
    elif choice2 == '3':
        check() 
    else:
        print('error 404')
        time.sleep(1)

def check():
    chek = input('Ready?? y/n: ')
    if chek == 'y':
        print(time_on // 60, 'minutes concentration')
        bar(time_on)
        print('time out, take a ',time_off // 60,' minutes rest')
        bar(time_off)
        time.sleep(1)
        check()
    elif chek == 'n':
        print('aborting operation...')
        time.sleep(1)
    else:
        print('error 404')
        time.sleep(1)
        check()

while True:
  userchoice = input('choose an option [0]exit  [1]start default timer  [2]personalice timer  [3]start personaliced:  ')
  if userchoice == '0':
        break
  elif userchoice == '1':
      time_off = 300
      time_on = 1500
      check()     
  elif userchoice == '2':
      choice2 = input('choose an option [0]go back  [1]set time on   [2]set time off :  ')
      if choice2 == '0':
         pass
      elif choice2 == '1':
         time_on = int(input('Set time to work in minutes:  ')) * 60
         time.sleep(1)
      elif choice2 == '2':
         time_off =  int(input('Set time to break in minutes:  ')) * 60
         time.sleep(1)
      else:
         print('error 404')
         time.sleep(1)
  elif userchoice == '3':
      check()
  elif userchoice == 'debug':
      print('starting debug mode, please wait')
      time.sleep(1)
      print('---')
      print('var values:')
      print(time_on, '= time on')
      print(time_off, '= time off')
      print(userchoice, '= userchoice')
      time.sleep(1)
      print('---')
      print('reseting var values')
      time_on = 0
      time_off = 0
      userchoice = 'none'
      chek = 'none'
      choice2 = 'none'
      bar(5)
      print('values rested correctly')
      time.sleep(1)
      print('---')
      print('exiting debug...')
      time.sleep(1)
  else:
    print('error 404')  
    time.sleep(1)    