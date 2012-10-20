About
=====

Enumerating GWT RPC calls from obfuscated cache HTML files.

Might output some gibberish, but hopefully you will get the most important parts of the RPC interface.

"Works-on-my-single-target" version, needs heavy testing.

Usage
=====

> python S2GWTEnum.py XXXXXXXXXXX.cache.html

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
*   Documentating how this script actually works...

License
=======

This script uses MIT license
