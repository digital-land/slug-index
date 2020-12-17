include makerules/makerules.mk
# include makerules/render.mk

# DATASET_PATH := data/dataset.csv
# DATASET := brownfield-land

collect:
	mkdir -p data
	wget -O data/brownfield-land.csv https://raw.githubusercontent.com/digital-land/brownfield-land-collection/main/dataset/brownfield-land.csv
	wget -O data/conservation-area.csv https://raw.githubusercontent.com/digital-land/conservation-area-collection/main/dataset/conservation-area.csv
	wget -O data/organisation.csv https://github.com/digital-land/organisation-dataset/blob/main/collection/organisation.csv

# local: clean
# 	digital-land --pipeline-name $(DATASET) render --dataset-path $(DATASET_PATH) --local

# build: clean collect render

# clean::
# 	rm -r ./docs/
# 	mkdir docs
