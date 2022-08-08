from selenium import webdriver      # Abre o webdriver do chrome e dá a permissão para acesso a internet /navegador#
from selenium.webdriver.common.keys import Keys    # Dá acesso ao teclado para o Robo
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import xlrd

#INICIANDO VARIÁVEIS GLOBAIS----------------------#
#obs:em caminhos as barras devem ser invertidas, ou utilize o "r" a frente do caminho ex: r'C:\....'#

#ARQUIVO TXT#
arq = open("resultado.txt","w")
#--------------------------------------------------#

#ARQUIVO DO EXCEL# 
workbook = xlrd.open_workbook('C:/Users/fefranci/OneDrive - Stefanini/Python aula/robots/projeto 1 - webscraping/sites.xls')
#ABA DA PLANILHA NO EXCEL#
sheet = workbook.sheet_by_name('Plan1')
#LINHA DA PLANILHA NO EXCEL#
rows = sheet.nrows
#COLUNAS DA PLANILHA DO EXCEL#
columns = sheet.ncols
#-------------------------------------------------------#
#CONTAGEM#
x=0
#-------------------------------------------------------#

#Ocultar os erros emitidos pelo chrome driver#
options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")
#---------------------------------------------#

print("Iniciando boot... \n")
#ABRIR O NAVEGADOR---------------------------------------------------#
#primeiro valida o webDriver online e instala o atualizado automáticamente
validaWebDriver = Service(ChromeDriverManager().install())
#adiciona o caminho do chrome driver para o bot #
driver = webdriver.Chrome(service = validaWebDriver, options=options)#options = options complemento para ocultar os erros#

#ACESSAR O SITE ALVO--------------------------------------------------#
#passa para o navegador chrome driver a url que se deseja acessar#
driver.get("https://registro.br")

#CONSULTAR DADOS PARA PESQUISA-----------------------------------------#
#lista de sites para pesquisa de dominios
#dominios = ["globo.com","uol.com.br","brasil.com.br","magodosboots.com.br","facebook.com.br","abandonados.com.br"]

#INICIAR PESQUISA COLOCANDO OS DADOS NA BARRA DE PESQUISA ----------------------#
#Utilizando o laço de repetição para buscar todos os dominios da lista
for curr_row in range(0,rows):   
        #criando ação para pesquisa dentro do campo de pesquisa
    x = x+1
            #VARIÁVEL x INICIA PEGANDO O VALOR DE CADA CÉLULA NO EXCEL
    dominio = sheet.cell_value(curr_row,0)
    time.sleep(1)
            #insere dentro da variavel pesquisa o id do campo da busca (retirado em inspecionar cod html)
    pesquisa = driver.find_element(By.ID,"is-avail-field")
    time.sleep(1)
            #Após clicar no campo pesquisa o robô irá apagar oq estiver escrito no campo
    pesquisa.clear()      
    time.sleep(1)
            #Agora o robô irá digitar o valor informado em keys 
    pesquisa.send_keys(dominio)
    time.sleep(1)
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
    
#CAPTURANDO O STATUS APÓS PESQUISA--------------------------------------------------#    
    status = driver.find_element(By.XPATH,'//*[@id="app"]/main/section/div[2]/div/p/span/strong').text
    time.sleep(1)
    #Saida da pesquisa , exibe uma mensagem com o dominio e o status do site pesquisado.
    resultPesquisa = ">%s Dominio %s %s \n"%(x,dominio,status)
    #Escreve resultado recebido na variavel texto no arquivo criado .txt#
    arq.write(resultPesquisa)
    
#determina o tempo que a aplicação fica aberta em segundos
#time.sleep(8)

#FINAL DA APLICAÇÃO FECHANDO O NAVEGADOR E ARQUIVO TEXTO----------------------------#
arq.close()
driver.close()
