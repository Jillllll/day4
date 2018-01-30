#!/env /bin python
# _*_ coding:utf-8_*_

def outer(whatever):
    def wrapper():
        whatever()
        print 'this is a wrapper'

    return wrapper()


@outer
def func1():
    print 'func1'


@outer
def func2():
    print 'func2'


@outer
def func3():
    print 'func3'
