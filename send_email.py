import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

qqMail=smtplib.SMTP_SSL("smtp.qq.com",465)
mailUser="..."#我的邮箱
mailPass="........."#我的授权码
qqMail.login(mailUser,mailPass)

sender="..."#我的邮箱
receiver="..."#对方的邮箱
message=MIMEMultipart()
message["subject"]=Header("...照片")
message["From"]=Header(f"aling<{sender}>")#aling我的名字
message["To"]=Header(f"she{receiver}")#she对方的名字

textContent="..同学，这是..同学绘制的...照片，望查收~"
mailContent=MIMEText(textContent,"plain","utf-8")
filePath=r"..."#路径
with open(filePath,"rb") as imageFile:
    fileContent=imageFile.read()

attachment=MIMEImage(fileContent)
attachment.add_header("Content-Disposition","attachment",filename="...照片.jpg")

message.attach(mailContent)
message.attach(attachment)
qqMail.sendmail(sender,receiver,message.as_string())