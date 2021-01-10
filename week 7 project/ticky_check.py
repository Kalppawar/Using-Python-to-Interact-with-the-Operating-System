#!/usr/bin/env python3

import re
import subprocess
import operator
import csv

errorSet = dict()
errorCount = list()
userList = dict()
# subprocess.run(["./helper.sh"])

with open('error.log') as log:
    for line in log:
        error = re.search(r" ticky: ERROR ([\w \']*) \(", line)
        if error.group(1) in errorSet:
            errorSet[error.group(1)] += 1
        else:
            errorSet[error.group(1)] = 1

errorSet = sorted(errorSet.items(), key=operator.itemgetter(1), reverse=True)

for item in errorSet:
    row = {"Error": item[0], "Count": item[1]}
    errorCount.append(row)

writer = csv.DictWriter(open('error_message.csv', "w"), ["Error", "Count"])
writer.writeheader()
for data in errorCount:
    writer.writerow(data)



with open('syslog.log') as logfile:
    for line in logfile:
        log = re.search(r' ticky: ([A-Z]*) [\w \#\[\]\']* \(([a-z \.]*)\)', line)
        logType = log.group(1)
        logUser = log.group(2)
        if logUser in userList:
            if logType == 'ERROR':
                userList[logUser][1]+=1
            else:
                userList[logUser][0]+=1

        else:
            userList[logUser] = [0, 0]
            if logType == 'ERROR':
                userList[logUser][1]+=1
            else:
                userList[logUser][0]+=1

userList = sorted(userList.items())
writer = csv.DictWriter(open('user_statistics.csv', "w"), ["Username", "INFO", "ERROR"])
writer.writeheader()
for data in userList:
    row = {'Username': data[0], 'INFO': data[1][0], 'ERROR': data[1][1]}
    writer.writerow(row)