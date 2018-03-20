#!/bin/bash

# ~/ml4/public/csv/curlGSPC.bash
# Demo:
# bash -x curlGSPC.bash
/usr/bin/curl http://tkrprice.herokuapp.com/static/CSV/history/^GSPC.csv|grep -v null > GSPC.csv

exit
