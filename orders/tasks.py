from darproject.celery import app
from .models import Order
import os
import smtplib
from configparser import ConfigParser
from django.conf import settings


def send_mail(to_addr, subject, text, encode='utf-8'):
    """
    Отправка электронного письма (email)
    """
    server = ''
    port = ''
    from_addr = ''
    passwd = settings.EMAIL_HOST_PASSWORD

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")
    # проверка наличия файла `email.ini`
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
        # извлечение переменных из конфигурации
        server = cfg.get("smtp", "server")
        port = cfg.get("smtp", "port")
        from_addr = cfg.get("smtp", "email")

    charset = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    # формируем тело письма
    body = "\r\n".join((f"From: {from_addr}", f"To: {', '.join(to_addr)}",
                        f"Subject: {subject}", mime, charset, "", text))

    try:
        # подключаемся к почтовому сервису
        smtp = smtplib.SMTP_SSL(':'.join([server, port]))
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(from_addr, passwd)
        # пробуем послать письмо
        smtp.sendmail(from_addr, to_addr, body.encode(encode))
    except smtplib.SMTPException as err:
        raise err
    finally:
        smtp.quit()


@app.task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Заказ №. {}'.format(order_id)
    message = 'Уважаемый {},\n\nВы успешно оформили заказ.\
                Ваш заказ № {}.'.format(order.customer_name,
                                             order.id)
    send_mail([order.customer_email],
              subject,
              message)

