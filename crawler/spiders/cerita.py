import scrapy  #Import library
from scrapy.selector import HtmlXPathSelector

class Cerita(scrapy.Spider):
    #Nama spider
    name = "cerita"

    #Membatasi domain yg akan di crawling
    allowed_domains = ["ceritabokep.me"]

    #Domain yg akan di crawling
    start_urls = ['http://ceritabokep.me/']

    def parse(self, response):
        urls = response.css('div.post_text_inner > h5.entry_title > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        #follow pagination link
        for next_page in response.css('li > a.inactive::attr(href)'):
            yield response.follow(next_page, self.parse)
            
    def parse_details(self, response):
        yield {
            'content': " ".join(response.xpath('//body').extract())
        }
