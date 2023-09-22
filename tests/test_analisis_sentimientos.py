import pytest
from modelo.analisis_sentimientos import Analizador

@pytest.fixture
def mensaje_positivo():
    return "Este es un feedback muy positivo. :)"

def test_sentimiento_positivo(mocker, mensaje_positivo):
    mocker.patch('modelo.analisis_sentimientos.Analizador.analizar', return_value='POSITIVO')

    resultado = Analizador().analizar(mensaje_positivo)

    assert resultado == 'POSITIVO'

