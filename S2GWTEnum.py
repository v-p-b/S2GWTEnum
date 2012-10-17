import re
import sys

html=open(sys.argv[1],"r").read()

# Gathering string definitions
string_def_re=re.compile("[a-zA-Z$_]+='[^']*'")
string_defs={}

for d in string_def_re.findall(html):
    parts=d.split('=')
    string_defs[parts[0]]=parts[1]

# Gathering caller functions
function_def_re=re.compile("function [a-zA-Z0-9_$]+\([a-zA-Z0-9,$_]+\){var [a-zA-Z0-9$_,]+;[a-zA-Z0-9$_]+=new [a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,'[a-zA-Z0-9$_]+'\).*}")
functions_raw=[]
functions={}
for f in function_def_re.findall(html):
    functions_raw.append(f)

# TODO Gather more hidden functions based on executer function name

# Parsing function infromation

for f in functions_raw:
    function_name=re.search("new [a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,'([a-zA-Z0-9$_]+)'\)",f).group(1)
    functions[function_name]={}
    #u4(g,s4(g,vUb))
    param_callers=re.findall("[a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,[a-zA-Z0-9$_]+\([a-zA-Z0-9$_]+,([a-zA-Z0-9$_]+)\)\)",f)
    functions[function_name]['params']=[]
    for p in param_callers:
        try:
            functions[function_name]['params'].append(string_defs[p])
        except KeyError:
            pass
print repr(functions)
