import webbrowser

idols = ['bts', '아이유','obama']
for search in idols:
    # string interpolation
    # 문자열 보간법 : f-string / 3.6+
    webbrowser.open(f'https://search.naver.com/search.naver?query={search}')