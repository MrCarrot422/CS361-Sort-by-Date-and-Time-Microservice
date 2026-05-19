# Author: Elliot Glass
# Description: Implementation of test program that calls on a microservice to sort a list of upcoming dates.
# Date: 5/18/2026

import os
import time

while True:
    response = input("Press 1 to test the microservice.\n") # Use CLI to test microservice

    if response == "1":
        if not os.path.exists('./requests'): # Check if directory exists
            os.mkdir("./requests")
            
        filename = "./requests/request.txt"
        print(os.path.abspath(filename))

        with open(filename, "w") as fn:
            fn.write("items = [[basketball, 5/16, 5pm], [volleyball, 5/14, 1pm], [spikeball, 5/15, 3pm]]\n") # Sample file
            fn.write("relevant_times = True\n")
    
        print("Created test file.")
        time.sleep(5) # Wait a moment for the service to respond

        if os.path.exists("./responses/response.txt"):
            with open("./responses/response.txt", "r") as fn:
                print("Response file located. Viewing contents:\n")
                print(fn.read())
        
        else:
            print("No response file received.")