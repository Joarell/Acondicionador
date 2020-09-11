


class Pipedo:
    cubing = float() 

    def __init__(self, dimensions):      #Medidas necessárias para definção da obra e caixa
        self.dimensions = dimensions
       # sizes = dimensions
        #print(sizes)

    def cubing (self):
        dimensions = self.dimensions
        cubed = float()
        total = float()
        i = 0

        for sizes in range(len(dimensions)):
            cubing_calc = self.dimensions[i][0] * self.dimensions[i][1] * self.dimensions[i][2]/6000
            i += 1
            total += cubing_calc

        cubed = total


        return cubed

    def crate_factory(self):
        dimensions = self.dimensions
        crate_sizes = []
        i = 0
        crate_sketch = []
        work = float()
        base = int()

        for sizes in range(len(dimensions)):
            cubing_calc = self.dimensions[i][0] * self.dimensions[i][1] * self.dimensions[i][2]/6000


            if cubing_calc > work:
                work = cubing_calc
                crate_sketch = dimensions[i]
                
            else:
                pass
            i += 1

        print(crate_sketch)

        base = dimensions.index(crate_sketch)
        print(base)
        dimensions.remove(crate_sketch)
        print(dimensions)
        
#        while len(dimensions) >= 0:
            











caixa = Pipedo([[100, 5, 90], [210, 10, 170], [60, 5, 90], [290, 10, 180], [100, 5, 70]])

print("A cubagem total é de:" + '{:05.3f}' .format(caixa.cubing()) + "kgs cubados.")
print(caixa.crate_factory())































