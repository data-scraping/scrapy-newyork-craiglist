import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['https://newyork.craigslist.org/search/egr']
    start_urls = ['http://newyork.craigslist.org/search/egr/']

    def parse(self, response):
        # Get titles jobs
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        for title in titles:
            yield {'Title' : title}