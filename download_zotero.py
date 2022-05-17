from zotero_utils import get_listbibl, update_listbibl

list_bibl = "./indices/listbibl.xml"

new_doc = update_listbibl(get_listbibl(limit="50"), orig_file=list_bibl)
new_doc.tree_to_file(list_bibl)
