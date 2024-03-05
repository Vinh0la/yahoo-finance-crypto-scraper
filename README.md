# Crypto Scraper

![Project Image](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Yahoo%21_Finance_logo_2021.png/800px-Yahoo%21_Finance_logo_2021.png)

Este é um web scraper escrito em Python usando Selenium para coletar dados de criptomoedas da página de criptomoedas do Yahoo Finance.

## Pré-requisitos

- Python 3.9
- Pandas
- Selenium
- Google Chrome
- ChromeDriver

Certifique-se de instalar todas as dependências antes de executar o script.

## Instalação

1. Clone este repositório:
   git clone https://github.com/Vinh0la/yahoo-finance-crypto-scraper.git

2. Instale as dependências:
  pip install selenium, pandas

3. Faça o download do ChromeDriver e coloque o arquivo na mesma pasta do script ou atualize a variável `path` no script com o caminho para o ChromeDriver.

4. Execute o script:
   python crypto_scraper.py

## Funcionamento

O script irá coletar os dados das criptomoedas disponíveis na página de criptomoedas do Yahoo Finance. Os dados coletados incluem o nome da criptomoeda, preço e fornecimento circulante. Os dados serão salvos em um arquivo CSV chamado `CryptoCoins.csv`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para relatar bugs ou solicitar novos recursos.








