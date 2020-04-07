from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
"profile.default_content_setting_values.notifications": 1 
})

def facebook_message(email='',password='',message='',profile_names=['']):
	"""
	Send messages on facebook
	"""
	url = "https://facebook.com"

	driver = webdriver.Chrome(chrome_options=option)
	driver.get(url)
	sleep(1)
	email_box = driver.find_element_by_xpath('//*[@id="email"]')
	password_box = driver.find_element_by_xpath('//*[@id="pass"]')
	login_btn = driver.find_element_by_xpath('//*[@id="u_0_b"]')
	email_box.send_keys(email)
	password_box.send_keys(password)
	login_btn.click()
	try:
		for name in profile_names:
			message_link = 'https://www.facebook.com/messages/t/{}'.format(profile_name)
			driver.get(message_link)
			sleep(2)
			actions = ActionChains(driver)
			actions.send_keys(message)
			actions.send_keys(Keys.ENTER)
			actions.perform()
			sleep(2)
	except Exception as e:
		print('something error:{}'.format(e))

def send_reddit_chat(username='',password='',message='',user_names=['']):
	"""
	Send reddit directs
	"""
	driver = webdriver.Chrome(chrome_options=option)
	driver.get('https://www.reddit.com/login')
	username_input = driver.find_element_by_id('loginUsername')
	password_input = driver.find_element_by_id('loginPassword')
	signin_button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/fieldset[5]/button')
	username_input.send_keys(username)
	password_input.send_keys(password)
	signin_button.click()
	sleep(4)
	for user_name in user_names:
		try:
			url = "https://www.reddit.com/user/{}".format(user_name)
			driver.get(url)
			sleep(2)
			chat_button = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[5]/div[2]/div/div[1]/div/div[5]/div[2]/button')
			chat_button.click()
			sleep(4)
			actions = ActionChains(driver)
			actions.send_keys(message)
			actions.send_keys(Keys.ENTER)
			actions.perform()
			sleep(2)
		except:
			print('bad user')

def instagram_dm_automation(username,password,message='',users=['']):
	"""
	Send instagram dms
	"""
	driver = webdriver.Chrome(chrome_options=option)
	driver.get('https://www.instagram.com/accounts/login/')
	sleep(3)
	username_input = driver.find_element_by_name('username')
	password_input = driver.find_element_by_name('password')
	username_input.send_keys(username)
	password_input.send_keys(password)
	login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
	login_button.click()
	sleep(3)
	for user in users:
		driver.get('https://www.instagram.com/{}/'.format(user))
		sleep(6)
		message_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button')
		message_button.click()
		sleep(4)
		actions = ActionChains(driver)
		actions.send_keys(message)
		actions.send_keys(Keys.ENTER)
		actions.perform()