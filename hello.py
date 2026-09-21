#!/usr/bin/env python3

"""Hello Word multilinguas

Programa exibe mensagem de acordo com a lingua configurada no ENV.

Como usar:

Tenha a variavel de ambiente LANG devidamente configurada. Ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Ana"
__license__ = "Unlicense"

import os


msg = "Hello, World!"
current_language = os.getenv("LANG", "en_US")[:5]

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"


print (msg)



