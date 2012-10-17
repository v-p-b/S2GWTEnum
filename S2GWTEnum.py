#!/usr/bin/env pytohn
#
# Enumerating GWT RPC calls from obfuscated cache HTML files.
# Might output some gibberish, but hopefully you will get the most important parts of the RPC interface.
#
# Many thanks to Gotham Digital Science for their great publications about GWT:
#     * http://blog.gdssecurity.com/labs/2010/7/20/gwtenum-enumerating-gwt-rpc-method-calls.html
#     * http://www.gdssecurity.com/l/t.php
#     * https://www.owasp.org/images/7/77/Attacking_Google_Web_Toolkit.ppt
#
# Usage: python S2GWTEnum.py <XXXXXXXXXXX.cache.html>
#
# Contact: vpbalint@silentsignal.hu

import re
import sys

html=open(sys.argv[1],"r").read()

# Gathering string definitions
string_def_re=re.compile("[a-zA-Z$_]+='[^']*'")
string_defs={}

for d in string_def_re.findall(html):
    parts=d.split('=')
    val=parts[1]
    string_defs[parts[0]]=val[1:len(val)-1]

# Gathering caller functions
function_def_re=re.compile("function [a-zA-Z0-9_$]+\([a-zA-Z0-9,$_]+\){var [a-zA-Z0-9$_,]+;[a-zA-Z0-9$_]+=new [a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,'?[a-zA-Z0-9$_]+'?\);try.*}")
functions_raw=[]
functions={}
for f in function_def_re.findall(html):
    functions_raw.append(f)

# Parsing function infromation
for f in functions_raw:
    function_name=re.search("new [a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,('?[a-zA-Z0-9$_]+'?)\)",f).group(1)
    if function_name[0]=="'":
        function_name=function_name[1:len(function_name)-1]
    else:
        function_name=string_defs[function_name]
    functions[function_name]={}
    param_callers=re.findall("[a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,[a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,([a-zA-Z0-9$_]+)\)\)",f)
    functions[function_name]['params']=[]
    for p in param_callers:
        try:
            functions[function_name]['params'].append(string_defs[p])
        except KeyError:
            pass

# Output
for fname,f in functions.iteritems():
    print "%s(%s)" % (fname,','.join(list(f['params'])))
