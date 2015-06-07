#!/usr/bin/env python
import sys

__author__ = 'nodir.azam'

error_counter = 0
table_name = 'nodir.azam'
control_value = 130

for line in sys.stdin:
    line = line.strip()
    line = line.strip("\n").strip("\t")

    if line is None or len(line) <= 0:
        continue

    try:
        parts = line.split("\t")

        if len(parts) == 3:

            str_uid, str_ts, str_url = line.split("\t")

            str_uid = str_uid.strip()
            str_ts = str_ts.strip()
            str_url = str_url.strip()

            if str_uid is None or len(str_uid) <= 0 or str_uid == '-':
                continue

            if str_ts is None or len(str_ts) <= 0:
                continue

            if str_url is None or len(str_url) <= 0:
                continue

            uid = int(str_uid)
            ts = int(float(str_ts))
            str_url = str_url.strip()

            if uid % 256 <> control_value:
                continue

            if ts <= 0:
                continue

            if str_url is None or len(str_url) <= 0:
                continue

            print "%d %d %s" % (uid, ts, str_url)
    except:
        error_counter += 1
        if error_counter > 10:
            continue
        else:
            print ("error: %s", line)
