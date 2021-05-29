import smtplib, time, os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header



# 配置邮箱属性
# 准备附件，增加附件，组装邮件内容和标题
# 登录并发送邮件


class SendEmail():

    def senMail(self):

        sender = '18612863544@163.com'

        receiver = '249298402@qq.com'

        t = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())

        subject = '自动化测试结果' + t

        smtserver = 'smtp.163.com'

        username = '18612863544'

        password = 'TSCRKXYSBFDJRLKX'

        file = os.listdir(os.path.dirname(os.path.dirname(__file__))+'/report/')[-1]
        with open(os.path.dirname(os.path.dirname(__file__))+'/report/'+file, 'rb') as f:
            mail_body = f.read()
            msg = MIMEMultipart()
            att = MIMEText(mail_body, 'plain', 'utf-8')
            att['Contest-Type'] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename=report.html'
            msg.attach(att)

            content = 'python测试报告'

            msg.attach(MIMEText(content, 'plain', 'utf-8'))
            msg['Subject'] = Header(subject, 'utf-8')
            msg['Form'] = sender
            msg['To'] = receiver

        try:
            s = smtplib.SMTP()
            s.connect(smtserver)
            s.login(username, password)
            s.sendmail(sender, receiver, msg.as_string())
        except Exception as msg:
            print(u'邮件发送失败%s' % msg)

        else:
            print('邮件发送成功')


if __name__ == '__main__':
    mail = SendEmail()
    mail.senMail()
