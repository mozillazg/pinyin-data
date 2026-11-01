PYTHON ?= python3

.PHONY: help
help:
	@echo "merge_unihan          merge Unihan data"
	@echo "pua                   generate PUA"
	@echo "check                 check unexpected char"
	@echo "cc_cedict             generate cc_cedict.txt"

.PHONY: merge_unihan
merge_unihan: check
	$(PYTHON) merge_unihan.py

.PHONY: pua
pua:
	PYTHONPATH=. $(PYTHON) tools/gen_gb_pua.py > GBK_PUA.txt

.PHONY: check
check:
	-rg 'ɡ|ɑ|í|è'

# 注：phrase-pinyin-data v0.20.0 的 cc_cedict.txt 有一处损坏数据，
# "闺女: guī nu:"（应为 "guī nǚ"）会导致 gen_phrases_dict.py 解析失败，
# 这里先修正再生成。上游修复后此 sed 自动变为空操作。
.PHONY: cc_cedict
cc_cedict:
	cd tools && \
		sed 's/^闺女: guī nu:$$/闺女: guī nǚ/' phrase-pinyin-data/cc_cedict.txt > cc_cedict.fixed.txt && \
		$(PYTHON) python-pinyin/gen_phrases_dict.py cc_cedict.fixed.txt cc_cedict.py && \
		$(PYTHON) gen_cc_cedict.py > ../cc_cedict.txt; \
		rm -f cc_cedict.fixed.txt
