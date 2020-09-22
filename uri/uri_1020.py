age = int(input())
years = age//365
age -= years*365
months = age//30
days = age - months*30
print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")