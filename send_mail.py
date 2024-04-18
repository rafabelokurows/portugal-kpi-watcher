import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl 
import os

sender = 'rafabelokurows@gmail.com' #if you're reading this and you're not me, change this e-mail to whichever e-mail you wanna use for this.
recipient = 'rafabelokurows@gmail.com' #if you're reading this and you're not me, change this e-mail to whichever e-mail you wanna use for this.
password = os.getenv('APP_PASSWORD') #the APP PASSWORD as generated on the Security Settings of the Gmail account configured above.
subject = 'The latest Portugal KPI report is out'
body = """<p>Hello, there!</p>
<p>The latest Portugal KPI report was released just now. If you want to check this one out, go to: <a href="https://rafabelokurows.github.io/portugal-kpi-watcher/">Portugal KPI Watcher</a>
\n
             <p>There you will find the latest data on tourism and economy indicators based on official government sources.</p>
             <p>Hope you like it, and if you have any questions, let me know :)</p>"""
    
message = MIMEMultipart()
message['From'] = sender
message['To'] = recipient
message['Subject'] = subject
message.attach(MIMEText(body, 'html'))

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,recipient,message.as_string())

print('Email sent to ',recipient)