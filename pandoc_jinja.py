#!/usr/bin/env python3

"""
Pandoc filter to render jinja templates on regular text.
"""

from panflute import *
import jinja2, yaml

def prepare(doc):
    """ Load the doc metadata into a jinja Environment
    """
    doc.jj=None
    if not doc.get_metadata('jinja',True): return
    doc.jj=jinja2.Environment()
    doc.jj.globals={ k: stringify(v) for k,v in doc.metadata.content.items() }

def action(elem, doc):
    """ Apply combined jinja variables to all strings in document.
    """
    if doc.jj and type(elem) == Str:
        elem.text = doc.jj.from_string(elem.text).render()
        return elem

def main(doc=None):
    return run_filter(action, prepare=prepare, doc=doc)

if __name__ == '__main__':
    main()
