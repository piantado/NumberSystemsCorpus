"""
iso6393 = "bom"
sourcecite = "\\citealt[256-259]{g:Bouquiaux:Birom}"

sourcebib = '''
@book{g:Bouquiaux:Birom,
    author = {Bouquiaux, Luc},
    title = {La langue Birom (Nigeria Septentrional): phonologie, morphologie, syntaxe},
    publisher = {Paris: Soci\'{e}t\'{e} d'\'{E}dition "les belles lettres"},
    address = {Paris},
    series = {Biblioth\`{e}que de la Facult\'{e} de Philosophie et Lettres de l'Universit\'{e} de Li\`{e}ge -- Fascicule CLXXXV},
    year = {1970},
    alnumcodes = {bero1242},
    fn = {africa/bouquiaux_birom1970.pdf},
    glotto_id = {18497},
    glottolog_ref_id = {125830},
    hhtype = {grammar},
    inlg = {French [fra]},
    languoidbase_ids = {31914},
    last_changed = {2007-09-13},
    lgcode = {Berom [bom]}
}
'''
"""

f[1] = "-d\=ini\ng{}"
f[2] = "-ba"
f[3] = "-tat"
f[4] = "-na:s"
f[5] = "-tu\ng{}un" 
f[6] = "-ti:m\`in"
f[7] = "-ta:m\`a"
f[8] = "rwi:t"
f[1*12-r] = "sya:" , f[r]
f[1*12+r] = "kuru" , {"n\'a" , f[r]}
f[p*12+r] = "bakuru" , "ba"+f[p] , {"n\'a" , f[r]}
f[144] = "n\`ak\'a"
f[1*144+r] = "n\`ak\'a" , {"n\'a" , f[r]}
f[p*144+r] = "bin\`ak\'a" , "bi"+f[p] , {"n\'a" , f[r]}


