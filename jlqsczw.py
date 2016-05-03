bookname = '金鳞岂是池中物（未删节全本）'
fw = open(bookname + '.txt','w' )

for x in range(1,43):
    filename = bookname + str(x) + '.txt'
    print(filename)
    fr = open(filename, 'r')
    fw.write(fr.read())
    fw.write('\n')

fw.close()

    
