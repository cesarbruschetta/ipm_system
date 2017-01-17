# -*- coding: utf-8 -*-

from django.conf import settings
from loremipsum import generate_paragraph
from keyczar.keyczar import Crypter


def gera_license():

    _, _, paragraph = generate_paragraph()

    crypter = Crypter.Read(settings.ENCRYPTED_FIELDS_KEYDIR)
    ciphertext = crypter.Encrypt(paragraph)

    return ciphertext
