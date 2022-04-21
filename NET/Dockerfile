# Base Image
FROM python:3.10-alpine

# Installing curl
RUN apk update \
    && apk upgrade \
    && apk add curl

WORKDIR /home
# Adding program to image
COPY net.py /home

# Running command
CMD ["python3", "./net.py"]

# docker build -t net-eater .
# docker run --name [CONTAINER_NAME] -d net-eater

# OR!

# docker pull mauriciohc/net-eater
# docker run --name [CONTAINER_NAME] -d mauriciohc/net-eater
