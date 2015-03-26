"""
@article{noticesreinaud1861
    author = {Par M. Reinaud},
    title = {Les Dictionnaires Geographiques Arabes et Sur le systeme Primitif de la Numeration Chez chez le peuples de race berbere},
    journal = {Asiatique},
    pages = {46},
    year = {1861},
    localfile = {afr10}
}
'''
"""

f[1] = "ighem"
f[2] = "tzem"
f[3] = "charet"
f[4] = "occas"
f[5] = "fous"
f[1*5+r] = f[5] + f[r]
f[10] = "meraoun"
f[1*10+r] = f[10] + f[r]
f[p*10+0] = f[p] + f[10]
f[p*10+r] = f[p] + f[10] + f[r]
