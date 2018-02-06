#!/bin/bash

# ~/ml4/public/class10/curlGSPC.bash

# This script should curl GSPC prices.

set -x

curl 'https://tkrprice.herokuapp.com/static/CSV/history/^GSPC.csv'  > GSPC.csv

exit
