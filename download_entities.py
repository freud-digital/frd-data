import os
import jinja2

from baserow_utils import (
    yield_rows,
    BASEROW_TOKEN,
    BASEROW_TABLE_MAPPING,
    PERSON_IN_USE_FILTER,
    KEYWORD_IN_USE_FILTER
)
BASE_URI = "https://vocabs.acdh.oeaw.ac.at/freud-hka"
templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
templateEnv = jinja2.Environment(loader=templateLoader)

template = templateEnv.get_template('template_person.xml')
table_id = BASEROW_TABLE_MAPPING['persons']
items = [x for x in yield_rows(table_id, BASEROW_TOKEN, filters=PERSON_IN_USE_FILTER)]
with open('./indices/listperson.xml', 'w') as f:
        f.write(template.render({"items": items}))


template = templateEnv.get_template('template_place.xml')
table_id = BASEROW_TABLE_MAPPING['places']
items = [x for x in yield_rows(table_id, BASEROW_TOKEN)]
with open('./indices/listplace.xml', 'w') as f:
        f.write(template.render({"items": items}))

template = templateEnv.get_template('template_skos.xml')
table_id = BASEROW_TABLE_MAPPING['keywords']
items = [x for x in yield_rows(table_id, BASEROW_TOKEN, filters=KEYWORD_IN_USE_FILTER)]
with open('./indices/keywords.rdf', 'w') as f:
        f.write(template.render(
            {
                "items": items,
                "base_uri": BASE_URI
            }
        )
    )