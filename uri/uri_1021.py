bills = [100, 50, 20, 10, 5, 2,]
coins = [1, 0.5, 0.25, 0.1, 0.05, 0.01,]
valid_input = False

while valid_input is False:
    cash = float(input())
    if 0 <= cash <= 1000000.00:
        cash += 0.001
        valid_input = True

print("NOTAS:")
for bill in bills:
    n_bills = int(cash//bill)
    print(f"{n_bills} nota(s) de R$ {bill:.2f}")
    cash -= n_bills*bill

print("MOEDAS:")
for coin in coins:
    n_coins = int(cash//coin)
    print(f"{n_coins} moeda(s) de R$ {coin:.2f}")
    cash -= n_coins*coin