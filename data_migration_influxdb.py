from influxdb import InfluxDBClient
import numpy as np
import time
import math
import datetime
import sys
from datetime import datetime 

'''
This program is for migrating data from one database to the other.

InfluxDB performs best when data is written to the database in batches.
This helps minimize the network overhead of opening and closing HTTP connections by transmitting more data at once. 
The ideal batch size for InfluxDB is 5,000-10,000 points.
'''

#Remote data base information
IP = 'localhost'
PORT = 8086
USER = 'aaronli'
PASSWORD = '7781'
# specify the measurement name you are going to migrate data from
sname = 'temperature' 

# keys of tags and fields of the measurement, must be specified
tags = ['location', 'mood', 'vibe']
fields = ['value']

# The ideal batch size for InfluxDB is 5,000-10,000 points.
write_batch_size = 5000

# Source database information
sDB = 'tests'

# Destination database information
dDB = 'testd'

s_client = InfluxDBClient(IP, PORT, USER, PASSWORD, sDB)
d_client = InfluxDBClient(IP, PORT, USER, PASSWORD, dDB)

# Time range, Y-M-D-h-m
starttime = datetime(2020, 7, 30, 11, 22, 0)
endtime = datetime(2020, 7, 30, 11, 35, 0)

timestamp = starttime.timestamp()*1000
start_str = str(int((timestamp)*1000000))

timestamp = endtime.timestamp()*1000
end_str=str(int((timestamp)*1000000))

PORT = 8086
USER = 'aaronli'
PASSWORD = '7781'
# Query data from source database
data_json = {} 
query = 'SELECT * FROM '+ sname +' WHERE time > '+ start_str +' and time < '+end_str
result = s_client.query(query)
values = list(result.get_points())

data = []
for point in values:
    data.append(
        {
            "measurement": sname,
            # The tags and fields part must be specified manually based on user's data
            "tags":{
                tags[0]: point[tags[0]],
                tags[1]: point[tags[1]],
                tags[2]: point[tags[2]],
            },
            "fields":{
                fields[0]: point[fields[0]]
            },
            "time": point['time']
        }
    )

# Write data to destination database
client_write_start_time = time.perf_counter()
d_client.write_points(data, database=dDB, time_precision='ms', batch_size = write_batch_size, protocol='json')
client_write_end_time = time.perf_counter()

print("Migration completed! Data write time: {time}s".format(time=client_write_end_time - client_write_start_time))