import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python' 
response = requests.get(url) 
html = BeautifulSoup(response.text, 'html.parser') 

for issues in html.select('.s-post-summary.js-post-summary'): 
    title = issues.select_one('.s-link')
    date = issues.select_one('.relativetime') 
    vote = issues.select_one('.s-post-summary--stats-item-number') 

    print(date.text, title.text, f'| votos: {vote.text}', sep='\t')