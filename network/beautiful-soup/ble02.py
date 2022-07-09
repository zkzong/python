import bleach

# tag参数示例
print(bleach.clean(
    u'<b><i>an example</i></b>',
    tags=['b'],
))

# attributes为list示例
print(bleach.clean(
    u'<p class="foo" style="color: red; font-weight: bold;">blah blah blah</p>',
    tags=['p'],
    attributes=['style'],
    styles=['color'],
))
# attributes为dict示例
attrs = {
    '*': ['class'],
    'a': ['href', 'rel'],
    'img': ['alt'],
}
print(bleach.clean(
    u'<img alt="an example" width=500>',
    tags=['img'],
    attributes=attrs
))


# attributes为function示例
def allow_h(tag, name, value):
    return name[0] == 'h'


print(bleach.clean(
    u'<a href="http://example.com" title="link">link</a>',
    tags=['a'],
    attributes=allow_h,
))

# style参数示例
tags = ['p', 'em', 'strong']
attrs = {
    '*': ['style']
}
styles = ['color', 'font-weight']
print(bleach.clean(
    u'<p style="font-weight: heavy;">my html</p>',
    tags=tags,
    attributes=attrs,
    styles=styles
))
# protocol参数示例
print(bleach.clean(
    '<a href="smb://more_text">allowed protocol</a>',
    protocols=['http', 'https', 'smb']
))
print(bleach.clean(
    '<a href="smb://more_text">allowed protocol</a>',
    protocols=bleach.ALLOWED_PROTOCOLS + ['smb']
))

# strip参数示例
print(bleach.clean('<span>is not allowed</span>'))
print(bleach.clean('<b><span>is not allowed</span></b>', tags=['b']))

print(bleach.clean('<span>is not allowed</span>', strip=True))
print(bleach.clean('<b><span>is not allowed</span></b>', tags=['b'], strip=True))

# strip_comments参数示例
html = 'my<!-- commented --> html'
print(bleach.clean(html))
print(bleach.clean(html, strip_comments=False))
