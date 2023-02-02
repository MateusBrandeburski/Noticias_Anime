import scrapy


class NoticiasSpider(scrapy.Spider):
    name = "noticias"
    allowed_domains = ["animenew.com.br"]
    start_urls = ["https://animenew.com.br/noticias/animes/"]

    def parse(self, response):
        
        contador = 0
        for noticias in response.css('.elementor-post__title'):
            contador += 1
        
            
            yield{
                f'noticias {contador}' : noticias.css('.elementor-post__title').extract()
            }
            
            noticias = response.css('.load-more-align-center a::text').get
            
            print(noticias)

