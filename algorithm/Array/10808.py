#백준 10808 알파벳 개수
#알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
s = input()
alphabet_list = [0] * 26

for i in s:
    alphabet_list[ord(i)-97] += 1

for i in alphabet_list:
    print(i, end=" ")