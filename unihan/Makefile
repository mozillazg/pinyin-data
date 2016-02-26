.PHONY: help
help:
	@echo "update		update Unihan database"
	@echo "diff		diff between Unihan data and parsed data"

.PHONY:update
update:
	rm Unihan*
	wget ftp://ftp.unicode.org/Public/UNIDATA/Unihan.zip -O Unihan.zip
	unzip Unihan.zip
	python parse_pinyin.py

.PHONY:diff
diff:
	@bash diff.sh
