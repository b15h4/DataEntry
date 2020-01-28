# -*- coding: utf-8 -*-
from century21.items import Century21Item
import xlsxwriter
import string

class Century21Pipeline(object):
	# def __init__(self):
	# 	self.Century_obj = Century21Item()
	# 	self.row = 1
	# 	self.col = 0
	
	# def open_spider(self,spider):
	# 	self.workbook = xlsxwriter.Workbook(filename="Century21.xlsx")
	# 	self.spreadsheet = self.workbook.add_worksheet(name="Century21")
	# 	self.fields = self.Century_obj.fields.keys()
	# 	cell_format = self.workbook.add_format({'bold': 1, 'bg_color': 'green'})
	# 	self.spreadsheet.write("A1", "Name", cell_format)
	# 	self.spreadsheet.write("B1", "Phone", cell_format)
	# 	self.spreadsheet.write("C1", "Email", cell_format)
	# 	self.spreadsheet.write("D1", "Website", cell_format)

	# def close_spider(self,spider):
	# 	self.workbook.close()
	
	def process_item(self,item,spider):
	# 	for field in self.fields:
	# 		self.spreadsheet.write(self.row,self.col,item['Name'])
	# 		self.col+=1
	# 		self.spreadsheet.write(self.row,self.col,item['Phone'])
	# 		self.col+=1
	# 		self.spreadsheet.write(self.row,self.col,item['Email'])
	# 		self.col+=1
	# 		self.spreadsheet.write(self.row,self.col,item['Website'])
	# 		self.col=0

	# 	self.row +=1
	# 	self.col = 0
		return item