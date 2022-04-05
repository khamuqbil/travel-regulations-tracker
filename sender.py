import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sender@something.com"  # Enter your address
receiver_email = "receiver@something.com"  # Enter receiver address
password = input("Type your password and press enter: ") # or you can use env variable 

message = """\

Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
