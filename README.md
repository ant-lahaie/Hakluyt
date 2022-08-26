# Hakluyt's Voyages--Computational Explorations WIP

## Overview

The repository documents my 2021-2022 experiments with computational analysis focused on a late 16th-century compilation of exploration and discovery narratives. [Richard Hakluyt](https://en.wikipedia.org/wiki/Richard_Hakluyt), an English clergyman most famous for his promotion of English imperial/colonial expansion, amassed just about every kind of text related to European travel in the world. *The Principall Navigations, Voiages and Discoveries of the English Nation* was first published in 1589, then greatly expanded in a second, three-volume edition printed between 1598 and 1600 (he kept gathering yet more documents thereafter, posthumously published by Samuel Purchas). It is a curious text, which, coming at a little over 2,000,000 words, is eminently suited for computational analysis, despite the technical difficulty of processing Early Modern English. My work started with extracting text from a PDF edition, moved on to broad-methods exploration and then focused on representations of violence and the ways in which Hakluyt occludes colonial violence against non-European people while highlighting intra-European (and especially English-Spanish) hostilities.

The majority of the work was done in Python running on Jupyter notebooks, with occasional use of other tools such as MALLET or MorphAdorner. This is very much a learning work-in-progress, but if you see anything of use, feel free to ~~pilfer~~ borrow, just as I often did in putting this together. 

## Table of Contents
### code
- main research notebooks:
    - **HK_arg: a consolidated formal computational argument carried from text cleaning, through computational analysis, and to discussion of significance. The main notebook worth reading unless you are interested in messy code.**
    - HK_expl: main working text-mining notebook
    - HK_ledgers: various ledger operations, incrementally recording added per-chapter findings
    - MALLET_prep: supplementary code for running the text files through [MALLET](https://mimno.github.io/Mallet/index) topic modeling
    - plot-gephi: supplementary code for running the text files through [Gephi](https://gephi.org/) network-graphing 
- one-off operations:
    - HK_genre_categories: an attempt to identify meaning genre-like categories based on top frequent words in chapter titles.
    - HK_pdfminer_extract_from_CambridgeCore_pdfs: using the pdfminer package to extract text from the PDF files obtained from [CambridgeCore](https://www.cambridge.org/core/search?q=%22The+Principal+Navigations+Voyages+Traffiques+and+Discoveries+of+the+English+Nation%22&_csrf=ClRQrSp5-1YX3NsOYk38Ttaf8Q1oq0_c_5Xw). Soon abandoned in favor of slightly better quality OCR through ABBYY FineReader.
    - FineReader texts processing: cleaning up the text obtained through ABBYY FineReader.
    - HK_trim_page_chapters: in splitting the text into chapters, CambridgeCore created quite a bit of duplication: when a chapter ends mid-page, as they usually do, that page is included in both chapter files. Repeat ~600 times, and you get an extra 125,000 words or so. The notebook trims chapter text files in a semi-automatic, supervised manner.
    - HK_MorphAdorner_lem_corpus: supplementary code building a lemmatized corpus based on [MorphAdorner](http://morphadorner.northwestern.edu/morphadorner/)
    - text cleaning: routines to identify common misspellings through fuzzy search and fix them globally.
    - HK_AM_cat_corpus: created a modified corpus based on the American volume hand-tagged for colonial encounter categories
    - HK_basics.py: shared functions to extract basic metadata from filenames


### text data
Most of the text-data subfolders contain the Hakluyt corpus, one .txt file per chapter, variously processed. 'Variously' is captured through a series of abbreviations as follows:
- CambridgeCore / Cambridge / CC: corpus originates in PDF files obtained from [CambridgeCore](https://www.cambridge.org/core/search?q=%22The+Principal+Navigations+Voyages+Traffiques+and+Discoveries+of+the+English+Nation%22&_csrf=ClRQrSp5-1YX3NsOYk38Ttaf8Q1oq0_c_5Xw).
- MacLehose / ML: the text reflects the 1903 MacLehose and Sons edition, reprinting the 1598-1600 text with only slight modernizations.
- *note: all of my text data leans on CC & ML.*
- pdfminer: text extracted via the pdfminer Python library.
- FineReader_OCR / FR: text extracted through ABBYY FineReader.
- EN: removed non-English text (when including non-English passages, Hakluyt typically provides a translation immediately after)
- morphad_lem / MAlem: text lemmatized through [MorphAdorner](http://morphadorner.northwestern.edu/morphadorner/).
- MAspel: spelling normalized through [MorphAdorner](http://morphadorner.northwestern.edu/morphadorner/).
- trimmed: eliminated overlap between chapter beginning/endings introduced through page duplications in the PDF chapter splitting
- chunked: text broken down into smaller text files for topic modeling
- AMER: only the American volume present.
- cat: some chapters split into sub-sections for better differentiation of intercultural encounter
- cat_mod: as above, but with filenames marked for explorer's nation, for colonial encounters and for exploration accounts
<br>

Other files and folders:
- mallet: MALLET topic modeling outputs, often processed with interpretative topic names & incidence graphs in Excel
- Gephi: Gephi working files and graph outputs in PDF format
- text-data/comparison_texts: several English historical texts roughly from the same era for baseline comparison.
- text-data/morphadorner-outputs: raw output from [MorphAdorner](http://morphadorner.northwestern.edu/morphadorner/).
- text-data/ledger***.csv: spreadsheets tracking metadata and research findings per chapter (and sometimes smaller text chunks).
- text-data/stopwords.csv: stopwords organized into different classes.
- text-data/replacement_record: keeps track of programmatic spelling modifications, see "text cleaning" notebook.


## Contact

Feel free to reach out at lahaie.anton@gmail.com