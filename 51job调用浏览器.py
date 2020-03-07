# coding:utf-8

import selenium.webdriver #模拟浏览器
import  re

def gethtml(city,name):
    url ="https://search.51job.com/list/"+city+",000000,0000,00,9,99,"+name+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    driver = selenium.webdriver.Chrome()#调用浏览器
    driver.get(url)#访问链接
    respones = driver.page_source#获取源代码
    regstr_one= """<div class="rt">([\s\S]*?)</div>"""  # 正则表达式
    regex_one= re.compile(regstr_one, re.IGNORECASE)  # 预编译
    respone = regex_one.findall(respones)  # 第一次正则
    newstr = respone[0].strip()  # 去除空格换行符号
    regstr_two = "(\\d+)"  # 正则表达式_two
    regex_two=re.compile(regstr_two,re.IGNORECASE)#预编译
    number = regex_two.findall(newstr)  # 第二次正则
    driver.close()
    print(name, number[0])  # 输出


citylist = ["010000", "080200", "020000", "030200"]  # 城市代码
professionlist = ["python", "java", "python%2520数据", "python%2520爬虫", "UI", "C/C++"]  # 职业
for i in citylist:  # 遍历城市
    def city(citys):
        num = {
            "010000": "北京",
            "080200": "杭州",
            "020000": "上海",
            "030200": "广州",
        }
        return num.get(citys, None)
    print(city(i))  # 根据代码输出城市
    for j in professionlist:  # 遍历profession
        # time.sleep(3)#延时3秒
            gethtml(i, j)




