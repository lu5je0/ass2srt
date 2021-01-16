#!/usr/bin/env python3

from zhconv import convert
import re
import sys
import os
import asstosrt
import chardet


def main(path):
    subs = []

    # 如果是目录
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for ass_file in files:
                if re.match("(?i).*(ass)$", ass_file):
                    subs.append(os.path.join(root, ass_file))
    # 如果是文件
    else:
        subs = {path}
        path = os.path.split(path)[0]

    for sub_file in subs:
        with open(sub_file, "rb") as ass_file:
            charset = chardet.detect(ass_file.read())["encoding"].lower()

        ass_file_name = '.'.join(sub_file.split('.')[:-1]) + '.srt'
        with open(sub_file, "r", encoding=charset) as ass_file:
            with open(ass_file_name, "wb") as srt_file:
                srt_file.write(convert(asstosrt.convert(ass_file), 'zh-cn').encode('utf8'))
                print(ass_file_name, "done")


if __name__ == '__main__':
    main(sys.argv[1])
