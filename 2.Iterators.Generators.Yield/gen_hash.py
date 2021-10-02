import hashlib
from hashlib import md5

def gen_hash(path):
    with open(path, 'rb') as f:
        for item in f:
            yield hashlib.md5(item).hexdigest()

for item in gen_hash('D:\\Projects\homeworks-advanced\\2.Iterators.Generators.Yield\\country_wikilink.txt'):
    print(item)
