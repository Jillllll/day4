#!/bin /env python
# _*_coding=utf-8_*_

class Province:
    # static field:belong to class;can't access to dynamic field
    memo = 'one out of 23 provinces'

    def __init__(self, name, capital):
        # dynamic field:belong to object;can access to static field
        self.Name = name
        self.Capital = capital

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


js = Province('JiangSu', 'NanJing')
print js.Name
print(js.Capital)
print(Province.memo)
js.athletic_meet()
Province.establish()

# can't add ()
js.Bar
