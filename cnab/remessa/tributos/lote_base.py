from cnab.core.common.dominio import TipoOperacao, TipoRegisto
from cnab.core.fields import AlphanumericoField, NumericoField


class HeaderLote:
    cnab_1 = AlphanumericoField(padrao=" ", inicio=17, tamanho=1, nome_campo="cnab_1")
    cnab_2 = AlphanumericoField(padrao=" ", inicio=225, tamanho=6, nome_campo="cnab_2")

    def __init__(
        self,
        *,
        codigo_banco: str,
        lote_servico: str,
        tipo_inscricao: str,
        numero_inscricao: str,
        codigo_convenio: str,
    ):
        self.codigo_banco = NumericoField(
            value=codigo_banco, nome_campo="codigo_banco", tamanho=3, inicio=1
        )
        self.lote_servico = NumericoField(
            value=lote_servico, nome_campo="lote_servico", inicio=4, tamanho=4
        )
        self.tipo_registro = NumericoField(
            value=TipoRegisto.HEADER_LOTE,
            inicio=8,
            tamanho=1,
            nome_campo="tipo_registro",
        )
        self.tipo_operacao = AlphanumericoField(
            value=TipoOperacao.LANCAMENTO_CREDITO,
            inicio=9,
            tamanho=1,
            nome_campo="tipo_operacao",
        )
        self.tipo_servico = NumericoField(
            tamanho=2, inicio=10, nome_campo="tipo_servico"
        )
        self.forma_lancamento = NumericoField(
            tamanho=2, inicio=12, nome_campo="forma_lancamento"
        )
        self.layout_lote = NumericoField(
            tamanho=3, inicio=14, nome_campo="layout_lote", padrao="012"
        )
        self.tipo_inscricao = NumericoField(
            value=tipo_inscricao, inicio=18, tamanho=1, nome_campo="tipo_inscricao"
        )
        self.numero_inscricao = NumericoField(
            value=numero_inscricao, inicio=19, tamanho=14, nome_campo="numero_inscricao"
        )
        self.codigo_convenio = AlphanumericoField(
            value=codigo_convenio,
            inicio=33,
            tamanho=20,
            nome_campo="codigo_convenio",
        )
        self.codigo_agencia = AlphanumericoField(
            inicio=53, tamanho=5, nome_campo="agencia"
        )
        self.agencia_dv = AlphanumericoField(
            inicio=58, tamanho=1, nome_campo="agencia_dv"
        )
        self.numero_conta = NumericoField(inicio=59, tamanho=12, nome_campo="conta")
        self.dv_conta = AlphanumericoField(inicio=71, tamanho=1, nome_campo="dv_conta")

        self.dv_verificador = AlphanumericoField(
            inicio=72, tamanho=1, nome_campo="dv_verificador"
        )
        self.nome_empresa = AlphanumericoField(
            inicio=73, tamanho=30, nome_campo="nome_empresa"
        )
        self.mensagem = AlphanumericoField(
            inicio=103, tamanho=40, nome_campo="mensagem"
        )
        self.endereco = AlphanumericoField(
            inicio=143, tamanho=30, nome_campo="endereco"
        )
        self.endereco_numero = NumericoField(
            inicio=173, tamanho=5, nome_campo="endereco_numero"
        )
        self.endereco_complemento = AlphanumericoField(
            inicio=178, tamanho=15, nome_campo="endereco_complemento"
        )
        self.endereco_cidade = AlphanumericoField(
            inicio=192, tamanho=20, nome_campo="endereco_cidade"
        )
        self.endereco_cep = NumericoField(
            inicio=213, tamanho=5, nome_campo="endereco_cep"
        )
        self.endereco_complemento_cep = AlphanumericoField(
            inicio=218, tamanho=3, nome_campo="endereco_complemento_cep"
        )
        self.endereco_uf = AlphanumericoField(
            inicio=221, tamanho=2, nome_campo="endereco_uf"
        )
        self.forma_pagamento = NumericoField(
            inicio=223, tamanho=2, nome_campo="forma_pagamento"
        )
        self.ocorrencias = AlphanumericoField(
            inicio=231, tamanho=10, nome_campo="ocorrencias"
        )
