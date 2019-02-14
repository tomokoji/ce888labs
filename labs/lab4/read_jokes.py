"""
===========================================================================
                         r e a d _ j o k e s . p y
---------------------------------------------------------------------------
This code reads jokes from html files in jokes folder.

Author          : Tomoko Ayakawa
Created on      : 14 February 2019
Last modified on: 14 February 2019
===========================================================================
"""

# -------------------------------------------------------------------------
# Read jokes from the file
# -------------------------------------------------------------------------
def get_jokes():
    import bs4
    import glob

    files = glob.glob('./jokes/*.html')
    jokes_list=[]
    
    for file in files:
        with open(file , encoding='utf-8') as f:
            html = f.read()
    
        soup = bs4.BeautifulSoup(html, "html.parser")
        table = soup.find_all("table")    
        joke = table[0].find_next().text.strip()
        jokes_list.append(joke)
        
    return jokes_list

# -------------------------------------------------------------------------
# Allow the programme to be ran from the command line.
# -------------------------------------------------------------------------
if __name__ == '__main__':
    # file = open_dialogue ()
    
    get_jokes()
