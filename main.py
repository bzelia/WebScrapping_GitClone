from bs4 import BeautifulSoup
import requests
import html5lib
import os

if __name__ == '__main__':

    usuario = str(input('Insira o usuário do github: '))
    url = 'https://github.com/' + usuario + '/'
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')

    repositorio = soup.find_all('span', {'class': 'repo'})
    for x in range(len(repositorio)):
        print(str(x) + ' = ' + repositorio[x].text)



    projeto = int(input('Número do repositório para o clone: '))
    caminho = repositorio[projeto].text

    url = url + caminho
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')

    nome_pasta = 'pasta_de_' + caminho
    os.chdir('c://')
    os.system('git clone ' + url)
