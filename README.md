# Cab Project

## Description
This project developed with the Django framework, we used redis and mysql to store data on disk and memory.
You can find more details about the architecture of the app [Here](http://google.com "Documentation").
Also you can see api's input/output data in http://localhost:8000/shema/redoc/ ,after the project gets running.


## Getting Started
#### Dependencies
docker-compose version:3.9
#### Up and Running
```
docker-compose up -d
```
[Warning!] mysql needs a few minutes to run healthy, so the above command may take a little time. Please be patient.

after all services running healthy, you can call api's in http://localhost:8000

[Warning!] Do not forget to fiil the threshold_requsts_database with create/api before calling cab-price-coefficient/ api
 


