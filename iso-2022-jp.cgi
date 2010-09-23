#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb
cgitb.enable()

from email.Header import decode_header
from email.Header import Header

html = '''Content-Type: text/html

<html>
<head><title>iso-2022-jp エンコード デコード</title></head>
<body>
<form action="iso-2022-jp.cgi" method="post">
<input type="text" style="width: 800px" name="txt1" value="%(txt1)s" /><br />
<input type="submit" name="btnDecode" value="↓decode" />
<input type="submit" name="btnEncode" value="↑encode" /><br />
<input type="text" style="width: 800px" name="txt2" value="%(txt2)s" /><br />
</form>
</body>
</html>
'''

def decode(s):
    x = decode_header(s)
    decoded_string = x[0][0]
#   charset = x[0][1]
    charset = 'iso-2022-jp'
    return decoded_string.decode(charset).encode('utf-8')

def encode(s):
    x = Header(s.decode('utf-8'), 'iso-2022-jp')
    return str(x)

form = cgi.FieldStorage()

dic = {}

if form.getfirst('btnDecode'):
    s = form.getfirst('txt1', '')
    dic['txt1'] = s
    dic['txt2'] = decode(s)
elif form.getfirst('btnEncode'):
    s = form.getfirst('txt2', '')
    dic['txt1'] = encode(s)
    dic['txt2'] = s
else:
    dic['txt1'] = '=?iso-2022-jp?b?GyRCJTslbCVWJEo/TTpKJEg9UDJxJEMkRhsoQg==?='
    dic['txt2'] = 'セレブな人妻と出会って'

for key in dic:
    dic[key] = cgi.escape(dic[key], True)

print html % dic

