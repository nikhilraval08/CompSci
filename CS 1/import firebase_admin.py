import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import smtplib
s = smtplib.SMTP('protonmail.com', 1025)
s.starttls()
s.login("your email", "pass0")
cred = credentials.Certificate('you_Secret.json')
firebase_admin.initialize_app(cred)


# creating the user
email = input('Please enter your email address : ')
password = input("Please enter your password : ")

user = auth.create_user(email=email, password=password )
link = auth.generate_email_verification_link(email, action_code_settings=None)
message = link
print(link)
s.sendmail("sender email", "reciever email", message)

# terminating the session
s.quit()