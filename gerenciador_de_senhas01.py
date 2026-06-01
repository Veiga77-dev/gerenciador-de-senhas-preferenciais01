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
    return linha_encontrada

def achar_coluna_do_servico(servico):
    coluna_encontrada = 0
    for j in range(len(servicos)):
        if servicos[j] == servico:
            coluna_encontrada = j 
    return coluna_encontrada

def somar_linha(numero_da_linha):
    total = 0
    for j in range(len(tipos)):
        total += matriz_atendimentos[numero_da_linha][j]
    return total

def soma_coluna(numero_da_coluna):
    total = 0
    for i in range(len(tipos)):
        total += matriz_atendimentos[i][numero_da_coluna]
    return total

def registrar_na_matriz(tipo, servico):
    linha = achar_linha_do_tipo(tipo)
    coluna = achar_coluna_do_servico(servico)
    matriz_atendimentos[linha][coluna] += 1

def minusculas(texto):
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    for letra in texto:
        achou = False
        for i in range(len(letras_maiusculas)):
            if letra == letras_maiusculas[i]:
                resultado += letras_minusculas[i]
                achou = True
                break
        if achou == False:
            resultado += letra
    return resultado
           
def tirar_espacos(texto):
    resultado = ""
    for letra in texto:
        if letra != " ":
            resultado += letra
    return resultado

def tirar_espacos_pontas(texto):
    inicio = 0
    fim = len(texto) - 1

    while inicio <= fim:
        if texto[inicio] == " ":
            inicio += 1
        else:
            break

    while fim >= inicio:
        if texto[fim] == " ":
            fim -= 1
        else:
            break

    resultado = ""
    for i in range(inicio, fim + 1):
        resultado += texto[i]
    return resultado

def pegar_primeiros(texto, quantidade):
    resultado = " "
    for i in range(quantidade):
        if i < len(texto):
            resultado += texto[i]
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
    for i in range(len(lista)-1):
        nova_lista.append(lista[i])
    return nova_lista

