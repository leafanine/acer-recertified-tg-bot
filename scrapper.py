import requests

filename = "acer-store.csv"
f = open(filename, "w")
f.close()

from bs4 import BeautifulSoup
url = "https://store.acer.com/en-in/acer-recertified/recertified-laptops?product_list_limit=all"
with requests.Session() as session:
    page = session.get(
        url,
        timeout=10,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'},
        allow_redirects=True
    )
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.find('ol', {"class": 'products list items product-items'})
    item = items.find_all('li', {"class": 'item product product-item'})
    link = items.find_all('a', {"class": 'product-item-link'})
    price = items.find_all('span', {"class": 'price'})
    price = price[1::2] # discounted price
    actions = items.find_all('div', {"class": 'product actions product-item-actions'})
    
    # images = soup.find_all('img', {"class": 'product-image-photo mf-loaded'})
    # j=0
    # for all in images:
    #     img_data=requests.get(images[j]['src']).content
    #     with open(f'images/image{j}.jpg','wb+') as f:
    #         f.write(img_data)
    #     j=j+1
        
    
    with open('acer-store.csv', 'a', encoding="UTF-8") as f:
        f.write("item, price, available, link")
        f.close()
    for i in range(1,len(item)):
        available = actions[i].find('div', {"class": 'stock available'})
        if available is not None:
            available = "Available"
        else:
            available = "Unavailable"
        data = f"\n\"{link[i].text.lstrip().lstrip('Acer Recertified').rstrip().replace(',', '')}\", \"{price[i].text.replace(',', '').replace('₹','INR ')}\", \"{available}\", \"{link[i].get('href')}\""    
        with open('acer-store.csv', 'a', encoding="UTF-8") as f:
            f.write(data)
            f.close()