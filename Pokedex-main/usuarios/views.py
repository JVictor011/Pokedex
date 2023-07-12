from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('user')
        password = request.POST.get('password')
        print(username)
        print(password)
        
        if not username.strip() or not password.strip():
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect("/auth/login/")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/auth/home/")
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect("/auth/login/")

@login_required(login_url='/auth/login')
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        search_query = request.POST.get('search_query')
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_num, nome, nivel, sexo, velocidade, defesa, matricula FROM pokemon WHERE nome LIKE %s", ['%' + search_query + '%'])
            results = cursor.fetchall()

        return render(request, 'home.html', {'results': results, 'home': search_query})


def deletePokemon(request, pokemon_id):
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM pokemon WHERE id_num = %s",
                [pokemon_id]
            )
        return redirect("/auth/home/")

def addTreinador(request):
    if request.method == "GET":
        return render(request, 'addTreinador.html')
    else:
        matricula = request.POST.get('matricula')
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        notas_pess = request.POST.get('notas_pess')
        obj_captu = request.POST.get('obj_captu')
        cpf = request.POST.get('cpf')
        favorito1 = request.POST.get('favorito1')
        favorito2 = request.POST.get('favorito2')
        favorito3 = request.POST.get('favorito3')
        favorito4 = request.POST.get('favorito4')
        favorito5 = request.POST.get('favorito5')
        favorito6 = request.POST.get('favorito6')
        
        try:
            print("1111111111")
            user = User.objects.create_user(username=matricula, email=email, password=senha)
            print("22222222")
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO treinador (matricula, nome, idade, email, senha, notas_pess, obj_captu, cpf, favorito1, favorito2, favorito3, favorito4, favorito5, favorito6) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",[matricula, nome, idade, email, senha, notas_pess, obj_captu, cpf, favorito1, favorito2, favorito3, favorito4, favorito5, favorito6]
                )
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
            return render(request, 'addTreinador.html')
        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Não foi possível cadastrar o treinador')
            return render(request, 'addTreinador.html')
        
def addItens(request):
    if request.method == "GET":
        return render(request, 'addItens.html')
    else:
        print('12121212')
        cod_item = request.POST.get('cod_item')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        efeito = request.POST.get('efeito')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')

        try:
            print("3232323232")
            print(nome)
            print(preco)
            print(efeito)
            print(descricao)
            print(categoria)
            print(cod_item)
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO itens (Cod_Item, Nome, Preco, Efeito, Descricao, Categoria) VALUES (%s, %s, %s, %s, %s, %s)",
                    [cod_item, nome, preco, efeito, descricao, categoria]
                )
            messages.add_message(request, constants.SUCCESS, 'Item adicionado')
            return render(request, 'addItens.html')
        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Não foi possível adicionar o item')
            return render(request, 'addItens.html')
        
def visao(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT nome, total_pokemon FROM treinador_pokemon_count")
            results = cursor.fetchall()

        return render(request, 'visao.html', {'results': results})
    else:        
        with connection.cursor() as cursor:
            cursor.execute("SELECT nome, total_pokemon FROM treinador_pokemon_count")
            results = cursor.fetchall()

        return render(request, 'visao.html', {'results': results})