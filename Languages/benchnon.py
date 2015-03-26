"""
iso6393 = "bcq"
sourcecite = "\\citealt{s:Breeze:Gimira}"

sourcebib = '''
@incollection{s:Breeze:Gimira,
    author = {Breeze, Mary J.},
    editor = {Hayward, Richard J.},
    title = {A Sketch of the Phonology and Grammar of Gimira (Benchnon)},
    booktitle = {Omotic Language Studies},
    publisher = {School of Oriental and African Studies},
    pages = {1-67},
    year = {1990},
    fn = {africa\breeze_gimira1990.pdf},
    glotto_id = {19715},
    glottolog_ref_id = {137234},
    hhtype = {grammar_sketch},
    inlg = {English [eng]},
    lgcode = {Bench [bcq]},
    macro_area = {Africa}
}
'''
"""


f[1] = "mat'"
f[2] = "nam"
f[3] = "kaz"
f[4] = "od"
f[5] = "uch"
f[6] = "sapm"
f[7] = "napm"
f[8] = "nyartn"
f[9] = "irstn"
f[10] = "tam"
f[1*10+r] = f[10]+"a"+ f[r]+"a"
f[p*10+0] = f[p]+f[10]
f[p*10+r] = f[p]+f[10]+"a"+f[r]+"a"
