#!/bin/bash

# wgetibm.bash

# This script should download ibm.csv and then load it into a table called prices.

cd /tmp/
rm -f ibm.csv
/usr/bin/wget http://ml4.us/csv/ibm.csv

/usr/bin/psql -aP pager=no<<EOF
DROP TABLE IF EXISTS prices;

CREATE TABLE prices(
cdate   varchar
,openp  numeric
,highp  numeric
,lowp   numeric
,closep numeric
,adjp   numeric
,volume numeric
)
;

COPY prices(
cdate   
,openp  
,highp  
,lowp   
,closep 
,adjp   
,volume 
) FROM '/tmp/ibm.csv' WITH csv header
;
EOF

exit

