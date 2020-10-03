from wordcloud import WordCloud
from PIL import Image
import numpy as np
# import matplotlib.font_manager as fm #font search
text = ''
with open("KakaoTalk.txt", "r", encoding="utf-8") as f:#카톡 파일을 open
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('이모티콘\n', '').replace('사진\n', '').replace('ㅋ', '').replace('ㄱㄱ','').replace('ㅠ', '').replace('ㅜ', '').replace('나도', '').replace('진짜', '').replace('근데', '').replace('오늘', '').replace('https', '').replace('샵검색', '').replace('삭제된 메시지입니다', '')

#word  clord

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/WINDOWS/Fonts/malgun.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")


# 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)


