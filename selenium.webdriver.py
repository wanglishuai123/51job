# coding=utf-8
from selenium import webdriver
#web浏览器地址需要放到path内，并且需要下载chrom驱动，放到环境变量内，
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
