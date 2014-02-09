iso6393 = "taq"
sourcecite = "\\citealt[245]{g:Heath:Tamashek}"

sourcebib = '''
@book{g:Heath:Tamashek,
    author = {Heath, Jeffrey},
    title = {A grammar of Tamashek (Tuareg of Mali)},
    publisher = {Berlin: Mouton de Gruyter},
    series = {Mouton Grammar Library},
    volume = {35},
    pages = {xvi+745},
    year = {2005},
    fn = {africa\heath_tamashek2005.pdf},
    glotto_id = {59165},
    glottolog_ref_id = {131507},
    hhtype = {grammar},
    inlg = {English [eng]},
    isbn = {9783110184846},
    lgcode = {Mali Tamasheq [taq]},
    macro_area = {Africa},
    subject_headings = {Tamashek language--Grammar}
}
'''
"""


f[1] = "d-iy-\ae{}n"
f[2] = "d-\textschwa{}ssin"
f[3] = "k\ae{}r\textscripta{}d"
f[4] = "d-\ae{}kkoz"
f[5] = "s\ae{}mmos"
f[6] = "s\textschwa{}dis"
f[7] = "\ae{}ssa"
f[8] = "\ae}tt\textscripta{}m"
f[9] = "t\ae{}zza"
f[10] = "m\ae{}r\textscripta{}w"
f[k*10] = f[r] + "t-i-m\textschwa{}rw-en"
##for complex numbers it's the first part of the number and then the second part of the number without the ten's name with it. if counting nouns the noun is inserted in between both digits.##
f[k*10+r] = f[r1] + f[r2]
