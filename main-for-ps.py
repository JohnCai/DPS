import pandas as pd
from time import time
from datetime import date
from datetime import datetime
from datetime import timedelta
from csv2xml import *
import os

currentDate = date.today() + timedelta(days=-1)
batchStr = str(currentDate.strftime("%Y%m%d"))
source_dir = batchStr
target_dir = batchStr
if os.path.exists(target_dir) == False:
    os.makedirs(target_dir)

for filename in os.listdir(source_dir):
    if (filename.find('.csv', len(filename)-5, len(filename)) != -1) == True:
        f = os.path.join(source_dir, filename)

        pdObj = pd.read_csv(f)

        sequenceId = int(time() * 1000)
        target_f = os.path.join(target_dir, "from_" + filename + "_PhoenixAsia_SHA_" + str(sequenceId) + "_RUN.xml")
        csv2xml(pdObj, sequenceId).write(target_f, encoding= 'utf-8' ,xml_declaration= True)