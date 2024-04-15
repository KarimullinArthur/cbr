import os

from dotenv import load_dotenv


load_dotenv()


VERSION = os.getenv('VERSION')
PORT = os.getenv('PORT')


try:
    if 1 <= int(PORT) <= 65535:
        pass
    else:
        PORT = 8000
except ValueError:
    PORT = 8000
