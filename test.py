# pip : pypi.org(도서관) 에서 라이브러리를 컴퓨터로 받아오는 프로그램
# import : 다른 파일에 있는 클래스, 함수, 변수를 해당 파일에서 사용함

import googletrans
from googletrans import Translator
x = 0
d = googletrans.LANGUAGES
text1 = "Hello"
translator = Translator()
for i in d:
    x += 1
    trans1 = translator.translate(text1, src='ko', dest=i)
    print(f"{d[i]} {x} 인사 : ", trans1.text)