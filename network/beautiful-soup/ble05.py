from bleach.linkifier import Linker
linker = Linker(skip_tags=['pre'])
print(linker.linkify('a b c http://example.com d e f'))