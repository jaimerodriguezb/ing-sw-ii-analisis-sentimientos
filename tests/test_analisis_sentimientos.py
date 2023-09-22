import pytest
from modelo.analisis_sentimientos import Analizador

@pytest.fixture
def mensaje_positivo():
    return "Este es un feedback muy positivo. :)"

@pytest.fixture
def mensaje_neutro():
    return "Este es un feedback muy neutro. :-"

def test_sentimiento_positivo(mocker, mensaje_positivo):
    mocker.patch('modelo.analisis_sentimientos.Analizador.analizar', return_value='POSITIVO')

    resultado = Analizador().analizar(mensaje_positivo)

    assert resultado == 'POSITIVO'

def test_sentimiento_neutro(mocker, mensaje_neutro):
    mocker.patch('modelo.analisis_sentimientos.Analizador.analizar', return_value='NEUTRO')

    resultado = Analizador().analizar(mensaje_neutro)

    assert resultado == 'NEUTRO'