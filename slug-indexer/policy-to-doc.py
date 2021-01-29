import csv

doc_dataset = "data/development-plan-document.csv"
dp_dataset = "data/development-policy.csv"


# set up output
output_file = "index/policy-to-doc-index.csv"
output_fields = [
    "development-policy",
    "development-policy-slug",
    "development-plan-document",
]

writer = csv.DictWriter(open(output_file, "w"), fieldnames=output_fields)
writer.writeheader()

# create a dict of policies (ids and slugs)
reader = csv.DictReader(open(dp_dataset))
policies = {row['development-policy']:row for row in reader}

def output_row(dp, slug, doc):
    return {
        "development-policy": dp,
        "development-policy-slug": slug,
        "development-plan-document": doc,
    }

doc_reader = csv.DictReader(open(doc_dataset))
# loop over docs
for d in doc_reader:
    if not d.get('development-policies') == "":
        # convert policies string into list of ids
        pl = d.get('development-policies').split(";")
        # loop over ids in list and add doc id to policy dict
        for p in pl:
            if p in policies.keys():
                out_row = output_row(p, policies[p]['slug'], d['development-plan-document'])
                writer.writerow(out_row)
    else:
        print(d['development-plan-document'], "has no policies")
