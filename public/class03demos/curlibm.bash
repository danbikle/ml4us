#!/bin/bash

# wgetibm.bash

# This script should download ibm.csv and then load it into a table called prices.

cd /tmp/
rm -f ibm.csv
/usr/bin/wget https://ml4.herokuapp.com/csv/ibm.csv

/usr/bin/psql -aP pager=no<<EOF
DROP TABLE IF EXISTS prices;
EOF

exit

