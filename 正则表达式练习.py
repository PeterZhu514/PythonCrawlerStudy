
#正则表达式

#匹配以".com"和".cn"结尾的域名
import re
pattern ="[a-zA-Z]+://[^\s]*[.com|.cn]"
string="<a href='http://www.baidu.com'>百度首页</a>"
result=re.search(pattern,string)
print(result)


#匹配电话号码
import re
pattern="\d{4}-\d{7}|\d{3}-\d{8}"
string="021-6728263652341"
result=re.search(pattern,string)
print(result)

#匹配电子邮件地址
import re
pattern="\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
string="<a href='http://www.baidu.com'>百度首页</a><br><a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮件地址</a>"
result=re.search(pattern,string)
print(result)


