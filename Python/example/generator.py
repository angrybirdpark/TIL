def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

#Case 1
print(get_natural_number())
'''
결과값 : <generator object get_natural_number at 0x102b43b30>
'''

#Case 2
g = get_natural_number()

for i in range(0, 100):
    print(next(g))
'''
결과값 :
1
2
...
99
100
'''
