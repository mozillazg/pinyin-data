# -*- coding: utf-8 -*-
import collections


def remove_dup_items(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst


def parse_pinyins(lines):
    pinyin_map = {}
    for line in lines:
        if line.startswith('#'):
            continue
        code, pinyin = line.split('#')[0].split(':')
        pinyin_map[code.strip()] = pinyin.strip().split(',')
    return pinyin_map


def merge(raw_pinyin_map, adjust_pinyin_map, overwrite_pinyin_map):
    new_pinyin_map = {}
    for code, pinyins in raw_pinyin_map.items():
        if code in overwrite_pinyin_map:
            pinyins = overwrite_pinyin_map[code]
        elif code in adjust_pinyin_map:
            pinyins = adjust_pinyin_map[code] + pinyins
        new_pinyin_map[code] = remove_dup_items(pinyins)

    return new_pinyin_map


def save_data(pinyin_map, writer):
    for code, pinyins in pinyin_map.items():
        hanzi = chr(int(code.replace('U+', '0x'), 16))
        line = '{code}: {pinyin}  # {hanzi}\n'.format(
            code=code, pinyin=','.join(pinyins), hanzi=hanzi
        )
        writer.write(line)


def extend_pinyins(old_map, new_map):
    for code, pinyins in new_map.items():
        old_map.setdefault(code, []).extend(pinyins)

if __name__ == '__main__':
    raw_pinyin_map = {}
    with open('kHanyuPinyin.txt') as fp:
        khanyupinyin = parse_pinyins(fp.readlines())
        raw_pinyin_map.update(khanyupinyin)
    with open('kHanyuPinlu.txt') as fp:
        khanyupinyinlu = parse_pinyins(fp.readlines())
        extend_pinyins(raw_pinyin_map, khanyupinyinlu)
    with open('kXHC1983.txt') as fp:
        kxhc1983 = parse_pinyins(fp.readlines())
        extend_pinyins(raw_pinyin_map, kxhc1983)
    with open('nonCJKUI.txt') as fp:
        noncjkui = parse_pinyins(fp.readlines())
        extend_pinyins(raw_pinyin_map, noncjkui)
    with open('kMandarin.txt') as fp:
        adjust_pinyin_map = parse_pinyins(fp.readlines())
        extend_pinyins(raw_pinyin_map, adjust_pinyin_map)

    with open('overwrite.txt') as fp:
        overwrite_pinyin_map = parse_pinyins(fp.readlines())

    new_pinyin_map = merge(raw_pinyin_map, adjust_pinyin_map,
                           overwrite_pinyin_map)
    new_pinyin_map = collections.OrderedDict(
        sorted(new_pinyin_map.items(),
               key=lambda item: int(item[0].replace('U+', '0x'), 16))
    )
    assert len(new_pinyin_map) == len(raw_pinyin_map)
    code_set = set(new_pinyin_map.keys())
    assert set(khanyupinyin.keys()) - code_set == set()
    assert set(khanyupinyinlu.keys()) - code_set == set()
    assert set(kxhc1983.keys()) - code_set == set()
    assert set(adjust_pinyin_map.keys()) - code_set == set()
    assert set(overwrite_pinyin_map.keys()) - code_set == set()
    with open('pinyin.txt', 'w') as fp:
        save_data(new_pinyin_map, fp)
