import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

host_server = 'smtp.qq.com'    # 邮箱服务器

# qq
sender = '912073960@qq.com'     # 发件人邮箱
pwd = 'tulzafwtxmlubcje'    # qq密码
# receiver = '690032154@qq.com'       # 收件人邮箱
receiver = 'smartloveit@163.com'       # 收件人邮箱

mail_title = 'python自动化办公'     # 邮件标题
mail_content = "带超链接的内容<p><a href='https://www.runoob.com/python3/python3-tutorial.html'>Python</a></p>"   # 邮件的内容

msg = MIMEMultipart()   # 邮件主题
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender
msg["To"] = Header("测试邮箱", 'utf-8')
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

try:
    smtp = SMTP_SSL(host_server)    # ssl登录
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("邮件发送失败")
