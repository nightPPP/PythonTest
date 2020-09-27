import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

host_server = 'smtp.qq.com'    # 邮箱服务器

# 163
# sender = 'smartloveit@163.com'     # 发件人邮箱
# pwd = 'KMCBBEOUNBUUJCXV'    # 163密码
# receiver = '912073960@qq.com'       # 收件人邮箱

# qq
sender = '912073960@qq.com'     # 发件人邮箱
pwd = 'tulzafwtxmlubcje'    # qq密码
# receiver = '690032154@qq.com'       # 收件人邮箱
receiver = '784976854@qq.com'       # 收件人邮箱

mail_title = '嗨起来'     # 邮件标题
mail_content = '小舅子呢'   # 邮件的内容

msg = MIMEMultipart()   # 邮件主题
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender
msg["To"] = Header("测试邮箱", 'utf-8')
msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

smtp = SMTP_SSL(host_server)    # ssl登录
smtp.login(sender, pwd)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()