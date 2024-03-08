#!/usr/bin/env python3

"""
Pandoc filter to render metadata as jinja variables
"""

import panflute as pf
import jinja2

# Which classes are rendered by jinja
PF_RENDER_CLASSES=(pf.Str, pf.CodeBlock)

## Max number of pandoc elements for a jinja statement
## This is just a security to avoid looping through the entire document
SEARCH_LIMIT=100

def prepare(doc):
    """ Load the doc metadata into a jinja Environment
    """
    doc.element_id=0
    doc.elements_to_delete=[]
    doc.env=None
    if not doc.get_metadata('jinja',True): pass
    doc.env=jinja2.Environment()
    doc.env.filters['bool'] = bool
    doc.env.globals=doc.get_metadata()

def action(elem, doc):
    """ Apply jinja variables to all strings in document.
    """
    if doc.env:
        doc.element_id+=1
        if doc.element_id in doc.elements_to_delete:
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
        nested_elements=0
        for i in range(0,SEARCH_LIMIT):
            # get the next element, stop if not found
            next_elem=elem.offset(i)
            if not next_elem : break
            # add the element to the template
            template += pf.stringify(next_elem)
            # remove the next elements of the jinja expression
            # the rendered expression will replace the 1rst element
            doc.elements_to_delete.append(doc.element_id+i)
            if isinstance(next_elem,pf.Quoted):
                nested_elements+=len(next_elem.content)+1
            # stop when we find the closing tag
            if '}}' in template: break

        for j in range(0,nested_elements):
            doc.elements_to_delete.append(doc.element_id+i+j)

        if doc.get_metadata('panflute.debug'): pf.debug(template)
        elem.text = doc.env.from_string(template).render()

def main(doc=None):
    """ Panflute setup
    """
    return pf.run_filter(action, prepare=prepare, doc=doc)

if __name__ == '__main__':
    main()
