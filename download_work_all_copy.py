import pandas as pd
import glob
from config import (
    FWF_MANIFESTATIONS
)  

works_fwf = pd.read_csv(FWF_MANIFESTATIONS)
out_dir = "./werke"

exists = glob.glob(f"{out_dir}/*")
werk_path_loaded = []
for x in exists:
    werk_path_loaded.append(x.split("/")[-1])

print(len(werk_path_loaded))

werk_ids = {}

for index, row in works_fwf.iterrows():
    w_id = row['work_id']
    w_path = row['werk_signatur']
    werk_ids[w_path] = w_id

print(len(werk_ids))

for x in werk_path_loaded:
    if x not in werk_ids:
        print(f"starting to download work: {x}")
        