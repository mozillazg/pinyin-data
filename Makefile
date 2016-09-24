.PHONY: help
help:
	@echo "merge_unihan          merge Unihan data"
	@echo "pua                   generate PUA"

.PHONY: merge_unihan
merge_unihan:
	python merge_unihan.py

.PHONY: pua
pua:
	python tools/gen_gb_pua.py > GBK_PUA.txt
