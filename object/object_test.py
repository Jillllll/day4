#!/bin /env python
# _*_coding=utf-8_*_

class Province:
    def __init__(self, name, capital):
        self.Name = name
        self.Capital = capital


js = Province('JiangSu', 'NanJing')
print js.Name
print(js.Capital)