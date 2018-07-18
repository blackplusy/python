#coding=utf-8
#文件的默认字符集是utf-8
#字符集就是翻译官
#为了维护代码的统一性，一般统一设置成utf-8
#常见字符集GBK2312(中文字符集)

#input输入
#设置一个变量名字是a,接受键盘传入的数据
#输出a这个变量的值

a=input('请输入您的法号：')
print(a)

#raw_input在py3中未定义
b=raw_input('请输入您的银行密码：')
print(b)

#补充:常见报错
#NameError: name 'raw_input' is not defined
#未定义错误
