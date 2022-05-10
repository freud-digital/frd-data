import os
import requests


BASEROW_TOKEN = os.environ.get('BASEROW_TOKEN')
BASEROW_TABLE_MAPPING = {
    "keywords": "62157",
    "persons": "62168",
}
BASEROW_API = "https://api.baserow.io/api/database/rows/table/"

PERSON_GND_FILTER = {
    "filter__field_363950__contains": "d-nb"
}


def yield_rows(table_id, token, filters={}):
    url = f"{BASEROW_API}{table_id}/?user_field_names=true"
    if filters:
        for key, value in filters.items():
            url += f"&{key}={value}"
    next_page = True
    while next_page:
        print(url)
        response = None
        result = None
        x = None
        response = requests.get(
            url,
            headers={
                "Authorization": f"Token {token}"
            }
        )
        result = response.json()
        next_page = result['next']
        url = result['next']
        for x in result['results']:
            yield(x)