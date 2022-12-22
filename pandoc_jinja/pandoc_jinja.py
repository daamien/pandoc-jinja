#!/usr/bin/env python3

"""
Pandoc filter to render jinja templates on regular text.
"""

from panflute import *
import jinja2, yaml

def prepare(doc):
    """ Parse metadata to obtain list of mustache templates,
        then load those templates.
    """
    doc.jj_env=None
    doc.jj_mhash=None
    doc.jj_files = doc.get_metadata('jinja',None)
    if doc.jj_files is not None:
        doc.jj_hashes = [yaml.load(open(file, 'r').read(), Loader=yaml.SafeLoader) for file in doc.jj_files]
        # combine list of dicts into a single dict
        doc.jj_mhash = { k: v for mdict in doc.jj_hashes for k, v in mdict.items() }
        doc.jj_env=jinja2.Environment()

def action(elem, doc):
    """
    Apply combined jinja variables to all strings in document.
    """
    if type(elem) == Str and doc.jj_mhash is not None:
        elem.text = doc.jj_env.from_string(elem).render(doc.jj_mhash)
        return elem

def main(doc=None):
    return run_filter(action, prepare=prepare, doc=doc)

if __name__ == '__main__':
    main()
