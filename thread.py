# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:50:19 2021

@author: ashra
"""

import threading, os, edge_fileread, json, requests


stopFlag = threading.Event()

def retrySendingdata(self, row):
    while not self.stopped.wait(5):
            #Call HTTP API 
            json_stirng  = json.dumps(row)
            response = requests.post("127.0.0.1:8000", data=json_stirng)
            # if response 200 then return
            if response.status_code == 200:
                return
            
#Repeat Timer implementation
class SendTimerThread(threading.Thread):
    def __init__(self, event, arg):
        threading.Thread.__init__(self)
        self.stopped = event
        
    def run(self):       
        print("automatically runs run")
        # Start an infinite loop, allow the loop to be interrupted and stopped using the stopped event
        # wait for 60 seconds and run the body of the loop
        while not self.stopped.wait(60):
            try:
                row = edge_fileread.getRowFromCSV()
                #JSON Dump
                json_stirng  = json.dumps(row)
                print("This json needs to be sent ", json_stirng)
                #Call HTTP API
                response = requests.post("http://127.0.0.1:8000", data=json_stirng)
                #Check response, if response is 400, retry after 5 secs
                if response.status_code == 400:
                    retrySendingdata(self, row)
            except Exception as ex:
                print(ex)

        
  
    #Main function
if __name__ == '__main__':
    print("entered")
    def startForeverLoop():
    
        try:
            # Clear the interrupt in case it was set earlier
            stopFlag.clear()
            arg = {}
            timer = SendTimerThread(stopFlag, arg)
            timer.start()
        except Exception as ex :
            print(ex)
            
    startForeverLoop()

def stopForeverLoop():
    stopFlag.set()