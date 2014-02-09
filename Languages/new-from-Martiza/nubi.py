@article{heinekibera1982
    author = {Bernd Heine & Wilhelm JG Mohlig},
    title = {Language and Dialect Atlas of Kenya},
    journal = {The Nubi Language of Kibera - an Arabic Creole},
    pages = {32-33},
    year = {1982},
    localfile = {creol1}
}


f[1] = "wai"
f[2] = "tinin"
f[3] = "talata"
f[4] = "arba"
f[5] = "kamsa"
f[6] = "sita"
f[7] = "saba"
f[8] = "tamania"
f[9] = "tisa
f[10] = "ashara"
f[11] = "ida", f[10]
f[12] = "idna", f[10]
f[10+r] = f[r],f[10] 
f[20] = "ishirin"
f[30] = "teletin"
f[k*10] = f[r], "in"
#for numbers 40, 70, and 90 the a in the original form of the number is changed to an e before adding the ending"
f[20+r] = f[r], f[20]
f[30+r] = f[r], f[20]
f[k*10+r] = f[r], f[k*10],
#1 becomes waid when added to the tens#
f[100] = "mia"