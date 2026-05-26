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
    [0, 0, 0]
    [0, 0, 0]
    [0, 0, 0]
]

def achar_linha_do_tipo(tipo):
    linha_encontrada = 0
    for i in range(len(tipos))
    if tipos [i] == tipo:
        linha_encontrada = i
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
    for i in range(qauntidade)
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
