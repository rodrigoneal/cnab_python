class TipoRegisto:
    HEADER_ARQUIVO = "0"
    HEADER_LOTE = "1"
    REGISTROS_INICIAIS_LOTE = "2"
    DETALHE = "3"
    REGISTROS_FINAIS_LOTE = "4"
    TRAILER_LOTE = "5"
    TRAILER_ARQUIVO = "9"

class Banco:
    ITAU = "341"
    BRADESCO = "237"
    BANCO_BRASIL = "001"
    SANTANDER = "033"
    CAIXA = "104"

class TipoInscricao:
    ISENTO = "0"
    CPF = "1"
    CNPJ = "2"
    PIS = "3"
    OUTROS = "9"