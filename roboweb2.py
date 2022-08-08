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

dominio= "globo.com"
        #Agora o robô irá digitar o valor informado em keys 
pesquisa.send_keys(dominio)
        #Agora o robô irá dar ENTER 
pesquisa.send_keys(Keys.RETURN)
time.sleep(2) #tempo para recarregamento da página#
#---------------------------------------#

#busca o caminho do codigo html no site, para capturar o xpath no site 
#primeiro procure o elemento via inspecionar no navegador
#segundo clique com o botão direito , copiar , copiar xpath
#terceiro colar no código do boot
#No código abaixo a variável status recebe o resultado da busca (site disponivel ou não disponivel)
#transformado em texto 

status = driver.find_element_by_xpath ('//*[@id="app"]/main/section/div[2]/div/p/span/strong').text

#Saida da pesquisa , exibe uma mensagem com o dominio e o status do site pesquisado.
print("Dominio %s %s "%(dominio,status))

#determina o tempo que a aplicação fica aberta em segundos
time.sleep(8)
driver.close()
