import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def g_personagem(nome):
    classe = ['bruxo', 'Guerreiro', 'ladino', 'atirador', 'mago', 'monge', 'bárbaro']
    raça = ['humano', 'anjo', 'elfo', 'goblin', 'esqueleto', 'vampiro', 'lobisomem', 'orc']
    genero = ['homem', 'mulher']
    altura = random.randint(1, 5)
    poder = ['bola de fogo', 'nenhum', 'invisibilidade', 'explosão de 1000 sóis', 'invocar um dragão', 'Super inteligência', 'Roubar', 'disparar laser pelos olhos', 'imortalidade', 'invulnerabilidade']
    n_poder = ['mosquito', 'cachorro', 'humano comum', 'criança', 'exército', 'bomba nuclear', 'buraco negro', 'Deus']

    hp = random.randint(1, 15000)

    if hp >= 14000:
        hp = 'infinito'

    c_classe = random.choice(classe)
    c_raça = random.choice(raça)
    c_genero = random.choice(genero)
    c_poder = random.choice(poder)
    c_n_poder = random.choice(n_poder)

    texto = (
        '**_Seu personagem:_**\n\n'
        f'Nome = {nome}\n'
        f'Classe = {c_classe}\n'
        f'Raça = {c_raça}\n'
        f'Gênero = {c_genero}\n'
        f'Altura = {altura}m\n'
        f'Poder = {c_poder}\n'
        f'Força = {c_n_poder}\n'
        f'Pontos de vida = {hp}'
    )

    return texto