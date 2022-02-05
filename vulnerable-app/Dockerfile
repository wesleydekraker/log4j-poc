FROM openjdk:8u181-jdk-alpine

EXPOSE 8080

WORKDIR /app
COPY vulnerable-app.jar .
CMD ["java", "-jar", "/app/vulnerable-app.jar"]
