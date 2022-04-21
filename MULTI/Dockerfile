# Base Image
FROM python:3.10-alpine

# Installing curl
RUN apk update \
    && apk upgrade \
    && apk add curl

WORKDIR /home
# Adding files to image
COPY cpu.py \
    disk.py \
    mem.py \
    net.py \
    choosing.sh /home/

# Setting the env variable we're gonna use
ENV EATER="no"

# Running the script
CMD ["sh", "choosing.sh"]

# docker build -t multi-eater .
# docker run --name [CONTAINER_NAME] -e EATER=[VALUE] -d multi-eater

# OR!

# docker pull mauriciohc/multi-eater
# docker run --name [CONTAINER_NAME] -d mauriciohc/multi-eater
