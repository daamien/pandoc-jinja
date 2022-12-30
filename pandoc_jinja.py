#!/usr/bin/env python3

"""
Pandoc filter to render metadata as jinja variables
"""

import panflute as pf
import jinja2

def prepare(doc):
    """ Load the doc metadata into a jinja Environment
    """
    doc.env=None
    if not doc.get_metadata('jinja',True): pass
    doc.env=jinja2.Environment()
    doc.env.globals={ k: pf.stringify(v)
                      for k,v in doc.metadata.content.items() }

## Some Elements will be deleted, but we need to keep spaces.
pf_keep_classes=(pf.Space)
elements_to_delete=[]

##
SEARCH_LIMIT=100

def action(elem, doc):
    """ Apply jinja variables to all strings in document.
    """
    if doc.env:
        if elem in elements_to_delete and not isinstance(elem,pf_keep_classes):
            return []
        render(doc,elem)

def render(doc,elem):
    """
    Replace an element by the Jinja result
    """
    if isinstance(elem,pf.Str) and '{{' in elem.text:
        template=''
        for i in range(0,SEARCH_LIMIT):
            # get the next elemet, stop if not found
            n=elem.offset(i)
            if not n : break
            # add the element to the template
            template += pf.stringify(n)
            # Remove the element
            elements_to_delete.append(n)
            # Stop when we find the closing tag
            if '}}' in template: break
        if doc.get_metadata('panflute.debug'): pf.debug(template)
        elem.text = doc.env.from_string(template).render()

def main(doc=None):
    """ Panflute setup
    """
    return pf.run_filter(action, prepare=prepare, doc=doc)

if __name__ == '__main__':
    main()
