__author__ = 'ssinghal'

# Override the default behavior of "Template"

from string import Template

class MyTemplate(Template):
    delimiter = '#'
    idpattern = r'[a-z][_a-z0-9]*'


s = MyTemplate('#who likes $what')
print s.substitute(who='tim', what='kung pao')
