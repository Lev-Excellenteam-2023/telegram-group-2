from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_TOKEN: str = os.getenv('OPENAI_TOKEN')
TELEGRAM_TOKEN: str = os.getenv('TELEGRAM_TOKEN')
NGROK_FORWARDING: str = os.getenv('NGROK_FORWARDING')
DATABASE_URL: str = os.getenv('DATABASE_URL')
TELEGRAM_INIT_WEBHOOK_URL: str = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook?url={NGROK_FORWARDING}'
PRESENTATION_OF_BOT = "Hello! I'm a bot for personalized planting advice. I help you choose ideal plants based on " \
                      "your location, preferences, and experience. I also provide care tips for successful growth. " \
                      "How can I help you today?"
CHAT = 'gpt-3.5-turbo-16k'
MAX_TOKENS = 80

