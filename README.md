# pinyin-data [![Build Status](https://travis-ci.org/mozillazg/pinyin-data.svg?branch=master)](https://travis-ci.org/mozillazg/pinyin-data)

汉字拼音数据。


## 数据介绍

数据格式：`{code point}: {pinyins}  # {hanzi}` （示例：`U+4E2D: zhōng,zhòng  # 中`）

[Unihan Database][unihan] 数据版本：
> Date: 2016-06-01 07:01:48 GMT [JHJ]       
> Unicode version: 9.0.0

* `kHanyuPinyin.txt`: [Unihan Database][unihan] 中 [kHanyuPinyin](http://www.unicode.org/reports/tr38/#kHanyuPinyin) 部分的拼音数据（来源于《漢語大字典》的拼音数据）
* `kXHC1983.txt`: [Unihan Database][unihan] 中 [kXHC1983](http://www.unicode.org/reports/tr38/#kXHC1983) 部分的拼音数据（来源于《现代汉语词典》的拼音数据）
* `kHanyuPinlu.txt`: [Unihan Database][unihan] 中 [kHanyuPinlu](http://www.unicode.org/reports/tr38/#kHanyuPinlu) 部分的拼音数据（来源于《現代漢語頻率詞典》的拼音数据）
* `nonCJKUI.txt`: 不属于 [CJK Unified Ideograph](https://en.wikipedia.org/wiki/CJK_Unified_Ideographs) 但是却有拼音的字符
* `kMandarin.txt`: [Unihan Database][unihan] 中 [kMandarin](http://www.unicode.org/reports/tr38/#kMandarin) 部分的拼音数据（普通话中最常用的一个读音。zh-CN 为主，如果 zh-CN 中没有则使用 zh-TW 中的拼音）
* `overwrite.txt`: 手工纠正的拼音数据（**上面的拼音数据都是通过程序生成的，修改的话只修改这个就可以了**）
* `pinyin.txt`: 合并上述文件后的拼音数据
* `zdic.txt`: [汉典网](http://zdic.net) 的拼音数据


## 参考资料

* [Unihan Database Lookup](http://www.unicode.org/charts/unihan.html)
* [汉典 zdic.net](http://www.zdic.net/)

[unihan]: http://www.unicode.org/charts/unihan.html
