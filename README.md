# Resource_Eaters
Resource_Eaters is a small project that allows Docker users to consume PC resources to manage containers using some Docker GUIs, so they can choose which one best suits their needs.

The more containers you run, the more resources you consume.

# Prerequisites
Before you begin, ensure you have met the following requirements:
- Docker
- Docker Compose
- Python 3

Pull Docker images:
- ```docker pull mauriciohc/cpu-eater```
- ```docker pull mauriciohc/disk-eater```
- ```docker pull mauriciohc/mem-eater```
- ```docker pull mauriciohc/net-eater```
- ```docker pull mauriciohc/multi-eater```

# Using Resource_Eaters
To use it, follow these steps:

## Running a container
| PC RESOURCE | RUN                                                                                 | IMAGE REPOSITORY |
| ----------- | ----------------------------------------------------------------------------------- | ---------------- |
| CPU         | ```docker run --name [CONTAINER_NAME] -d mauriciohc/cpu-eater```                    | [```mauriciohc/cpu-eater```](https://hub.docker.com/r/mauriciohc/cpu-eater)   |
| DISK        | ```docker run --name [CONTAINER_NAME] -d mauriciohc/disk-eater```                   | [```mauriciohc/disk-eater```](https://hub.docker.com/r/mauriciohc/disk-eater)  |
| MEM         | ```docker run --name [CONTAINER_NAME] -d mauriciohc/mem-eater```                    | [```mauriciohc/mem-eater```](https://hub.docker.com/r/mauriciohc/mem-eater)   |
| NET         | ```docker run --name [CONTAINER_NAME] -d mauriciohc/net-eater```                    | [```mauriciohc/net-eater```](https://hub.docker.com/r/mauriciohc/net-eater)   |
| MULTI       | ```docker run --name [CONTAINER_NAME] -e EATER=[VALUE] -d mauriciohc/multi-eater``` | [```mauriciohc/multi-eater```](https://hub.docker.com/r/mauriciohc/multi-eater) |

## Running a ```docker-compose.yml``` file
1. Navigate into the ```docker-compose.yml``` file directory: ```cd [DIRECTORY_NAME]```
2. Make sure you're in the right directory: ```pwd```
3. Run the ```docker-compose.yml``` file: ```docker-compose up -d```

## Other commands
In case you want:
- to stop a container: ```docker stop [CONTAINER_NAME]```
- to remove a container: ```docker rm [CONTAINER_NAME]```
- to stop and remove a docker-compose stack: ```docker-compose down```
