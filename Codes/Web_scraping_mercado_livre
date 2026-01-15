import requests 
from bs4 import BeautifulSoup 

# USER AGENT, this is extremely important, because it informs the server who are doing the data request, in this case, a browser 

header = { 
    'User-Agent' : 
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' 
} 

# PRODUCT SELECTION 

product = input("Type your product: ") 
product = product.replace(' ','-') 

# URL BASE 

url = f'https://lista.mercadolivre.com.br/{product}_Desde_' 

# COUNT 

start = 1 

# SCRAPING LOOP 

loop = 0 
while loop == 0: 
    final_url = url + str(start) + '_NoIndex_True' 
    
    # REQUEST 
    r = requests.get(final_url,headers=header) 
    site = BeautifulSoup(r.content,'html.parser') 
    
    # FINDING THE RESULTS 
    
    descriptions = site.find_all('h3', class_= 'poly-component__title-wrapper') 
    prices = site.find_all('span', class_ = 'andes-money-amount__fraction') 
    links = site.find_all('a', class_ = 'poly-component__title') 
    
    if not descriptions: 
        print("No more products") 
        loop = 1 
    
    # DATA CAPTURE 
    for description, price, link in zip(descriptions, prices, links): 
        print('\033[mPRODUCT : ' + description.get_text()) 
        print('\033[32mPRICE : R$' + price.get_text()) 
        print(f'\033[34mLINK : {link.get("href")}\n') 
    
    # PAGES INDEX 
    start += 48
