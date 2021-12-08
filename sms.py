import install


REST_API_ID = 'ae800224ee5eaba53e9f4aef8794ed60'  # вставляем свое значение
REST_API_SECRET = '5cd91c648ac9928a61f78033854f02f1'  # вставляем свое значение
TOKEN_STORAGE = 'memcached'
MEMCACHED_HOST = '127.0.0.1:11211'
SENDER_NAME = 'TravelCode'


def send_sms(phone_number, email_address, username):
    install.install_lib("pysendpulse")
    install.install_lib("requests")
    from pysendpulse.pysendpulse import PySendPulse

    SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE, memcached_host=MEMCACHED_HOST)

    phones_for_send = [phone_number]

    SPApiProxy.sms_send(SENDER_NAME, phones_for_send,
                        f"Уважаемый {username}, информация по Вашей скидке отправлена на адрес {email_address}. "
                        f"С уважением, команда {SENDER_NAME}")

    # print(f"sms отправлено на номер - {phone_number}")
