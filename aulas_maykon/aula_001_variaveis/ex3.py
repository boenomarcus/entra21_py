#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

# Declarando variaveis
livro = {
    "title": "Permanent Record",
    "edition": "First Edition",
    "author": "Edward Snowden",
    "date": "2019"
}

livro["sample"] = """
    When you go online at the CIA, you have to check a box for a
Consent to Monitoring Agreement, which basically says that ev-
erything you do is being recorded an that you agree that you
have no expectation of any privacy whatsoever. You end up check-
ing this box so often that it becomes second nature. These agree-
ments become invisible to you when you're working at the agency,
because they pop up constantly and you're always trying to just
click them down and get back to what you were doing. This, to my
mind, is a major reason why most IC workers don't share civilian
concerns about being tracked online: not because they have any
insider information about how digital surveillance helps to protect
America, but because to those in IC, being tracked by the boss
just comes with the job.
    Anyway, it's not like there's a lot to be found out there on the
public Internet that's more interesting than what the agency al-
ready has internally. Few realize this, but the CIA has its own In-
ternet and Web. It has its own kind of Facebook, which allows
agents to interact socially; its own type of Wikipedia, which pro-
vides agents with information about agency teams, projects, and
missions; and its own internal version of Google - actually pro-
vided by Google - which allows agents to search this sprawling
classified network. Every CIA component has its own website on
this network that discusses what it does and posts meeting min-
utes and presentations. For hours and hours every night this was
my education."""

# Apresentando informacoes
print("\n" + "=-"*30 + "\n")

print(""">>> Informações sobre Livro:

Título: {}
Edição: {}
Autor: {}
Ano de Publicação: {}
Amostra: 
{}""".format(
            livro["title"],
            livro["edition"],
            livro["author"],
            livro["date"],
            livro["sample"],
            )
    )

print("\n" + "=-"*30 + "\n")