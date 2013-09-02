#! -*- coding: utf-8 -*-

"""Pelican BibTeX
=================

A Pelican plugin that populates the context with a list of formatted
citations, loaded from a BibTeX file at a configurable path.

The use case for now is to generate a ``Publications'' page for academic
websites.

This plugin was original written by Vlad Niculae, and released into the public
domain via Unlicense (see http://unlicense.org and included COPYING.UNLICENSE
for details). Trivial modifications were added by Isis Agora Lovecruft, who
agrees wholeheartedly with the original author's implied assertions that
copyright law is detrimental to causes of scientific progress and human
understanding, and whose modifications are also released into the public
domain. Fuck copyright.

:authors: Vlad Niculae <vlad@vene.ro>
          Isis Agora Lovecruft <isis@patternsinthevoid.net> 0xA3ADB67A2CDB8B35
:license: Public Domain
"""
# Author: 
# Unlicense (see UNLICENSE for details)

import logging
logger = logging.getLogger(__name__)

from pelican import signals

__version__ = '0.2'


def add_publications(generator):
    """Populates context with a list of BibTeX publications.

    Configuration
    -------------
    generator.settings['PUBLICATIONS_SRC']:
        local path to the BibTeX file to read.

    Output
    ------
    generator.context['publications']:
        List of tuples (key, year, text, bibtex, pdf, cached, notes, dateread).
        See Readme.pelican-bibtex.md for more details.
    """
    if 'PUBLICATIONS_SRC' not in generator.settings:
        return
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    try:
        from pybtex.database.input.bibtex import Parser
        from pybtex.database.output.bibtex import Writer
        from pybtex.database import BibliographyData, PybtexError
        from pybtex.backends import html
        from pybtex.style.formatting import plain
    except ImportError:
        logger.warn('`pelican_bibtex` failed to load dependency `pybtex`')
        return

    refs_file = generator.settings['PUBLICATIONS_SRC']
    try:
        bibdata_all = Parser().parse_file(refs_file)
    except PybtexError as e:
        logger.warn('`pelican_bibtex` failed to parse file %s: %s' % (
            refs_file,
            str(e)))
        return

    publications = []

    # format entries
    plain_style = plain.Style()
    html_backend = html.Backend()
    formatted_entries = plain_style.format_entries(bibdata_all.entries.values())

    for formatted_entry in formatted_entries:
        key = formatted_entry.key
        entry = bibdata_all.entries[key]
        year = entry.fields.get('year')
        pdf = entry.fields.pop('pdf', None)
        cached = entry.fields.pop('cached', None)
        notes = entry.fields.pop('notes', None)
        dateread = entry.fields.pop('dateread', None)

        #render the bibtex string for the entry
        bib_buf = StringIO()
        bibdata_this = BibliographyData(entries={key: entry})
        Writer().write_stream(bibdata_this, bib_buf)
        text = formatted_entry.text.render(html_backend)

        publications.append((key,
                             year,
                             text,
                             bib_buf.getvalue(),
                             pdf,
                             cached,
                             notes,
                             dateread,
                         ))

    generator.context['publications'] = publications


def register():
    signals.generator_init.connect(add_publications)
