"""
rpt09.py

This script should report on data in this download:

http://ml4.us/class09predictions.tar.bz2

Demo:
~/anaconda3/bin/python rpt09.py
"""

import glob
import os
import pandas as pd
import pdb
import re

# I should get the download:
shellcmd_s = '/usr/bin/curl -L ml4.us/class09predictions.tar.bz2 > /tmp/class09predictions.tar.bz2'
print('Busy with this:')
print(shellcmd_s)
os.system(shellcmd_s)

# I should untar it:
shellcmd_s = 'cd /tmp/; tar jxf class09predictions.tar.bz2'
print('Busy with this:')
print(shellcmd_s)
os.system(shellcmd_s)


# I should use glob.glob to create a list of file-names.
fn_l = glob.glob('/tmp/csv/predictions*USD*.csv')
# I should use that list to drive a loop:
for fn_s in sorted(fn_l):
    # I should use a RegExp to extract the integer and pair-name from fn_s
    pattern_re     = r'(predictions)(\d+)(.+)(.csv)'
    pattern_ma     = re.search(pattern_re, fn_s)
    train_i_s      = pattern_ma[2]
    pair_s         = pattern_ma[3]
    predictions_df = pd.read_csv(fn_s,names=['ts','cp','piplead','prediction','eff','acc'])
    effsum_f       = predictions_df.eff.sum()
    print('For this pair: ', pair_s, ' and this training count: ', train_i_s)
    print('Effectiveness sum is: ',effsum_f)
'bye'
