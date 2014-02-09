iso6393 = "zay"
sourcecite = "\\citealt{g:Hayward:Zayse}"

sourcebib = '''
@incollection{g:Hayward:Zayse,
    author = {Hayward, Richard J.},
    editor = {Hayward, Richard J.},
    title = {Notes on the Zayse Language},
    booktitle = {Omotic Language Studies},
    publisher = {School of Oriental and African Studies},
    pages = {210-355},
    year = {1990},
    alnumcodes = {zays1235},
    fn = {africa\hayward_zayse1990.pdf},
    glotto_id = {58793},
    glottolog_ref_id = {13443},
    hhtype = {grammar},
    inlg = {English [eng]},
    languoidbase_ids = {29117},
    last_changed = {2007-08-27},
    lgcode = {Zayse-Zergulla [zay]},
    macro_area = {Africa},
    modified = {False}
}
'''
"""

f[1] = "bizzo"
f[2] = "nam?"
f[3] = "hays"
f[4] = "?oydd"
f[5] = "?ishich"
f[6] = "?izup"
f[7] = "laap"
f[8] = "lakkuche"
f[9] = "s'ingo"
f[10] = "tamm"
f[20] = f[2]+"i", f[10]
f[30] = f[3]+"i", f[10]
f[40] = f[4]+"i", f[10]
f[50] = f[5], f[10]
f[(5+r)*10] = f[5+r], f[10]
f[100] = "s'eet"
f[10+r] = f[10]+"ane", f[r]
f[20+r] = f[20]+"ane", f[r]
f[30+r] = f[30]+"ane", f[r]
f[40+r] = f[40]+"ane", f[r]
f[50+r] = f[50]+"ane", f[r]
f[(5+p)*10+r] = f[(5+p)*10]+"ane", f[r]
