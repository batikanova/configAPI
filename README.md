# configAPI
Setup API for Devices

controllers folder has a device_controller.py which has deviceConfigController to check and send config to device also getDeviceInfo to get info that selected device's

emitters has a socketio.emit functions and endpoints

events has a socketio events

extensions has a socketio object and database objects

models has a schema cause to validate data that comes from front and queries.py has a db queries

repositories has a db funcions

routes has a API routes

services has a API Threads. 


use pip install -r requirements.txt
then you can run python run.py

1- Client connects with socketio and registers by sending ip, mac and hostname
2- Server sends device_info to front-end after client connected by using client_list socketio event.
3- Client can be got identify from front-end to backend by using device_config socketio event. 
