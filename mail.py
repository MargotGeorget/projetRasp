import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(destinataire,message): 
	msg = MIMEMultipart()
	msg['From'] = 'automaticcatfountain@gmail.com'
	msg['To'] = destinataire
	msg['Subject'] = 'Fontaine a eau' 
	msg.attach(MIMEText(message))
	mailserver = smtplib.SMTP('smtp.gmail.com', 587)
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	mailserver.login('automaticcatfountain@gmail.com', 'ccarre34')
	mailserver.sendmail('automaticcatfountain@gmail.com',destinataire, msg.as_string())
	mailserver.quit()
