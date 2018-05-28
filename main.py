import time
from selenium import webdriver
b = webdriver.Chrome("/home/oxygen_/Documents/chromedriver") # To open the firefox browser
Not_found = True


with open('username.txt') as f:
    content = f.readlines()
username_list = [x.strip() for x in content] 

with open('password.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
password_list = [x.strip() for x in content] 


for i in range(0,len(username_list)):
	while Not_found:#If the flash sale has not been started yet!!!!
		try:  # Has the flash sale started????
			b.get('https://www.flipkart.com/redmi-note-5-pro-black-64-gb/p/itmf2fc3xgmxnhpx?pid=MOBF28FTQPHUPX83&srno=s_1_1&otracker=search&lid=LSTMOBF28FTQPHUPX83H7IIOZ&fm=SEARCH&iid=e7b858f3-41d8-4faf-82be-f1354061d4ee.MOBF28FTQPHUPX83.SEARCH&ppt=Homepage&ppn=Homepage&ssid=28udd7icqo0000001527485757911&qH=286b43aac83aafdc')
			time.sleep(1)#go directly to the product you want

			b.find_element_by_class_name('_2AkmmA._3Plo8Q._16LyaZ._7UHT_c').click()#clicking the buy now button of the product
			time.sleep(1)
			Not_found = False #The product is available for sale now!
		except:
			print ("Product not found!")

	b.find_element_by_class_name('_2zrpKA._14H79F').send_keys(username_list[i])#Enter the username

	b.find_element_by_class_name('_2AkmmA._1poQZq._7UHT_c').click()#to click the next button

	time.sleep(1)
	b.find_element_by_class_name('_39M2dM._2ZvOfP').send_keys(password_list[i])#Enter the password
	time.sleep(1)
	b.find_element_by_class_name('_2AkmmA._1poQZq._7UHT_c').click()#to click the login button
	time.sleep(2)
	b.find_element_by_class_name('_2AkmmA._2Q4i61._7UHT_c').click()#to click continue and make the payment!!

	#Enter the captcha and click place order

	time.sleep(30)

	b.quit()# you just bought a product! Good Bye......
