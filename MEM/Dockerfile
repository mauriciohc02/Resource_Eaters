# Base Image
FROM python:3.10-alpine

WORKDIR /home
# Adding program to image
COPY mem.py /home

# Running command
CMD ["python3", "./mem.py"]

# docker build -t mem-eater .
# docker run --name [CONTAINER_NAME] -d mem-eater

# OR!

# docker pull mauriciohc/mem-eater
# docker run --name [CONTAINER_NAME] -d mauriciohc/mem-eater
