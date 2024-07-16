from filme import Review_Filme
from series import Series_Review
from menu import menu_principal
from menu import limparTela
from database import db, Filme, Serie

db.connect()
db.create_tables([Filme, Serie])

mymoviereviews = []
myseriesreview = []

def write_movie_reviews():
    filme = input("Digite o nome do filme: ")
    nota = float(input("Digite a nota do filme: "))
    review = input("Digite a sua review: ")

    new_review = Review_Filme(filme, nota, review)
    mymoviereviews.append(new_review)
    
    filme = Filme.create(nome = new_review.name, nota = new_review.score, review = new_review.review)
    print(f"riview adicionada \n Filme: {filme.nome}. Nota: {filme.nota}. Review: {filme.review}")
        

def write_series_reviews():
    serie = input("Digite o nome da série: ")
    nota = float(input("Digite a nota da série: "))
    review = input("Digite a sua review: ")

    new_review = Series_Review(serie, nota, review)
    myseriesreview.append(new_review)

    serie = Serie.create(nome = new_review.name, nota = new_review.score, review = new_review.review)
    print(f"riview adicionada \n Filme: {serie.nome}. Nota: {serie.nota}. Review: {serie.review}")

while True:
    films = Filme.select()
    series = Serie.select()
    menu_principal()
    opcao = input("Escolha uma opção: ")

    if int(opcao) == 1:   
        add_review = input("Deseja adicionar review de um filme? s/n? ")

        if add_review == 's':
            write_movie_reviews()
            limparTela()

        elif add_review == 'n':
            limparTela()
    
    elif int(opcao) == 2:
        add_review = input("Deseja adicionar review de um filme? s/n? ")

        if add_review == 's':
            write_series_reviews()
            limparTela()
        
        elif add_review == 'n':
            limparTela()
            
    elif int(opcao) == 3:
        limparTela()
        for i in films:
            print(f'Filme: {i.nome}. Nota: {i.nota}, Review: {i.review}')

    elif int(opcao) == 4:
        limparTela()
        for i in series:
            print(f'Série: {i.nome}. Nota: {i.nota}. Review: {i.review}')
        
    elif int(opcao) == 0:
        break
    