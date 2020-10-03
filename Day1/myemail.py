import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

#여러 사람한테 보내기
# 보내는 사람 정보
me = "보내는사람@gmail.com"
my_password = "비밀번호"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보

emails = ["이메일1", "이메일2"]

for you in emails:
    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "[공유] 추석기사"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "메일 내용"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    #파일 첨부하기
    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:#이전에 기사 크롤링해둿던 파일을 열어 읽어옴
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")#추석기사라는 파일제목으로 보냄
    msg.attach(part)

    # 메일 보내기
    s.sendmail(me, you, msg.as_string())

# 다 끝나고 닫기
s.quit()