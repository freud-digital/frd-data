import click
import pandas as pd
import glob
import os
import datetime
import freud_api_crawler.freud_api_crawler as frd
from config import (
    FRD_USER, FRD_PW, MANIFEST_DEFAULT_FILTER, FWF_MANIFESTATIONS
)  

works_fwf = pd.read_csv(FWF_MANIFESTATIONS)
out_dir = "./werke"
auth_items = frd.get_auth_items(FRD_USER, FRD_PW)

exists = glob.glob(f"{out_dir}/*")
werk_path_loaded = []
for x in exists:
    werk_path_loaded.append(x.split("/")[-1])

werk_ids = {}

for index, row in works_fwf.iterrows():
    w_id = row['work_id']
    w_path = row['werk_signatur']
    werk_ids[w_path] = w_id
    
for x in werk_ids:
    if x not in werk_path_loaded:
        print(f"starting to download work: {x}")
        WERK_ID = werk_ids[x]
        WERK_PATH = x
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
                frd_man.get_man_json_dump(lmt=False)
            except Exception as e:
                os.makedirs("logs", exist_ok=True)
                with open(f"logs/json_dump_error.txt", "a") as f:
                    f.write(f"processing Manifestation {x} of work {WERK_PATH} did not work due to Error {e}. {datetime.datetime}\n")
                click.echo(
                    click.style(
                        f"processing Manifestation {x} did not not work due to Error {e}",
                        fg='red'
                    )
                )
        try:
            frd.make_xml(save=True, out_dir=out_dir, workpath=WERK_PATH, test=False, dump={})
        except Exception as e:
            os.makedirs("logs", exist_ok=True)
            with open(f"logs/make_xml_error.txt", "a") as f:
                f.write(f"processing TEI/XML of work {WERK_PATH} did not work due to Error {e}. Run get_jsom_dump first {datetime.datetime}\n")
            click.echo(
                click.style(
                    f"processing TEI/XML of work {WERK_PATH} did not work due to Error {e}. Run get_jsom_dump first",
                    fg='red'
                )
            )

        click.echo(
            click.style(
                f"finished download\n{werk_obj.manifestations_count} Manifestations for {werk_obj.md__title}",
                fg='green'
            )
        )
