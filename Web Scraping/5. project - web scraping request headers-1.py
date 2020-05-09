#1 爬取猫眼电影信息，将电影名称，主演，上映时间爬取下来
# 爬取地址： url = https://maoyan.com/board 
#爬取内容：电影名称，主演，上映时间：
# <div class="movie-item-info">

#         <p class="name"><a href="/films/337058" title="不期而遇" data-act="boarditem-click" data-val="{movieId:337058}">不期而遇</a></p>

#         <p class="star">

#                 主演：张雨绮,张亮,王少雍

#         </p>

# <p class="releasetime">上映时间：2017-05-19</p>    </div>

import requests
from bs4 import BeautifulSoup

url = "https://maoyan.com/board"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}

response = requests.get(url=url, headers=headers)
print(response.status_code)

bs_movie = BeautifulSoup(response.text, 'html.parser')

movie_list = bs_movie.find_all("div", class_="movie-item-info")

for movie in movie_list:
    movie_name = movie.find('a')['title']
    movie_actor = movie.find('p', class_='star').text.replace(' ','').replace('\n','')
    movie_releasetime = movie.find('p', class_='releasetime').text.replace(' ','').replace('\n','')
    print(movie_name,movie_actor,movie_releasetime)