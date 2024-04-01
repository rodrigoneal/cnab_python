from cnab.core.abstract.abstract_remessa import AbstractRemessa
from cnab.core.common.dominio import TipoOperacao, TipoRegisto, TipoServico
from cnab.core.fields import AlphanumericoField, NumericoField


class HeaderLote(AbstractRemessa):
    cnab_1 = AlphanumericoField(padrao=" ", inicio=17, tamanho=1, nome_campo="cnab_1")
    cnab_2 = AlphanumericoField(padrao=" ", inicio=225, tamanho=6, nome_campo="cnab_2")

    def __init__(
        self,
        *,
        codigo_banco: str,
        lote_servico: str,
        forma_lancamento: str,
        tipo_inscricao: str,
        numero_inscricao: str,
        codigo_convenio: str,
        codigo_agencia: str,
        agencia_dv: str,
        numero_conta: str,
        conta_dv: str,
        dv_verificador: str,
        nome_empresa: str,
        mensagem: str,
        endereco: str,
        endereco_numero: str,
        endereco_complemento: str,
        endereco_cidade: str,
        endereco_cep: str,
        endereco_complemento_cep: str,
        endereco_uf: str,
        forma_pagamento: str,
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
            value=TipoServico.PAGAMENTO_CONTAS_TRIBUTOS_IMPOSTOS,
            tamanho=2,
            inicio=10,
            nome_campo="tipo_servico",
        )
        self.forma_lancamento = NumericoField(
            value=forma_lancamento, tamanho=2, inicio=12, nome_campo="forma_lancamento"
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
            value=codigo_agencia, inicio=53, tamanho=5, nome_campo="agencia"
        )
        self.agencia_dv = AlphanumericoField(
            value=agencia_dv, inicio=58, tamanho=1, nome_campo="agencia_dv"
        )
        self.numero_conta = NumericoField(
            value=numero_conta, inicio=59, tamanho=12, nome_campo="conta"
        )
        self.dv_conta = AlphanumericoField(
            value=conta_dv, inicio=71, tamanho=1, nome_campo="dv_conta"
        )

        self.dv_verificador = AlphanumericoField(
            value=dv_verificador, inicio=72, tamanho=1, nome_campo="dv_verificador"
        )
        self.nome_empresa = AlphanumericoField(
            value=nome_empresa, inicio=73, tamanho=30, nome_campo="nome_empresa"
        )
        self.mensagem = AlphanumericoField(
            value=mensagem, inicio=103, tamanho=40, nome_campo="mensagem"
        )
        self.endereco = AlphanumericoField(
            value=endereco, inicio=143, tamanho=30, nome_campo="endereco"
        )
        self.endereco_numero = NumericoField(
            value=endereco_numero, inicio=173, tamanho=5, nome_campo="endereco_numero"
        )
        self.endereco_complemento = AlphanumericoField(
            value=endereco_complemento,
            inicio=178,
            tamanho=15,
            nome_campo="endereco_complemento",
        )
        self.endereco_cidade = AlphanumericoField(
            value=endereco_cidade, inicio=192, tamanho=20, nome_campo="endereco_cidade"
        )
        self.endereco_cep = NumericoField(
            value=endereco_cep, inicio=213, tamanho=5, nome_campo="endereco_cep"
        )
        self.endereco_complemento_cep = AlphanumericoField(
            value=endereco_complemento_cep,
            inicio=218,
            tamanho=3,
            nome_campo="endereco_complemento_cep",
        )
        self.endereco_uf = AlphanumericoField(
            value=endereco_uf, inicio=221, tamanho=2, nome_campo="endereco_uf"
        )
        self.forma_pagamento = NumericoField(
            value=forma_pagamento, inicio=223, tamanho=2, nome_campo="forma_pagamento"
        )
        self.ocorrencias = AlphanumericoField(
            inicio=231, tamanho=10, nome_campo="ocorrencias"
        )


class TrailerLote(AbstractRemessa):
    cnab_1 = AlphanumericoField(value=" ", inicio=9, tamanho=9, nome_campo="cnab_1")

    def __init__(
        self,
        *,
        codigo_banco: str,
        lote_servico: str,
        qtd_registros: str,
        valor_total: str,
    ):
        self.codigo_banco = NumericoField(
            value=codigo_banco, nome_campo="codigo_banco", tamanho=3, inicio=1
        )
        self.lote_servico = NumericoField(
            nome_campo="lote_servico", value=lote_servico, inicio=4, tamanho=4
        )
        self.registro = NumericoField(
            value=TipoRegisto.TRAILER_LOTE, inicio=8, tamanho=1, nome_campo="registro"
        )
        self.qtd_registros = NumericoField(
            value=qtd_registros, inicio=18, tamanho=6, nome_campo="qtd_registros"
        )
        self.valor_total = NumericoField(
            value=valor_total,
            inicio=24,
            tamanho=6,
            nome_campo="valor_total",
            num_decimal=2,
        )
        self.complemento_registro = AlphanumericoField(
            value=" ", inicio=42, tamanho=189, nome_campo="complemento_registro"
        )
        self.ocorrencias = AlphanumericoField(
            value=" ", inicio=231, tamanho=10, nome_campo="ocorrencias"
        )
