#coding=utf-8
dic={'name':'heygor','tel':182000000000}
dic2={'name':'baidu','tel':110}

print(dic)
print(dic2)

dic['name']='wukong'
print(dic)
dic['tel']=119
print(dic)


print('******************')
dic={'name':'heygor','tel':182000000000}
print(dic)
del dic['name']
print(dic)
#del dic
#print(dic)

dic.clear()
print(dic)
