FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /app

RUN apt-get update && apt-get install -y openjdk-8-jdk python3 git maven

RUN git clone https://github.com/mbechler/marshalsec.git .
RUN git checkout f645788e6a75155fdfccab1fc036a032212d8484
RUN mvn clean package -DskipTests

COPY Exploit.java .
COPY main.py .

RUN javac Exploit.java

CMD ["python3", "-u", "main.py"]
