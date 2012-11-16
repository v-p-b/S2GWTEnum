" Vim syntax file
" Language: GWTEnum
" Maintainer: Andras Veres-Szentkiralyi <vsza@vsza.hu> 
"
" For version 5.x: Clear all syntax items
" For version 6.x: Quit when a syntax file was already loaded
if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif

syn region gwtParamList	start="("	end=")" contains=gwtSysType,gwtUserType,gwtRef
syn match gwtSysType    "java.[a-zA-Z\.]*" nextgroup=gwtRef
syn match gwtSysType    "[ZIB]"
syn match gwtRef	"/[0-9][0-9]*"
syn match gwtUserType	"com\.[a-zA-Z\.]*"
syn match gwtUserType	"hu\.[a-zA-Z\.]*"
syn match gwtClassName	"^[A-Z][A-Za-z0-9]*" nextgroup=gwtMethodName
syn match gwtMethodName	"[a-z][a-zA-Z0-9]*" nextgroup=gwtParamList

hi def link gwtSysType Type
hi def link gwtMethodName Function
hi def link gwtClassName Constant
hi def link gwtRef Statement
hi def link gwtUserType Special
