import os

FRD_USER = os.environ.get('FRD_USER')
FRD_PW = os.environ.get('FRD_PW')
WERK_ID = "9d035a03-28d7-4013-adaf-63337d78ece4"
WERK_PATH = "drei-abhandlungen-zur-sexualtheorie"
FULL_MANIFEST = "228361d0-4cda-4805-a2f8-a05ee58119b6"

MANIFEST_DEFAULT_FILTER = {
    "field_doc_component.id": FULL_MANIFEST,
    "field_status_umschrift": 2
}