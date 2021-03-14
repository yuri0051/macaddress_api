FROM python:3

RUN useradd -m macadderss_api

WORKDIR /home/macadderss_api

USER macadderss_api

COPY . .

RUN pip3 install -r requirements.txt

CMD ["main.py"]

ENTRYPOINT ["python3"]