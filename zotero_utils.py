from urllib.parse import urlencode
from acdh_tei_pyutils.tei import TeiReader
import lxml.etree as ET


def get_listbibl(group_id="4690432", limit="50"):
    base_url = f"https://api.zotero.org/groups/{group_id}/items"
    params = [
        ("format", "tei"),
        ("limit", f"{limit}"),
        ("sort", "dateModified"),
        ("direction", "desc")
    ]
    url = f"{base_url}?{urlencode(params)}"
    return url


def update_listbibl(url, orig_file='./indices/listbibl.xml'):
    doc = TeiReader(url)
    try:
        orig_doc = TeiReader(orig_file)
    except Exception as e:
        print(e)
        return doc
    list_bibl = orig_doc.any_xpath('.//tei:listBibl')[0]
    for x in doc.any_xpath('.//tei:biblStruct'):
        zot_id = x.attrib['corresp']
        orig_nodes = orig_doc.any_xpath(f".//tei:biblStruct[@corresp='{zot_id}']")
        for bad in orig_nodes:
            bad.getparent().remove(bad)
        list_bibl.append(x)
    ET.indent(orig_doc.tree)
    return orig_doc