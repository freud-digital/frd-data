import os

FULL_MANIFEST = "228361d0-4cda-4805-a2f8-a05ee58119b6"
HISTORISCHE_AUSGABE = "5b8d9c77-99d0-4a80-92d8-4a9de06ac7ca"
FRD_USER = os.environ.get('FRD_USER')
FRD_PW = os.environ.get('FRD_PW')

WERK_ID = "240e92d7-cdf2-4502-b6ff-7a1cbdbdfcba"
WERK_PATH = "1905-001"
READING_WIT = "sfe-1905-001__1925.xml"

MANIFEST_DEFAULT_FILTER = {
    "field_doc_component.id": FULL_MANIFEST,
    "field_manifestation_typ.id": HISTORISCHE_AUSGABE,
    "field_status_umschrift": 2
}
