#!/bin/bash

# railss.bash

# This script should start rails server on all IPs so I can see the app from another host.

`dirname $0`/../bin/rails s -p 3540 -b 0.0.0.0

# 0.0.0.0 declares that I want rails listening on all IPs bound to this host.
exit
