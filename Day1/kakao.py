from wordcloud import WordCloud
# import matplotlib.font_manager as fm #font search
text = ''
with open("KakaoTalk.txt", "r", encoding="utf-8") as f:#카톡 파일을 open
    lines = f.readlines()
    for line in lines:#1줄씩 읽고 text에 저장
        text += line


wc = WordCloud(font_path="C:/Windows/Fonts/LetterGothicStd.otf", background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")



# 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)


