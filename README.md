[![PyPI version](https://badge.fury.io/py/pandoc-jinja.svg)](https://pypi.org/project/pandoc-jinja/)

# pandoc-jinja

Render pandoc metadata inside the document itself

## Example

Write a markdown file, define metadata variable,
and use them inside the with double brackets.

```mardown
---
title: 'GREETINGS !'
bonjour: 'Hello'

...

## {{title}}

{{bonjour}}, {{name}} !
```

You can also define variable from the command line
with `--metadata` or `--metadata-file` :

```
$ pandoc foo.md --filter=pandoc-jinja --metadata=name:world
<h2 id="title">GREETINGS !</h2>
<p>Hello, world !</p>
```

## Disclaimer

* Variables are referenced by enclosing the variable name in double brackets,
  like `{{this}}`. **DO NOT** put spaces inside the brackets like
  ``{{ this_wont_work }}`

* Jinja conditionals, loops and filters are not supported.

## Install

```
pip install pandoc-jinja
```

## Similar filters

* [pandoc-mustache](https://github.com/michaelstepner/pandoc-mustache)
* [pandoc-abbreviations](https://github.com/scokobro/pandoc-abbreviations)
