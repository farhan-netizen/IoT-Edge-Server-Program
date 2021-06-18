# IoT-Edge-Server-Program

Edge Program - A forever executable python program to read sensor data and send it to the cloud server.
Server Program - A simple python HTTP server which accepts data(from edge api call) and save it in a CSV file.

Server.py file implements Server Program.
Thread.py and Edge_fileread.py file together implements Edge program. Edge_fileread is imported and called in thread.py file to read each row of given dataset. Thread.py is where threading has been implemented to achieve api calling after every 60 secs and publish buffered data after 5 secs in case server returns failure.
