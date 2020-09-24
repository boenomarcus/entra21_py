# Captura categorias
cat01, cat02, cat03 = input(), input(), input()

# Chave classificacao na forma de dicionario
animais = {
    "vertebrado":{
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado":{
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
    }
}

# Apresentando resultados
print(animais[cat01][cat02][cat03])