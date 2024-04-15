import uvicorn

import settings
from router import app


if __name__ == '__main__':
    uvicorn.run(app, port=settings.PORT)
