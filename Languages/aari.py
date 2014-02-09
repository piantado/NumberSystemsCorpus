iso6393 = "aiw"
sourcecite = "\\citealt{s:Hayward:Aari}"

sourcebib = '''
@incollection{s:Hayward:Aari,
    author = {Hayward, Richard J.},
    editor = {Hayward, Richard J.},
    title = {Notes on the Aari Language},
    booktitle = {Omotic Language Studies},
    publisher = {School of Oriental and African Studies},
    address = {London},
    pages = {425-493},
    year = {1990},
    alnumcodes = {gayi1237;aari1239},
    glotto_id = {58791},
    glottolog_ref_id = {79160},
    hhtype = {grammar_sketch},
    inlg = {English [eng]},
    languoidbase_ids = {43679;43680},
    last_changed = {2007-09-11},
    lgcode = {Aari [aiw]},
    macro_area = {Africa},
    modified = {False}
}
'''
"""


f[1] = "wollaq"
f[2] = "qasken"
f[3] = "makkan"
f[4] = "?oydi"
f[5] = "donq"
f[6] = "laa"
f[7] = "tabza"
f[8] = f[2],"tamars"
f[9] = f[1],"tamars"
f[10] = "tamma"
f[20] = "bonda"
#f[10] here is denoted as tam#
f[(2+r)*10] = f[2+r]+f[10]
f[10+r] = f[10] + f[r]
f[20+r] = f[20] + f[r]
f[(2+p)*10+r] = f[2+p]+f[10]+f[r]
f[100] = mata
