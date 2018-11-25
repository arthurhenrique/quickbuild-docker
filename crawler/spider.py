import scrapy
import requests

class LoginQb(scrapy.Spider):
    name = 'quickbuild'

    start_urls = ['http://127.0.0.1:8810/signin?0-1.IFormSubmitListener-form']
    
    def parse(self, response):

        return scrapy.FormRequest.from_response(
            response,
            formdata={'id1_hf_0': '','userName': 'admin', 'password': 'admin'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "User name and password must be specified." in str(response.body):
            self.logger.error("Login failed")
            return
        else:
            return scrapy.Request(url="http://127.0.0.1:8810/grid/active_nodes",
               callback=self.active_nodes)
    
    def active_nodes(self, response):
        print("--------------->", response.xpath('/html/body/div[8]/div[4]/div/div[2]/div/div[2]/div[2]/table/tbody/tr/td[3]/span/a/span').extract())
