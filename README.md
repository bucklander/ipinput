# ipinput.py

[![Build Status](https://travis-ci.org/bucklander/ipinput.svg?branch=main)](https://travis-ci.org/bucklander/ipinput)

An example coding and container deployment excercise for a simple route lookup process program (like Cisco process switching) with WSGI-enabled, REST API attached. Meant for educational/training purposes only. 

Imports a JSON list of routes as a virtual RIB, and takes input from the user to determine the best next-hop forwarding path(s).

## Build & Run Instructions
```
git clone git@github.com:bucklander/ipinput.git
cd ipinput/
docker build --tag ipinput:latest .
docker run -p 8080:5017 -d --name ipinput ipinput:latest
```

## Usage

Query route table for best route(s):  
`curl http://127.0.0.1:8080/route/<ip_address>`  

Display full route table:  
`curl http://127.0.0.1:8080/routetable`  