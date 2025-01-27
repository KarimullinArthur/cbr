import uvicorn

import settings
from router import app


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=settings.PORT)
