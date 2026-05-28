import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

fila_de_espera = []
historico = []
senha_atual = None
total_chamados = 0

cont_preferencial = 0
cont_urgente = 0
cont_normal = 0

tipo_escolhido = "NORMAL"

COR_FUNDO     = "#0d1117"
COR_TOPO      = "#161b22"
COR_CARD      = "#21262d"
COR_CARD2     = "#162032"
COR_AZUL      = "#58a6ff"
COR_VERDE     = "#3fb950"
COR_VERMELHO  = "#f85149"
COR_CIANO     = "#79c0ff"
COR_BRANCO    = "#e6edf3"
COR_CINZA     = "#8b949e"
COR_BORDA     = "#30363d"

servicos = [
    "Atendimento Geral",
    "Caixa / Pagamentos"
]

tipos = ["NORMAL", "PREFERENCIAL", "URGENTE"]

matriz_atendimentos = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def achar_linha_do_tipo(tipo):
    linha_encontrada = 0
    for i in range(len(tipos)):
        if tipos[i] == tipo:
            linha_encontrada = i
            break
    return linha_encontrada

def achar_coluna_do_servico(servico):
    coluna_encontrada = 0
    for j in range(len(servicos)):
        if servicos[j] == servico:
            coluna_encontrada = j 
    return coluna_encontrada

def somar_linha(numero_da_linha):
    total = 0
    for i in range(len(tipos)):
        total = total + matriz_atendimentos[numero_da_linha][j]
    return total

def soma_coluna(numero_da_coluna):
    total = 0
    for i in range(len(tipos)):
        total = total + matriz_atendimentos[i][numero_da_coluna]
    return total

def registrar_na_matriz(tipo, servico):
    linha = achar_linha_do_tipo(tipo)
    coluna = achar_coluna_do_servico(servico)
    matriz_atendimento[linha][coluna] = matriz_atendimentos[linha][coluna] + 1

def minusculas(texto):
    letras_maisculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    for letra in texto:
        achou = False
        for i in range(len(letras_maiusculas)):
            if letra == letras_maiusculas[i]:
                resultado = resultado + letras_minusculas[i]
                achou = True
                break
            if achou == False:
                resultado = resultado + letra
        return resultado
           
def tirar_espacos(texto):
    resultado = ""
    for letra in texto:
        if letra != " ":
            resultado = resultado + letra
    return resultado

def tirar_espacos_pontas(texto):
    inicio = 0
    fim = len(texto) - 1
    while inicio <= fim:
        if texto[inicio] == " ":
            inicio = inicio + 1
        else:
            break
    resultado = ""
    for i in range(inicio, fim + 1):
        resultado = resultado + texto[i]
    return resultado

def pegar_primeiros(texto, quantidade):
    resultado = ""
    for i in range(quantidade):
        if i < len(texto):
            resultado = resultado + texto[i]
    return resultado

def inserir_na_lista(lista, posicao, item):
    nova_lista = []
    for i in range(len(lista)):
        if i == posicao:
            nova_lista.append(item)
        nova_lista.append(lista[i])
    if posicao >= len(lista):
        nova_lista.append(item)
    return nova_lista

def remover_primeiro(lista):
    nova_lista = []
    for i in range(len(lista)):
        if i != 0:
            nova_lista.append(lista[i])
    return nova_lista

def remover_ultimo(lista):
    nova_lista = []
    for i in range(len(lista) -1):
        nova_lista.append(lista[i])
    return nova_lista

def par_ou_impar(numero):
    n = numero 
    while n >= 2:
        n = n - 2
    if n == 0:
        return 0
    else:
        return 1
    
def fazer_codigo(tipo, nome):
    global cont_preferencial, cont_urgente, cont_normal

    nome_limpo = minusculas(nome)
    nome_limpo = tirar_espacos(nome_limpo)

    if len(nome_limpo) == 0:
        nome_limpo = 'user'

    if len(nome_limpo) > 8:
        nome_limpo = pegar_primeiros(nome_limpo, 8)
    
    if tipo == 'PREFERENCIAL':
        cont_preferencial += 1
        numero = cont_preferencial
    elif tipo == 'URGENTE':
        cont_urgente += 1
        numero = cont_urgente
    else:
        cont_normal += 1
        numero = cont_normal
    
    if numero < 10:
        numero_texto = '00' + str(numero)
    elif numero < 100:
        numero_texto = '0' + str(numero)
    else:
        numero_texto = str(numero)
    
    codigo = nome_limpo + numero_texto
    return codigo

def adicionar_senha(tipo, servico, nome):
    global fila_de_espera

    codigo     = fazer_codigo(tipo, nome)
    nome_limpo = tirar_espacos_pontas(nome)

    if nome_limpo == "":
        nome_final = "Usuario"
    else:
        nome_final = nome

    nova_senha = {
        "codigo"    : codigo,
        "tipo"      : tipo,
        "servico"   : servico,
        "nome"      : nome_final
    }

    if tipo == "URGENTE":
        nivel_novo = 1
    elif tipo == "PREFERENCIAL":
        nivel_novo = 2
    else:
        nivel_novo = 3

    posicao = len(fila_de_espera)

    for i in range(len(fila_de_espera)):
        tipo_existente = fila_de_espera[i]["tipo"]

        if tipo_existente == "URGENTE":
            nivel_existente = 1
        elif tipo_existente == "PREFERENCIAL":
            nivel_existente = 2
        else:
            nivel_existente = 3

        if nivel_existente > nivel_novo:
            posicao = 1
            break

    fila_de_espera = inserir_na_lista(fila_de_espera, posicao, nova_senha)   
    registrar_na_matriz(tipo, servico)
    return nova_senha

def chamar_proximo():
    global fila_de_espera, historico, senha_atual, total_chamados

    if len(fila_de_espera) == 0:
        return None
    
    proximo = fila_de_espera[o]
    fila_de_espera = remover_primeiro(fila_de_espera)

    senha_atual = proximo
    total_chamados += 1

    historico = inserir_na_lista(historico, 0, proximo)

    if len(historico) > 20:
        historico = remover_ultimo(historico)
    
    return proximo

def cor_do_tipo(tipo):
    if tipo == 'URGENTE':
        return COR_VERMELHO
    elif tipo == 'PREFERENCIAL':
        return COR_AMARELO
    else:
        return COR_AZUL

def fundo_do_tipo(tipo):
    if tipo == 'URGENTE':
        return '#2d1117'
    elif tipo == 'PREFERENCIAL'
        return '#2d2000'
    else:
        return '#1c2333'