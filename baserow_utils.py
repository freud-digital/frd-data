import os
import requests


BASEROW_TOKEN = os.environ.get('BASEROW_TOKEN')
BASEROW_TABLE_MAPPING = {
    "keywords": "1470",
    "persons": "1474",
    "places": "1468",
    "orgs": "1476",
}
BASEROW_API = "https://baserow.acdh-dev.oeaw.ac.at/api/database/rows/table/"

PERSON_IN_USE_FILTER = {
    "filter__field_374371__boolean": "true"
}
KEYWORD_IN_USE_FILTER = {
    "filter__field_12414__boolean": "true"
}
ORGS_IN_USE_FILTER = {
    "filter__field_392883__boolean": "true"
}
PLACES_IN_USE_FILTER = {
    "filter__field_12399__boolean": "true"
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
