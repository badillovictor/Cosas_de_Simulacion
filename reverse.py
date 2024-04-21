import random
import matplotlib as mpt

if __name__ == '__main__':
    characters = [
        ['37', 'Star'],
        ['6', 'Intelligence'],
        ['A Knight', 'Spirit'],
        ['aliEn T', 'Star'],
        ['An-an Lee', 'Plant'],
        ['APPLe', 'Star'],
        ['Baby Blue', 'Star'],
        ['Balloon Party', 'Mineral'],
        ['Bette', 'Mineral'],
        ['Bkornblume', 'Plant'],
        ['Blonney', 'Star'],
        ['Bunny Bunny', 'Beast'],
        ['Centurion', 'Beast'],
        ['Charlie', 'Star'],
        ['Click', 'Spirit'],
        ['Cristallio', 'Mineral'],
        ['Darley Clatter', 'Beast'],
        ['Desert Flannel', 'Beast'],
        ['Diggers', 'Plant'],
        ['Dikke', 'Beast'],
        ['Door', 'Intelligence'],
        ['Druvis III', 'Plant'],
        ['Eagle', 'Plant'],
        ['Erick', 'Star'],
        ['Eternity', 'Mineral'],
        ['Ezra Theodore', 'Star'],
        ['Getian', 'Beast'],
        ['Horrorpedia', 'Mineral'],
        ['Isolde', 'Spirit'],
        ['Jessica', 'Plant'],
        ['Jiu Niangzi', 'Mineral'],
        ['John Titor', 'Intelligence'],
        ['Kaalaa Baunaa', 'Mineral'],
        ['Kanjira', 'Plant'],
        ['La Source', 'Plant'],
        ['Leilani', 'Beast'],
        ['Lilya', 'Star'],
        ['Marcus', 'Plant'],
        ['Matilda', 'Star'],
        ['Medicine Pocket', 'Beast'],
        ['Melania', 'Beast'],
        ['Mesmer Jr.', 'Intelligence'],
        ['Mondlicht', 'Mineral'],
        ['Ms. Moissan', 'Mineral'],
        ['Ms. NewBabel', 'Intelligence'],
        ['Ms. Radio', 'Spirit'],
        ['Necrologist', 'Mineral'],
        ['Nick Bootom', 'Beast'],
        ['Oliver Frog', 'Star'],
        ['ONiON', 'Mineral'],
        ['Pavia', 'Beast'],
        ['Pickles', 'Mineral'],
        ['Poltergeist', 'Spirit'],
        ['Rabies', 'Plant'],
        ['Regulus', 'Star'],
        ['Satsuki', 'Plant'],
        ['Shamane', 'Beast'],
        ['Sonetto', 'Mineral'],
        ['Sotheby', 'Plant'],
        ['Sputnik', 'Star'],
        ['Sweetheart', 'Beast'],
        ['Tennant', 'Beast'],
        ['The Fool', 'Star'],
        ['Tooth Fairy', 'Star'],
        ['TTT', 'Star'],
        ['Twins Sleep', 'Spirit'],
        ['Ulu', 'Mineral'],
        ['Voyager', 'Star'],
        ['Russina Guy', 'Plant'],
        ['X', 'Intelligence'],
        ['Yenisei', 'Star']
    ]

    stats = [
        ['Star', 0],
        ['Mineral', 0],
        ['Beast', 0],
        ['Plant', 0],
        ['Intelligence', 0],
        ['Spirit', 0],
    ]
    for i in range(10000):
        c = random.choice(characters)[1]
        if c == 'Star':
            stats[0][1] += 1
        elif c == 'Mineral':
            stats[1][1] += 1
        elif c == 'Beast':
            stats[2][1] += 1
        elif c == 'Plant':
            stats[3][1] += 1
        elif c == 'Intelligence':
            stats[4][1] += 1
        elif c == 'Spirit':
            stats[5][1] += 1
        else:
            print(c, 'Is written Wrong')

    for e in stats:
        print(e[0] + ',' + str(e[1]))
