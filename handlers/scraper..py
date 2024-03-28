import httpx
from parsel import Selector

async def fetch_anime_links():
    url = "https://animespirit.tv/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        selector = Selector(text=response.text)
        links = selector.css('.main-news .news-title a::attr(href)').getall()
    return links

