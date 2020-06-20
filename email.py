import pandas as pd
import smtplib
import imghdr
import pandas as pd
from email.message import EmailMessage
df = pd.read_excel(r'C:\Users\Suraj\Desktop\zzz.xlsx')


for key, value in df.iteritems(): 
    a.append(value )


for i in a:
    msg = EmailMessage()
    msg['Subject'] = 'Check out Bronx as a puppy!'
    msg['From'] = 'SENDER EMAIL ID'
    msg['To'] = i

    msg.set_content('This is a plain text email')

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">This is an HTML Email!</h1>
        </body>
    </html>
    """, subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL ID, PASSWORD)
        smtp.send_message(msg)
    