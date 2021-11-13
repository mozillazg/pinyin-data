# -*- coding: utf-8 -*-
from cc_cedict import phrases_dict


class Counter:
    def __init__(self):
        self._data = {}

    def add(self, item):
        if item not in self._data:
            self._data[item] = 0
        self._data[item] += 1

    def most_common(self):
        items = self._data.items()
        return sorted(items, key=lambda x: x[1], reverse=True)


def han_to_code(han):
    return 'U+' + hex(ord(han))[2:].upper()


def main():
    # { 'han': pinyin_counter }
    han_counter = {}
    for hans, pinyin_list in phrases_dict.items():
        if len(hans) != len(pinyin_list):
            continue
        for i, han in enumerate(hans):
            pinyins = pinyin_list[i]
            for pinyin in pinyins:
                if han not in han_counter:
                    han_counter[han] = Counter()
                counter = han_counter[han]
                counter.add(pinyin)

    for han, counter in sorted(han_counter.items(), key=lambda x: ord(x[0])):
        code = han_to_code(han)
        pinyin = ','.join([x[0] for x in counter.most_common()])
        if pinyin in ['xx']:
            continue
        print('{0}: {1}  # {2}'.format(code, pinyin, han))


if __name__ == '__main__':
    main()
