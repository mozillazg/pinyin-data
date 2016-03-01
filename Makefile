.PHONY: help
help:
	@echo "merge_unihan		merge Unihan data"

.PHONY: merge_unihan
merge_unihan:
	python merge_unihan.py
