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


def action(elem, doc):
    """ Apply jinja variables to all strings in document.
    """
    if doc.env and isinstance(elem,pf.Str):
        elem.text = doc.env.from_string(elem.text).render()

def main(doc=None):
    """ Panflute setup
    """
    return pf.run_filter(action, prepare=prepare, doc=doc)

if __name__ == '__main__':
    main()
