"""
iso6393 = "car"
sourcecite = "\\citealt[279-285]{g:Hoff:Carib}"

sourcebib = '''
@phdthesis{g:Hoff:Carib,
    author = {Berend Jacob Hoff},
    title = {The Carib Language: phonology, morphophonology, morphology, texts and word index},
    school = {Rijksuniversiteit te Leiden},
    publisher = {'s Gravenhage: N. V. de Nederlandsche boek- en steendrukkerij v/H H. L. Smits},
    address = {'s Gravenhage},
    series = {Verhandelingen van het Koninklijk instituut voor taal-, land- en volkenkunde, 55},
    pages = {300},
    year = {1968},
    alnumcodes = {gali1262},
    fn = {south_america\hoff_carib1968.pdf},
    glotto_id = {13872},
    glottolog_ref_id = {72877},
    hhtype = {grammar},
    inlg = {English [eng]},
    languoidbase_ids = {26774},
    lgcode = {Galibi Carib [car]},
    macro_area = {South America},
    modified = {False}
}
'''
"""

f[1] = "o:wi\~{\ng}"
f[2] = "o:ko"
f[3] = "o:ruwa"
f[4] = "o:kopaime"
f[5] = "aiyato:ne"
f[1*5+r] = f[r]+"tuwo:p\=iima"
f[9] = "o:winapo:sik\"ir\"i"
f[1*10+r] = "aiyapato:ro" , {"ku:pona:ka" , f[r]}
f[p*20+r] = f[p]+"kari\textglotstop{}na" , {"ku:pona:ka" , f[r]}
