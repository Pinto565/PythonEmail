import pandas as pd
import smtplib
from email.message import EmailMessage


df = pd.read_csv('list.csv')

def send_mail(name,r_mail,image,event):
    s_mail = "infantvalan02@gmail.com"
    s_pass = "Pinto@5650"
    message = f"Hello...{name}"
    msg=EmailMessage()
    msg['Subject'] = f"Certificate For {event}"
    msg['From'] = s_mail
    msg['To'] = r_mail
    msg.set_content(message)
    with open(image,"rb") as file:
        data = file.read()
        msg.add_attachment(data,maintype = "application", subtype = "pdf",filename = name)
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    try:
        server.login(s_mail,s_pass)
        print("Logged In Successfully")
        server.send_message(msg)
        print("Mail Sent")
        server.quit()
    except:
        print("Mail Not Sent")

for index,j in df.iterrows():
    Name = j["Name"]
    Email = j["Email"]
    Event = j["Event"]
    Image = f"Certificate-PDF/{Name}.pdf"
    send_mail(Name , Email,Image,Event)