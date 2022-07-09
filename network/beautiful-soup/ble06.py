from bleach import Cleaner
from bleach.linkifier import LinkifyFilter
#使用bleach.linkifier.LinkifyFilter的默认配置
cleaner = Cleaner(tags=['pre'])
print(cleaner.clean('<pre>http://example.com</pre>'))

cleaner = Cleaner(tags=['pre'], filters=[LinkifyFilter])
print(cleaner.clean('<pre>http://example.com</pre>'))
#下面演示传参后对比
from functools import partial
from bleach.sanitizer import Cleaner
from bleach.linkifier import LinkifyFilter

cleaner = Cleaner(
    tags=['pre'],
    filters=[partial(LinkifyFilter, skip_tags=['pre'])]
)
print(cleaner.clean('<pre>http://example.com</pre>'))