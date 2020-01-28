# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from soccerway.items import SoccerwayItem
import xlsxwriter
import string

class SoccerwayPipeline(object):
	def __init__(self):
		self.Soccer_obj = SoccerwayItem()
		self.row = 1
		self.col = 0
	
	def open_spider(self,spider):
		self.workbook = xlsxwriter.Workbook(filename="SoccerOutput.xlsx")
		self.spreadsheet = self.workbook.add_worksheet(name="SoccerWay")
		self.fields = self.Soccer_obj.fields.keys()
		cell_format = self.workbook.add_format({'bold': 1, 'bg_color': 'green'})
		self.spreadsheet.write("A1", "TeamA", cell_format)
		self.spreadsheet.write("B1", "TeamB", cell_format)
		self.spreadsheet.write("C1", "Score", cell_format)

	def close_spider(self,spider):
		self.workbook.close()
	
	def process_item(self,item,spider):
		for field in self.fields:
			self.spreadsheet.write(self.row,self.col,item['TeamA'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['TeamB'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['Score'])
			self.col=0

		self.row +=1
		self.col = 0
		return item