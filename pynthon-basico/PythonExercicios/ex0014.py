# converter ºC para fahrenheit

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32

# ºF = (1ºF − 32) × 5/9 = -17.22°C
# °C = (1°C × 9/5) + 32 = 92.84°F

print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
