from abc import ABC


class AbstractFields(ABC):
    fields: list

    def __iter__(self):
        for field in self.fields:
            yield field

    def __len__(self):
        return len(self.fields)

    def __getitem__(self, item):
        return self.fields[item]


class AbstractRemessa(ABC):
    fields: AbstractFields

    def texto(self):
        campos = ""
        for field in self.fields:
            campos += getattr(self, field).value
        return campos

    def __str__(self):
        return self.texto()
