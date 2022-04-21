# Base Image
FROM python:3.10-alpine

WORKDIR /home
# Adding program to image
COPY disk.py /home

# Running command
CMD ["python3", "./disk.py"]

# docker build -t disk-eater .
# docker run --name [CONTAINER_NAME] -d disk-eater

# OR!

# docker pull mauriciohc/disk-eater
# docker run --name [CONTAINER_NAME] -d mauriciohc/disk-eater
