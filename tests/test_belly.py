import pytest
from src.belly import Belly

def test_comer_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(0.5)
    assert belly.pepinos_comidos == 0.5

def test_comer_pepinos_negativos():
    belly = Belly()
    with pytest.raises(ValueError, match="La cantidad de pepinos no puede ser negativa."):
        belly.comer(-5)