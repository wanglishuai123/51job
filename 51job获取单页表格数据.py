# encoding:GBK
import re,time,requests

def getname(name):
    url ="https://search.51job.com/list/080200,000000,0000,00,9,99,"+name+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    respone1=requests.get(url).content.decode("gbk")#Դ����
    # print respone1
    reg = """<!--�б���-->([\s\S]*?)<!--�б��� END-->"""#������ʽ
    regex = re.compile(reg,re.IGNORECASE)#Ԥ����
    respone = regex.findall(respone1)#��һ������
    # return respone[0]#�����������

#��ȡ������
    reg = """<div class="el">([\s\S]*?)</div>"""
    regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
    getrespone = regex.findall(respone[0])  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
    a = ""
    for line in getrespone:
        # ��ȡ����ʦname
        reg = """<a target="_blank" title="([\s\S]*?)" """
        regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
        getnamerespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�

        #��ȡ��˾
        reg = """<span class="t2"><a target="_blank" title="([\s\S]*?)" """
        regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
        getcomrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
        #��ȡ�����ص�
        reg = """<span class="t3">([\s\S]*?)</span>"""
        regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
        getcityrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
        # ��ȡurl
        reg = """href="([\s\S]*?)" """
        regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
        geturlrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
        #��ȡ����
        reg = """class="t4">([\s\S]*?)<"""
        regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
        getmoneyrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
        #��������
        reg = """class="t5">([\s\S]*?)<"""
        regex = re.compile(reg, re.IGNORECASE)  # Ԥ����
        gettiemrespone = regex.findall(line)  # findall��ȡȫ�����������������Ϣ���洢Ϊ�б�
        # a = getnamerespone[0] + "\t", getcomrespone[0] + "\t", getmoneyrespone[0] + '\t' + gettiemrespone[0] +getcityrespone[0] + "\t"+geturlrespone[0] + "\n"
        a = getnamerespone[0] + "\t"+ getmoneyrespone[0] + '\t' + gettiemrespone[0] +getcityrespone[0] + geturlrespone[0]+"\n"

        with open("tex.txt","a") as f1:
            f1.writelines(a)
getname("python")