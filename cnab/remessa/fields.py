from cnab.core.abstract.abstract_remessa import AbstractFields


class HeaderArquivoFields(AbstractFields):
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


class TrailerArquivoFields(AbstractFields):
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
