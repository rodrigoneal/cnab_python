from datetime import datetime
from cnab.core.fields import AlpanumericoField, NumericoField
from cnab.core.types.field_types import TypesField, DictField


def criar_parametros(valor: TypesField) -> DictField:
    if isinstance(valor, dict):
        if hasattr(valor, "strict"):
            return valor

        valor["strict"] = False
        return valor
    else:
        return {"value": str(valor), "strict": False}

class HeaderArquivo:
    fields = ["codigo_banco", "lote_servico", "tipo_registro","cnab_1", "tipo_inscricao", "numero_inscricao","codigo_convenio", "codigo_agencia", "dv_agencia", "numero_conta", "dv_conta", "dv_verificador", "nome_empresa","nome_banco","cnab_2", "codigo_arquivo", "data_geracao", "hora_geracao", "numero_sequencial", "layout_arquivo", "densidade_arquivo", "cnab_3", "cnab_4", "cnab_5"]

class RemessaBase:
    cnab_1 = AlpanumericoField(nome_campo="cnab_1", padrao=" ", tamanho=9, inicio=9)
    cnab_2 = AlpanumericoField(nome_campo="cnab_2", padrao=" ", tamanho=10, inicio=133)
    cnab_3 = AlpanumericoField(nome_campo="cnab_4", padrao=" ", tamanho=20, inicio=172)
    cnab_4 = AlpanumericoField(nome_campo="cnab_5", padrao=" ", tamanho=20, inicio=192)
    cnab_5 = AlpanumericoField(nome_campo="cnab_6", padrao=" ", tamanho=29, inicio=212)

    def __init__(
        self,
        codigo_banco: TypesField,
        tipo_inscricao: TypesField,
        numero_inscricao: TypesField,
        codigo_convenio: TypesField,
        codigo_agencia: TypesField,
        dv_agencia: TypesField,
        numero_conta: TypesField,
        dv_conta: TypesField,
        dv_verificador: TypesField,
        nome_empresa: TypesField,
        nome_banco: TypesField,
    ):
        self.codigo_banco = NumericoField(
            **criar_parametros(codigo_banco),
            nome_campo="codigo_banco",
            tamanho=3,
            inicio=1,
        )
        self.lote_servico = NumericoField(
            nome_campo="lote_servico", value="0000", inicio=4, tamanho=4
        )
        self.tipo_registro = NumericoField(
            value="0", inicio=8, tamanho=1, nome_campo="tipo_registro"
        )
        self.tipo_inscricao = NumericoField(
            **criar_parametros(tipo_inscricao),
            inicio=18,
            tamanho=1,
            nome_campo="tipo_inscricao",
        )
        self.numero_inscricao = NumericoField(
            **criar_parametros(numero_inscricao),
            inicio=19,
            tamanho=14,
            nome_campo="numero_inscricao",
        )
        self.codigo_convenio = AlpanumericoField(
            **criar_parametros(codigo_convenio),
            inicio=33,
            tamanho=20,
            nome_campo="codigo_convenio",
        )
        self.codigo_agencia = NumericoField(
            **criar_parametros(codigo_agencia),
            inicio=53,
            tamanho=5,
            nome_campo="codigo_agencia",
        )
        self.dv_agencia = AlpanumericoField(
            **criar_parametros(dv_agencia),
            inicio=58,
            tamanho=1,
            nome_campo="dv_agencia",
        )
        self.numero_conta = NumericoField(
            **criar_parametros(numero_conta),
            inicio=59,
            tamanho=12,
            nome_campo="numero_conta",
        )
        self.dv_conta = AlpanumericoField(
            **criar_parametros(dv_conta), inicio=71, tamanho=1, nome_campo="dv_conta"
        )
        self.dv_verificador = AlpanumericoField(
            **criar_parametros(dv_verificador),
            inicio=72,
            tamanho=1,
            nome_campo="dv_verificador",
        )
        self.nome_empresa = AlpanumericoField(
            **criar_parametros(nome_empresa),
            inicio=73,
            tamanho=30,
            nome_campo="nome_empresa",
        )
        self.nome_banco = AlpanumericoField(
            **criar_parametros(nome_banco),
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
            padrao="103", inicio=164, tamanho=3, nome_campo="layout_arquivo"
        )
        self.densidade_arquivo = NumericoField(
            padrao="00000", inicio=167, tamanho=5, nome_campo="densidade_arquivo"
        )

    def __str__(self):
        valor = ""
        for field in HeaderArquivo.fields:
            valor += getattr(self, field).value
        return valor
