# -*- coding: utf-8 -*-

# Define your item pipelines here
from .items import SsenseItem
import xlsxwriter
import string


class SsensePipeline(object):
    def __init__(self):
        self.spider_obj = SsenseItem()
        self.row = 1
        self.col = 0
	
    def open_spider(self,spider):
        self.workbook = xlsxwriter.Workbook(filename="SSense.xlsx")
        self.spreadsheet = self.workbook.add_worksheet(name="SSense")
        self.fields = self.spider_obj.fields.keys()
        bold = self.workbook.add_format({'bold': 1})
        self.spreadsheet.write("A1", "Title", bold)
        self.spreadsheet.write("B1", "Price", bold)
        self.spreadsheet.write("C1", "Description", bold)
        self.spreadsheet.write("D1", "Url", bold)
        self.spreadsheet.write("E1", "Image", bold)


    def close_spider(self,spider):
        self.workbook.close()
	
    def process_item(self,item,spider):

        for field in self.fields:
            self.spreadsheet.write(self.row,self.col,item['Title'])
            self.col+=1
            self.spreadsheet.write(self.row,self.col,item['Price'])
            self.col+=1
            self.spreadsheet.write(self.row,self.col,item['Description'])
            self.col+=1
            self.spreadsheet.write(self.row,self.col,item['Url'])
            self.col+=1
            self.spreadsheet.write(self.row,self.col,item['Image'])
            self.col=0
        self.row +=1
        self.col = 0
        return item