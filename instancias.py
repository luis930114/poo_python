class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordendada):
        x_diff = (self.x - otra_coordendada.x)**2
        y_diff = (self.y - otra_coordendada.y)**2

        return suma(x_diff, y_diff)

    def suma(self, coord_1, coord_2):
        return (coord_1 + coord_2)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)
    print(coord_2.suma(coord_2.x,coord_2.y))
    #print(coord_1.distancia(coord_2))
    #print(isinstance(3, Coordenada))
