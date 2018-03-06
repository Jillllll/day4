#!/bin /env python
# _*_coding=utf-8_*_

class Province(object):
    # static field:belong to class;can't access to dynamic field
    memo = 'one out of 23 provinces'

    def __init__(self, name, capital, flag):
        # dynamic field:belong to object;can access to static field
        self.Name = name
        self.Capital = capital
        self.__private = flag

    # dynamic function
    def athletic_meet(self):
        print self.Name + 'is having a athletic meet'

    @staticmethod
    def establish():
        print 'Province establish capital'

    # speciality:convert the access to function from function to field
    @property
    def Bar(self):
        print self.Name

    def __internal(self):
        print 'This is an internal private func'

    def show(self):
        print self.__private

    def show2(self):
        self.__internal()

    # read only
    @property
    def show3(self):
        return self.__private

    # editable
    @show3.setter
    def show3(self, value):
        self.__private = value


js = Province('JiangSu', 'NanJing', 'flagvalue')
# print js.Name
# print(js.Capital)
# print(Province.memo)
# js.athletic_meet()
# Province.establish()

# can't add ()
# js.Bar

# js.show()
# js.show2()
# js.show3


print js.show3
js.show3 = 'changedflagvalue'
print(js.show3)
