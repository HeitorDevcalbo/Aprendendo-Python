dias = float(input('Digite por quantos dias o carro foi alugado: '))
km = float(input('Digite quantos quilometros você rodou: '))
precodias= 60 * dias
precokm = 0.15 * km
total = precokm + precodias
print(f'você alugou o carro por {dias} dias, rodou {km} quilometros e deverá pagar {total} reais!!!')