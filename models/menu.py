# -*- coding: utf-8 -*-

response.title = request.application
response.subtitle = T('customize me!')

#http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'you'
response.meta.description = 'Free and open source full-stack enterprise framework for agile development of fast, scalable, secure and portable database-driven web-based applications. Written and programmable in Python'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Enterprise Framework'
response.meta.copyright = 'Copyright 2007-2010'


response.menu = [
    (T('Home'), False, URL('default','index'), []),
    (T('Cart'), False, URL('default','cart'), []),
    (T('Buy'), False, URL('default','buy'), []),
    ]
