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
            
        filename = "./requests/sort_request.txt"

        with open(filename, "w") as fn:
            fn.write("items = [['basketball', '2026-5-20', '17:00'], ['volleyball', '2026-5-21', '13:00'], "
                     "['spikeball', '2026-5-17', '15:00']]\n") # Sample file
            fn.write("relevant_times = True\n")
    
        print("Created test file.")
        time.sleep(5) # Wait a moment for the service to respond

        if os.path.exists("./responses/sort_response.txt"):
            with open("./responses/sort_response.txt", "r") as fn:
                print("Response file located. Viewing contents:\n")
                print(fn.read())
        
        else:
            print("No response file received.")
