# coding:utf-8
import re
strtest ="""
<div class="rt">
                共38609条职位
            </div>
"""


regex = re.compile("(\\d+)",re.IGNORECASE)
respone = regex.findall(strtest)
print respone[0]