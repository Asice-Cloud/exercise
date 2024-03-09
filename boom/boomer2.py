import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def send_email():
    try:
        # 邮件相关信息
        subject = "Test Email"
        sender_email = ""
        password=""
        receiver_email = ""
        body = "This is a test email from Python."
        counter=20

        # 选择服务提供商
        # ...
        # Gmail or Outlook
        service_provider = input('Select the service provider (Gmail / Outlook): ').lower()

        if service_provider == "gmail":
            server = smtplib.SMTP('smtp.gmail.com', 587)
        elif service_provider == "outlook":
            server = smtplib.SMTP('smtp.office365.com', 587)
        else:
            print("Invalid service provider. Please choose either Gmail or Outlook.")
            return

        server.starttls()
        
        # 登录邮箱
        server.login(sender_email, password)

        # 创建一个 MIMEMultipart 对象作为邮件容器
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # 将文本内容添加到邮件中
        message.attach(MIMEText(body, "plain"))

        # 将邮件转换为字符串
        message_str = message.as_string()

        # 发送邮件
        for x in range(counter):
            print("Number of messages sent:", x + 1)
            server.sendmail(sender_email, receiver_email, message_str)
            time.sleep(1)

        server.quit()
        print("Emails sent successfully.")
    except Exception as e:
        print("Something went wrong. Please try again with valid inputs.")

if __name__ == "__main__":
    send_email()
