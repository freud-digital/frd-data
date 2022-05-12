import click
import freud_api_crawler.freud_api_crawler as frd
from config import (
    WERK_ID, FRD_USER, FRD_PW, MANIFEST_DEFAULT_FILTER
)


out_dir = "./werke"


auth_items = frd.get_auth_items(FRD_USER, FRD_PW)
werk_obj = frd.FrdWerk(
    auth_items=auth_items, werk_id=WERK_ID
)
rel_manifestations = werk_obj.get_manifestations(filters=MANIFEST_DEFAULT_FILTER)
print(
    f"found {len(rel_manifestations)} manifestion with settings {MANIFEST_DEFAULT_FILTER}"
)

for x in rel_manifestations:
    try:
        frd_man = frd.FrdManifestation(
            out_dir=out_dir,
            manifestation_id=x['man_id'],
            auth_items=auth_items
        )
        frd_man.make_xml(save=True, limit=False)
    except Exception as e:
        click.echo(
            click.style(
                f"processing Manifestation {x} did not not work due to Error {e}",
                fg='red'
            )
        )
click.echo(
    click.style(
        f"finished download\n{werk_obj.manifestations_count} Manifestations for {werk_obj.md__title}",
        fg='green'
    )
)
