import bleach
print(bleach.clean('an <script>evil()</script> example'))
print(bleach.linkify('an http://example.com url'))



