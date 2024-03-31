def test_se_o_banco_itau_emite_o_arquivo_correto():
    from cnab.bancos import Itau

    remessa = Itau(
        tipo_inscricao="2",
        numero_inscricao="12345678901",
        codigo_convenio="123456",
        codigo_agencia="1234",
        dv_agencia="5",
        numero_conta="123456",
        dv_conta="6",
        dv_verificador="7",
        nome_empresa="Teste",
    )
    assert len(remessa.texto()) == 240


def test_se_o_banco_bradesco_emite_o_arquivo_correto():
    from cnab.bancos import Bradesco

    remessa = Bradesco(
        tipo_inscricao="2",
        numero_inscricao="12345678901",
        codigo_convenio="123456",
        codigo_agencia="1234",
        dv_agencia="5",
        numero_conta="123456",
        dv_conta="6",
        dv_verificador="7",
        nome_empresa="Teste",
    )
    assert len(remessa.texto()) == 240
