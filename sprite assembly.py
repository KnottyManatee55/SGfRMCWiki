import codecs
a1 = str("      ['")
a2 = str("'] = {['поз'] = ")
a3 = str(", ['раздел'] = 1, ['en'] = '")
a4 = str("'},")
n = 0
i = 2
f = open('in.txt', encoding="utf8")
for l in f:
 #   print (l)
    id = (l.replace("\r", "").replace("\n", ""))
    n += 1
    if (n % 2) == 1:
        en = id
    else:
        ru = id
 #       print (ru + en)
        out = a1 + str(ru) + a2 + str(i) + a3 + str(en) + a4
        i += 1
        with codecs.open("out.txt", "a", "utf-8") as stream:
            stream.write(str(out) + "\n")
            stream.close()
