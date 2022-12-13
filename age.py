import os
import glob
import lxml.etree as ET
import json

from datetime import datetime, timezone
from acdh_tei_pyutils.tei import TeiReader

werke = glob.glob("./werke/*")

complete = ["1901-001", "1901-003", "1903-001", "1904-002", "1904-003", "1904-004", "1904-005", "1904-006", "1905-001", "1905-002", "1905-004", "1905-006", "1905-007", "1905-008", "1905-009", "1920-002", "1920-003", "1920-004", "1920-005", "1923-001", "1923-007", "1923-008", "1923-009", "1924-005"]
partially = ["1900-001", "1901-122", "1920-001", "1920-006", "1920-132", "1921-001", "1921-002", "1921-003", "1921-004", "1922-001", "1922-002", "1922-006", "1922-008", "1923-002", "1923-003", "1923-004", "1923-005"]
proposed = ["1900-002", "1901-002", "1901-121", "1902-121", "1903-301", "1905-003", "1905-005", "1922-007", "1922-009", "1900-241", "1900-242", "1902-122", "1902-123", "1904-121", "1904-122", "1904-131", "1904-211", "1905-131", "1921-301", "1922-004", "1922-005", "1922-211", "1923-006", "1923-101", "1923-211", ""]

# for x in werke:
#     d = datetime.fromtimestamp(os.path.getctime(x), tz=timezone.utc)
#     d = datetime.date(d)
#     if f"{d}" == "2022-12-07":
#         w = {
#             "age": f"{d}",
#             "sig": x
#         }
#         partially.append(w)
#     elif f"{d}" == "2022-12-09":
#         w = {
#             "age": f"{d}",
#             "sig": x
#         }
#         proposed.append(w)
#     else:
#         w = {
#             "age": f"{d}",
#             "sig": x
#         }
#         complete.append(w)
        
print(len(complete))
print(len(partially))
print(len(proposed))
    
for x in complete:
    sig = x
    sig = glob.glob(f"./werke/{sig}/*.xml")
    for s in sig:
        print(s)
        try:
            doc = TeiReader(s)
        except Exception as e:
            print(e)
        teiheader = doc.any_xpath(f".//tei:teiHeader")[0]
        revDesc = ET.Element("{http://www.tei-c.org/ns/1.0}revisionDesc")
        revDesc.attrib["status"] = "complete"
        chg = ET.Element("{http://www.tei-c.org/ns/1.0}change")
        chg.attrib["who"] = "#dstoxreiter"
        chg.attrib["when"] = "2022-12-13"
        chg.text = "Der Status 'complete' entspricht einer abgeschlossenen Korrektur der diplomatischen Umschrift."
        revDesc.append(chg)
        teiheader.append(revDesc)
        ET.indent(doc.tree)
        doc.tree_to_file(s)

for x in partially:
    sig = x
    sig = glob.glob(f"./werke/{sig}/*.xml")
    for s in sig:
        print(s)
        try:
            doc = TeiReader(s)
        except Exception as e:
            print(e)
        teiheader = doc.any_xpath(f".//tei:teiHeader")[0]
        revDesc = ET.Element("{http://www.tei-c.org/ns/1.0}revisionDesc")
        revDesc.attrib["status"] = "progress"
        chg = ET.Element("{http://www.tei-c.org/ns/1.0}change")
        chg.attrib["who"] = "#dstoxreiter"
        chg.attrib["when"] = "2022-12-13"
        chg.text = "Der Status 'progress' entspricht einer noch nicht abgeschlossenen Korrektur der diplomatischen Umschrift."
        revDesc.append(chg)
        teiheader.append(revDesc)
        ET.indent(doc.tree)
        doc.tree_to_file(s)

for x in proposed:
    sig = x
    sig = glob.glob(f"./werke/{sig}/*.xml")
    for s in sig:
        print(s)
        try:
            doc = TeiReader(s)
        except Exception as e:
            print(e)
        teiheader = doc.any_xpath(f".//tei:teiHeader")[0]
        revDesc = ET.Element("{http://www.tei-c.org/ns/1.0}revisionDesc")
        revDesc.attrib["status"] = "proposed"
        chg = ET.Element("{http://www.tei-c.org/ns/1.0}change")
        chg.attrib["who"] = "#dstoxreiter"
        chg.attrib["when"] = "2022-12-13"
        chg.text = "Der Status 'proposed' entspricht einer offenen Korrektur der diplomatischen Umschrift."
        revDesc.append(chg)
        teiheader.append(revDesc)
        ET.indent(doc.tree)
        doc.tree_to_file(s)
        
for x in complete:
    sig = x
    sig = glob.glob(f"./werke/{sig}/data/*.json")
    for s in sig:
        print(s)
        with open(s, "r") as f:
            data = json.load(f)
        data["status"] = {"id": "2", "name": "complete"}
        with open(s, "w") as f:
            json.dump(data, f)

for x in partially:
    sig = x
    sig = glob.glob(f"./werke/{sig}/data/*.json")
    for s in sig:
        print(s)
        with open(s, "r") as f:
            data = json.load(f)
        data["status"] = {"id": "1", "name": "progress"}
        with open(s, "w") as f:
            json.dump(data, f)

for x in proposed:
    sig = x
    sig = glob.glob(f"./werke/{sig}/data/*.json")
    for s in sig:
        print(s)
        with open(s, "r") as f:
            data = json.load(f)
        data["status"] = {"id": "0", "name": "proposed"}
        with open(s, "w") as f:
            json.dump(data, f)
            