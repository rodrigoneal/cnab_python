from datetime import datetime
import pytest
from cnab.core.fields import AlpanumericoField, NumericoField
from cnab.exceptions_custom.fields_exceptions import IsnotValidFieldException


def test_se_passar_um_valor_numerico_valido_para_um_campo():
    field = NumericoField(nome_campo="numero", value="123456789", tamanho=9, inicio=9)
    assert field


def test_se_passar_um_valor_numerico_invalido_para_um_campo():
    with pytest.raises(IsnotValidFieldException):
        NumericoField(nome_campo="numero", value="abc", tamanho=9, inicio=9)


def test_se_preencher_o_campo_automaticamente_com_valor_numerico_correto():
    field = NumericoField(nome_campo="numero", value="1", tamanho=9, inicio=9)
    assert field.value == "000000001"
    assert len(field.value) == 9


def test_se_preencher_o_campo_com_valor_alpanumerico_correto():
    field = AlpanumericoField(nome_campo="numero", value="abc", tamanho=9, inicio=9)
    assert field.value == "abc      "
    assert len(field.value) == 9


def test_se_chamar_funcao_para_preencher_o_campo_automaticamente_com_valor_numerico_correto():
    field = NumericoField(
        nome_campo="numero",
        tamanho=6,
        inicio=9,
        strict=True,
        funcao=lambda: datetime.now().strftime("%H%M%S"),
    )
    agora = datetime.now().strftime("%H%M%S")
    assert field.value == agora
