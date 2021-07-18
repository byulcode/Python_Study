# import sys
# print("Python", "Java", "JavaScript",file=sys.stdout) #표준 출력
# print("Python", "Java", "JavaScript",file=sys.stderr) #표준 에러

# #시험 성적
# scores = {"수학" : 0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(4), str(score).rjust(4),sep=":") #안의 숫자는 확보한 공간의 수

# #은행 대기순번표
# for num in range(1,11):
#     print("대기번호 : "+str(num).zfill(3))     #zfill : 0을 ()속의 숫자만큼 공간 확보 후 채우기

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신값은 "+answer+"입니다.")

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

#양수일 땐 +로, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬하고, 빈판을 _로 채움
print("{0:_<+10}".format(500))

#3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000))

#3자리마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))

#3자리마다 콤마를 찍고, 부호도 붙이고, 자릿수 확보, 빈자리는 ^로 채우기
print("{0:^<+20,}".format(-1000000000))

#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리수까지 출력
print("{0:.2f}".format(5/3))