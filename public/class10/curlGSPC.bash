#!/bin/bash

# ~/ml4/public/class10/curlGSPC.bash

# This script should curl GSPC prices.

curl https://tkrprice.herokuapp.com/static/CSV/GSPC.csv  > GSPC.csv

exit
