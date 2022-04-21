# Base Image
FROM python:3.10-alpine

WORKDIR /home
# Adding program to image
COPY cpu.py /home

# Running command
CMD ["python3", "./cpu.py"]

# docker build -t cpu-eater .
# docker run --name [CONTAINER_NAME] -d cpu-eater

# OR!

# docker pull mauriciohc/cpu-eater
# docker run --name [CONTAINER_NAME] -d mauriciohc/cpu-eater
