import requests
from bs4 import BeautifulSoup

headers = {
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'	
}

url = input('Quizlet URL to import: ')

print('Making request...')
req = requests.get(url, headers=headers)

if (req.status_code == 200):
	print('Got good response (%d)' % req.status_code)
else:
	print('Got bad response (%d)' % req.status_code)

soup = BeautifulSoup(req.content, 'html.parser')

terms = soup.find_all(class_='SetPageTerms-term')

for term in terms:
	termText = term.find_all(class_='TermText')
	frontText = termText[0].get_text()
	backText = termText[1].get_text()
	print(frontText, ':', backText)