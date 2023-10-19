from typing import List
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from .models import users
from .config import settings
from jinja2 import Environment, select_autoescape, PackageLoader


env = Environment(
    loader=PackageLoader("core", "templates"),
    autoescape=select_autoescape(["html", "xml"]),
)


class Email:
    def __init__(self, user: users.User, url: str, email: List[EmailStr]):
        self.name = user.first_name
        self.sender = "kishu@fusemachines.com"
        self.ema
        self.url = url
        pass

    async def send_mail(self, subject, template):
        # Define the config
        conf = ConnectionConfig(
            MAIL_USERNAME=settings.EMAIL_USERNAME,
            MAIL_PASSWORD=settings.EMAIL_PASSWORD,
            MAIL_FROM=settings.EMAIL_FROM,
            MAIL_PORT=settings.EMAIL_PORT,
            MAIL_SERVER=settings.EMAIL_HOST,
            MAIL_STARTTLS=False,
            MAIL_SSL_TLS=False,
            USE_CREDENTIALS=True,
            VALIDATE_CERTS=True,
        )
        # Generate the HTML template base on the template name
        template = env.get_template(f"{template}.html")

        html = template.render(url=self.url, first_name=self.name, subject=subject)

        # Define the message options
        message = MessageSchema(
            subject=subject, recipients=self.email, body=html, subtype="html"
        )

        # Send the email
        fm = FastMail(conf)
        await fm.send_message(message)

    async def send_verification_code(self):
        await self.send_mail("Your verification code (Valid for 10min)", "email-verification")
