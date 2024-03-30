from cnab.core.common.dominio import TipoRegisto
from cnab.core.fields import AlphanumericoField, NumericoField


class HeaderLotePagamento:
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
