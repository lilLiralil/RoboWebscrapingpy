from selenium import webdriver      # Abre o webdriver do chrome e dá a permissão para acesso a internet /navegador#
from selenium.webdriver.common.keys import Keys    # Dá acesso ao teclado para o Robo
import time

#Ocultar os erros emitidos pelo chrome driver#
options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")
#---------------------------------------------#
#adiciona o caminho do chrome driver para o bot #
driver = webdriver.Chrome('C:/Users/fefranci/OneDrive - Stefanini/Python aula/robots/chromedriver', options=options)#options = options complemento para ocultar os erros#

#passa para o navegador chrome driver a url que se deseja acessar#
driver.get("https://registro.br")

#criando ação para pesquisa dentro do campo de pesquisa
        #insere dentro da variavel pesquisa o id do campo da busca (retirado em inspecionar cod html)
pesquisa = driver.find_element_by_id("is-avail-field")
        #Após clicar no campo pesquisa o robô irá apagar oq estiver escrito no campo
pesquisa.clear
        #Agora o robô irá digitar o valor informado em keys 
pesquisa.send_keys("globo.com")
        #Agora o robô irá dar ENTER 
pesquisa.send_keys(Keys.RETURN)


#determina o tempo que a aplicação fica aberta em segundos
time.sleep(8)
driver.close()
