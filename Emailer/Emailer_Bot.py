import smtplib
import os
from email.message import EmailMessage


def emailer(*args):
    while True:
        try:
            email_address = input("Enter your email address: ")
            password = input("Enter email password: ")
            contacts = input("Enter contact emails (use commas to separate addresses): ")
            subject = input("Enter subject: ")
            message = input("Enter message: ")

            msg = EmailMessage()
            msg['To'] = contacts
            msg['From'] = email_address
            msg['Subject'] = subject
            msg.set_content(message)

            while True:
                send_attachments = input('Add attachments? (Y/N): ').lower()
                if send_attachments == 'y':
                    attachments = [x.strip() for x in
                                   input("Paths of Attachments (use commas to separate paths): ").split(',')]
                    for file in attachments:
                        with open(file, 'rb') as f:
                            msg.add_attachment(f.read(), filename=f.name, maintype='application',
                                               subtype='octet-stream')
                    break
                elif send_attachments == 'n':
                    break
                else:
                    continue

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email_address, password)
                smtp.send_message(msg)

                print('\nMessage sent')
                print('Thanks for using this program!')

        except Exception as e:
            print(e)
            while True:
                response = input('Try again? (Y/N): ').lower()
                if response == 'y':
                    break
                    continue
                elif response == 'n':
                    print('\nThanks for using this program!')
                    return
                else:
                    continue


if __name__ == "__main__":
    emailer()
