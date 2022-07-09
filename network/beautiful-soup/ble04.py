from bleach.linkifier import Linker

def allowed_attrs(attrs, new=False):
    """Only allow href, target, rel and title."""
    allowed = [
        (None, u'href'),
         (None, u'target'),
         (None, u'rel'),
         (None, u'title'),
        u'_text',
     ]
    return dict((k, v) for k, v in attrs.items() if k in allowed)

linker = Linker(callbacks=[allowed_attrs])
print(linker.linkify('<a style="font-weight: super bold;" href="http://example.com">link</a>'))

#除了删除白名单之外的属性，还可以删除指定属性
def remove_title(attrs, new=False):
    attrs.pop((None, u'title'), None)
    return attrs
linker = Linker(callbacks=[remove_title])
print(linker.linkify('<a href="http://example.com">link</a>'))
print(linker.linkify('<a title="bad title" href="http://example.com">link</a>'))

