import re
fhand = open('stemmen.csv')
count = 0
dict = {}
tmp = list()
lijst2 = []

for line in fhand:   
    line = line.decode("utf-8")
    lijst = line.split('","')
    movie = lijst[1]
    jaar = lijst[2]
    x = list(movie)
    x.remove("\"")
    x.remove("\"")
    y = list(jaar)
    y.remove("\"")
    y.remove("\"")
    count = count + 1
    dict["".join(x)] = "".join(y)

for key, value in dict.items():
    tmp.append( (value, key) ) 

tmp.sort()

for year, title in tmp[:-1]:
    print year + "-" + title

print '\nTotaal aantal films gezien:',count


def most_common(lst):
    return max(set(lst), key=lst.count)


fhand2 = open('stemmen.csv')
count = 0
jaarlijst = []
for line in fhand2:
    x = line.rstrip()
    y = x.split(',')
    for word in y:
        jaar = re.findall("([^0-9-:][0-9][0-9][0-9][0-9][^0-9-:])", word)
        if len(jaar) > 0:
            jaarlijst = jaarlijst + jaar
            count = count+1

print "Oudste film komt uit: " ,min(jaarlijst)
print "Nieuwste film komt uit: ",max(jaarlijst)
print "Jaartal waarvan je de meeste films gezien heb: ", most_common(jaarlijst)        