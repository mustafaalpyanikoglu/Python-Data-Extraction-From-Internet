import requests
from bs4 import BeautifulSoup
IMDURL1="https://www.imdb.com/chart/top"

r=requests.get(IMDURL1)
soup = BeautifulSoup(r.content,"html.parser")

data= soup.find_all("table",{"class":"chart full-width"})
#print((data))
print("---------------------")
#print(len(data)) #"class" adı "chart full-width" olan bir tablo vardır

moviePainting= (data[0].contents)[len(data[0].contents)-2]
#print(moviePainting)

moviePainting=moviePainting.find_all("tr")
for film in moviePainting:
    movieTitles=film.find_all("td",{"class":"titleColumn"})
    filmMove = movieTitles[0].text
    filmMove=filmMove.replace("\n","") #her bir '\n' i "" karakteri ile değiştirdik
    print((filmMove))
    print("---------")


