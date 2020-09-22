# influxdb_migration

### Migrate the data from one Influxdb database to another.
add argument '-h' for help

Usage:

```
influxDB_copy.py sURL sDB sUser sPasswd dURL dDB dUser dPasswd startTime endTime
```

Here is a real example:

```
python influxDB_copy.py https://sensorweb.us shake test sensorweb https://sensorweb.us testdb test sensorweb 2020-08-07T19:22:31 2020-08-07T19:22:35
```
open browser with user/password:guest/sensorweb_guest to see the result at grafana https://sensorweb.us:3000



positional arguments:
  - sURL        the URL of source database. e.g. "http://localhost"
  - sDB         name of the source database.
  - sUser       username of the source database.
  - sPasswd     password of the source database.
  - dURL        the URL of destination database.
  - dDB         name of the destination database.
  - dUser       username of the destination database.
  - dPasswd     password of the destination database.
  - startTime   start time. format: Year-Mon-Day-Hour-Min-Sec. e.g. "2020-06-04T15:40:00"
  - endTime     end time. format: Year-Mon-Day-Hour-Min-Sec. e.g. "2020-06-05T15:40:00"

### Generate a sinewave form and save to the influxdb
```
python sine_influx.py ipaddr username passwd
```