from typing import Callable, Optional

from cnab.exceptions_custom.fields_exceptions import IsnotValidFieldException


class BaseField:
    def __init__(
        self,
        tamanho: int,
        inicio: int,
        nome_campo: str,
        value: Optional[str] = None,
        padrao: Optional[str] = None,
        strict: bool = False,
        funcao: Optional[Callable] = None,
    ):
        if funcao:
            value = funcao()
        self.value = value
        self.padrao = padrao
        self.tamanho = tamanho
        self.inicio = inicio
        self.fim = inicio + (tamanho - 1)
        self.strict = strict
        self.subclass_name = self.__class__.__name__
        self.nome_campo = nome_campo
        self.fill_field()
        self.check_field()

    def __check_numerico(self, valor):
        if not valor.isdigit():
            raise IsnotValidFieldException(
                message=f"O valor {self.value} não é um valor numérico válido"
            )
        if not len(self.value) == self.tamanho:
            raise IsnotValidFieldException(
                message=f"O campo {self.nome_campo} deve ter {self.tamanho} dígitos, mas foi dado {len(self.value)}"
            )

    def check_field(self):
        valor = self.value or self.padrao
        if not valor:
            raise IsnotValidFieldException(
                message=f"É Necessário informar um valor para o campo {self.nome_campo}"
            )
        if self.subclass_name == "NumericoField":
            self.__check_numerico(valor)
        elif self.subclass_name == "AlpanumericoField":
            if not len(valor) == self.tamanho:
                raise IsnotValidFieldException(
                    message=f"O valor {valor} deve ter {self.tamanho} caracteres para o campo {self.nome_campo}"
                )

    def fill_field(self):
        valor = self.value or self.padrao
        if len(valor) < self.tamanho:
            if self.subclass_name == "NumericoField":
                self.value = valor.zfill(self.tamanho)
            elif self.subclass_name == "AlpanumericoField":
                self.value = valor.ljust(self.tamanho)
        else:
            self.value = valor


class NumericoField(BaseField):
    def __init__(
        self,
        tamanho: int,
        inicio: int,
        nome_campo: str,
        value: Optional[str] = None,
        padrao: Optional[str] = None,
        num_decimal: int = 0,
        strict: bool = False,
        funcao: Optional[Callable] = None,
    ):
        self.num_decimal = num_decimal
        super().__init__(
            value=value,
            tamanho=tamanho,
            inicio=inicio,
            padrao=padrao,
            strict=strict,
            funcao=funcao,
            nome_campo=nome_campo,
        )


class AlpanumericoField(BaseField):
    def __init__(
        self,
        tamanho: int,
        inicio: int,
        nome_campo: str,
        padrao: Optional[str] = None,
        value: Optional[str] = None,
        strict: bool = False,
        funcao: Optional[Callable] = None,
    ):
        self.value = value
        self.padrao = padrao
        self.tamanho = tamanho
        self.inicio = inicio
        self.strict = strict

        super().__init__(
            value=value,
            tamanho=tamanho,
            inicio=inicio,
            padrao=padrao,
            strict=strict,
            funcao=funcao,
            nome_campo=nome_campo,
        )
