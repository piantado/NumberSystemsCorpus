iso6393 = "kna"
sourcecite = "\\citealt[20]{g:Newman:Kanakuru}"

sourcebib = '''
@book{g:Newman:Kanakuru,
    author = {Newman, Paul},
    title = {The Kanakuru language},
    publisher = {in association with the West African Linguistic Society: Institute of Modern English Language Studies, University of Leeds},
    series = {West African language monographs},
    volume = {9},
    pages = {x+139},
    year = {1974},
    fn = {africa\newman_kanakuru1974.pdf},
    glotto_id = {101098},
    glottolog_ref_id = {81988},
    hhtype = {grammar},
    inlg = {English [eng]},
    isbn = {9780904550009},
    lgcode = {kna},
    macro_area = {Africa},
    subject_headings = {Kanakuru language -- Grammar}
}
'''
"""

f[1] = "dumoi"
f[2] = "rap"
f[3] = "kunu\ng{}"
f[4] = "parau"
f[5] = "baac"
f[6] = "beeme"
f[7] = "boila"
f[8] = "toorumen"
f[9] = "wandumoi"
f[10] = "gum"
f[10+r] = f[10], "d\textschwa{}", f[r]
f[k*10] = f[r]+"\ng{}gumni"
f[k*10+r] = f[k*10],"d\textschwa{}",f[r]
