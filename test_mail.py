import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'leowu102000@gmail.com'
receiver = ['jufengwu102000@gmail.com','leowu102000@gmail.com']
passwd = "vcir stub gqny vunq"
for i in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    msg["Subject"] = Header("Test send email","utf-8").encode()

    body = "This is send by python\n"
    body2 = "how are you?"

    msg_text=MIMEText(body)
    msg.attach(msg_text)
    c = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
        server.login(sender,passwd)
        server.sendmail(sender,i,msg.as_string())
print("success send mail!")

