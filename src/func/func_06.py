
def make_tag(element, **attrs):
    pattrs = ' '.join(['{}="{}"'.format(k, v) for k, v in attrs.items()])
    return '<{} {}>'.format(element, pattrs)

print (make_tag('div', id='header'))
#'<div id="header">'
print (make_tag('a', href='https://www.python.org/', title='Visit Python.org'))
#'<a href="https://www.python.org/" title="Visit Python.org">'
print (make_tag('img', src='logo.png', alt='Python logo'))
#'<img src="logo.png" alt="Python logo">'
