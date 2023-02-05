#before using this code make sure you have installed whatsapp and logged in
#ArfeenDev
import pyautogui as auto #importing module
import time

whatsapp_no= auto.prompt(text='Enter Mobile number here:', title='Whatsapp Messsager:' , default='') #getting mobile no 
#name= auto.prompt(text='Enter Name here:', title='Whatsapp Messsager:' , default='') #If you want to search name and send message
message=auto.prompt(text='Type message here!', title='Message to be sent on: {}'.format(whatsapp_no), default='') #getting information what to send on whatsapp
confirm=auto.confirm(text='Are sure want confirm', title='Confirm', buttons=['OK', 'Cancel']) #confirming whether to send or not
while confirm=='OK': #if we press 'OK' then it will continue
 auto.press('Win', interval=1)
 time.sleep(0.5)
 auto.write('whatsapp')
 time.sleep(1)
 auto.press("enter")
 time.sleep(1)
 auto.click(x=165, y=111)
 time.sleep(1)
 auto.write(whatsapp_no) # replace with 'name' variable if you want to search name and send message instead of number
 time.sleep(2)
 auto.click(x=196, y=178)
 time.sleep(1)
 auto.click(x=797, y=1055)
 time.sleep(1)
 auto.write(message, interval=0.3)
 time.sleep(1)
 auto.press('Enter', interval=1)
 time.sleep(1)
 break
 
 #ArfeenDev
else: #if we press 'CANCEL' it will be exited and informed in console log
 print("Successfully Exited ✅")

#ArfeenDev
#ArfeenDev
