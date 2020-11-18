#encoding: UTF-8
from time import sleep
import os
import sys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

n = -1
options_0 = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
options_1 = sys.argv[4]
n_user = sys.argv[5]
n_password = sys.argv[6]
head = sys.argv[7]

option = Options()
option.headless = True
firefox_binary = FirefoxBinary('/usr/lib/firefox/firefox')

print('configurando o BOT...')

#zona da conf basica
if (head == '--headless'):
	firefox = webdriver.Firefox(options=option,firefox_binary=firefox_binary)
elif (head == '--head'):
	firefox = webdriver.Firefox(firefox_binary=firefox_binary)

print('BOT configurado.')


#area das funções
def changeip():
	try:
		os.system('curl http://ipecho.net/plain > ip.txt')
		os.system('curl http://ipecho.net/plain > new_ip.txt')
		ip_before = open('ip.txt').read()
		current_ip = open('new_ip.txt').read()
		
		while (current_ip==ip_before):
			os.system('curl http://ipecho.net/plain > new_ip.txt')
			current_ip = open('new_ip.txt').read()
			print('\n\n\nAguardando modficação de ip...\n\n\n')

		print('ip modificado, reiniciando Venomsons')
	except:
		print('algo interrompeu o programa, verifique sua internet ou suas credenciais com protonvpn init')


def gni_login(n_user,n_password,firefox,link):
	print('logando no site: '+link)

	email = firefox.find_element_by_name("email")
	senha = firefox.find_element_by_name("senha")
	email.send_keys(n_user)
	senha.send_keys(n_password)
	senha.send_keys(Keys.ENTER)

	print('logado com sucesso no site: '+link)

	sleep(5)

	firefox.get("https://www.ganharnoinsta.com/painel/?pagina=sistema")  
	
	print('iniciando o loop de ciclos')
	
	sleep(6)

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

def gni(firefox):
	def Venom_actions(firefox):
		
		sleep(4)
		
		try:
			firefox.find_element_by_css_selector('button.aOOlW:nth-child(2)')
					
			print('seu ip foi bloqueado, esse é um BOT filho então ele ira esperar a ordem de BOT_MASTER!\nAguarde até que o ip seja alterado...')
					
			firefox.quit()
			changeip()

			if (head == '--headless'):
				firefox = webdriver.Firefox(options=option,firefox_binary=firefox_binary)
			elif (head == '--head'):
				firefox = webdriver.Firefox(firefox_binary=firefox_binary)

			verifyer(firefox)
		except:
			pass

	def like(firefox):
		try:
			obj_1 = firefox.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
			obj_1.click()

			sleep(3)

			Venom_actions(firefox)

			firefox.close()
			firefox.switch_to_window(firefox.window_handles[0])

			sleep(1)

			confirmar = firefox.find_element_by_id('btn-confirmar')
			confirmar.click()

			print('ciclo concluido com sucesso')
		except:
			print('erro ao concluir o ciclo: verifique sua conexao com a internet e tente de novo.')

	def follow(firefox):
		try:
			try:
				obj_1 = firefox.find_element_by_xpath('//span/span[1]/button')
				obj_1.click()

				Venom_actions(firefox)
			except:
				print('tempo expirado, tentando novamente.')
				sleep(5)
				try: 
					obj_1 = firefox.find_element_by_xpath('//span/span[1]/button')
					obj_1.click()

					Venom_actions(firefox)
				except:
					try:
						obj = firefox.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button')
						obj.click()

						Venom_actions(firefox)
					except:
						obj_2 = firefox.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/div[2]/button')
						obj_2.click()

						sleep(10)

						obj_1 = firefox.find_element_by_xpath('//span/span[1]/button')
						obj_1.click()

						Venom_actions(firefox)

			sleep(3)

			firefox.close()
			firefox.switch_to_window(firefox.window_handles[0])

			sleep(1)

			confirmar = firefox.find_element_by_id('btn-confirmar')
			confirmar.click()

			print('ciclo concluido com sucesso')
		except:
			print('erro ao concluir o ciclo: verifique sua conexao com a internet e tente de novo.\nBOT desligado.')
			quit()

	sleep(5)

	try:
		acessar = firefox.find_element_by_link_text('Acessar Perfil')
		acessar.click()
		
		print('um novo ciclo iniciou')

		sleep(6)
		
		firefox.switch_to_window(firefox.window_handles[-1])

		follow(firefox)
	except:
		acessar = firefox.find_element_by_link_text('Acessar Publicação')
		acessar.click()

		print('um novo ciclo iniciou')

		sleep(6)
		
		firefox.switch_to_window(firefox.window_handles[-1])

		like(firefox)

#fim da area das funções


def verifyer(firefox):
	#area dos logins
	if (options_0 == '-f'):
	#zona do facebook
		try:
			firefox.get('https://www.instagram.com/')
			print('logando no instagram')
			sleep(6)
			face_login(user,password,firefox)
			print('logado com sucesso no instagram \naguarde...')
		except:
			print('erro ao logar no instagram: verifique as credenciais ou conexao com a internet e tente de novo')

	elif (options_0 == '-i'):
	#zona do instagran
		try:
			firefox.get('https://www.instagram.com/')
			print('logando no instagram')
			sleep(6)
			insta_login(user,password,firefox)
			print('logado com sucesso no instagram \naguarde...')
		except:
			print('erro ao logar no instagram: verifique as credenciais ou conexao com a internet e tente de novo')	
	else:
		print('parametro:'+options_0+' não reconhecido')
		quit()

	sleep(15)

	#areas das actions
	if(options_1 == '--gni'):
	#zona do gni
		print('acessando o site: https://www.ganharnoinsta.com/painel/')

		try:
			firefox.get('https://www.ganharnoinsta.com/painel/')
			gni_login(n_user,n_password,firefox,'https://www.ganharnoinsta.com/painel/')
		except:
			print('erro ao logar no site: https://www.ganharnoinsta.com/painel/ verifique susa credenciais e conexao com a internet')

		try:
			while(True):
				gni(firefox)
		except:		
			print('programa encerrado')
	else:
		print('parametro:'+options_1+' não reconhecido')
		quit()

verifyer(firefox)