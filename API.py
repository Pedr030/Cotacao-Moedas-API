import requests

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL,JPY-BRL,ARS-BRL')

cotacao_dolar = float(cotacoes.json()['USDBRL']['bid'])
cotacao_euro = float(cotacoes.json()['EURBRL']['bid'])
cotacao_libra = float(cotacoes.json()['GBPBRL']['bid'])
cotacao_iene = float(cotacoes.json()['JPYBRL']['bid'])
cotacao_peso_argentino = float(cotacoes.json()['ARSBRL']['bid'])


print("\tCOTAÇÕES DAS PRINCIPAIS MOEDAS DO MUNDO\n")
print("Cotação do Dólar Americano - R${:.4f}".format(cotacao_dolar))
print("Cotação do Euro - R${:.4f}".format(cotacao_euro))
print("Cotação da Libra Esterlina - R${:.4f}".format(cotacao_libra))
print("Cotação do Iene Japonês - R${:.4f}".format(cotacao_iene))
print("Cotação do Peso Argentino - R${:.4f}".format(cotacao_peso_argentino))



