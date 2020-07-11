import base64
from itsdangerous import URLSafeTimedSerializer

from creativecoin import app
from creativecoin.email import EmailSender

def generate_email_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    token = serializer.dumps(email, salt=app.config['SECRET_SALT_KEY'])
    encoded_token = base64.b64encode(token.encode("utf-8")).decode("utf-8")
    return encoded_token


def confirm_token(token, expiration=3600):
    decoded_token = base64.b64decode(token).decode("utf-8")
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            decoded_token,
            salt=app.config['SECRET_SALT_KEY'],
            max_age=expiration
        )
    except Exception as e:
        app.logger.error(e)
        raise Exception()

    return email

def send_verification_email(email):
    token = generate_email_token(email)
    params = [
        {
            "verification_link": "{root_url}/confirm/{token}".format(root_url = app.config['SERVER_NAME'], token = token)
        }
    ]
    mail = EmailSender()
    mail.generate_verification_body()

    mail.send_mail()


