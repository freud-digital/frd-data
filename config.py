import os

FULL_MANIFEST = "228361d0-4cda-4805-a2f8-a05ee58119b6"
FRD_USER = os.environ.get('FRD_USER')
FRD_PW = os.environ.get('FRD_PW')

WERK_ID = "7f1ce2ef-dc26-45e2-b90a-85d866403b1c"
WERK_PATH = "josef-popper-lynkeus-und-die-theorie-des-traumes"

MANIFEST_DEFAULT_FILTER = {
    "field_doc_component.id": FULL_MANIFEST,
    "field_status_umschrift": 1
}