#encoding: UTF-8
import sys
import actions 
import logins
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

#o bloco de codigo a seguir é o bloco de verificação de parametros e execução de funções pensando em expansão no futuro 
if (options_0 == '-f'):
	try:
		firefox.get('https://www.instagram.com/')
		print('logando no instagram')
		sleep(6)
		logins.face_login(user,password,firefox)
		print('logado com sucesso no instagram \naguarde...')
	except:
		print('erro ao logar no instagram: verifique as credenciais ou conexao com a internet e tente de novo')

elif (options_0 == '-i'):
	try:
		firefox.get('https://www.instagram.com/')
		print('logando no instagram')
		sleep(6)
		logins.insta_login(user,password,firefox)
		print('logado com sucesso no instagram \naguarde...')
	except:
		print('erro ao logar no instagram: verifique as credenciais ou conexao com a internet e tente de novo')	
			
else:
	print('parametro:'+options_0+' não reconhecido')
	quit()

sleep(15)

if(options_1 == comand_list[0]):
	try:
		print('acessando o site:'+link_list[0])

		firefox.get(link_list[0])
		logins.gni_login(n_user,n_password,firefox)

		print('logado com sucesso no site: '+link_list[0])
	except:
		print('erro ao logar no site:'+link_list[0]+'verifique susa credenciais e conexao com a internet')

	try:
		print('iniciando o loop de ciclos')
		while(True):
			actions.gni(firefox)
	except:
		print('programa encerrado')
else:
	print('parametro:'+options_1+' não reconhecido')
	quit()
