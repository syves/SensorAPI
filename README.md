# Fullstack Developer Job Application Assignment


Our servers receive health reports from different types of devices. Our backend generates a report based on pre-defined formula of device and status.

Your assignment consists of the following:

### Part #1: Processing

* Attached an example of a report that was generated based on the devices health reports - see `report.csv`.
* You need to process the incoming CSV data, let's assume this will run in a periodic manner (how?)
* The CSV is formatted with the following columns:
  * timestamp, id, type, status
* You can do with the data whatever you like (store in-memory, database, files, etc.)
* The data will be used *only* for the *status report* (Part #2).
* Write a script/tool that will pre-process the data from this CSV and prepare it for Part #2.
* You can write this script in any language you want, preferably Python or Ruby.
* Keep this script as simple as possible, it has one task and should do only this one task!

### Part #2: Reporting
#### View 1
* Users selects a day
* Display the 10 most "popular" devices, Popularity of a device is defined as the number of **distinct** occurrences in the same day
* For each device in the report, show the percentage change of occurrences in the same day a week before.
#### View 2
* User selects a device type from the list of available types and status.
* Display a table of day and total devices for each day (for the last 30 days).
* The web-app is read-only (the user cannot add/modify the data).

##### Implementation details:
* The trends reporting must be implemented as a web-application.
* No need to implement authentication / login for the web application.
* Design (colors etc.) is not really important for this assignment, don't waste your time on CSS tweaks.


### Sample data

    timestamp,id,type,status
    2009-12-01T06:59:22Z,1q2w3e4r,sensor,online
    2009-12-01T06:59:22Z,1q2w3e4r,gateway,offline

### Shakrah's notes.

1. Processing incoming CSV data periodically.
  * If CSV files arrive regularly. They should be uploaded to an AWS bucket. Then a nightly cron job would run the processing job 'preprocess.py' for each report in reports.
  * Processing is defined in 'models.py'

2. Populate the db.
  * run store_data.py

3. Todo Items:
  * If this was in production I would enable caching to improve performance time on sql queries.
  * And encrypt secret keys.
  * If I knew how the incoming reports were named I would create an output file for each report.
