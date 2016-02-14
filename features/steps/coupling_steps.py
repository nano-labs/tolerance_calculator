# -*- encoding: utf-8 -*-
u"""Steps para checar as tolerâncias."""

from behave import given, then
from ensure import ensure
from tolerancias import calculator

@given(u'I have {coupling} coupling')
def coupling_calculation(context, coupling):
    u"""Calcula os valores de tolerância do encaixe."""
    setattr(context, "results", calculator(coupling))

@then(u'diameter should be {diameter} milimiter')
def check_diameter(context, diameter):
    u"""Checa se o diametro encontrado está correto."""
    diameter = float(diameter)
    return ensure(context.results["diameter"]).equals(diameter)

@then(u'{elemento}\'s {limite} deviation should be {afastamento} micrometer')
def afastamentos(context, elemento, limite, afastamento):
    """Verifica os afastamentos do acoplamento."""
    afastamento = float(afastamento)
    valor = context.results[elemento][limite]
    return ensure(valor).equals(afastamento)

@then(u'{limite} clearance should be {folga} micrometer')
def ajustes(context, limite, folga):
    """Verifica os ajustes do acoplamento."""
    folga = float(folga)
    valor = context.results["clearance"][limite]
    return ensure(valor).equals(folga)