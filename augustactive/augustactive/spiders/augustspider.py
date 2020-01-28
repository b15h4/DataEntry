import scrapy
from ..items import AugustactiveItem

class AugustSpider(scrapy.Spider):
    name = 'augustactive'
    allowed_domains = ['augustaactive.com']
    start_urls = [
        'https://www.augustaactive.com/sports/baseball',
        'https://www.augustaactive.com/sports/basketball',
        'https://www.augustaactive.com/sports/cheerleader-uniforms',
        'https://www.augustaactive.com/sports/football',
        'https://www.augustaactive.com/sports/field-hockeylacrosse',
        'https://www.augustaactive.com/sports/soccer',
        'https://www.augustaactive.com/sports/tennis',
        'https://www.augustaactive.com/sports/trackcross-country',
        'https://www.augustaactive.com/sports/rugby']

    def parse(self,response):
        product_names = response.xpath("//h2[@class='product-name']/a/text()").extract()
        style_numbers = response.xpath("//div[@class='style-number ng-binding ng-scope']/text()").extract()
        prices = response.xpath("//div[@class='price-box']/@price").extract()
        links = response.xpath("//li[@class='item ng-scope']/a/@href").extract()

        items = []

        for product_name,style_number,price,link in zip(product_names,style_numbers,prices,links):
            item = AugustactiveItem()
            item['product_name'] = product_name.strip()
            item['style_number'] = style_number.strip()
            item['price'] = price.strip()
            item['link'] = response.urljoin(link).strip()
            items.append(item)
            yield item