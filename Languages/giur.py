iso6393 = "lwo"
sourcecite = "\\citealt[12-13]{s:Hayward:Aari}"

sourcebib = '''
@book{s:Santandrea:Giur,
    author = {Santandrea, Stefano},
    title = {Grammatichetta Giur},
    publisher = {Verona: Missioni Africane},
    address = {Verona},
    pages = {142},
    year = {1946},
    alnumcodes = {luwo1239},
    fn = {africa/santandrea_giur1946.pdf},
    glotto_id = {121038},
    glottolog_ref_id = {75997},
    hhtype = {grammar_sketch},
    inlg = {Italian [ita]},
    languoidbase_ids = {23596},
    last_changed = {2009-03-12},
    lgcode = {Luwo [lwo]},
    macro_area = {Africa},
    modified = {False}
}
'''
"""


f[1] = "acyelo"
f[2] = "aryou"
f[3] = "adak"
f[4] = "a\ng{}w\textepsilon{}n"
f[5] = "abic"
f[10] = "apaar"
f[20] = "dhano aduno"
f[30] = f[20], "w\textopeno{}\ng{}", f[10]
f[50] = "ji", "aryou", "w\textopeno{}\ng{}", f[10]
f[60] = "ji", "adak"
f[70] = f[60], "w\textopeno{}\ng{}", f[10]
f[80] = "ji", "a\ng{}w\textepsilon{}n"
f[90] = f[80], "w\textopeno{}\ng{}", f[10]
##remove the initial "a" before adding f[r] to abi##
f[5+r] = f[5], "abi", f[r]
##f[10] here is apar##
##for 11 - 15##
f[10+r] = f[10],"w\textopeno{}\ng{}",f[r]
##for 16 to 19 and no initial "a" before the f[r]##
f[15+r] = f[10] , "w\textopeno{}\ng{}", f[5] , "abi", f[r]
f[20+r] = f[20] , "w\textopeno{}\ng{}",f[r]
f[25+r] = f[20] , "w\textopeno{}\ng{}", f[5] , "abi", f[r]
#f[30+r] = f[30] , "w\textopeno{}\ng{}",f[r]
#f[35+r] = f[30] , "w\textopeno{}\ng{}", f[5],"abi", f[r]
#f[40] = f[20] ,"w\textopeno{}\ng{}" , f[20]
f[40+r] = "ji" , "aryou" ,"w\textopeno{}\ng{}", f[r]
f[45+r] = f[40+r], "abi" , f[r]
#f[50 + r] = f[50], "w\textopeno{}\ng{}",f[r]
#f[55+r] = f[50], "w\textopeno{}\ng{}", f[5], "abi", f[r]
#f[60+1] = f[60], "w\textopeno{}\ng{}", f[r]
#f[65+r] = f[60], "w\textopeno{}\ng{}", f[5], "abi", f[r]
#f[70+r] = f[70], "w\textopeno{}\ng{}", f[r]
#f[75+r] = f[70], "w\textopeno{}\ng{}", f[5], "abi", f[r]
#f[80+r] = f[80], "w\textopeno{}\ng{}", f[r]
#f[85+r] = f[80], "w\textopeno{}\ng{}", f[5], "abi", f[r]
#f[90+r] = f[90], "w\textopeno{}\ng{}", f[r]
#f[95+r] = f[90], "w\textopeno{}\ng{}", f[5], "abi", f[r]
