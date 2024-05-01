"""
David solicitó un crédito a 30 años para comprar una vivienda, con
una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó
un pago mensual fijo de $2684,11.

Supongamos que David adelanta pagos extra de $1000/mes
durante los primeros 12 meses de la hipoteca.

Modificá el programa para incorporar estos pagos extra y que
imprima el monto total pagado junto con la cantidad de meses
requeridos.

¿Cuánto pagaría David si agrega $1000 por mes durante cuatro
años, comenzando en el sexto año de la hipoteca (es decir,
luego de 5 años)?

Modificá tu programa de forma que la información sobre pagos
extras sea incorporada de manera versátil.

Ya que estamos, corregí el código anterior de forma que el pago
del último mes se ajuste a lo adeudado.
"""

saldo = 500000
tasa = 0.05
pagoMensual = 2684.11
totalPagado = 0
adelanto = 1000
mesAdelantoInicio = 61
mesAdelantoFin = 108
meses = 0

while saldo > 0:
    meses += 1
    if meses >= mesAdelantoInicio and meses <= mesAdelantoFin :
        saldo = saldo * (1 + tasa / 12) - (pagoMensual + adelanto)
        totalPagado += pagoMensual + adelanto
    elif saldo <= pagoMensual:
        totalPagado += saldo
        saldo -= saldo
    else:
        saldo = saldo * (1 + tasa / 12) - pagoMensual
        totalPagado += pagoMensual
    print(f'{meses}\t{totalPagado:10.2f}\t{saldo:10.2f}')

print('Total pagado',round(totalPagado,2),'Meses',meses)