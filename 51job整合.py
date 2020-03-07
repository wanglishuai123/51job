# coding:gbk
#第一步爬取全部列表，存储到list
#第二步循环list爬取每页的表格数据，并爬取其职位描述
#第三步存储到文件
#第四部 生成词云,其余文件生成，本源码不处理。

import requests,re
def getnum(city,content):
    url = "https://search.51job.com/list/" + city + ",000000,0000,00,9,99," + content + ",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    respone1 = requests.get(url).content.decode('gbk')  # 源代码
    reg = """<div class="rt">([\s\S]*?)</div>"""  # 正则表达式
    regex = re.compile(reg, re.IGNORECASE)  # 预编译
    respone = regex.findall(respone1)  # 第一次正则
    newstr = respone[0].strip()  # 去除空格换行符号
    newreg = "(\\d+)"  # 正则表达式
    number = re.findall(newreg, newstr)  # 第二次正则
    print(number[0])# 输出

    def getallurl(city,content):
        num = eval(number[0])#2511
        if num%50==0:
            pages = num//50
        else:
            pages = num//50+1

        newlist=""
        for i in range(1,pages+1):
            newlist=newlist+"http://search.51job.com/list/"+city+",000000,0000,00,9,99,python,2,"+str(i)+".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="+"\n"
        newlist = newlist.split("\n")
        print(newlist)
        return newlist


    def gettable(city,content):
        i = 0
        for lin in getallurl(city,content):
            i = i + 1
            print(str(i)+"页")
            print (lin)
            respone1 = requests.get(lin).content.decode('gbk')  # 源代码
            # print respone1
            reg = """<!--列表表格-->([\s\S]*?)<!--列表表格 END-->"""  # 正则表达式
            regex = re.compile(reg, re.IGNORECASE)  # 预编译
            respone = regex.findall(respone1)  # 第一次正则
            # return respone[0]#返回整个表格

            # 获取单个行
            reg = """<div class="el">([\s\S]*?)</div>"""
            regex = re.compile(reg, re.IGNORECASE)  # 预编译
            getrespone = regex.findall(respone[0])  # findall获取全部符合这个条件的信息，存储为列表
            a = ""
            num = 0
            for line in getrespone:
                num = num + 1
                print(str(num) + "行")
                # 获取工程师name
                reg = """<a target="_blank" title="([\s\S]*?)" """
                regex = re.compile(reg, re.IGNORECASE)  # 预编译
                getnamerespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表

                # 获取公司
                reg = """<span class="t2"><a target="_blank" title="([\s\S]*?)" """
                regex = re.compile(reg, re.IGNORECASE)  # 预编译
                getcomrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
                # 获取工作地点
                reg = """<span class="t3">([\s\S]*?)</span>"""
                regex = re.compile(reg, re.IGNORECASE)  # 预编译
                getcityrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
                # 获取url
                reg = """href="([\s\S]*?)" """
                regex = re.compile(reg, re.IGNORECASE)  # 预编译
                geturlrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
                # 获取工资
                reg = """class="t4">([\s\S]*?)<"""
                regex = re.compile(reg, re.IGNORECASE)  # 预编译
                getmoneyrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
                # 发布日期
                reg = """class="t5">([\s\S]*?)<"""
                regex = re.compile(reg, re.IGNORECASE)  # 预编译
                gettiemrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
                #获取职位描述
                url = geturlrespone[0]
                headers = {
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
                try:
                    respones =requests.get(url, headers=headers).content.decode('gbk')
                    reg = """<div class="bmsg job_msg inbox">([\s\S]*?)<div class="mt10">"""  # 表达式
                    regex = re.compile(reg, re.IGNORECASE)  # 预编译
                    text = regex.findall(respones)
                    content_s=""# 正则
                    for line in text:#处理文本
                        content_s = content_s +\
                            line.strip().replace("</p>","").replace("<b>","").replace("</b>","").replace("</i>","").replace("<i>","").replace("</u>","")\
                              .replace("&nbsp","").replace("</b>","").replace("<br>","").replace("<span>","").replace("<span>", "")\
                        .replace("</span>", "").replace("</li>","").replace("</ol>","").replace("<li>","").replace("<ol>","")
                    content_s.split("<p>")#以<p>为中卷，新建list
                    content_plus=""
                    for line in content_s:#循环组成str，进行清洗
                        content_plus= content_plus+line.strip()
                        content_plus = content_plus.replace("<p>","")


                    # a = getnamerespone[0] + "\t", getcomrespone[0] + "\t", getmoneyrespone[0] + '\t' + gettiemrespone[0] +getcityrespone[0] + "\t"+geturlrespone[0] + "\n"
                    a =  content_plus+"\n"
                    with open("tex1.txt", "a") as f1:
                        f1.writelines(a)
                except UnicodeDecodeError:
                    print("--------------------------有错误编码--------------------------------")
    return gettable(city,content)
getnum("010000","java")

