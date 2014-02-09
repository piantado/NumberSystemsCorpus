"""
iso6393 = "chv"
sourcecite = "\\citealt[172-176]{g:Krueger:Chuvash}"

sourcebib = '''
@book{g:Krueger:Chuvash,
    author = {John R. Krueger},
    title = {Chuvash Manual: Introduction, Grammar, Reader, and Vocabulary},
    publisher = {Bloomington: Indiana University},
    address = {Bloomington},
    series = {Indiana University Publications: Uralic and Altaic Series},
    volume = {7},
    pages = {274},
    year = {1961},
    alnumcodes = {chuv1255},
    fn = {eurasia/krueger_chuvash1961.pdf},
    glotto_id = {68812},
    glottolog_ref_id = {52886},
    hhtype = {grammar},
    inlg = {English [eng]},
    languoidbase_ids = {23911},
    lgcode = {Chuvash [chv]},
    macro_area = {Eurasia},
    modified = {False}
}
'''
"""

f[1] = "p\u{e}r"
f[2] = "ik\u{e}"
f[3] = "vi\'s\u{e}"
f[4] = "t\u{a}vat\u{a}"
f[5] = "pil\u{e}k"
f[6] = "ult\u{a}"
f[7] = "\'si\v{c}\u{e}"
f[8] = "sak\u{a}r"
f[9] = "t\u{a}\textchi{}\u{a}r"
f[10] = "vun\u{a}"
f[1*10+r] = "vun"+f[r]
f[20] = "\'sir\u{e}m"
f[30] = "v\u{a}t\u{a}r"
f[40] = "\textchi{}\u{e}r\u{e}\textchi{}"
f[50] = "all\u{a}"
f[60] = "utm\u{a}l"
f[70] = "\'sitm\u{e}l"
f[80] = "sak\u{a}rvunn\u{a}"
f[90] = "t\u{a}\textchi{}\u{a}rvun\u{a}"
f[p*10+r] = f[p*10] , f[r]
f[1*100+r] = "\'s\u{e}r" , {"te" , f[r]}
f[p*100+r] = f[p]+"\'s\u{e}r" , {"te" , f[r]}
f[1*1000+r] = "pin" , {"te" , f[r]}
f[p*1000+r] = f[p] , "pin" , {"te" , f[r]}
