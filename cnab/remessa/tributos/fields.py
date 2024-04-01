from cnab.core.abstract.abstract_remessa import AbstractFields


class TributoHeaderFields(AbstractFields):
    fields = [
        "codigo_banco",
        "lote_servico",
        "tipo_registro",
        "cnab_1",
        "tipo_operacao",
        "tipo_servico",
        "forma_lancamento",
        "layout_lote",
        "tipo_inscricao",
        "numero_inscricao",
        "codigo_convenio",
        "codigo_agencia",
        "agencia_dv",
        "numero_conta",
        "conta_dv",
        "dv_verificador",
        "nome_empresa",
        "mensagem",
        "endereco",
        "endereco_numero",
        "endereco_complemento",
        "endereco_cidade",
        "endereco_cep",
        "endereco_complemento_cep",
        "endereco_uf",
        "forma_pagamento",
        "cnab_2",
        "ocorrencias",
    ]
