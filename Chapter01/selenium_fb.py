from selenium import webdriver

#Create browser object, by default it creates Firefox object
browser = webdriver.Firefox()
print "WebDriver Object", browser

#Maximize browser and browse to facebook website
browser.maximize_window()
browser.get('https://facebook.com')

#Find email and password fields
email = browser.find_element_by_name('email')
password = browser.find_element_by_name('pass')
print "Html elements:"
print "Email:", email, "\nPassword:", password

#Enter email and password to login
email.send_keys('abc@gmail.com') #Enter correct email address
password.send_keys('pass123') #Enter correct password

#Click on login
browser.find_element_by_id('loginbutton').click()

#Quit once logged in
browser.quit()
