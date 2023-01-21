import pandas as pd
from time import time
from datetime import date
from csv2xml import *
import os
import shutil

source_dir = 'source'
batchStr = str(date.today())
source_archive_dir = os.path.join('source_archive', batchStr)
target_dir = os.path.join('target', batchStr)
if os.path.exists(source_archive_dir) == False:
    os.makedirs(source_archive_dir)
if os.path.exists(target_dir) == False:
    os.makedirs(target_dir)



for filename in os.listdir(source_dir):
    f = os.path.join(source_dir, filename)

    pdObj = pd.read_csv(f)

    sequenceId = int(time() * 1000)
    target_f = os.path.join(target_dir, "from_" + filename + "_PhoenixAsia_SHA_" + str(sequenceId) + "_RUN.xml")
    csv2xml(pdObj, sequenceId).write(target_f, encoding= 'utf-8' ,xml_declaration= True)

    # shutil.move(f, source_archive_dir)