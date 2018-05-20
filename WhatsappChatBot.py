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

#read_box_array = driver.find_element_by_class_name('selectable-text invisible-space copyable-text');

print ('user click done ')
#read_box_array = driver.find_element_by_class_name("//div[contains(@class, 'selectable-text') and contains(@class, 'invisible-space') and contains(@class, 'copyable-text')]")

#working for movie -- selects the ChupBe chat bubble (last bubble magic number = 14)
read_box_array = driver.find_elements_by_xpath("//*[@id='main']/div[2]/div/div/div[3]")	


	#this works are puts all the message thread (which is loaded into the driver, len of driver is 1)
	#read_box_array = driver.find_elements_by_xpath("//*[@id='main']/div[2]/div/div/div[3]")

#print('read the array'+read_box_array.text)
print('size of array is ',len(read_box_array))

read_box = read_box_array[len(read_box_array)-1]
print(read_box.text)

s = read_box.text

f= open("chat.txt","w+")
f.write(s);
f.close();

g = open("chat.txt","r")
text = g.readlines()
g.close()

lines = []
[lines.append(line) for line in text]

print(lines)


#LINES NOW HAS ALL CHAT in different lines




print("length of s is 			",len(s))
print("length of s[0] is 		",len(s[0]))
print("statement is need is 	"+lines[len(lines)-2])

replyFromUser = lines[len(lines)-2]

driver.execute_script("window.open('','_blank');")
driver.switch_to_window(driver.window_handles[1])
driver.get('http://www.square-bear.co.uk/mitsuku/nfchat.htm')
time.sleep(5)
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
button.click()



#for i in range(int(count)):
#	msg_box.send_keys(msg)
#	button = driver.find_element_by_class_name('_2lkdt')
#	button.click()