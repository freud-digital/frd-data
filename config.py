import os

FULL_MANIFEST = "228361d0-4cda-4805-a2f8-a05ee58119b6"
HISTORISCHE_AUSGABE = "5b8d9c77-99d0-4a80-92d8-4a9de06ac7ca"
FRD_USER = os.environ.get('FRD_USER')
FRD_PW = os.environ.get('FRD_PW')

WERK_ID = "e5a96721-6662-4884-96c5-0f29b6340e30"
WERK_PATH = "1920-004"
# READING_WIT = "sfe-1904-006__1904.xml"

MANIFEST_DEFAULT_FILTER = {
    "field_doc_component.id": FULL_MANIFEST,
    "field_manifestation_typ.id": HISTORISCHE_AUSGABE,
    "field_status_umschrift": 2
}
