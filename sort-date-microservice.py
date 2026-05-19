# Author: Garret Simon
# Description: Sort by Date and Time Microservice for CS361. Receives a list of items with dates and times through a
# text file. Sorts "items" by soonest to latest. If relevant_times is True, dates/times that have already passed are
# removed from "items". Sends sorted "items" to a different text file.
# Date: 5/18/2026
import time
import ast
from datetime import datetime
import os

variables = {}

while True:
    time.sleep(2)

    with open("./requests/request.txt", "r") as f:
        content = f.read(5)

    if content == "items":
        print("Request Received")
        with open("./requests/request.txt", "r") as text:
            for line in text:

                line = line.strip()

                if "=" not in line:
                    continue

                name, value = line.split("=", 1)

                variables[name.strip()] = ast.literal_eval(value.strip())

        items = variables.get("items", [])
        relevant_times = variables.get("relevant_times", False)
        # remove past days/times if relevant_times is true
        if relevant_times:
            now = datetime.now()

            items = [
                item for item in items
                if datetime.strptime(
                    f"{item[1]} {item[2]}",
                    "%Y-%m-%d %H:%M"
                ) > now
            ]

        # always sort
        items.sort(
            key=lambda item: datetime.strptime(
                f"{item[1]} {item[2]}",
                "%Y-%m-%d %H:%M"
            )
        )
        if not os.path.exists('./responses'): # Check if directory exists
            os.mkdir("./responses")
        file = "./responses/response.txt"
        with open(file, "w") as fn:
            fn.write("items = " + str(items) + "\n")
        print("Response Sent")
        with open("./requests/request.txt", "w") as f:
            f.truncate(0)
