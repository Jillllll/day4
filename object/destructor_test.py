# _!_ coding:utf-8_!_
# !/bin/env python

class Foo:
    def __init__(self):
        pass

    # destructor
    def __del__(self):
        print 'The destructor is going to destruct me.'

    def Go(self):
        print('Go!')

    def __call__(self):
        print 'Call!'


# execute __init__ func
f1 = Foo()

f1.Go()

# execute call func
f1()
