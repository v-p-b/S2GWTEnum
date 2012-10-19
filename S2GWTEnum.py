#!/usr/bin/env python
#
# Copyright (c) 2012 Balint Varga-Perke
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

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
functions_raw=function_def_re.findall(html)
functions={}

# Parsing function infromation
for f in functions_raw:
    function_name=re.search("new [a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,('?[a-zA-Z0-9$_]+'?)\)",f).group(1)
    if function_name.startswith("'"):
        function_name=function_name[1:-1]
    else:
        function_name=string_defs[function_name]
    functions[function_name]={}
    param_callers=re.findall("[a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,[a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,([a-zA-Z0-9$_]+)\)\)",f)
    functions[function_name]['params']=[string_defs[p] for p in param_callers if p in string_defs]

# Output
for fname,f in functions.iteritems():
    print "%s(%s)" % (fname,','.join(f['params']))
