import json

from fastapi import FastAPI, Response

import settings
import parser


app = FastAPI()


@app.get("/info")
def get_info():
    result = {
        'version': settings.VERSION,
        'service': 'currency',
        'author': 'a.karimullin'
    }

    return Response(content=json.dumps(result, indent=4),
                    media_type="application/json")


@app.get("/info/currency")
def get_rate(currency: str, date: str = ''):
    result = {
        'service': 'currency',
        'data': {
            currency: parser.get_rate(currency, date)
        }
    }

    return Response(content=json.dumps(result, indent=4),
                    media_type="application/json")
