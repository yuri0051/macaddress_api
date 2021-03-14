1) Install module:

source venv/bin/activate
pip install

2) Build docker image

Using thin, short-lived containers. Using USER with least privileged access.

docker build -t macadderss_api:0.1 .

3) Run module:

Put your Api key into main.py API_KEY

Example: python3 main.py --macaddress 44:38:39:ff:ef:57

Example docker: docker run -it macadderss_api:0.1 main.py --macaddress 44:38:39:ff:ef:57
