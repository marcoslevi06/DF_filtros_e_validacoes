''' 
    Os campos de validação partem da condição verdadeira. Ou seja, True.
    Assim, eu defino a função no validator.py com a CONDIÇÃO QUE CONSIDERO CORRETA a ser preenchida.

    Quando chamamos as funções de validação na serialização, temos que:

        Se a condição da função chamada não for verdadeira, mostre o seguinte erro.
            A lógica da frase acima se deve a sintaxe IF NOT. Assim, tendo a função no arquivo
            validator.py como TRUE, ao se chamar a função no Serializer, para que caia na verificação
            de erro, é necessário usar o IF NOT, invertendo o valor boleano da função.

            Desse modo, tem-se quê:

                def valitador(self, data):
                    if not validate_cpf(): # ou seja, SE O CAMPO DE CPF NÃO FOR VÁLIDO, mostre a mensagem em raise
                        raise serializer.ValidateError ('Digite seu erro aqui.')
'''

import re
from validate_docbr import CPF


def validate_cpf(cpf):
    cpf = CPF()
    return cpf.validate(cpf)


def validate_nome(nome):
    return nome.isalpha()


def validate_rg(rg):
    return len(rg) == 9


def validate_celular(celular):
    """Verifica se o  celular é valido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
