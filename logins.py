from time import sleep
from selenium.webdriver.common.keys import Keys

def gni_login(n_user,n_password,firefox):
	email = firefox.find_element_by_name("email")
	senha = firefox.find_element_by_name("senha")
	email.send_keys(n_user)
	senha.send_keys(n_password)
	senha.send_keys(Keys.ENTER)

	sleep(5)
	firefox.get("https://www.ganharnoinsta.com/painel/?pagina=sistema")  
	sleep(2)

	button = firefox.find_element_by_id("btn_iniciar")
	button.click()

def face_login(user,password,firefox):
	firefox.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button/span[2]').click()
	firefox.find_element_by_id('email').send_keys(user)
	firefox.find_element_by_id('pass').send_keys(password)
	firefox.find_element_by_id('loginbutton').send_keys(Keys.ENTER)

def insta_login(user,password,firefox):
	firefox.find_element_by_name('username').send_keys(user)
	firefox.find_element_by_name('password').send_keys(password)
	firefox.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').send_keys(Keys.ENTER)