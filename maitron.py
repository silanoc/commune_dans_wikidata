#https://pypi.org/project/googlesearch-python/
#https://stacklima.com/effectuer-une-recherche-google-a-laide-du-code-python/

import random

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
def lst_maitron():
	# to search
	query = "site:maitron.fr communard"
	lst = []
	#for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	for j in search(query, num_results=100):
	   	lst.append(j)	
	return lst
    
def faire_liste():
	lst_total = lst_maitron()
	return lst_total

def une_page_dans_la_liste(une_liste):
	url = une_liste[random.randint(0, len(une_liste) - 1)]
	print(url)
	print("firefox " + url)

if __name__ == "__main__()":
	les_articles_du_maitron = faire_liste()
	une_page_dans_la_liste(les_articles_du_maitron)
