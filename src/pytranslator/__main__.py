import translators as ts
from cache3 import DiskCache
import fileinput

cache = DiskCache()
if __name__ == '__main__':
    for line in fileinput.input():
        # line = "Còn đợi Merge với confirm nữa là xong"
        line=line.strip()
        print(line)
        if cache.has_key(line):
            print(cache.get(line))
        else:
            res = ts.translate_text(line, to_language='en')
            cache.set(line, res)
            print(res)