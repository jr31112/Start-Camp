# dictionary
# key - value
# key : string, integer, float, boolean
# !list, dictionary는 key가 될 수 없다.
# value : 모든 값을 가질 수 있다.
lunch = {'중국집' : '042-0548-5789'}
print(lunch)
dinner = dict(한식='042-9564-8464')
print(dinner)
bf = {}
bf['분식'] = '042-4546-8789'
print(bf)

menu = {'bf' : bf, 'lunch' : lunch, 'dinner' : dinner}
print(menu)
print(menu['bf'])
print(menu['bf']['분식'])

ssafy = {'김은정' : '학생', '김인성' : '학생', '연용흠' : '반장'}
# 기본적으로 dictionary는 key값을 전달한다.
for name in ssafy:
    print(name)
    print(ssafy[name])

# key와 value를 같이 리턴하기 위해서는 .items()를 사용하여 전달한다.
for name, student_type in ssafy.items():
    print(name, student_type)

# .items()를 사용하면 tuple 형태가 담겨있는 list형태로 나온다.
print(ssafy.items())
print(type(ssafy.items()))

# .values()을 사용하면 value값이 list형태로 나온다.
for name in ssafy.values():
    print(name)
print(ssafy.values())

# .keys()를 사용하면 value값이 list형태로 나온다.
for student_type in ssafy.keys():
    print(student_type)
print(ssafy.keys())
