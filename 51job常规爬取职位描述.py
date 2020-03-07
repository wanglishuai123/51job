# coding:GBK
import urllib
import requests
import re
url ="https://jobs.51job.com/taiyuan/114798520.html?s=01&t=0"
headers ={
    "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Connection":"keep-alive"
          }
respones = requests.get(url,headers=headers)
# request.add_header("Connection","keep-alive")
respones = respones.content.decode('gbk')
reg = """<div class="bmsg job_msg inbox">([\s\S]*?)<div class="mt10">"""#表达式
regex = re.compile(reg,re.IGNORECASE)#预编译
text = regex.findall(respones)#正则

for line in text:
    print(line.strip().replace("</p>","").replace("<b>","").replace("</b>","").replace("<br>",""))
