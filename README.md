# ipinput.py

An example coding and container deployment excercise for a super simple route lookup process program (like Cisco process switching) with WSGI-enabled, REST API bolted on. 

Imports a JSON list of routes as a virtual RIB, and takes input from the user to determine the best next-hop forwarding path(s).

## Build & Run Instructions
```
git clone git@github.com:bucklander/ipinput.git
docker build --tag ipinput:1.0 .
docker run -p 8080:5017 -d --name ipinput ipinput:1.0
```

## Usage

Query route table for best route(s):  
`curl http://127.0.0.1:8080/route/<ip_address>`  

Display full route table:  
`curl http://127.0.0.1:8080/routetable`  