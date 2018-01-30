#!/env /bin python
# _*_ coding:utf-8_*_

def outer(whatever):
    def wrapper(arg):
        result = whatever(arg)
        print 'this is a wrapper'
        return result

    return wrapper


@outer
def func2(arg):
    print 'func2', arg
    return 'return'


# func2('arg')
result1 = func2('arg')
print result1

'''
@outer
def func1():
    print 'func1'


@outer
def func3():
    print 'func3'
'''
