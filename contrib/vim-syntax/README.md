Vim syntax highlight for GWT enumeration output
===============================================

Description and usage
---------------------

When dealing with a huge amount of GWT enumeration output, I found it easier to
read in VIM, using syntax highlight. In order to enable VIM to use this ruleset
with any file with `gwt*.txt`, copy or link `gwtenum.vim` to your
`~/.vim/syntax/` directory, and append the following lines to your `~/.vimrc`.

	au BufRead,BufNewFile gwt*.txt set filetype=gwtenum

Compatibility
-------------

The syntax highlight file works both with S2GWTEnum and the excellent GWTEnum
developed at GDS Security.

Known issues
------------

I admit that I'm a noob when it comes to VIM syntax files, so it's currently
hackish and supports only `hu.` and `com.` namespaces in case of external
parameter types. Feel free to improve it and send me a pull request or patch.
