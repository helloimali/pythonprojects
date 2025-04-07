import dd_content
import datetime
from email.message import EmailMessage

class DailyDigestEmail:

    def __init__(self):
        self.content = {
            'quote':{'include': True, 'content': dd_content.get_random_quote() },
            'weather':{'include': True, 'content':  dd_content.get_weather_forecast()},
            'wikipedia':{'include': True, 'content': dd_content.get_wikipedia_article()}
        }
        self.recipients_list = ['test@email.com']
        self.sender_creds = {'email':'new@email.com', 'pass': 'passpasspasspass'}

    def send_email(self):
        msg = EmailMessage()
        msg['Subject'] = f'Daily Digest - {datetime.date.today().strftime("%d %b %Y")}'
        msg['From'] = self.sender_credentials['email']
        msg['To'] = ', '.join(self.recipients_list)

        # add Plaintext and HTML content
        msg_body = self.format_message()
        msg.set_content(msg_body['text'])
        msg.add_alternative(msg_body['html'], subtype='html')

        # secure connection with STMP server and send email
        with smtplib.SMTP('smtp.office365.com', 587) as server:
            server.starttls()
            server.login(self.sender_credentials['email'],
                         self.sender_credentials['password'])
            server.send_message(msg)

    def format_message(self):
        # gen plaintext
        text = f"Daily Digest - {datetime.date.today()}"

        if self.content['quote']['include'] and self.content['quote']['content']:
            text += f"Quote \n\n"
            text += f"{self.content['quote']['content']['quote']} - by: {self.content['quote']['content']['author']}"
        text += f"\n\n"

        if self.content['weather']['include'] and self.content['weather']['content']:
            text += f"Weather: {self.content['weather']['content']['city']} \n\n"
            for forecast in self.content['weather']['content']['period']:
                text += f"{forecast['temp']} - Desc: {forecast['desc']}"
        text += f"\n\n"

        if self.content['wikipedia']['include'] and self.content['wikipedia']['content']:
            text += f"Wiki \n\n"
            text += f"{self.content['wikipedia']['content']} \n"
            # text += f"{self.content['wikipedia']['content']['summary']} \n"
            # text += f"URL: {self.content['wikipedia']['content']['url']} \n"

        return text
if __name__ == '__main__':
    email = DailyDigestEmail()
    print(email.format_message())