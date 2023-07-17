from datetime import date
import pandas as pd
import smtplib
from email.message import EmailMessage

SHEET_ID ="1EPLTYCBU_28lwkDxC0LEgAQ0VMV27ljqN84dIRNLdRg"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_df(url):
    parse_dates = ['due_date','reminder_date']
    df = pd.read_csv(url,parse_dates=parse_dates,dayfirst=True)
    return df


def Send_email(df):
    current = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (current.day == row["reminder_date"].day):
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login("sakshishinde5315@gmail.com",'ukjtvkhiohotbmqs')
                email = EmailMessage()
                name=row["name"],
                invoice_no=row["invoice_no"],
                amount=row["amount"],
                due_date=row["due_date"].strftime("%d, %b %Y"),
                email["From"] ="sakshishinde5315@gmail.com"
                email["to"] = row["email"],
                email["Subject"] = f'Regarding Your {row["monthly_expense"]}: {row["invoice_no"]}'
                email.set_content( f"""\
                Hi {name},
                I hope you are well.
                I just wanted to drop you a quick note to remind you that {amount} Rupees in respect of our invoice {invoice_no} is due for payment on {due_date}.
                I would be really grateful if you could confirm that everything is on track for payment.
                Best regards
                """)
                
                email_counter += 1
                server.send_message(email)
    return f"Total Emails Sent: {email_counter}"

df = load_df(URL)
result = Send_email(df)
print(result)