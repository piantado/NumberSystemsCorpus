iso6393 = "eko"
sourcecite = "\\citealt[56-57]{g:SchadebergMucanheia:Ekoti}"

sourcebib = '''
@book{g:SchadebergMucanheia:Ekoti,
    author = {Schadeberg, Thilo C. and Mucanheia, Francisco Ussene},
    title = {Ekoti: the Maka or Swahili language of Angoche},
    publisher = {K\"oln: R\"udiger K\"oppe},
    series = {East African Languages and Dialects},
    volume = {11},
    pages = {272},
    year = {2000},
    fn = {africa\schadeberg_ekoti2000_o.pdf, africa\schadeberg_ekoti2000.pdf},
    glotto_id = {121962},
    glottolog_ref_id = {130457},
    hhtype = {grammar},
    inlg = {English [eng]},
    lgcode = {Ekoti = Koti [eko]},
    macro_area = {Africa}
}
'''
"""


f[1] = "moote"
f[2] = "piiri"
f[3] = "ttatthu"
f[4] = "nne"
f[5] = "thaanu"
f[6] = "sitha"
f[7] = "sapa"
f[8] = "naane"
f[9] = "tiisiya"
f[10] = "khumi"
f[100] = "miiya"
f[10+r] = f[10], "na", f[r]
f[k*10] = f[r], f[10]
f[k*10+r] = f[k], "miiya", f[k*10]
