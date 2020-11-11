#encoding: UTF-8
import sys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
from selenium.webdriver.common.keys import Keys

link_list = ['https://www.ganharnoinsta.com/painel/']
comand_list = ['--gni']

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

if (head == '--headless'):
	firefox = webdriver.Firefox(options=option,firefox_binary=firefox_binary)
elif (head == '--head'):
	firefox = webdriver.Firefox(firefox_binary=firefox_binary)

print('BOT configurado.')

def gni(firefox):
	sleep(5)
	acessar = firefox.find_element_by_link_text('Acessar Perfil')
	acessar.click()
	
	sleep(6)

	firefox.switch_to_window(firefox.window_handles[-1])
	
	print('um novo ciclo iniciou')

	try:
		try:
			obj_1 = firefox.find_element_by_xpath('//span/span[1]/button')
			obj_1.click()
		except:
			obj = firefox.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button')
			obj.click()

		sleep(3)

		firefox.close()
		firefox.switch_to_window(firefox.window_handles[0])

		sleep(1)

		confirmar = firefox.find_element_by_id('btn-confirmar')
		confirmar.click()

		print('ciclo concluido com sucesso')
	except:
		print('erro ao concluir o ciclo: verifique sua conexao com a internet e tente de novo.')

def face_login(user,password,firefox):
	firefox.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button/span[2]').click()
	firefox.find_element_by_id('email').send_keys(user)
	firefox.find_element_by_id('pass').send_keys(password)
	firefox.find_element_by_id('loginbutton').send_keys(Keys.ENTER)

def insta_login(user,password,firefox):
	firefox.find_element_by_name('username').send_keys(user)
	firefox.find_element_by_name('password').send_keys(password)
	firefox.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').send_keys(Keys.ENTER)

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

#o bloco de codigo a seguir é o bloco de verificação de parametros e execução de funções pensando em expansão no futuro (ainda em trabalho)
if (options_0 == '-f'):
	try:
		firefox.get('https://www.instagram.com/')
		print('logando no instagram')
		sleep(6)
		face_login(user,password,firefox)
		print('logado com sucesso no instagram \naguarde...')
	except:
		print('erro ao logar no instagram: verifique as credenciais ou conexao com a internet e tente de novo')

elif (options_0 == '-i'):
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

if (options_1 != comand_list[0]):
	print('parametro:'+options_1+' não reconhecido')
	quit()
else:
	print('acessando o site:'+link_list[0])
	firefox.get(link_list[0])
	gni_login(n_user,n_password,firefox)
	print('logado com sucesso no site: '+link_list[0])
#fim do bloco de verificação

try:
	print('iniciando o loop de ciclos')
	while(True):
		gni(firefox)
except:
	print('programa encerrado')