#!/bin /env python
# _*_coding=utf-8_*_

class Province:
    # static field:belong to class
    memo = 'one out of 23 provinces'

    def __init__(self, name, capital):
        # dynamic field:belong to object
        self.Name = name
        self.Capital = capital


js = Province('JiangSu', 'NanJing')
print js.Name
print(js.Capital)
print(Province.memo)
