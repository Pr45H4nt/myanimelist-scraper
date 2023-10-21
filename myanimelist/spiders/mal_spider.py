import scrapy


class MalSpiderSpider(scrapy.Spider):
    name = "mal_spider"
    
    start_urls = ["https://myanimelist.net/topanime.php"]

    def parse(self, response):
        links = response.xpath('//tr[@class="ranking-list"]//td[contains(@class , "title")]/a[1]/@href').getall()
        for link in links:
            yield scrapy.Request(
                url = link, 
                callback=self.parse_details
            )

        next_btn = response.xpath('//a[@class="link-blue-box next"]/@href').get()
        if next_btn:
            yield scrapy.Request(
                url = "https://myanimelist.net/topanime.php" + next_btn, 
                callback=self.parse,

            )

    def parse_details(self, response):
        title = response.xpath('//meta[@property="og:title"]/@content').get()
        plot = response.xpath('//meta[@property="og:description"]/@content').get()
        poster = response.xpath('//meta[@property="og:image"]/@content').get()
        rating = response.xpath('//div[@data-title="score"]/div/text()').get()
        people_rated = response.xpath('//div[@data-title="score"]/@data-user').get()
        japanese_name = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Japanese:"]/following-sibling::text()').get()
        if japanese_name:
            japanese_name= japanese_name.strip()

        episodes = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Episodes:"]/following-sibling::text()').get()
        if episodes:
            episodes = episodes.strip()

        status = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Status:"]/following-sibling::text()').get()
        if status:
            status = status.strip()
        
        aired = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Aired:"]/following-sibling::text()').get()
        if aired:
            aired = aired.strip()
        
        
        duration = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Duration:"]/following-sibling::text()').get()
        if duration:
            duration = duration.strip()
        
        popularity = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Popularity:"]/following-sibling::text()').get()
        if popularity:
            popularity = popularity.strip()
        
        
        certificate = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Rating:"]/following-sibling::text()').get()
        if certificate:
            certificate = certificate.strip()

        members = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Members:"]/following-sibling::text()').get()
        if members:
            members = members.strip()

        favourites = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Favorites:"]/following-sibling::text()').get()
        if favourites:
            favourites = favourites.strip()

        producers = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Producers:"]/following-sibling::a/text()').getall()        
        licensors = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Licensors:"]/following-sibling::a/text()').getall()        
        genre = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Genres:"]/following-sibling::a/text()').getall()        
        studios = response.xpath('//div[@class="spaceit_pad"]/span[@class="dark_text"][text()= "Studios:"]/following-sibling::a/text()').getall()        

        anime_data = {
            "TITLE": title,
            "PLOT": plot,
            "POSTER": poster,
            "RATING": rating,
            "PEOPLE_RATED": people_rated,
            "JAPANESE_NAME": japanese_name,
            "EPISODES": episodes,
            "STATUS": status,
            "AIRED": aired,
            "DURATION": duration,
            "POPULARITY": popularity,
            "CERTIFICATE": certificate,
            "MEMBERS": members,
            "FAVOURITES": favourites,
            "PRODUCERS": producers,
            "LICENSORS": licensors,
            "GENRE": genre,
            "STUDIOS": studios
        }
        for key , value in anime_data.items():
            if value == "add some":
                anime_data[key] = None
        
        yield anime_data

        
