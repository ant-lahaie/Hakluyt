def HK_date(fileid):
    #extracts date component from Hakluyt text file name, returns as integer
    return(int(fileid[11:15]))
def HK_geog(fileid):
    #extracts geography component from Hakluyt text file name, returns as string
    return(fileid[6:10])
def HK_title(fileid):
    #extracts geography component from Hakluyt text file name, returns as string
    return(fileid[16:-15])
def HK_vol(fileid):
    #extracts volume component from Hakluyt text file name, returns as integer
    return(int(fileid[:2]))
def HK_chap(fileid):
    #extracts chapter component from Hakluyt text file name, returns as integer
    return(int(fileid[3:5]))
def HK_pages(fileid):
    #extracts page range component from Hakluyt text file name, returns as tuple of integers
    pages_char = fileid[-11:-4]
    pages_char_split = pages_char.split('-')
    return(int(pages_char_split[0]), int(pages_char_split[1]))
def HK_page_length(fileid):
    #extracts page length component from Hakluyt text file name, returns as integer
    first_page, last_page = HK_pages(fileid)
    return(last_page-first_page+1)