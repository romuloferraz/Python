import requests
requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = requisicao.json()
dolar = float(cotacao['USD']['bid'])
btc = float(cotacao['BTC']['bid'])*1000
carteira = float(input('Quantos reais você tem na carteira?\nR$'))
print(f'A cotação do dólar no momento é de R${dolar}\n'
      f'você tem o equivalente a U$${carteira/dolar:.2f}\n'
      f'A cotação do BTC no momento é de R${btc}\n'
      f'você tem o equivalente a {carteira/btc:.3f} BTC!')
