from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        section = response.css("section#index-by-category")
        tables = section.css("table")
        search_headers = {"PEP", "Title", "Authors"}

        for table in tables:
            headers = {th.css("::text").get() for th in table.css("th")}
            if search_headers & headers != search_headers:
                continue

            for row in table.css("tbody tr"):
                pep_number = row.css("td:nth-child(2) a::text").get()
                pep_link = row.css("td:nth-child(2) a::attr(href)").get()
                pep_link = urljoin(response.url, pep_link)

                yield response.follow(
                    pep_link,
                    self.parse_pep,
                    cb_kwargs={"number": pep_number}
                )

    def parse_pep(self, response, number):
        status = response.css("abbr::text").get()
        name = response.css("h1.page-title::text").get()
        yield PepParseItem(number=number, name=name, status=status)
