# coding:GBK
import requests
import re
import selenium.webdriver

url ="https://jobs.51job.com/hangzhou-xcq/105395277.html?s=01&t=0"
driver = selenium.webdriver.Chrome()  # 调用浏览器
driver.get(url)  # 访问链接
respones = driver.page_source  # 获取源代码
# respones = respones.encode("")
driver.close()
# print respones
reg = """<div class="bmsg job_msg inbox">([\s\S]*?)<div class="mt10">"""#表达式
regex = re.compile(reg,re.IGNORECASE)#预编译
text = regex.findall(respones)#正则
print(text[0].strip().replace("</p>","").replace("<p>",""))#替换)

