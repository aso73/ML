import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from geopy.geocoders import Nominatim

def send_email(sender_email, sender_password, receiver_email, subject, body, file_path):

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body,'plain'))

    attachment = open(file_path, 'rb')
    mime_base = MIMEBase('application', 'octet-stream')
    mime_base.set_payload(attachment.read())
    encoders.encode_base64(mime_base)
    mime_base.add_header('Content-Disposition', f'attachment; filename= {file_path.split("/")[-1]}')
    message.attach(mime_base)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_email, sender_password)
    text = message.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    print('Mail Sent')

def get_location_by_ip():
    locator = Nominatim(user_agent="myGeocoder")
    ip_location = locator.geocode('')
    return ip_location

location = get_location_by_ip()
print("Latitude:", location.latitude)
print("Longitude:", location.longitude)


if __name__ == "__main__":
    sender_email = 'sreciantrinit@gmail.com'
    sender_password = 'triNIT-23srecian'
    receiver_email = 'devanand6111@gmail.com'
    subject = 'Miserable condition of Roads.'

    location = get_location_by_ip()
    a = str(location.latitude)
    b = str(location.longitude)

    body = '''Sir, I would like to draw attention of the authority regarding 
    the poor condition of the roads in our locality through the column of your esteemed 
    daily. In our locality, there are many potholes on the roads. The vehicles 
    have to halt after some seconds to adjust with the road. ''' +" Latitude : " +a+" Longitude: "+b
    file_path = 'D:\\road damage(2)\\yolov8-roadpothole-detection-main\\output.avi'
    send_email(sender_email, sender_password, receiver_email, subject, body, file_path)
