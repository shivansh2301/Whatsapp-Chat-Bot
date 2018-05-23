from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import time
import math



driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = raw_input('Enter the name')
msg = raw_input('Enter your message')
count = raw_input('enter the number of times u want to send this msg')

print(name+' and '+msg+' + ' +count)

raw_input('press any key after QR scanning')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
print ('user click done ')


#PING OF DEATH
#msg_box = driver.find_element_by_class_name('_2S1VP')
#for i in range(int(count)):
#	msg_box.send_keys(msg)
#	button = driver.find_element_by_class_name('_2lkdt')
#	button.click()



#read_box_array = driver.find_element_by_class_name('selectable-text invisible-space copyable-text');

#	waste code
#read_box_array = driver.find_element_by_class_name("//div[contains(@class, 'selectable-text') and contains(@class, 'invisible-space') and contains(@class, 'copyable-text')]")



"""
#	WORKS :
#	read_box_array has all the messages of the thread and selects LAST message of the THREAD.
#		problem : can be a problem if its sender's message 

read_box_array = driver.find_elements_by_xpath("//*[@id='main']/div[2]/div/div/div[3]")	
print('size of array is ',len(read_box_array))
read_box = read_box_array[len(read_box_array)-1]
print(read_box.text)

s = read_box.text
s=s.encode('utf-8')
f= open("chat.txt","w+")
f.write(s);
f.close();

g = open("chat.txt","r")
text = g.readlines()
g.close()

lines = []
[lines.append(line) for line in text]

print(lines)		#to print the entire thread of conversation
k = len(lines)-2
for i in range(len(lines)-1,0,-1):
	if(lines[i].equals(name)):
		k=i
		break
	else:
		continue
#now k+1'th index is the latest message by the sender
print (lines[k+1])

"""



#DOESNT WORK : read_box_array3 = driver.find_elements_by_class_name("vW7d1")


# ***********************REPLACING THE WRITE AND READ FILE WITH THIS SOLUTION:*********************
#	WORKS :
#	message-in is for incoming messages (actualy class is "message-in tail" but i couldnt find how to find element with multiple class name)
read_box_array41 = driver.find_elements_by_class_name("message-in")
print("size of classname 'message-in' is ",(len(read_box_array41)))
lastElement1=read_box_array41[len(read_box_array41)-1]
print ("1: "+name+": "+lastElement1.text.split('\n')[0])

driver.execute_script("window.open('','_blank');")
driver.switch_to_window(driver.window_handles[1])
driver.get('http://www.square-bear.co.uk/mitsuku/nfchat.htm')
driver.switch_to_window(driver.window_handles[0])

for i in range(100):
	print ""
	print "i=",i
	read_box_array4 = driver.find_elements_by_class_name("message-in")
	print("size of classname 'message-in' is ",(len(read_box_array4)))
	lastElement=read_box_array4[len(read_box_array4)-1]
	txt=lastElement.text.split('\n')[0].lower()			#lower is needed cuz 'Mitsuku' and 'You' are magic numbers

	print ("2: "+name+": "+txt)

	if(lastElement.text==lastElement1.text and i!=0):
		print("no new message")
		time.sleep(2)
		continue
	print "NEW message"

	driver.switch_to_window(driver.window_handles[1])
	print("z")
	time.sleep(1)
	#driver.sleep(5000)
	#driver.switch_to_window(driver.window_handles[1])
	driver.switch_to_default_content()
	print("zz")
	driver.switch_to.frame('input')
	print("zzz")
	textField = driver.find_elements_by_tag_name("input")[1]
	print("zzzz going to sleep2")
	time.sleep(1)
	print ("going to send "+txt+" to the bot")
	textField.send_keys(txt+Keys.ENTER);
	print("zzzzz")

	time.sleep(1)

	fontTags = driver.find_elements_by_tag_name("font")
	print("zzzzzz")
	for tag in fontTags:
	    if tag.get_attribute("face") == "Trebuchet MS,Arial" and tag.get_attribute("color") == "#000000":
	        responseBody = tag
	        break
	print("zzzzzzz")
	start = responseBody.text.find("Mitsuku:")
	end = responseBody.text.find("You:", 4)
	#firstName = message.user.split(' ')[0]
	resp = responseBody.text[start + 10:end - 2]
	print(start, end, repr(resp))

	print('value of resp = '+resp)

	print('\n\ndone with mitsuku page now reverting back to previous page\n\n')

	time.sleep(1)

	driver.switch_to_window(driver.window_handles[0])
	print("zzzzzzzz")

	lastElement1=lastElement

	msg_box = driver.find_element_by_class_name('_2S1VP')
	msg_box.send_keys(resp)
	button = driver.find_element_by_class_name('_2lkdt')
	button.click()
print("how did u come out of loop?????")


	#this works are puts all the message thread (which is loaded into the driver, len of driver is 1)
	#read_box_array = driver.find_elements_by_xpath("//*[@id='main']/div[2]/div/div/div[3]")

	

	#***********************************************************************************************
	#***********************************************************************************************
	#***********************************************************************************************
	#***********************************************************************************************

		#TO DO
		# 	find the latest message by finding message after Username(not by len()-2)

		#	run 1 second loop in which it will read the chat script
		#		detect new message by comparing with previous script

		#	run mitsuku for every new message
		#	create mitsuku chat scipt by appending messages/saving chat script and reading last message
	#***********************************************************************************************
	#***********************************************************************************************
	#***********************************************************************************************
	#***********************************************************************************************


#LINES NOW HAS ALL CHAT in different lines


"""

print("length of s is 			",len(s))
print("length of s[0] is 		",len(s[0]))
print("statement is need is 	"+lines[len(lines)-2])

replyFromUser = lines[len(lines)-2]

driver.execute_script("window.open('','_blank');")
driver.switch_to_window(driver.window_handles[1])
driver.get('http://www.square-bear.co.uk/mitsuku/nfchat.htm')
time.sleep(2)
#driver.sleep(5000)
#driver.switch_to_window(driver.window_handles[1])
driver.switch_to_default_content()
driver.switch_to.frame('input')
textField = driver.find_elements_by_tag_name("input")[1]


textField.send_keys(replyFromUser+Keys.ENTER);

#driver.sleep(2000)
time.sleep(2)

fontTags = driver.find_elements_by_tag_name("font")

for tag in fontTags:
    if tag.get_attribute("face") == "Trebuchet MS,Arial" and tag.get_attribute("color") == "#000000":
        responseBody = tag
        break

start = responseBody.text.find("Mitsuku")
end = responseBody.text.find("You", 4)
#firstName = message.user.split(' ')[0]
resp = responseBody.text[start + 10:end - 2]
print(start, end, repr(resp))

print('value of resp = '+resp)

print('\n\ndone with mitsuku page now reverting back to previous page\n\n')
driver.switch_to_window(driver.window_handles[0])




msg_box = driver.find_element_by_class_name('_2S1VP')
msg_box.send_keys(resp)
button = driver.find_element_by_class_name('_2lkdt')
#button.click()



#for i in range(int(count)):
#	msg_box.send_keys(msg)
#	button = driver.find_element_by_class_name('_2lkdt')
#	button.click()


"""