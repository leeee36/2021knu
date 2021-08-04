# 간단한 파일 읽기
print('# read함수')
f = open('third week.txt', 'r')
a = f.read()
print(a)
f.close()

print('# readlines() 함수')
f = open('third week.txt', 'r')
b = f.readlines()
print(b)
f.close()

print('# readline() 함수')
f = open('third week.txt', 'r')
c = f.readline()
print(c)
f.close()

