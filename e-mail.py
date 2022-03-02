from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTP_SSL

from tools import weather

def sendEmail(message):
    host_server = "smtp.qq.com"  # qq邮箱smtp服务器
    sender_qq = "1789304430@qq.com"  # 发件人邮箱
    pwd = "qgqlafodlouscjih"  # 授权码
    receiver = ["1789304430@qq.com"]  # 收件人邮箱
    mail_title = "每日早报"  # 标题
    mail_content = message  # 内容

    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title,"utf-8")
    msg["From"] = sender_qq
    msg["To"] = ";".join(receiver)
    msg.attach(MIMEText(mail_content,"plain","utf-8"))
    smtp = SMTP_SSL(host_server) # ssl登陆
    smtp.login(sender_qq,pwd)
    smtp.sendmail(sender_qq,receiver,msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    message = weather.Weather("南京")
    sendEmail(message)