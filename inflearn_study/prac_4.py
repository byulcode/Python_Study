#pickle 사용
import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"김건호", "나이":30, "취미":["축구", "배구", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb") 
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


#with --> close필요 없음
with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file: #쓰기
    study_file.write("파이썬 공부하고 있어요")
with open("study.txt", "r", encoding="utf8") as study_file: #읽기
    print(study_file.read())