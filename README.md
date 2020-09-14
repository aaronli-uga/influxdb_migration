# influxdb_migration

### Migrate the data from one Influxdb database to another.
add argument '-h' for help

Usage:

```
influxDB_copy.py sURL sDB dURL dDB startTime endTime
```

positional arguments:
  - sURL        the URL of source database. e.g. "localhost"
  - sDB         name of the source database.
  - sUser       username of the source database.
  - sPasswd     password of the source database.
  - dURL        the URL of destination database.
  - dDB         name of the destination database.
  - dUser       username of the destination database.
  - dPasswd     password of the destination database.
  - startTime   start time. format: Year-Mon-Day-Hour-Min-Sec. e.g. "2020-07-31-11-59-59"
  - endTime     end time. format: Year-Mon-Day-Hour-Min-Sec. e.g. "2020-08-01-11-59-59"

### Generate a sinewave form and save to the influxdb
