FROM python:3.12-alpine3.19
ARG uid=1001
ARG gid=51

RUN adduser --system --no-create-home nonroot && addgroup --gid $gid nonroot

COPY --chown=nonroot:nonroot . /app
RUN pip install --no-cache-dir -r /app/requirements.txt
#    pip install pytest httpx
#
#RUN cp /app/tests/test_main.py /app/src

USER nonroot

CMD ["python3", "/app/src/main.py"]
