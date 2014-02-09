"""
iso6393 = "brx"
sourcecite = "\\citealt[134-136]{g:Bhattacharya:Boro}"

sourcebib = '''
@book{g:Bhattacharya:Boro,
    author = {Pramod Chandra Bhattacharya},
    title = {A Descriptive Analysis of the Boro Language},
    publisher = {Department of Publication, Gauhati University},
    pages = {24+380},
    year = {1977},
    alnumcodes = {boro1277},
    fn = {eurasia/bhattacharya_boro1977_o.pdf},
    glotto_id = {111831},
    glottolog_ref_id = {8408},
    hhtype = {grammar},
    inlg = {English [eng]},
    languoidbase_ids = {29126},
    lgcode = {brx},
    macro_area = {Eurasia},
    modified = {False}
}
'''
"""

f[1] = "-2se"
f[2] = "-1n\=oy"
f[3] = "-2tham"
f[4] = "-1br\=oy"
f[5] = "-1ba" 
f[6] = "-2do"
f[7] = "-1sni"
f[8] = "-1da\.{n}"
f[9] = "-2si1kho"
f[10] = "1zi" 
f[1*10+r] = "2zi"+"1"+f[r]
f[19] = "2zi"+"1gu"
f[p*10+r] = f[p]+"1zi" , f[r]
f[9*10+r] = "2gu"+"1zi" , f[r]
f[1*100+r] = "2zow1se" , f[r]
f[p*100+r] = f[p] , "2zow1se" , f[r]
f[1*1000+r] = "2r\=o2za1se" , f[r]
f[p*1000+r] = f[p] , "2r\=o2za1se" , f[r]


