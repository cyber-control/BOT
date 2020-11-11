#encoding: UTF-8
from time import sleep
from selenium.webdriver.common.keys import Keys

def gni(firefox):
	def like(firefox):
		try:
			obj_1 = firefox.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
			obj_1.click()

			sleep(3)

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

	sleep(5)
	try:
		acessar = firefox.find_element_by_link_text('Acessar Perfil')
		acessar.click()
		
		sleep(6)
		
		firefox.switch_to_window(firefox.window_handles[-1])
		print('um novo ciclo iniciou')

		follow(firefox)
	except:
		acessar = firefox.find_element_by_link_text('Acessar Publicação')
		acessar.click()

		sleep(6)
		
		firefox.switch_to_window(firefox.window_handles[-1])
		print('um novo ciclo iniciou')

		like(firefox)