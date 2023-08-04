daList = []
x=0
with open('uris.txt') as f:
    for uri in f.readlines():
        daList[x] = uri.replace('\n', '')
    x += 1
    print(daList)