import pandas as pd
from time import time
from csv2xml import *
import os
import shutil

source_dir = 'source'
source_archive_dir = 'source_archive'
target_dir = 'target'
if os.path.exists(source_archive_dir) == False:
    os.mkdir(source_archive_dir)
if os.path.exists(target_dir) == False:
    os.mkdir(target_dir)

for filename in os.listdir(source_dir):
    f = os.path.join(source_dir, filename)

    pdObj = pd.read_csv(f)

    batchId = int(time() * 1000)

    target_f = os.path.join(target_dir, "from_" + filename + "_PhoenixAsia_SHA_" + str(batchId) + "_RUN.xml")
    csv2xml(pdObj, batchId).write(target_f, encoding= 'utf-8' ,xml_declaration= True)

    # shutil.move(f, source_archive_dir)