import os
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup


class DownloadTempreture:
    def __init__(self, url, path, desired_years):
        self.month_code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        self.url = url
        self.path = path
        self.desired_years = desired_years
    def downloadData(self):
        for i in self.desired_years:
            for j in self.month_code:
                driver = webdriver.Chrome(self.path)
                driver.get(self.url)
                sleep(3)
                
                
                year_ = str(i)
                year_ = '' + year_ + ''
                y_1 = "//form[@ id = 'stnRequest207-sm']//select[@id = 'Year207-sm']//option[@ value ="
                xpath_year = y_1 + year_ + "]"
                year = driver.find_element_by_xpath(xpath_year)
                year.click()
                
                
                xpath_month = "//form[@ id = 'stnRequest207-sm']//select[@id = 'Month207-sm']//option[@ value =" + j +"]"
                month = driver.find_element_by_xpath(xpath_month)
                month.click()
                
                Go = driver.find_element_by_xpath("//form[@ id = 'stnRequest207-sm']//input[@type = 'submit'] ")
                Go.click()
                
                download_button = driver.find_element_by_xpath("//input[@ class = 'btn btn-default text-center mrgn-bttm-md']")
                download_button.click()
                
                sleep(4)
                driver.close()

# URL of the site                
url = "http://climate.weather.gc.ca/historical_data/search_historic_data_stations_e.html?searchType=stnProv&timeframe=1&lstProvince=AB&optLimit=yearRange&StartYear=1840&EndYear=2018&Year=2018&Month=2&Day=27&selRowPerPage=25&txtCentralLatMin=0&txtCentralLatSec=0&txtCentralLongMin=0&txtCentralLongSec=0&startRow=201"

# Chrome driver path
path = "F:\\Project_incubator\\chromedriver_win32\\chromedriver"

# Need to have the data from 2010
test = DownloadTempreture(url, path, [2010,2011,2012,2013,2014,2015,2016,2017])
test.downloadData()