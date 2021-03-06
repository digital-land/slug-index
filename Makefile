include makerules/makerules.mk
# include makerules/render.mk

# DATASET_PATH := data/dataset.csv
# DATASET := brownfield-land
#
.PHONY: index collect

collect:
	mkdir -p data
	wget -O data/brownfield-land.csv https://raw.githubusercontent.com/digital-land/brownfield-land-collection/main/dataset/brownfield-land.csv
	wget -O data/conservation-area.csv https://raw.githubusercontent.com/digital-land/conservation-area-collection/main/dataset/conservation-area.csv
	wget -O data/local-plan.csv https://github.com/digital-land/alpha-data/raw/master/local-plans/development-plan-slug.csv
	wget -O data/organisation.csv https://github.com/digital-land/organisation-dataset/raw/main/collection/organisation.csv
	curl -qsL https://raw.githubusercontent.com/digital-land/development-policy/main/dataset/development-policy.csv > data/development-policy.csv
	curl -qsL https://raw.githubusercontent.com/digital-land/development-plan-document-collection/main/dataset/development-plan-document.csv > data/development-plan-document.csv 
	curl -qsL https://raw.githubusercontent.com/digital-land/development-plan-type/main/dataset/development-plan-type.csv > data/development-plan-type.csv 

index:
	python slug-indexer/index.py
	python slug-indexer/policy-to-doc.py

# local: clean
# 	digital-land --pipeline-name $(DATASET) render --dataset-path $(DATASET_PATH) --local

# build: clean collect render

# clean::
# 	rm -r ./docs/
# 	mkdir docs
