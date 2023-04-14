from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        # Se o CPF não for válido, exiba o seguinte erro.
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': "Número de CPF inválido"})
        # Se o NOME não for válido, exiba o seguinte erro.
        if not validate_nome(data['nome']):
            raise serializers.ValidationError(
                {'nome': "Não inclua números neste campo"})
        # Se o RG não for válido, exiba o seguinte erro.
        if not validate_rg(data['rg']):
            raise serializers.ValidationError(
                {'rg': "O RG deve ter 9 dígitos"})
        # Se o CELULAR não for válido, exiba o seguinte erro.
        if not validate_celular(data['celular']):
            raise serializers.ValidationError(
                {'celular': "O número de celular deve ser informado no seguinte formato: 00 91234-5678"})
        return data
