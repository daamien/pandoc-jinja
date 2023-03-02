#!/usr/bin/env python3

"""
Pandoc filter to render metadata as jinja variables
"""

import panflute as pf
import jinja2

# Which classes are rendered by jinja
PF_RENDER_CLASSES=(pf.Str, pf.CodeBlock)

## Some Elements will be deleted, but we need to keep spaces
## Because if a pf.Space object is deleted, all the following will be deleted too
PF_KEEP_CLASSES=(pf.Space,)

## Max number of pandoc elements for a jinja statement
## This is just a security to avoid looping through the entire document
SEARCH_LIMIT=100

def prepare(doc):
    """ Load the doc metadata into a jinja Environment
    """
    doc.elements_to_delete=[]
    doc.env=None
    if not doc.get_metadata('jinja',True): pass
    doc.env=jinja2.Environment()
    doc.env.filters['bool'] = bool
    doc.env.globals={ k: pf.stringify(v)
                      for k,v in doc.metadata.content.items() }


def action(elem, doc):
    """ Apply jinja variables to all strings in document.
    """
    if doc.env:
        if elem in doc.elements_to_delete:
            return []
        render(doc,elem)
    return elem

def render(doc,elem):
    """
    Replace an element by the Jinja result
    """
    if isinstance(elem,pf.CodeBlock):
        disable=pf.get_option(  options=elem.attributes,
                                local_tag="pandoc-jinja-disable",
                                doc=doc,
                                doc_tag="pandoc-jinja.disable",
                                default='')
        if disable.lower() in ( 'true', 'on', '1', 'yes'):
            return

    if isinstance(elem,PF_RENDER_CLASSES) and '{{' in elem.text:
        template=''
        for i in range(0,SEARCH_LIMIT):
            # get the next element, stop if not found
            next_elem=elem.offset(i)
            if not next_elem : break
            # add the element to the template
            template += pf.stringify(next_elem)
            # remove the element
            if not isinstance(next_elem,PF_KEEP_CLASSES):
                doc.elements_to_delete.append(next_elem)
            # stop when we find the closing tag
            if '}}' in template: break
        if doc.get_metadata('panflute.debug'): pf.debug(template)
        elem.text = doc.env.from_string(template).render()

def main(doc=None):
    """ Panflute setup
    """
    return pf.run_filter(action, prepare=prepare, doc=doc)

if __name__ == '__main__':
    main()
