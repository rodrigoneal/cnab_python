from cnab.remessa.base import RemessaBase


def test_remessa_base():
    remessa = RemessaBase(
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,


    )
    assert len(str(remessa)) == 240
