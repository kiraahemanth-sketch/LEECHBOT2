FROM alonekingstar77/hemanth:v3

WORKDIR /usr/src/app

RUN chmod 777 /usr/src/app
RUN uv venv --system-site-packages

COPY requirements.txt .
RUN uv pip install --no-cache-dir -r requirements.txt && \
    uv pip install --no-cache-dir "urllib3<2.0.0"

COPY . .

CMD ["bash", "start.sh"]