def par_ou_impar(numero):
    n = numero 
    while n >= 2:
        n -= 2
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

    codigo = fazer_codigo(tipo, nome)
    nome_limpo = tirar_espacos_pontas(nome)

    if nome_limpo == "":
        nome_final = "Usuario"
    else:
        nome_final = nome

    nova_senha = {
        "codigo": codigo,
        "tipo": tipo,
        "servico": servico,
        "nome": nome_final
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
            posicao = i
            break

    fila_de_espera = inserir_na_lista(fila_de_espera, posicao, nova_senha)   
    registrar_na_matriz(tipo, servico)
    return nova_senha

def chamar_proximo():
    global fila_de_espera, historico, senha_atual, total_chamados

    if len(fila_de_espera) == 0:
        return None
    
    proximo = fila_de_espera[0]
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
        return COR_VERDE
    else:
        return COR_AZUL

def fundo_do_tipo(tipo):
    if tipo == 'URGENTE':
        return '#2d1117'
    elif tipo == 'PREFERENCIAL':
        return '#2d2000'
    else:
        return '#1c2333'

def simbolo_do_tipo(tipo):
    if tipo == "URGENTE":
        return " "
    elif tipo == "PREFENCIAL":
        return " "
    else: 
        return " "

label_senha_atual = None
label_tipo_func = None
label_servico_func = None
label_qtd_fila     = None
area_fila          = None
area_historico     = None
campo_nome         = None
combo_servico      = None
botao_pref         = None
botao_urg          = None
botao_norm         = None
num_na_fila        = None
num_chamados       = None

janela_principal   = None

def escolher_tipo(tipo):
    global tipo_escolhido
    tipo_escolhido = tipo

    botao_urg.configure(fg_color=COR_CARD2,  hover_color=COR_BORDA, text_color=COR_CINZA)
    botao_pref.configure(fg_color=COR_CARD2, hover_color=COR_BORDA, text_color=COR_CINZA)
    botao_norm.configure(fg_color=COR_CARD2, hover_color=COR_BORDA, text_color=COR_CINZA)

    if tipo == "URGENTE":
        botao_urg.configure(fg_color=COR_VERMELHO, hover_color=COR_VERMELHO, text_color=COR_BRANCO)
    elif tipo == "PREFERENCIAL":
        botao_pref.configure(fg_color=COR_AMARELO, hover_color=COR_AMARELO, text_color=COR_BRANCO)
    else:
        botao_norm.configure(fg_color=COR_AZUL, hover_color=COR_AZUL, text_color=COR_BRANCO)


def clicou_gerar():
    nome = tirar_espacos_pontas(campo_nome.get())

    if nome == "":
        messagebox.showwarning("Aviso", "Por favor, digite o nome antes de gerar a senha.")
        return

    servico = combo_servico.get()
    adicionar_senha(tipo_escolhido, servico, nome)

    atualizar_fila_na_tela()
    atualizar_contadores()
    campo_nome.delete(0, "end")


def clicou_chamar():
    resultado = chamar_proximo()

    if resultado is None:
        messagebox.showinfo("Aviso", "Nao tem ninguem na fila no momento.")
        return

    mostrar_senha_chamada(resultado)
    atualizar_fila_na_tela()
    atualizar_contadores()
    atualizar_historico()


def mostrar_senha_chamada(senha):
    cor     = cor_do_tipo(senha["tipo"])
    simbolo = simbolo_do_tipo(senha["tipo"])

    label_senha_atual.configure(text=senha["codigo"], text_color=cor)
    label_tipo_func.configure(text=simbolo + "  " + senha["tipo"], text_color=cor)
    label_servico_func.configure(text=senha["servico"], text_color=COR_CINZA)


def atualizar_contadores():
    num_na_fila.configure(text="Fila: " + str(len(fila_de_espera)))
    num_chamados.configure(text="Chamados: " + str(total_chamados))

def atualizar_fila_na_tela():
    for widget in area_fila.winfo_children():
        widget.destroy()
    
    qtd = len(fila_de_espera)

    if qtd == 1:
        label_qtd_fila.configure(text="1 pessoa")
    else:
        label_qtd_fila.configure(text=str(qtd) + " pessoas")
    
    if qtd == 0:
        ctk.CTkLabel(area_fila, text="Fila vazia", font=("Consolas", 19), text_color=COR_CINZA).pack(pady=30)
        return
    
    for i in range(qtd):
        senha = fila_de_espera[i]
        cor = cor_do_tipo(senha["tipo"])
        fundo = fundo_do_tipo(senha["tipo"])
        simbolo = simbolo_do_tipo(senha["tipo"])

        if par_ou_impar(i) == 0:
            cor_bg = COR_CARD2
        else:
            cor_bg = COR_CARD
        
        linha = ctk.CTkFrame(area_fila, fg_color=cor_bg, corner_radius=6)
        linha.pack(fill="x", pady=1, padx=2)

        numero_pos = i + 1
        if numero_pos < 10:
            texto_pos = "0" + str(numero_pos)
        else:
            texto_pos = str(numero_pos)
        
        ctk.CTkLabel(linha, text=texto_pos, font=("Consolas", 18, "bold"),
                     text_color=COR_CINZA, width=24).pack(side="left", padx=(8, 4), pady=6)
        
        ctk.CTkLabel(linha, text=simbolo + " " + senha["tipo"], font=("Consolas", 17),
                     text_color=cor, fg_color=fundo, corner_radius=4).pack(
                     side="left", padx=4, pady=4, ipadx=6, ipady=2)
        
        ctk.CTkLabel(linha, text=senha["codigo"], font=("Consolas", 24, "bold"),
                     text_color=cor, width=110).pack(side="lefft", padx=6)
        
        ctk.CTkLabel(linha, text=senha["servico"], font=("Consolas", 19),
                     text_color=COR_CINZA).pack(side="right", padx=8)
    
        ctk.CTkLabel(linha, text=senha["nome"], font=("Consolas", 19),
                     text_color=COR_CINZA).pack(side="right", padx=8)
  