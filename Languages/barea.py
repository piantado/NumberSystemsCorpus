"""
iso6393 = "nrb"
sourcecite = "\\citealt[41-43]{g:Reinisch:Barea}"

sourcebib = '''
@book{g:Reinisch:Barea,
    author = {Reinisch, Leo},
    title = {Die Barea-Sprache: Grammatik, Text und W\"orterbuch},
    publisher = {Wien: Wilhelm Braum\"{u}ller},
    series = {Sprachen von Nord-Ost-Afrika},
    volume = {1},
    pages = {xxviii+186},
    year = {1874},
    fn = {africa\reinisch_barea1874.pdf},
    glotto_id = {115124},
    hhtype = {grammar},
    inlg = {German [deu]},
    lgcode = {Nara [nrb]},
    macro_area = {Africa}
}
'''
"""

f[1] = "doko"
f[2] = "arega"
f[3] = "san\`e"
f[4] = "\v{s}one"
f[5] = "oita"
f[6] = "data"
f[7] = "jariga"
f[8] = "dissena"
f[9] = "lef\'etemada"
f[10] = "lefek"
f[1*10+r] = "lefka" , f[r]
f[2*10+r] = "dokuta" , f[r]
f[p*10+r] = f[p] , {"lefeta" , f[r]}
f[100] = "m\"ot" 
f[p*100+r] = f[p] , f[100] , f[r] 
