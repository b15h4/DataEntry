import scrapy
from ..items import SoccerwayItem

class SoccerWaySpider(scrapy.Spider):
	name = 'soccerwayspy'

	#### ---!!!     ADD LINKS HERE !!!--- ####
	start_urls = [
		'https://int.soccerway.com/national/england/premier-league/20182019/regular-season/r48730/matches/',
		'https://int.soccerway.com/national/greece/super-league/19981999/1st-round/r906/matches/',
		'https://int.soccerway.com/national/albania/super-league/20182019/regular-season/r48259/matches/?ICID=PL_3N_02'
	]


	def parse(self,response):
		TeamsA = response.xpath("//td[@class='team team-a ']/a/text()").extract()
		TeamsB = response.xpath("//td[@class='team team-b ']/a/text()").extract()
		Scores = response.xpath("//td[@class='score-time score']/a/text()").extract()
		Dates = response.xpath("//td[@class='date no-repetition']/text()").extract()

		for TeamA,TeamB,Score in zip(TeamsA,TeamsB,Scores):
			item = SoccerwayItem()
			item['TeamA'] = TeamA.strip()
			item['TeamB'] = TeamB.strip()
			item['Score'] = Score.strip()
			yield item
