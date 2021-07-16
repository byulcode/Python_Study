#파일 입출력

# score_file = open("score.txt", "w", encoding="utf8") 
# print("수학 : 0", file=score_file) 
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")    #이어서 쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

##한번에 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())    
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True: #무한루프
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()
print("\n\n")

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()