import glob
import lxml.etree as ET
from acdh_collatex_utils.acdh_collatex_utils import CxCollate
from acdh_collatex_utils.post_process import merge_tei_fragments

from config import WERK_PATH

input_glob = f"./werke/{WERK_PATH}/{WERK_PATH}*.xml"
output_dir = f"./werke/{WERK_PATH}/collated"
werk_path = "{WERK_PATH}"

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

with open(f'{WERK_PATH}.xml', 'w') as f:
    f.write(ET.tostring(full_doc, encoding='UTF-8').decode('utf-8'))