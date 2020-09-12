class Pipedo:
    cubing = float()
    #Constructor métod for works and
    def __init__(self, dimensions):
        self.dimensions = dimensions


    #méthod for cubing calculation for all works in the Pipedo object
    def cubing (self):
        dimensions = self.dimensions
        cubed = float()
        total = float()
        i = 0

        for sizes in range(len(dimensions)):
            cubing_calc = dimensions[i][0] * dimensions[i][1] * dimensions[i][2]/6000
            i += 1
            total += cubing_calc

        cubed = total
        return cubed

#    def crate_factory(self):
#        works = self.dimensions
#        crate = []
        
#        for w in works range(len(works)):
#            cubing_calc = works



caixa = Pipedo([[100, 5, 90], [210, 10, 170], [60, 5, 90]])
print("A cubagem total é de:" + '{:05.3f}' .format(caixa.cubing()) + "kgs cubados.")








































