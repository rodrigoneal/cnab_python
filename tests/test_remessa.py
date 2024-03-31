import pytest

from cnab.remessa.arquivo_base import RemessaBase, TrailerRemessaBase


@pytest.fixture
def valores():
    return {
        "codigo_banco": "001",
        "tipo_inscricao": "1",
        "numero_inscricao": "12345678901234",
        "codigo_convenio": "12345678901234567890",
        "codigo_agencia": "12345",
        "dv_agencia": "X",
        "numero_conta": "1234567890",
        "dv_conta": "X",
        "dv_verificador": "X",
        "nome_empresa": "Teste",
        "nome_banco": "Banco Teste",
    }


@pytest.fixture
def remessa(valores):
    return RemessaBase(**valores)


def test_se_ajeitar_o_campo_automaticamente_com_valor_numerico_correto(valores):
    valores["codigo_banco"] = "1"
    remessa = RemessaBase(**valores)
    assert remessa.codigo_banco.value == "001"


def test_se_ajeitar_o_campo_automaticamente_com_valor_alpanumerico_correto(valores):
    valores["nome_banco"] = "Banco Teste"
    remessa = RemessaBase(**valores)
    assert remessa.nome_banco.value == "BANCO TESTE                   "


def test_remessa_base(remessa):
    assert len(remessa.texto()) == 240

def test_se_remessa_comecao_com_banco_correto(remessa):
    assert remessa.texto()[0:3] == "001"

def test_remessa_base_trailer():
    trailer = TrailerRemessaBase(codigo_banco="001", quantidade_lotes="1")
    assert len(str(trailer)) == 240

