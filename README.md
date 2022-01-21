You'd probably want to run this as a cronjob.

check https://ostechnix.com/a-beginners-guide-to-cron-jobs/ for a beginner's guide

if your lazy and want to run this every 10 minutes:

in Terminal:
```Bash
crontab -e
```

scroll down to the bottom and paste the following:
```
*/5 * * * * /usr/bin/python3 /path/to/the/main.py
```