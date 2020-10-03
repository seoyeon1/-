#파일 쓰기
# f = open("test.txt", "w", encoding="utf-8")
# for i in [1,2,3,4,5]:
#     f.write(f"{i}번 안녕, 스파르타!!!!!!!\n")
#
# f.close()

#파일 읽기
text = ''
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:#1줄씩 읽고 출력
        text += line

print(text)