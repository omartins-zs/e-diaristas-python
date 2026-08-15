from django import template

register = template.Library()


@register.filter
def cep(valor):
    """Formata um CEP de 8 digitos como 00000-000.

    Substitui o filtro homonimo do pacote easy-mask, cujo ultimo release
    foi em 2016 e que nao e mais compativel com as versoes atuais do Django.
    """
    digitos = ''.join(filter(str.isdigit, str(valor or '')))

    if len(digitos) != 8:
        return valor

    return f'{digitos[:5]}-{digitos[5:]}'


@register.filter
def cpf(valor):
    """Formata um CPF de 11 digitos como 000.000.000-00."""
    digitos = ''.join(filter(str.isdigit, str(valor or '')))

    if len(digitos) != 11:
        return valor

    return f'{digitos[:3]}.{digitos[3:6]}.{digitos[6:9]}-{digitos[9:]}'


@register.filter
def telefone(valor):
    """Formata um telefone de 10 ou 11 digitos como (00) 00000-0000."""
    digitos = ''.join(filter(str.isdigit, str(valor or '')))

    if len(digitos) == 11:
        return f'({digitos[:2]}) {digitos[2:7]}-{digitos[7:]}'

    if len(digitos) == 10:
        return f'({digitos[:2]}) {digitos[2:6]}-{digitos[6:]}'

    return valor
