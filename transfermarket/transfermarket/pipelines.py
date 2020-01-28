# -*- coding: utf-8 -*-
from transfermarket.items import TransfermarketItem
import xlsxwriter
import string
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TransfermarketPipeline(object):
	def __init__(self):
		self.obj = TransfermarketItem()
		self.row = 1
		self.col = 0
	
	def open_spider(self,spider):
		self.workbook = xlsxwriter.Workbook(filename="TransferMarketTable.xlsx")
		self.spreadsheet = self.workbook.add_worksheet(name="TransferMarket")
		self.fields = self.obj.fields.keys()
		cell_format = self.workbook.add_format({'bold': 1, 'bg_color': 'green'})
		self.spreadsheet.write("A1", "club_name", cell_format)
		self.spreadsheet.write("B1", "club_link_TFM", cell_format)
		self.spreadsheet.write("C1", "loan_players", cell_format)
		self.spreadsheet.write("D1", "loan_players_link", cell_format)
		self.spreadsheet.write("E1", "average_loan_period_in_years", cell_format)
		self.spreadsheet.write("F1", "appearances", cell_format)
		self.spreadsheet.write("G1", "starting_formation", cell_format)
		self.spreadsheet.write("H1", "goals", cell_format)
		self.spreadsheet.write("I1", "average_minutes_played", cell_format)
		self.spreadsheet.write("J1", "loan_fee", cell_format)
		self.spreadsheet.write("K1", "market_value_at_start_of_loan", cell_format)
		self.spreadsheet.write("L1", "filter_season_id_TFM", cell_format)
		self.spreadsheet.write("M1", "filter_loan_type_TFM", cell_format)

	def close_spider(self,spider):
		self.workbook.close()
	
	def process_item(self,item,spider):
		for field in self.fields:
			self.spreadsheet.write(self.row,self.col,item['club_name'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['club_link_TFM'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['loan_players'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['loan_players_link'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['average_loan_period_in_years'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['appearances'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['starting_formation'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['goals'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['average_minutes_played'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['loan_fee'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['market_value_at_start_of_loan'])
			self.col+=1
			self.spreadsheet.write(self.row,self.col,item['filter_season_id_TFM'])
			self.col+=1																		
			self.spreadsheet.write(self.row,self.col,item['filter_loan_type_TFM'])
			self.col=0

		self.row +=1
		self.col = 0
		return item