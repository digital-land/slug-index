import csv
from digital_land.slug import Slugger

org_dataset = "data/organisation.csv"
bfl_dataset = "data/brownfield-land.csv"
ca_dataset = "data/conservation-area.csv"

output_file = "index/slug-index.csv"
output_fields = [
    "organisation",
    "organisation-name",
    "organisaton-slug",
    "dataset",
    "dataset-name",
    "dataset-slug",
]

# create organisation lookup
org = {}
reader = csv.DictReader(open(org_dataset))
for row in reader:
    org[row["organisation"]] = row

writer = csv.DictWriter(open(output_file, "w"), fieldnames=output_fields)
writer.writeheader()

datasets = [
    (ca_dataset, "conservation-area", "Conservation Area"),
    (bfl_dataset, "brownfield-land", "Brownfield Land"),
]

try:
    for dataset_csv, dataset, dataset_name in datasets:
        for row in csv.DictReader(open(dataset_csv)):
            if not row["organisation"]:
                continue

            out_row = {
                "organisation": row["organisation"],
                "organisation-name": org[row["organisation"]]["name"],
                "organisaton-slug": f"organisation/{row['organisation'].replace(':', '/')}",
                "dataset": dataset,
                "dataset-name": dataset_name,
                "dataset-slug": row["slug"],
            }
            if not out_row["dataset-slug"]:
                continue
            writer.writerow(out_row)
except Exception as e:
    __import__('pdb').post_mortem()
