import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import threading
lock = threading.Lock()
def send_email(x, server, sender_email, receiver_email, message_str):
    with lock:
        print("Number of messages sent:", x + 1)
        server.sendmail(sender_email, receiver_email, message_str)

def main():
    try:
        # 邮件相关信息
        subject = "Hello dude, you think you did a good job?"
        sender_email = ""
        password=""
        receiver_email = "2254644589@qq.com"
        body = "Sometimes you are not smart enough so that I suggest you do not acting recklessly while rashly fantasy you can cheat others."
        counter=100

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

        threads = []
        # 发送邮件
        for x in range(counter):
            thread = threading.Thread(target=send_email, args=(x, server, sender_email, receiver_email, message_str))
            thread.start()
            threads.append(thread)
            time.sleep(1)
        for thread in threads:
            thread.join()
        
        server.quit()
        print("Emails sent successfully.")
    except Exception as e:
        print("Something went wrong. Please try again with valid inputs.")
        

if __name__ == "__main__":
    main()