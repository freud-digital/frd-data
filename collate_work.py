import glob
import os
import lxml.etree as ET
from acdh_collatex_utils.acdh_collatex_utils import CxCollate
from acdh_collatex_utils.post_process import (
    merge_tei_fragments,
    make_full_tei_doc,
    merge_html_fragments
)

from config import WERK_PATH

input_glob = f"./werke/{WERK_PATH}/{WERK_PATH}__*.xml"
output_dir = f"./werke/{WERK_PATH}/collated"
result_file = f'{output_dir}/{WERK_PATH}.xml'
result_html = f'{output_dir}/{WERK_PATH}.html'

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


files = glob.glob(f"{output_dir}/*.html")
full_doc = merge_html_fragments(files)
with open(result_html, 'w') as f:
    f.write(full_doc.prettify("utf-8").decode('utf-8'))


for x in glob.glob(f"{output_dir}/out__*"):
    print(f"removing {x}")
    os.remove(x)