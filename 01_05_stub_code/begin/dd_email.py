import dd_content
import datetime

class DailyDigestEmail:

    def __init__(self):
        self.content = {
            'quote':{'include': True, 'content': dd_content.get_random_quote() },
            'weather':{'include': True, 'content':  dd_content.get_weather_forecast()},
            'wikipedia':{'include': True, 'content': dd_content.get_wikipedia_article()}
        }

    def send_email(self):
        pass

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