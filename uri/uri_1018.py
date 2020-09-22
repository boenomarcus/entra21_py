bills = [100, 50, 20, 10, 5, 2, 1,]
valid_input = False

while valid_input is False:
    cash = int(input())
    if 0 < cash < 1000000:
        valid_input = True

print(cash)
for bill in bills:
    n_bills = cash//bill
    print(f"{n_bills} nota(s) de R$ {bill},00")
    cash -= n_bills*bill