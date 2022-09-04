import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python' # pagina
response = requests.get(url) # baixando a paina
html = BeautifulSoup(response.text, 'html.parser') # formata o html da pagina

for issues in html.select('.s-post-summary.js-post-summary'): # selecionando objeto pela classe css
    title = issues.select_one('.s-link') # selecionando um elemento por classe css
    date = issues.select_one('.relativetime') # selecionando um elemento por classe css
    vote = issues.select_one('.s-post-summary--stats-item-number') # selecionando um elemento por classe css

    print(date.text, title.text, f'| votos: {vote.text}', sep='\t')