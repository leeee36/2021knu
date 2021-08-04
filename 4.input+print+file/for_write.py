# for문을 활용한 파일 출력
f = open('for_write.txt', 'w')

for i in range(10):
    f.write(f"hello sangwook {i}\n")

print('종료')

f.close()