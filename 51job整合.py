# coding:gbk
#��һ����ȡȫ���б��洢��list
#�ڶ���ѭ��list��ȡÿҳ�ı�����ݣ�����ȡ��ְλ����
#�������洢���ļ�
#���Ĳ� ���ɴ���,�����ļ����ɣ���Դ�벻����

import requests,re
def getnum(city,content):
    url = "https://search.51job.com/list/" + city + ",000000,0000,00,9,99," + content + ",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    respone1 = requests.get(url).content.decode('gbk')  # Դ����
    reg = """<div class="rt">([\s\S]*?)</div>"""  # ������ʽ
    regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
    respone = regex.findall(respone1)  # ��һ������
    newstr = respone[0].strip()  # ȥ���ո��з���
    newreg = "(\\d+)"  # ������ʽ
    number = re.findall(newreg, newstr)  # �ڶ�������
    print(number[0])# ���

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
            print(str(i)+"ҳ")
            print (lin)
            respone1 = requests.get(lin).content.decode('gbk')  # Դ����
            # print respone1
            reg = """<!--�б���-->([\s\S]*?)<!--�б��� END-->"""  # ������ʽ
            regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
            respone = regex.findall(respone1)  # ��һ������
            # return respone[0]#�����������

            # ��ȡ������
            reg = """<div class="el">([\s\S]*?)</div>"""
            regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
            getrespone = regex.findall(respone[0])  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
            a = ""
            num = 0
            for line in getrespone:
                num = num + 1
                print(str(num) + "��")
                # ��ȡ����ʦname
                reg = """<a target="_blank" title="([\s\S]*?)" """
                regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
                getnamerespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�

                # ��ȡ��˾
                reg = """<span class="t2"><a target="_blank" title="([\s\S]*?)" """
                regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
                getcomrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
                # ��ȡ�����ص�
                reg = """<span class="t3">([\s\S]*?)</span>"""
                regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
                getcityrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
                # ��ȡurl
                reg = """href="([\s\S]*?)" """
                regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
                geturlrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
                # ��ȡ����
                reg = """class="t4">([\s\S]*?)<"""
                regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
                getmoneyrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
                # ��������
                reg = """class="t5">([\s\S]*?)<"""
                regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
                gettiemrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
                #��ȡְλ����
                url = geturlrespone[0]
                headers = {
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
                try:
                    respones =requests.get(url, headers=headers).content.decode('gbk')
                    reg = """<div class="bmsg job_msg inbox">([\s\S]*?)<div class="mt10">"""  # ���ʽ
                    regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
                    text = regex.findall(respones)
                    content_s=""# ����
                    for line in text:#�����ı�
                        content_s = content_s +\
                            line.strip().replace("</p>","").replace("<b>","").replace("</b>","").replace("</i>","").replace("<i>","").replace("</u>","")\
                              .replace("&nbsp","").replace("</b>","").replace("<br>","").replace("<span>","").replace("<span>", "")\
                        .replace("</span>", "").replace("</li>","").replace("</ol>","").replace("<li>","").replace("<ol>","")
                    content_s.split("<p>")#��<p>Ϊ�о��½�list
                    content_plus=""
                    for line in content_s:#ѭ�����str��������ϴ
                        content_plus= content_plus+line.strip()
                        content_plus = content_plus.replace("<p>","")


                    # a = getnamerespone[0] + "\t", getcomrespone[0] + "\t", getmoneyrespone[0] + '\t' + gettiemrespone[0] +getcityrespone[0] + "\t"+geturlrespone[0] + "\n"
                    a =  content_plus+"\n"
                    with open("tex1.txt", "a") as f1:
                        f1.writelines(a)
                except UnicodeDecodeError:
                    print("--------------------------�д������--------------------------------")
    return gettable(city,content)
getnum("010000","java")

