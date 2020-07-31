#!/usr/bin/python3
'''
Generate customised sine wave form and save in to influxDB
usage:
./sine_influx.py ${IPAD} ${USER} ${PASS}
'''

import time
import math
import datetime
import subprocess
import sys

f_sampling = 100
f_wave = 10
timestamp = datetime.datetime.now().timestamp()

while True:
    http_post = "curl -i -XPOST \'http://%s:8086/write?db=tests\' -u %s:%s --data-binary \'" % (sys.argv[1], sys.argv[2], sys.argv[3])
    for i in range(f_sampling):
        timestamp += 1 / f_sampling
        value = math.sin(2 * math.pi * f_wave * timestamp)
        http_post += "\ntemperature,location=UGA,mood=happy,vibe=edm value=" 
        http_post += str(value) + " " + str(int(timestamp*10e8))
        time.sleep(1 / f_sampling)
    http_post += "\'"
    subprocess.call(http_post, shell=True)
