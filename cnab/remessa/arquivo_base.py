from datetime import datetime

from cnab.core.common.dominio import TipoRegisto
from cnab.core.fields import AlphanumericoField, NumericoField


class HeaderArquivo:
    fields = [
        "codigo_banco",
        "lote_servico",
        "tipo_registro",
        "cnab_1",
        "tipo_inscricao",
        "numero_inscricao",
        "codigo_convenio",
        "codigo_agencia",
        "dv_agencia",
        "numero_conta",
        "dv_conta",
        "dv_verificador",
        "nome_empresa",
        "nome_banco",
        "cnab_2",
        "codigo_arquivo",
        "data_geracao",
        "hora_geracao",
        "numero_sequencial",
        "layout_arquivo",
        "densidade_arquivo",
        "cnab_3",
        "cnab_4",
        "cnab_5",
    ]


class TrailerArquivo:
    fields = [
        "codigo_banco",
        "lote_servico",
        "tipo_registro",
        "cnab_1",
        "quantidade_lotes",
        "quantidade_registros",
        "quantidade_contas",
        "cnab_2",
    ]


class RemessaBase:
    cnab_1 = AlphanumericoField(nome_campo="cnab_1", padrao=" ", tamanho=9, inicio=9)
    cnab_2 = AlphanumericoField(nome_campo="cnab_2", padrao=" ", tamanho=10, inicio=133)
    cnab_3 = AlphanumericoField(nome_campo="cnab_4", padrao=" ", tamanho=20, inicio=172)
    cnab_4 = AlphanumericoField(nome_campo="cnab_5", padrao=" ", tamanho=20, inicio=192)
    cnab_5 = AlphanumericoField(nome_campo="cnab_6", padrao=" ", tamanho=29, inicio=212)

    def __init__(
        self,
        *,
        codigo_banco: str,
        tipo_inscricao: str,
        numero_inscricao: str,
        codigo_convenio: str,
        codigo_agencia: str,
        dv_agencia: str,
        numero_conta: str,
        dv_conta: str,
        dv_verificador: str,
        nome_empresa: str,
        nome_banco: str,
        layout_arquivo: str = "103",
    ):
        self.codigo_banco = NumericoField(
            value=codigo_banco, nome_campo="codigo_banco", tamanho=3, inicio=1
        )
        self.lote_servico = NumericoField(
            nome_campo="lote_servico", value="0000", inicio=4, tamanho=4
        )
        self.tipo_registro = NumericoField(
            value=TipoRegisto.HEADER_ARQUIVO,
            inicio=8,
            tamanho=1,
            nome_campo="tipo_registro",
        )
        self.tipo_inscricao = NumericoField(
            value=tipo_inscricao,
            inicio=18,
            tamanho=1,
            nome_campo="tipo_inscricao",
        )
        self.numero_inscricao = NumericoField(
            value=numero_inscricao,
            inicio=19,
            tamanho=14,
            nome_campo="numero_inscricao",
        )
        self.codigo_convenio = AlphanumericoField(
            value=codigo_convenio,
            inicio=33,
            tamanho=20,
            nome_campo="codigo_convenio",
        )
        self.codigo_agencia = NumericoField(
            value=codigo_agencia,
            inicio=53,
            tamanho=5,
            nome_campo="codigo_agencia",
        )
        self.dv_agencia = AlphanumericoField(
            value=dv_agencia,
            inicio=58,
            tamanho=1,
            nome_campo="dv_agencia",
        )
        self.numero_conta = NumericoField(
            value=numero_conta,
            inicio=59,
            tamanho=12,
            nome_campo="numero_conta",
        )
        self.dv_conta = AlphanumericoField(
            value=dv_conta, inicio=71, tamanho=1, nome_campo="dv_conta"
        )
        self.dv_verificador = AlphanumericoField(
            value=dv_verificador,
            inicio=72,
            tamanho=1,
            nome_campo="dv_verificador",
        )
        self.nome_empresa = AlphanumericoField(
            value=nome_empresa,
            inicio=73,
            tamanho=30,
            nome_campo="nome_empresa",
        )
        self.nome_banco = AlphanumericoField(
            value=nome_banco,
            inicio=103,
            tamanho=30,
            nome_campo="nome_banco",
        )
        self.codigo_arquivo = NumericoField(
            padrao="1",
            inicio=143,
            tamanho=1,
            nome_campo="codigo_arquivo",
        )
        self.data_geracao = NumericoField(
            funcao=lambda: datetime.now().strftime("%d%m%Y"),
            inicio=144,
            tamanho=8,
            nome_campo="data_geracao",
        )
        self.hora_geracao = NumericoField(
            funcao=lambda: datetime.now().strftime("%H%M%S"),
            inicio=152,
            tamanho=6,
            nome_campo="hora_geracao",
        )
        self.numero_sequencial = NumericoField(
            padrao="0", inicio=158, tamanho=6, nome_campo="numero_sequencial"
        )
        self.layout_arquivo = NumericoField(
            value=layout_arquivo,
            padrao="103",
            inicio=164,
            tamanho=3,
            nome_campo="layout_arquivo",
        )
        self.densidade_arquivo = NumericoField(
            padrao="00000", inicio=167, tamanho=5, nome_campo="densidade_arquivo"
        )

    def __str__(self):
        valor = ""
        for field in HeaderArquivo.fields:
            valor += getattr(self, field).value
        return valor


class TrailerRemessaBase:
    cnab_1 = AlphanumericoField(padrao=" ", inicio=9, tamanho=9, nome_campo="cnab_1")
    cnab_2 = AlphanumericoField(padrao=" ", inicio=36, tamanho=205, nome_campo="cnab_2")

    def __init__(self, *, codigo_banco: str, quantidade_lotes: str) -> None:
        self.codigo_banco = NumericoField(
            value=codigo_banco,
            nome_campo="codigo_banco",
            tamanho=3,
            inicio=1,
        )

        self.lote_servico = NumericoField(
            padrao="9999",
            nome_campo="lote_servico",
            tamanho=4,
            inicio=4,
        )
        self.tipo_registro = NumericoField(
            value=TipoRegisto.TRAILER_ARQUIVO,
            inicio=8,
            tamanho=1,
            nome_campo="tipo_registro",
        )
        self.quantidade_lotes = NumericoField(
            value=quantidade_lotes, inicio=18, tamanho=6, nome_campo="quantidade_lotes"
        )
        self.quantidade_registros = NumericoField(
            padrao="0", inicio=24, tamanho=6, nome_campo="quantidade_registros"
        )
        self.quantidade_contas = NumericoField(
            padrao="0", inicio=30, tamanho=6, nome_campo="quantidade_contas"
        )

    def __str__(self):
        valor = ""
        for field in TrailerArquivo.fields:
            valor += getattr(self, field).value
        return valor
