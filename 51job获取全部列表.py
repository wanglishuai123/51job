# encoding=utf-8
#51job常规爬取
import re,requests
import time

def getname(name):
    url ="https://search.51job.com/list/080200,000000,0000,00,9,99,"+name+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    respone1=requests.get(url)#源代码
    reg = """<div class="rt">([\s\S]*?)</div>"""#正则表达式
    regex = re.compile(reg,re.IGNORECASE)#预编译
    respone = regex.findall(respone1)#第一次正则
    newstr = respone[0].strip()#去除空格换行符号
    newreg = "(\\d+)"#正则表达式
    number = re.findall(newreg,newstr)#第二次正则
    return  number[0]#输出


num = eval(getname("python"))#2511
if num%50==0:
    pages = num//50
else:
    pages = num//50+1
#newlist = ["http://search.51job.com/list/080200,000000,0000,00,9,99,python,2,"+ str(i) for i in range(1,pages+1)+".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="]
newlist=""
for i in range(1,pages+1):
    newlist=newlist+"http://search.51job.com/list/080200,000000,0000,00,9,99,python,2,"+str(i)+".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="+"\n"
newlist = newlist.split("\n")
for line in newlist:
    print(line)
