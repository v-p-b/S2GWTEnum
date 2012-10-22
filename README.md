About
=====

Enumerating GWT RPC calls from obfuscated cache HTML files.

Might output some gibberish, but hopefully you will get the most important parts of the RPC interface.

"Works-on-my-single-target" version, needs heavy testing.

Usage
=====

> python S2GWTEnum.py XXXXXXXXXXX.cache.html

How does it work?
=================

The script was constructed by debugging the GWT RPC calls of an application. I found that most of the method and parameter type names of the RPC interface are represented as simple string constants or variables. I could look for known method names in the obfuscated source, and found that the function that constructs the calls have a quite unique structure that I could represent as a regular expression. 

So we first create a dictionary for the variable-string pairs defined by simple assignment in the code, than look for the caller functions and parse them:

```javascript
function bnb(b, c, d) {
    var a, e, f, g; // The number of methods indicates the number of paramaters but we don't really need this
    f = new d5(b, 'methodName'); // here's the method name - maybe we should resolve it from a string variable
    try { // this try block is a good identifier of these caller functions
        g = c5(f, 1);
        u4(g, s4(g, vUb)); // here's one parameter with the type defined in the vUb string
        v4(g, c);
        b5(f, d, (x5(), t5))
    } catch (a) {
        a = jY(a);
        if (zK(a, 106)) {
            e = a;
            h9();
            Dzb(lUb + e.g, kUb, null)
        } else
            throw a
    }
}
```


Thanks
======

Many thanks to Gotham Digital Science for their great publications about GWT:
*   http://blog.gdssecurity.com/labs/2010/7/20/gwtenum-enumerating-gwt-rpc-method-calls.html
*   http://www.gdssecurity.com/l/t.php
*   https://www.owasp.org/images/7/77/Attacking_Google_Web_Toolkit.ppt

Known issues / TODO
===================

*   Scripts are sometimes splitted into multiple HTML files, we should be able to handle these situations
*   Sripathi Krishnan's method should be evaluated to make the script more reliable: https://code.google.com/p/degwt/wiki/HowDeGWTWorks
*   We always need more tests

License
=======

This script uses MIT license
