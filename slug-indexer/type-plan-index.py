import csv

doc_dataset = "data/development-plan-document.csv"
dpt_dataset = "data/development-plan-type.csv"


# set up output
output_file = "index/type-to-plan-index.csv"
output_fields = [
    "development-plan-type",
    "development-plan-type-slug",
    "development-plan-document",
    "development-plan-document-slug",
]

writer = csv.DictWriter(open(output_file, "w"), fieldnames=output_fields)
writer.writeheader()

# create a dict of types (ids and slugs)
reader = csv.DictReader(open(dpt_dataset))
types = {row['development-plan-type']:row for row in reader}

def output_row(dpt, slug, doc, doc_slug):
    return {
        "development-plan-type": dpt,
        "development-plan-type-slug": slug,
        "development-plan-document": doc,
        "development-plan-document-slug": doc_slug,
    }

doc_reader = csv.DictReader(open(doc_dataset))
# loop over docs
idx_field = 'development-plan-types'
for d in doc_reader:
    if not d.get(idx_field) == "":
        # convert types string into list of types
        ts = d.get(idx_field).split(";")
        # loop over types in list and add doc id to types dict
        for t in ts:
            if t in types.keys():
                out_row = output_row(t, types[t]['slug'], d["development-plan-document"], d['slug'])
                writer.writerow(out_row)
    else:
        print(d['development-plan-document'], "has no associated type")
