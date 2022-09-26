FROM tensorflow/tensorflow:latest-gpu

ENV DEBIAN_FRONTED noninteractive

WORKDIR /app
COPY requirements.txt /app

RUN pip install --prefer-binary --no-cache-dir -q -r requirements && \
  rm -rf ~/.cache

COPY . /app/
VOLUME /root/.keras

EXPOSE 7860
CMD ["python", "webui.py"]
