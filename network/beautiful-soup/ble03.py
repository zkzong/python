from bleach.linkifier import Linker

def set_title(attrs, new=False):
     attrs[(None, u'title')] = u'link in user text'
     return attrs

linker = Linker(callbacks=[set_title])
print(linker.linkify('abc http://example.com def'))

#下面的代码将生成的链接设置为内部链接在当前页打开、外部链接在新建页打开
import urllib
from bleach.linkifier import Linker

def set_target(attrs, new=False):
    p = urllib.parse.urlparse(attrs[(None, u'href')])
    if p.netloc not in ['my-domain.com', 'other-domain.com']:
        attrs[(None, u'target')] = u'_blank'
        attrs[(None, u'class')] = u'external'
    else:
        attrs.pop((None, u'target'), None)
    return attrs

linker = Linker(callbacks=[set_target])
print(linker.linkify('abc http://example.com def'))