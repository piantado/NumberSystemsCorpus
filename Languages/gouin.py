iso6393 = "cme"
sourcecite = "\\citealt[110-111]{ew:Tauxier:Gouin-Tourouka}"

sourcebib = '''
@article{ew:Tauxier:Gouin-Tourouka,
    author = {Tauxier, Louis},
    title = {Les Gouin et les Tourouka (R\'esidence de Banfora, cercle de Bobo-Dioulasso): \'Etude ethnographique suivie d'un double vocabulaire},
    journal = {Journal de la Soci\'et\'e des Africanistes},
    volume = {3},
    pages = {77-128},
    year = {1933},
    fn = {africa\tauxier_gouin-tourouka1933.pdf},
    glotto_id = {132553},
    glottolog_ref_id = {156706},
    hhtype = {ethnographic;wordlist},
    inlg = {French [fra]},
    lgcode = {Gouin [cme], Tourouka [tuz]},
    macro_area = {Africa}
}
'''
"""

f[1] = "nde"
f[2] = "bain"
f[3] = "nsie"
f[4] = "nain"
f[5] = "n'di"
f[6] = "nedi"
f[5+r] = f[5]+f[r]
f[10] = "kiunkilo"
f[11] = "n'diele-kou-di"
f[10+r] = "n'diele" + f[r]
f[20] = "komore"
f[30] = "komore", "ntielo"
f[40] = "komovinnbain"
f[50] = f[40], "ba", "intielo"
f[60] = "komofinn-asie"
f[70] = f[60] + f[10]
f[80] = "komofina-nain"
f[90] = "komofina", f[10]
f[k*10+r] = f[k*10], "ou", f[r]
f[100] = "komofinan", "di"
