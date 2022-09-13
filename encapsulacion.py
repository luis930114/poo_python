

class CasillaVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'la region {region} no es valida en {self._pais}')

if __name__ == '__main__':
    casilla = CasillaVotacion(123,['mexico', 'morelos'])
    print(f'{casilla.region} es una _region')
    casilla.region = 'mexico'
    print(f'{casilla.region} es una _region')
