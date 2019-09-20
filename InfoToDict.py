import pprint
def putInfoToDict(fileName):
    fo=open(fileName)
    info=fo.read().split(',\n\t')
    info[0]=info[0].strip()
    info[-1] = info[-1].split(';')[0]
    dicta = {}
    lista = []
    for file in info:
        file = tuple(eval(file))
        if file[2] not in dicta.keys():
            lista.append({'lessonid': file[1], 'checktime': file[0]})
            dicta[file[2]] = lista
            lista = []
        else:
            dicta[file[2]].append({'lessonid': file[1], 'checktime': file[0]})
    return dicta
pprint.pprint(putInfoToDict('E:\\DESKTOP\\0005_1.txt'))
