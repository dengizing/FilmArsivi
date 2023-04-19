#themoviedb.org => film ve dizi arşivi
#themoviedb'nin dunfuğu spyi uygulamanızda kullanınız
#Anahtar kelimeye göre arama
#En popüler film listesi
#Vizyondaki film listesi


import requests #alt+enter
class theMovieDb:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3"#sitenin adresş ve keyini kydum
        self.api_key="e8a9d5f82d78ca210c8076d648685c12"
        #https://api.themoviedb.org/3/movie/popular?api_key=e8a9d5f82d78ca210c8076d648685c12&language=en-US&page=1
    def getPopulars(self):
        #En popülerleri alıyorum.
        response =requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")#request modülüyle get sorgusu sayesinde popülerlerin bilgisini alıyorum
        print(response.json)
        return response.json()#dönen bilgiyide pytonda kullana bildiğim json(sözcük veri yapısı) a çeviriyorum.

    def getSearchResults(self,keyword):
        response =requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi=theMovieDb()

while True:
    secim =input("1-Popular Movies\n2-Search Movies\n3-Exit\nSecim:  ")#kullanıcı 1 e basarsa popüler filmler,2 ye basarsa çıkış yapar.

    if secim=="3":#Eğer seçim 2 ise direk çıksın
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars() #1 e bastığımızda popüler filmleri getirmesini istiyorum.
            for movie in movies['results']:#movies in içindeki result bilgilerini alıcak
                    print(movie['title'])#gelen movieleri ekrana yaazdıralım

        if secim == "2":
            keyword=input('keyword: ')
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                    print(movie['name'])

