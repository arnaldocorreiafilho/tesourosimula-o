from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas
import json
import io
import  Investimento



def get_data():

    df = pandas.read_csv('calculo_tesouro.csv',names=["data","juros","investimento","taxa_projetada"],header=None ,delimiter=";")


    display = Display(visible=0, size=(800, 600))
    display.start()

    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    firefox_capabilities['binary'] = '/usr/bin/firefox'

    b = webdriver.Chrome()
    b.wait = WebDriverWait(b, 5)


    lista_inv =[]

    b.get("http://sisnet.tesouro.gov.br/CalculadoraTesouroDireto/calculadora_novosite.aspx")
    # navigate to the page

    b.set_script_timeout(30)
    b.set_page_load_timeout(30)
    mes = "mes"
    numero_mes = 1
    soma = 0.0
    for index, row in df.iterrows():
        inv = Investimento.investimento()
        dic_investimento = {}
        b.find_element_by_id('btnLimpar').click()

        option_visible_text = "Tesouro IPCA+ (NTN-B Principal)"
        select = b.wait.until(EC.presence_of_element_located(
                (By.NAME, "cbTitulo")))

    #now use this to select option from dropdown by visible text
        b.execute_script("var select = arguments[0]; for(var i = 0; i < select.options.length; i++){ if(select.options[i].text == arguments[1]){ select.options[i].selected = true;  } }", select, option_visible_text)


        inputDataCompra = b.find_element_by_id("txtDtCompra")
        inputDataCompra.send_keys((str(row.data)))
        dataCompra = inputDataCompra.get_attribute("value")
        print  dataCompra
        inv.data_compra = dataCompra

        b.execute_script("document.getElementById('cbTitulo').onchange();")

        # now you dropdown will be open

        # now you dropdown will be open


        b.find_element_by_xpath("//select[@id='cbTitulo']/option[text()='Tesouro IPCA+ (NTN-B Principal)']").click()
        #this will click the option which text is custom and onchange event will be triggered.




        inputVencimento = b.find_element_by_id("txtDtVencimento")
        inputVencimento.send_keys("05/05/2035")
        vencimento = inputVencimento.get_attribute("value")
        print vencimento
        inv.data_vencimento = vencimento

        inputValor = b.find_element_by_id("txtValorInvestido")
        inputValor.send_keys(str(row.investimento))
        valor = inputValor.get_attribute("value")
        print valor
        inv.valor_investimento = valor

        inputTaxaCompra = b.find_element_by_id("txtTaxaCompra")
        inputTaxaCompra.send_keys(str(row.juros))
        taxaCompra = inputTaxaCompra.get_attribute("value")
        print  taxaCompra
        inv.taxa_compra = taxaCompra

        inputTaxaAdm = b.find_element_by_id("txtTaxaAdministracao")
        inputTaxaAdm.send_keys("0")
        taxaInput = inputTaxaAdm.get_attribute("value")
        print taxaInput
        inv.taxa_adm = taxaInput



        inputInflacao = b.find_element_by_id("txtTaxaGenerica")
        inputInflacao.send_keys(str(row.taxa_projetada))
        taxaInflacao = inputInflacao.get_attribute("value")
        print taxaInflacao
        inv.taxa_inflacao = taxaInflacao

        b.find_element_by_id('btnCalcular').click()

        valorLiquido = b.find_element_by_id("lblVendaLiquido")
        valor = valorLiquido.text
        valor2 =  (valor[2:])

        value = valor2.replace(".", '')
        value = value.replace(",", '.')


        print "o valor liquido e " ,valor +"\n"
        print "o valor liquido e  value", value
        inv.valor_liquido = value
        soma = soma +  float(value)
        dic_investimento = inv.__dict__
        #dic_investimento["data_compra"] = inv.data_compra
        #dic_investimento["valor_investimento"] = inv.valor_investimento
        #dic_investimento["data_vencimento"] = inv.data_vencimento
        #dic_investimento["taxa_compra"] = inv.taxa_compra
       # dic_investimento["taxa_adm"] = inv.taxa_adm
        #dic_investimento["taxa_inflacao"] = inv.taxa_inflacao
        lista_inv.append(dic_investimento)
        numero_mes = numero_mes + 1
       #

    print soma

    display.stop()
    return  json.dumps(lista_inv)


