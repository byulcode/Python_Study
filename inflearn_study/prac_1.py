def std_weight(height):
    sw = height * height * 22
    return sw
height = 1.75
stdw = std_weight(height)

print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다".format(height,stdw))
print('-'*100)
