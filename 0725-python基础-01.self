学习目标
掌握self的应用

学习内容
a.self实例
b.注意事项

a.self实例
class student:
        def __init__(self,name):
                self.name=name
        def info(self):
                print('您的名字是%s'%self.name)

def studentinfo(student):
        student.info()
#heygor是student类的实例化
heygor=student('simida')
#对象实例化之后可以使用类中的方法
#studentinfo括号中传入的heygor是一个已经实例化的对象，可以调用类中的方法
studentinfo(heygor)

o8ma=student('o8ma')
studentinfo(o8ma)
注意：函数的传参可以传入常规参数也可以传入对象

b.注意事项
self可以理解为自己
可以把self当作c++类里面的指针一样理解就是对象自身意思
当某个对象调用其方法时候，python解释器会把这个对象作为第一个参数传给self，所以开发者只需要传递后面的参数即可
