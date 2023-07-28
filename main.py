

class EsmFamil():
    def __init__(self):
        self.tedad = 0
        self.currentB = {'esm':'', 'shahr':'', 'ghaza':'', 'rang':'', 'point':'0'}
        self.dataa = {}

    def setEsm(self, esm):
        self.dataa[self.currentB][esm] = esm

    def setShahr(self, shahr):
        self.dataa[self.currentB][shahr] = shahr

    def setGhaza(self, ghaza):
        self.dataa[self.currentB][ghaza] = ghaza

    def setRang(self, rang):
        self.dataa[self.currentB][rang] = rang

    def calculatePoint(self):
        point = {}
        for i, currentB in enumerate(self.dataa):
            point_esm = 0
            point_shahr = 0
            point_rang = 0
            point_ghaza = 0
            for B in self.dataa:
                if currentB is not B:
                    if currentB['esm'].lower() == B['esm'].lower():
                        point_esm = 5
                    if currentB['shahr'].lower() == B['shahr'].lower():
                        point_shahr = 5
                    if currentB['ghaza'].lower() == B['ghaza'].lower():
                        point_ghaza = 5
                    if currentB['rang'].lower() == B['rang'].lower():
                        point_rang = 5
            if currentB['esm'] == '':
                point_esm = 0
            if currentB['shahr'] == '':
                point_shahr = 0
            if currentB['ghaza'] == '':
                point_ghaza = 0
            if currentB['rang'] == '':
                point_rang = 0

            point[i] = point_esm + point_shahr + point_ghaza + point_rang
            currentB['point'] = point[i]
        return point

    def winner(self):
        # points = {}
        # for b in self.dataa:
        #     points.append(b,self.dataa[self.currentB]['point'])
        points = self.calculatePoint()
        max_point = max(self.calculatePoint().values())
        return max_point, points


class Person():
    pass









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/