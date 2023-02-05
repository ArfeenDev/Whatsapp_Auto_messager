import pyautogui as auto
import time

whatsapp_no= auto.prompt(text='Enter Mobile number here:', title='Whatsapp Messsager:' , default='')
message=auto.prompt(text='Type message here!', title='Message to be sent on: {}'.format(whatsapp_no), default='')
confirm=auto.confirm(text='Are sure want confirm', title='Confirm', buttons=['OK', 'Cancel'])
while confirm=='OK':
 auto.press('Win', interval=1)
 time.sleep(0.5)
 auto.write('whatsapp')
 time.sleep(1)
 auto.press("enter")
 time.sleep(1)
 auto.click(x=165, y=111)
 time.sleep(1)
 auto.write(whatsapp_no)
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
 
 
else:
 print("Successfully Exited ✅")
