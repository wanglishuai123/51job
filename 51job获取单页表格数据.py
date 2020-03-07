# encoding:GBK
import re,time,requests

def getname(name):
    url ="https://search.51job.com/list/080200,000000,0000,00,9,99,"+name+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    respone1=requests.get(url).content.decode("gbk")#源代码
    # print respone1
    reg = """<!--列表表格-->([\s\S]*?)<!--列表表格 END-->"""#正则表达式
    regex = re.compile(reg,re.IGNORECASE)#预编译
    respone = regex.findall(respone1)#第一次正则
    # return respone[0]#返回整个表格

#获取单个行
    reg = """<div class="el">([\s\S]*?)</div>"""
    regex = re.compile(reg, re.IGNORECASE)  # 预编译
    getrespone = regex.findall(respone[0])  # findall获取全部符合这个条件的信息，存储为列表
    a = ""
    for line in getrespone:
        # 获取工程师name
        reg = """<a target="_blank" title="([\s\S]*?)" """
        regex = re.compile(reg, re.IGNORECASE)  # 预编译
        getnamerespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表

        #获取公司
        reg = """<span class="t2"><a target="_blank" title="([\s\S]*?)" """
        regex = re.compile(reg, re.IGNORECASE)  # 预编译
        getcomrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
        #获取工作地点
        reg = """<span class="t3">([\s\S]*?)</span>"""
        regex = re.compile(reg, re.IGNORECASE)  # 预编译
        getcityrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
        # 获取url
        reg = """href="([\s\S]*?)" """
        regex = re.compile(reg, re.IGNORECASE)  # 预编译
        geturlrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
        #获取工资
        reg = """class="t4">([\s\S]*?)<"""
        regex = re.compile(reg, re.IGNORECASE)  # 预编译
        getmoneyrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
        #发布日期
        reg = """class="t5">([\s\S]*?)<"""
        regex = re.compile(reg, re.IGNORECASE)  # 预编译
        gettiemrespone = regex.findall(line)  # findall获取全部符合这个条件的信息，存储为列表
        # a = getnamerespone[0] + "\t", getcomrespone[0] + "\t", getmoneyrespone[0] + '\t' + gettiemrespone[0] +getcityrespone[0] + "\t"+geturlrespone[0] + "\n"
        a = getnamerespone[0] + "\t"+ getmoneyrespone[0] + '\t' + gettiemrespone[0] +getcityrespone[0] + geturlrespone[0]+"\n"

        with open("tex.txt","a") as f1:
            f1.writelines(a)
getname("python")