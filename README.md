# influxdb_migration

### Migrate the data from one Influxdb database to another.
Usage:

influxDB_copy.py [-h] sURL sDB dURL dDB startTime endTime

Migrate data from one influxDB database to another.

positional arguments:
  sURL        the URL of source database.
  sDB         name of the source database.
  dURL        the URL of destination database.
  dDB         name of the destination database.
  startTime   start time. format: Year-Mon-Day-Hour-Min-Sec
  endTime     end time. format: Year-Mon-Day-Hour-Min-Sec

### Generate a sinewave form and save to the influxdb
