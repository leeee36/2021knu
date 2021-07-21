# 리스트
# 리스트 이름 = [요소1, 요소2, 요소3, ...]

# 리스트 선언
Haedal_friends = ["해달이", "시라용", "아리", "메기", "사스미"]

# 빈 리스트
mylist = []
print(mylist)

# 파이썬 리스트 특징 
mylist = [1, 2, "해달이", True, ['1', '2', '3']]
print(mylist)


# 리스트 인덱싱
a = [1,2,3,4,5,6,7,8,9,10]
print(a[0]) #1
print(a[5]) #6

# 음수 인덱싱
print(a[-1]) #10
print(a[-7]) #4

# 리스트 슬라이싱
print(a[5:9]) # 6,7,8,9  # a:b = a부터 b-1까지 리스트 슬라이싱  # a이상 b미만
print(a[0:4]) # 1,2,3,4
print(a[:4])
print(a[5:])
print(a[:])
print(a[-4:-1])

# 리스트 수정
a[0] = 10
print(a)  #[10,2,3,4, ...]

# 리스트 삭제
del a[1]
print(a)
del a[5:]
print(a)

# 리스트 길이 구하기
a = [1,2,3,4,5]
print(len(a))

# 리스트 값 추가하기
mylist = ['a', 'b', 'c']
mylist.append('d')
print(mylist)

# 리스트 값 정렬하기
mylist = [1,4,2,3]
mylist.sort()
print(mylist)  #1,2,3,4
mylist.sort(reverse=True)
print(mylist)  #4,3,2,1 