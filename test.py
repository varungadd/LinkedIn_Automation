import smtplib

EMAIL = "varungadi2003@gmail.com"
PASSWORD = "npbrzpajquhsvswo"

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL, PASSWORD)
print("Login success")