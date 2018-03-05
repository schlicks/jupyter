# Markdown and GitHub Flavor Markdown

---

<!-- First comment -->

First section
=============

First subsection
----------------

Standard block including *some words in italics*, **some words in bold**, _**some words in bold-italics**_, `some words in monospace`, ~~some words in stroke~~ and even an direct URL reference: http://www.wikipedia.org

> Quoted block (starting with **>**) including *some words in italics*, **some words in bold**, _**some words in bold-italics**_, `some words in monospace`, ~~some words in stroke~~ and even an indirect URL reference: [Wikipedia](http://www.wikipedia.org)

    Literal block (starting with four spaces), preserving any layout and *special* characters

And finally a source block with syntax highlighting

```python
a = sum(range(5))
```

# Second section

## Second subsection

* First item of unordered list
* Second item of unordered list
* Third item of unordered list

1. First item of ordered list
1. Second item of ordered list
1. Third item of ordered list

A. First item of (alphabetical) ordered list
A. Second item of ordered list
A. Third item of ordered list

- [x] First item of todo list
- [x] Second item of definition list
- [ ] Third item of definition list

----

| References to numeric footnotes [#]_ and [#]_
| References to symbolic footnotes [*]_ and [*]_
| References to bibliography [ABC2000]_ and [XYZ2000]_
| Document jumps: go to `First section`_ or go to lists_ paragraph

.. [#] First footnote
.. [#] Second footnote
.. [*] Third footnote
.. [*] Fourth footnote
.. [ABC2000] First bibliographic reference
.. [XYZ2000] Second bibliographic reference
