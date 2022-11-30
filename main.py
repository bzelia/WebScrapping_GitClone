from bs4 import BeautifulSoup
import requests
import html5lib
import os


def yes_or_no(pergunta):
    while "Resposta inválida.":
        resposta = str(input(pergunta +' (s/n): ')).lower().strip()
        if resposta == 's':
            return True
        if resposta == 'n':
            return False


def lista_repos():
    for x in range(len(repositorio)):
        print(str(x) + ' = ' + repositorio[x].text)


def define_caminho():
    lista_repos()
    projeto = int(input('Insira um número do repositório para o clone: '))
    if projeto < len(repositorio):
        return repositorio[projeto].text
    else:
        print('Repositório inexistente, tente novamente.')
        define_caminho()


if __name__ == '__main__':
    url = 'https://github.com/'
    usuario = str(input('Insira o usuário do GitHub: '))
    url = url + usuario
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')

    repositorio = soup.find_all('span', {'class': 'repo'})

    caminho = '/' + str(define_caminho())
    url = url + str(caminho)
    print(url)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')

    if os.path.isdir('c://' + caminho):
        if yes_or_no('Arquivo já existe. Proceder com pull?'):
            os.chdir('c://' + caminho)
            os.system('git pull')
    else:
        os.chdir('c://')
        os.system('git clone ' + url)
