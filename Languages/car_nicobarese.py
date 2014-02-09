"""
iso6393 = "caq"
sourcecite = "\\citealt[116-123]{g:Braine:Nicobarese}"

sourcebib = '''
@phdthesis{g:Braine:Nicobarese,
    author = {Jean C. Braine},
    title = {Nicobarese Grammar (Car Dialect)},
    school = {Berkeley: University of California},
    year = {1970},
    pages = {271},
    fn = {eurasia/braine_car1970v2.pdf, eurasia/braine_nicobarese1970_o.pdf, eurasia/braine_car1970.pdf},
    glotto_id = {19280},
    hhtype = {grammar},
    inlg = {English [eng]},
    lgcode = {Nicobarese-Car [caq]},
    macro_area = {Eurasia}
}
'''
"""

f[1] = "kah\'o.k"
f[2] = "n\'{\textepsilon{}}.t"
f[3] = "l\'u.y\textschwa{}"
f[4] = "f\'{\textepsilon{}}.n"
f[5] = "tan\'{\textbari{}}y"
f[6] = "taf\'u"
f[7] = "s\'at"
f[8] = "h\'ev\textschwa{}\~r"
f[9] = "mac\'uht\textschwa{}\~r"
f[10] = "s\'i.n"
f[1*10+r] = f[r]+"s\'i.n"
f[p*10+r] = f[p] , "\textglotstop{}an\'a.y" , f[r]
f[1*100+r] = "h\'e\ng{}\'o\ng{}" , f[r]
f[p*100+r] = f[p] , "r\'o.\ng{}" , f[r]
f[p*1000+r] = f[p] , "k\textschwa{}\~n" , f[r]
