import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
    

class NoticiasSpider(scrapy.Spider):
    name = "noticias"
    allowed_domains = ["animenew.com.br"]
    start_urls = ["https://animenew.com.br/noticias/animes/"]

    def parse(self, response):
        global raspagem
        contador = 0
        for noticias in response.css('.load-more-align-center a'):
            raspagem = noticias.css('a::text').get() 
            contador = contador+1
            print(raspagem)
            print(contador)

def start():
    process = CrawlerProcess(get_project_settings())

    process.crawl(NoticiasSpider)
    process.start()

start()