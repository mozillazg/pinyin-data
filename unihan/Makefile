PYTHON ?= python3

.PHONY: help
help:
	@echo "parse		parse Unihan database "
	@echo "update		update Unihan database"
	@echo "diff		diff between Unihan data and parsed data"

.PHONY: parse
parse:
	@$(PYTHON) parse_pinyin.py

.PHONY: update
update:
	-rm Unihan*
	wget https://www.unicode.org/Public/UNIDATA/Unihan.zip -O Unihan.zip
	unzip Unihan.zip
	$(PYTHON) parse_pinyin.py

.PHONY: diff
diff:
	@bash diff.sh
