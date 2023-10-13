import pytest
from modelo.analisis_sentimientos import Analizador

@pytest.fixture
def mensaje_positivo():
    return "Este es un feedback muy positivo. :)"

@pytest.fixture
def mensaje_neutro():
    return "Este es un feedback muy neutro. :-"

@pytest.fixture
def mensaje_negativo():
    return "Este es un feedback muy negativo. :("

def test_sentimiento_positivo(mocker, mensaje_positivo):
    mocker.patch('modelo.analisis_sentimientos.Analizador.analizar', return_value='POSITIVO')

    resultado = Analizador().analizar(mensaje_positivo)

    assert resultado == 'POSITIVO'

def test_sentimiento_neutro(mocker, mensaje_neutro):
    mocker.patch('modelo.analisis_sentimientos.Analizador.analizar', return_value='NEUTRO')

    resultado = Analizador().analizar(mensaje_neutro)

    assert resultado == 'NEUTRO'

def test_sentimiento_negativo(mocker, mensaje_negativo):
    mocker.patch('modelo.analisis_sentimientos.Analizador.analizar', return_value='NEGATIVO')

    resultado = Analizador().analizar(mensaje_negativo)

    assert resultado == 'NEGATIVO'

"""

✈️ Thanks @XYZAirlines for the ultra-comfy flight! Your service made me feel right at home in the skies. 🌟 #FlyingInComfort #XYZAirlines

🤔 Hey @XYZAirlines, how can I change my reservation? I need a little help, please! 🙏 #ReservationAssistance #XYZAirlines

😡 Disappointed with @XYZAirlines today – my flight was seriously delayed. Time is precious, and punctuality matters! ⏰ #LateFlight #XYZAirlines

"""