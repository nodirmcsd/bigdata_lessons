# -*- coding: utf-8 -*-
s = u"У Мэри есть овечка"
l = s.split(' ')
s1 = '_'.join(l)
print(s1)

s = u"Привет {0} девочек и {1} мальчиков"
print(s.format(7,5))

s = "{people} eats {food}"

print(s.format(people="Uzbeks", food = "plov"))


s = "{people} eats {food} too"

d = {"people": "Russians", "food": "plov"}

print(s.format(**d))
