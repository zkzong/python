import cssutils

css = u'''/* a comment with umlaut &auml; */
     @namespace html "http://www.w3.org/1999/xhtml";
     @variables { BG: #fff }
     html|a { color:red; background: var(BG) }'''
sheet = cssutils.parseString(css)

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        # 遍历属性
        for property in rule.style:
            if property.name == 'color':
                property.value = 'green'
                property.priority = 'IMPORTANT'
                break
        # 简易处理:
        rule.style['margin'] = '01.0eM' # or: ('1em', 'important')

sheet.encoding = 'ascii'
sheet.namespaces['xhtml'] = 'http://www.w3.org/1999/xhtml'
sheet.namespaces['atom'] = 'http://www.w3.org/2005/Atom'
sheet.add('atom|title {color: #000000 !important}')
sheet.add('@import "sheets/import.css";')

# cssutils.ser.prefs.resolveVariables == True
print(sheet.cssText)