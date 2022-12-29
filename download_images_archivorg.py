import json
import glob
import os
import requests

from zipfile import ZipFile


werke = glob.glob(
    os.path.join("werke", "*", "data", "*.json")
)
# werke = glob.glob("werke/1900-001/data/sfe-1900-001__1900.json")


def download_url(url, save_path, chunk_size):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


def export_zip(fn, save_path):
    with ZipFile(fn, "r") as zip:
        zip.printdir()
        print("extracting all files...")
        zip.extractall(save_path)
        print("done!")


endpoint = "https://archive.org/download"
url_ext = "_jp2.zip"
for x in werke:
    with open(x, "r") as f:
        data = json.load(f)
    repo = data["repository"]
    path = x.split("/")
    save_path = os.path.join(path[0], path[1], "facs")
    os.makedirs(save_path, exist_ok=True)
    main_log = os.path.join(save_path, "log.txt")
    try:
        repo_name = repo["name"]
    except KeyError as err:
        repo_name = None
        print("name not found")
        with open(main_log, "a") as f:
            f.write(f"Key: {err} in file: {x} not found\n")
    if repo_name == "IPU":
        try:
            url_id = repo["orig_archiv_id"]
        except KeyError as err:
            url_id = None
            print("orig_archiv_id not found")
            with open(main_log, "a") as f:
                f.write(f"Key: {err} in file: {x} not found\n")
        if url_id is not None:
            url = f"{endpoint}/{url_id}/{url_id}{url_ext}"
            fn = path[3].replace('.json', '')
            save_dir = os.path.join(save_path, fn)
            os.makedirs(save_dir, exist_ok=True)
            archive = os.path.join(save_dir, f"{fn}.zip")
            log = os.path.join(save_dir, f"{fn}.txt")
            try:
                print(url)
                download_url(
                    url=url,
                    save_path=archive,
                    chunk_size=128
                )
                print(f"download of {archive} complete")
                try:
                    export_zip(fn=archive, save_path=save_dir)
                except Exception as err:
                    with open(log, "a") as f:
                        f.write(f"error: {err} in archive extraction of {archive}\n")
                    print(f"archive extraction of {archive} \
                        failed. Open log {log} to read more.")
                try:
                    print(f"removing {archive} ...")
                    os.remove(archive)
                except Exception as err:
                    print(f"error: {err} in file. {archive} could not be removed.")
            except Exception as err:
                with open(log, "a") as f:
                    f.write(f"error: {err} in {x} for orig_archive_id: {url_id}. \
                        accessed url: {url}.\n")
                print(f"download of {archive} \
                    failed. Open log {log} to read more.")
    else:
        print(f"repository name is not IPU but {repo_name}")
        with open(main_log, "a") as f:
            f.write(f"repository name is not IPU but {repo_name}\n")
