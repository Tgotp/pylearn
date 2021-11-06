from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = '435822082@qq.com'
    receivers = ['3224065977@qq.com']
    message = MIMEText('窝嫩叠窝嫩叠窝嫩叠窝嫩叠窝嫩叠', 'plain', 'utf-8')
    message['From'] = Header('xdxdxd', 'utf-8')
    message['To'] = Header('张小胖', 'utf-8')
    message['Subject'] = Header('PY测试.', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    smtper.login(sender, 'zgvqveputplnbjdi')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()
