# encoding=GBK
#51job������ȡ
import requests
import re
from urllib.parse import quote,unquote
def getname(city,name):
    name = quote(quote(name,"utf-8"),"utf-8")#url���룬������������
    url ="https://search.51job.com/list/"+city+",000000,0000,00,9,99,"+name+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    respone1=requests.get(url).content.decode('gbk')#Դ����
    reg = """<div class="rt">([\s\S]*?)</div>"""#������ʽ
    regex = re.compile(reg,re.IGNORECASE)#Ԥ����
    respone = regex.findall(respone1)#��һ������
    newstr = respone[0].strip()#ȥ���ո��з���
    newreg = "(\\d+)"#������ʽ
    number = re.findall(newreg,newstr)#�ڶ�������
    print(unquote(unquote(name,"utf-8"),"utf-8"),number[0]+"��")#���
citylist = ["010000","080200","020000","030200"]#���д���
professionlist = ["python", "java", "python ����", "python ����", "UI","C/C++"]#ְҵ
for i in citylist:#��������
    def city(citys):
        num={
            "010000":"����",
            "080200":"����",
            "020000":"�Ϻ�",
            "030200":"����",
        }
        return num.get(citys,None)
    print(city(i))#���ݴ����������
    for j in professionlist:#����profession
        # time.sleep(3)#��ʱ3��
        getname(i,j)


