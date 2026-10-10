import requests
from bs4 import BeautifulSoup


for start_num in range(0,250,25):
    print(start_num)

##请求头伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(f'https://movie.douban.com/top250?start={start_num}', headers=headers)
    if response.ok:
        print("Request was successful!")
    #    print(response.text)
    else:
        print("Request failed with status code:", response.status_code)

    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    all_movie_name = soup.find_all('span', attrs={"class": "title"})
    for movie_name in all_movie_name:
        if "/" not in movie_name.string :
            print(movie_name.string)

# content = requests.get('https://books.toscrape.com').text
# soup = BeautifulSoup(content, 'html.parser')

# all_price = soup.find_all('p',attrs={"class" : "price_color"} )
# for price in all_price:
#     print(price.string)

# all_bookname = soup.find_all('h3')
# for bookname in all_bookname:
#     find = bookname.find('a')
#     print(find.string)

