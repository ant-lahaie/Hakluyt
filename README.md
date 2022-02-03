# Hakluyt's Voyages--Computational Explorations

## Overview

The repository documents my 2021-2022 experiments with computational analysis focused on a late 16th-century compilation of exploration and discovery narratives. [Richard Hakluyt](https://en.wikipedia.org/wiki/Richard_Hakluyt), an English clergyman most famous for his promotion of English imperial/colonial expansion, amassed just about every kind of text related to European travel in the world. *The Principall Navigations, Voiages and Discoveries of the English Nation* was first published in 1589, then greatly expanded in a second, three-volume edition printed between 1598 and 1600 (he kept gathering yet more documents thereafter, posthumously published by Samuel Purchas). It is a curious text, which, coming at a little over 2,000,000 words, is eminently suited for computational analysis, despite the technical difficulty of processing Early Modern English. My work started with extracting text from a PDF edition, moved on to broad-methods exploration and then focused on representations of violence and the ways in which Hakluyt occludes colonial violence against non-European people while highlighting intra-European (and especially English-Spanish) hostilities.

The majority of the work was done in Python running on Jupyter Lab notebooks, with occasional use of other tools such as MALLET or MorphAdorner. This is very much a learning work-in-progress, but if you see anything of use, feel free to ~~pilfer~~ borrow, just as I did in putting this together. 

## Table of Contents
### code
- HK_expl: main text-mining notebook, starting with a broad numeric overview of volumes/chapters/etc., some word frequency counts, and then zeroing in on the American volume, and finally doing a deep-dive on representations of violence.
- HK_pdfminer_extract_from_CambridgeCore_pdfs: using the pdfminer package to extract text from the PDF files obtained from [CambridgeCore](https://www.cambridge.org/core/search?q=%22The+Principal+Navigations+Voyages+Traffiques+and+Discoveries+of+the+English+Nation%22&_csrf=ClRQrSp5-1YX3NsOYk38Ttaf8Q1oq0_c_5Xw). Soon abandoned in favor of slightly better quality OCR through ABBYY FineReader.
- FineReader texts processing: cleaning up the text obtained through ABBYY FineReader.
- HK_trim_page_chapters: in splitting the text into chapters, CambridgeCore created quite a bit of duplication: when a chapter ends mid-page, as they usually do, that page is included in both chapter files. Repeat ~600 times, and you get an extra 125,000 words or so. The notebook trims chapter text files in a semi-automatic, supervised manner.
- HK_MorphAdorner_lem_corpus: supplementary code building a lemmatized corpus based on [MorphAdorner](http://morphadorner.northwestern.edu/morphadorner/)
- text cleaning: routines to identify commin misspellings through fuzzy search and fix them globally.
- HK_txt_ledger: creating a csv ledger listing the file names with various metadata
- HK_genre_categories: an attempt to identify meaning genre-like categories based on top frequent words in chapter titles
- HK_AM_cat_corpus: creates a modified corpus based on the American volume hand-tagged for colonial encounter categories
- HK_basics.py: functions to extract basic metadata from filenames
- MALLET_prep: supplementary code for running the text files through [MALLET](https://mimno.github.io/Mallet/index) topic modeling
- plot-gephi: supplementary code for running the text files through [Gephi](https://gephi.org/) network-graphing 

### text data
Most of the text-data subfolders contain the Hakluyt corpus, one .txt file per chapter, variously processed. 'Variously' is captured through a series of abbreviations as follows:
- CambridgeCore / Cambridge / CC: corpus originates in PDF files obtained from [CambridgeCore](https://www.cambridge.org/core/search?q=%22The+Principal+Navigations+Voyages+Traffiques+and+Discoveries+of+the+English+Nation%22&_csrf=ClRQrSp5-1YX3NsOYk38Ttaf8Q1oq0_c_5Xw).
- MacLehose / ML: the text reflects the 1903 MacLehose and Sons edition, reprinting the 1598-1600 text with only slight modernizations.
- note: all of my text data leans on CC & ML.
- pdfminer: text extracted via the pdfminer Python library.
- FineReader_OCR / FR: text extracted through ABBYY FineReader.
- morphad_lem / MAlem: text lemmatized through [MorphAdorner](http://morphadorner.northwestern.edu/morphadorner/).
- trimmed: eliminated overlap between chapter beginning/endings .introduced through page duplications in the PDF chapter splitting
- AMER: only the American volume present.
- cat_mod: modified corpus marked for explorer's nation, for colonial encounters and for exploration accounts; some chapters split into sub-sections for better differentiation.
- enc_full_part: the above, only including chapters dealing with colonial encounter to a significant degree.
<br>

Other files and folders:
- comparison_texts: several English historical texts roughly from the same era for baseline comparison.
- morphadorner-outputs: raw output from [MorphAdorner](http://morphadorner.northwestern.edu/morphadorner/).
- ledger.csv: a list of all the chapter/filenames.
- ledgertagged.csv: same as above, but with added tags.
- AMledger: same, but only for the American volume and with added categories; see cat_mod above.
- stopwords.csv: stopwords organized into different classes.
- replacement_record: keeps track of programmatic spelling modifications, see "text cleaning" notebook.


## Contact

Feel free to reach out at lahaie.anton@gmail.com