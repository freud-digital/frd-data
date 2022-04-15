import glob
import os
import lxml.etree as ET
from acdh_collatex_utils.acdh_collatex_utils import CxCollate
from acdh_collatex_utils.post_process import (
    merge_tei_fragments,
    make_full_tei_doc
)

from config import WERK_PATH

input_glob = f"./werke/{WERK_PATH}/{WERK_PATH}__*.xml"
output_dir = f"./werke/{WERK_PATH}/collated"
result_file = f'{output_dir}/{WERK_PATH}.xml'

print("starting...")
out = CxCollate(
    glob_pattern=input_glob,
    glob_recursive=False,
    output_dir=output_dir,
    char_limit=False,
    chunk_size=5000,
).collate()

files = glob.glob(f"{output_dir}/*.tei")
print(len(files))
full_doc = merge_tei_fragments(files)
with open(result_file, 'w') as f:
    f.write(ET.tostring(full_doc, encoding='UTF-8').decode('utf-8'))
full_tei = make_full_tei_doc(result_file)
root = full_tei.tree
full_tei.tree_to_file(result_file)


for x in files:
    print(f"removing {x}")
    os.remove(x)
    print(f"removing {x.replace('.tei', '.html')}")
    os.remove(x.replace('.tei', '.html'))