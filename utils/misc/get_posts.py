import requests
from bs4 import BeautifulSoup

url = "https://kun.uz/uz/news/category/jahon"


def get_news_detail(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    single_content = soup.find('div', attrs={"class": "single-content"})
    subtitle = single_content.find("h4")
    context = ""
    for item in single_content.find_all("p"):
        context += f"{item}\n"

    return subtitle, context


def posts(link):
    data = []
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    news = soup.find_all("div", attrs={"class": "news"})
    for n in news:
        img = n.find_next("a").find("img")
        hour = n.find_next('div').find('span')
        title = n.find_next('a', attrs={'class': 'news__title'})
        if len(hour.text.split("/")) == 1:
            news_link = "https://kun.uz" + title['href']
            context = get_news_detail(news_link)
            data.append(
                {
                    "img": img['src'],
                    "title": title.text,
                    "context": context,
                    "date": hour.text,
                    "news_link": news_link,
                }
            )
    return data[:3]
