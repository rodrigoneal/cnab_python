from cnab.core.common.dominio import Banco
from cnab.remessa.arquivo_base import RemessaBase


class Bradesco(RemessaBase):
    def __init__(
        self,
        tipo_inscricao: str,
        numero_inscricao: str,
        codigo_convenio: str,
        codigo_agencia: str,
        dv_agencia: str,
        numero_conta: str,
        dv_conta: str,
        dv_verificador: str,
        nome_empresa: str,
    ):
        super().__init__(
            codigo_banco=Banco.BRADESCO,
            tipo_inscricao=tipo_inscricao,
            numero_inscricao=numero_inscricao,
            codigo_convenio=codigo_convenio,
            codigo_agencia=codigo_agencia,
            dv_agencia=dv_agencia,
            numero_conta=numero_conta,
            dv_conta=dv_conta,
            dv_verificador=dv_verificador,
            nome_empresa=nome_empresa,
            nome_banco="BANCO BRADESCO S.A.",
        )


class Itau(RemessaBase):
    def __init__(
        self,
        tipo_inscricao: str,
        numero_inscricao: str,
        codigo_convenio: str,
        codigo_agencia: str,
        dv_agencia: str,
        numero_conta: str,
        dv_conta: str,
        dv_verificador: str,
        nome_empresa: str,
    ):
        super().__init__(
            codigo_banco=Banco.ITAU,
            tipo_inscricao=tipo_inscricao,
            numero_inscricao=numero_inscricao,
            codigo_convenio=codigo_convenio,
            codigo_agencia=codigo_agencia,
            dv_agencia=dv_agencia,
            numero_conta=numero_conta,
            dv_conta=dv_conta,
            dv_verificador=dv_verificador,
            nome_empresa=nome_empresa,
            nome_banco="BANCO ITAU SA",
        )
