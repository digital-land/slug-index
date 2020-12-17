import logging
import csv

org_dataset = "data/organisation.csv"
bfl_dataset = "data/brownfield-land.csv"
ca_dataset = "data/conservation-area.csv"
lp_dataset = "data/local-plan.csv"

datasets = [
    (ca_dataset, "conservation-area", "name"),
    (bfl_dataset, "brownfield-land", "site"),
    (lp_dataset, "local-plan", "name"),
]

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
organisation = {}
reader = csv.DictReader(open(org_dataset))
for row in reader:
    organisation[row["organisation"]] = row

writer = csv.DictWriter(open(output_file, "w"), fieldnames=output_fields)
writer.writeheader()

try:
    for dataset_csv, dataset, name_field in datasets:
        for row in csv.DictReader(open(dataset_csv)):
            if "organisations" in row:
                orgs = row["organisations"].split(";")
            elif "organisation" in row and row["organisation"]:
                orgs = [row["organisation"]]
            else:
                continue

            for org in orgs:
                out_row = {
                    "organisation": org,
                    "organisation-name": organisation[org]["name"],
                    "organisaton-slug": f"organisation/{org.replace(':', '/')}",
                    "dataset": dataset,
                    "dataset-name": row[name_field],
                    "dataset-slug": row["slug"],
                }
                if not out_row["dataset-slug"]:
                    continue
                writer.writerow(out_row)
except Exception as e:
    logging.exception("Oh no")
    __import__("pdb").post_mortem()
