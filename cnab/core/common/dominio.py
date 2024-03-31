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

class TipoOperacao:
    LANCAMENTO_CREDITO = "C"
    LANCAMENTO_DEBITO = "D"
    EXTRATO_CONCILIACAO = "E"
    EXTRATO_GESTAO_CAIXA = "G"
    INFORMACOES_TITULOS = "I"
    ARQUIVO_REMESSA = "R"
    ARQUIVO_RETORNO = "T"

class FormaPagamento:
    CONTA_CORRENTE = "01"
    EMPRESTIMO = "02"
    CAETAO_CREDITO = "03"