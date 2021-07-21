# 기본 문자열
s2 = 'hello, sangwook!'
print(s2)
S2 = "hello, sangwook!"
print(S2)
s6 = '''hello, sangwook!'''
print(s6)
S6 = """hello, sangwook!"""
print(S6)

# 이스케이프 코드
# \n, \t, \\, \', \"
longtext1 = '''hello,
sangwook!'''
print(longtext1)
longtext2 = 'hello,\nsangwook!'
print(longtext2)

# string Interpolation
a = 1234
new_q = f'{a}'
print(new_q)


# 문자열 옛날 방식
print(f'%s %s' % ('one', 'two'))

# pyformat
print('{} {}'. format('one', 'two'))

# f-string
a, b = 'one', 'two'
print(f'{a} {b}')
print(f'{b} {a}')

# example
name = '상욱'
eng_name = 'sangwook'
print('안녕하세요 저는 {1}입니다. 영어이름은 {0}입니다.'.format(eng_name, name))
print(f'안녕하세요 저는 {name}입니다.')

# 문자열 인덱싱
a = 'hello, sangwook!'
print(a[1]) #e

# 문자열 슬라이싱
a = 'hello, sangwook!'
print(a[3:8])

# 문자열 길이 구하기
a = 'hello, sangwook!'
print(len(a))

# 문자열에서 최대최소 구하기 max(), min()
a = '312'
b = 'bac'
print(min(a))
print(max(a))
print(min(b))
print(a+b)  #312bac
print(max(a+b))

# 문자열의 소문자 대문자 변환
a = 'This is Justhis'
print(a.upper())
print(a.lower())

# 문자열을 구분자에 따라 나누는 split()
a = 'this, is, justhis'
print(a.split(sep=','))
b = 'this is justhis'
print(b.split())

# 문자열 사이에 구분자를 넣어주는 join()
mylist = ['hi', 'I am', 'sangwook']
mystring = '_'.join(mylist)
print(mystring)