# Markdown and GitHub Flavor Markdown

<!-- First comment -->

First section
=============

First subsection
----------------

Standard paragraph including *some words in italics*, **some words in bold**, _**some words in bold-italics**_, `some words in monospace`, ~~some words in stroke~~ and even an direct URL reference: http://www.wikipedia.org

> Quoted paragraph (starting with ``> ``) including *some words in italics*, **some words in bold**, _**some words in bold-italics**_, `some words in monospace`, ~~some words in stroke~~ and even an indirect URL reference: [Wikipedia](http://www.wikipedia.org)

    Literal paragraph (starting with ``    ``), preserving any layout and *special* characters

And finally a standard paragraph introducing an interactive Python session

>>> sum(range(5))
10

.. Second comment : the next line defines an document anchor
.. _lists:

# Second section

## Second subsection

* First item of unordered list
* Second item of unordered list
* Third item of unordered list

1. First item of (numerical) ordered list
1. Second item of ordered list
1. Third item of ordered list

A. First item of (alphabetical) ordered list
A. Second item of ordered list
A. Third item of ordered list

First term of definition list
  First item of definition list
**Second term of definition list** (in bold)
  Second item of definition list

:First field:    First item of field list
:Second field:   Second item of field list

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
