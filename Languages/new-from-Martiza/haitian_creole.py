@article{valdmanhaitiancreole1970
    author = {Albert Valman},
    title = {Basic Course in Haitian Creole},
    journal = {--},
    pages = {10.6, 11.9},
    year = {1970},
    localfile = {creol1}
}


f[1] = "youn"
f[2] = "deu"
f[3] = "troua"
f[4] = "kat"
f[5] = "senk"
f[6] = "sis"
f[7] = "set"
f[8] = "uit"
f[9] = "neuf
f[10] = "dis"
f[11] = "onz"
f[12] = "douz"
f[13] = "trez"
f[14] = "katoz"
f[15] = "kenz"
f[16] = "senz"
f[10+r] = f[10],f[r]
#the s in dis becomes a z before added to the other numbers#
f[20] = "ven"
f[30] = "trant"
f[40] = "karant"
f[70] = f[6], "ann", f[10]
f[80] = f[4], "re", f[20]
f[90] = f[80], "n", f[10]
f[k*10] = f[r], "ant"
f[70+r] = f[60], "n" f[10+r]
f[90+r] = f[80], "n" f[10+r]
#literally means 6 times 10 plus the teens#
f[k*10+1] = f[k*10], "teen"
f[k*10+r] = f[k*10], "n", f[r]
#the numbers ending in 8 and 9 do not have the extra n#
f[100] = "san"