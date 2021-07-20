from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#패키지 이용하기
# 다운 : pip install beautifulsoup4 
# 업데이트 : pip install --upgrade beautifulsoup4
# 디테일 : pip show beautifulsoup4
# 삭제 : pip uninstall beautifulsoup4
