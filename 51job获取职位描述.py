# coding:GBK
import requests
import re
import selenium.webdriver

url ="https://jobs.51job.com/hangzhou-xcq/105395277.html?s=01&t=0"
driver = selenium.webdriver.Chrome()  # ���������
driver.get(url)  # ��������
respones = driver.page_source  # ��ȡԴ����
# respones = respones.encode("")
driver.close()
# print respones
reg = """<div class="bmsg job_msg inbox">([\s\S]*?)<div class="mt10">"""#���ʽ
regex = re.compile(reg,re.IGNORECASE)#Ԥ����
text = regex.findall(respones)#����
print(text[0].strip().replace("</p>","").replace("<p>",""))#�滻)

