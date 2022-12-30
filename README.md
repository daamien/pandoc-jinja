[![PyPI version](https://badge.fury.io/py/pandoc-jinja.svg)](https://pypi.org/project/pandoc-jinja/)

# pandoc-jinja

Render pandoc metadata inside the document itself

## Example

Write a markdown file, define metadata variable,
and use them inside the with double brackets.

```mardown
---
title: 'Greetings !'
bonjour: 'Hello'
...

## {{ title | upper }}

{{ bonjour }}, {{name}} !
```

You can also define variable from the command line
with `--metadata` or `--metadata-file` :

```
$ pandoc foo.md --filter=pandoc-jinja --metadata=name:world
<h2 id="title">GREETINGS !</h2>
<p>Hello, world !</p>
```

## Disclaimer

* This filter is slow. In most cases, it is probably more efficient
  to render the entire document once and for all with jinja and then
  pass it to pandoc.

* Jinja conditionals and loops are not supported.

## Install

```
pip install pandoc-jinja
```

## Similar filters

* [pandoc-mustache](https://github.com/michaelstepner/pandoc-mustache)
* [pandoc-abbreviations](https://github.com/scokobro/pandoc-abbreviations)
