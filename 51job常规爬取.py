# encoding=GBK
#51job常规爬取
import requests
import re
from urllib.parse import quote,unquote
def getname(city,name):
    name = quote(quote(name,"utf-8"),"utf-8")#url编码，连续编码两次
    url ="https://search.51job.com/list/"+city+",000000,0000,00,9,99,"+name+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    respone1=requests.get(url).content.decode('gbk')#源代码
    reg = """<div class="rt">([\s\S]*?)</div>"""#正则表达式
    regex = re.compile(reg,re.IGNORECASE)#预编译
    respone = regex.findall(respone1)#第一次正则
    newstr = respone[0].strip()#去除空格换行符号
    newreg = "(\\d+)"#正则表达式
    number = re.findall(newreg,newstr)#第二次正则
    print(unquote(unquote(name,"utf-8"),"utf-8"),number[0]+"个")#输出
citylist = ["010000","080200","020000","030200"]#城市代码
professionlist = ["python", "java", "python 数据", "python 爬虫", "UI","C/C++"]#职业
for i in citylist:#遍历城市
    def city(citys):
        num={
            "010000":"北京",
            "080200":"杭州",
            "020000":"上海",
            "030200":"广州",
        }
        return num.get(citys,None)
    print(city(i))#根据代码输出城市
    for j in professionlist:#遍历profession
        # time.sleep(3)#延时3秒
        getname(i,j)


