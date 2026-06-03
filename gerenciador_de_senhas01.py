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

COR_FUNDO = "#0d1117"
COR_TOPO = "#161b22"
COR_CARD = "#21262d"
COR_CARD2 = "#162032"
COR_AZUL = "#58a6ff"
COR_VERDE = "#3fb950"
COR_VERMELHO = "#f85149"
COR_AMARELO = "#d29922"
COR_CIANO = "#79c0ff"
COR_BRANCO = "#e6edf3"
COR_CINZA = "#8b949e"
COR_BORDA = "#30363d"

servicos = [
    "Atendimento Geral",
    "Caixa / Pagamentos"
]

tipos = ["NORMAL", "PREFERENCIAL", "URGENTE"]

matriz_atendimentos = [
    [0, 0],
    [0, 0],
    [0, 0]
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
    for j in range(len(servicos)):
        total += matriz_atendimentos[numero_da_linha][j]
    return total

def somar_coluna(numero_da_coluna):
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
        return COR_AMARELO
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
    elif tipo == "PREFERENCIAL":
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
                     text_color=cor, width=110).pack(side="left", padx=6)
        
        ctk.CTkLabel(linha, text=senha["servico"],font=("Consolas", 19),
             text_color=COR_CINZA, anchor="w").pack(side="left", fill="x", expand=True)
    
        ctk.CTkLabel(linha, text=senha["nome"], font=("Consolas", 19),
                     text_color=COR_CINZA).pack(side="right", padx=8)
  

def atualizar_historico():
    for widget in area_historico.winfo_children():
        widget.destroy()

    if len(historico) == 0:
        ctk.CTkLabel(area_historico, text="Nenhuma senha chamada", font=("Consolas", 16), text_color=COR_CINZA).pack(pady=20)
        return

    for i in range(len(historico)):
        senha   = historico[i]
        cor     = cor_do_tipo(senha["tipo"])
        simbolo = simbolo_do_tipo(senha["tipo"])

        if par_ou_impar(i) == 0:
            cor_bg = COR_CARD2
        else:
            cor_bg = COR_CARD

        linha = ctk.CTkFrame(area_historico, fg_color=cor_bg, corner_radius=6)
        linha.pack(fill="x", pady=1, padx=2)

        ctk.CTkLabel(linha, text=senha["codigo"],
                     font=("Consolas", 17, "bold"), text_color=cor, width=120, anchor="center").pack(side="left", padx=4, pady=5)
        ctk.CTkLabel(linha, text=pegar_primeiros(senha["nome"], 12),
                     font=("Consolas", 17), text_color=COR_CINZA, width=110, anchor="center").pack(side="left", padx=4, pady=5)
        ctk.CTkLabel(linha, text=simbolo + " " + senha["tipo"],
                     font=("Consolas", 17), text_color=cor, width=120, anchor="center").pack(side="left", padx=4, pady=5)
        ctk.CTkLabel(linha, text=senha["servico"],
                     font=("Consolas", 17), text_color=COR_CINZA, anchor="w").pack(side="left", padx=8, pady=5, fill="x", expand=True)
        

janela_principal = ctk.CTk()
janela_principal.title("Gerenciador de Senhas")
janela_principal.geometry("1100x750")
janela_principal.configure(fg_color=COR_FUNDO)

cabecalho = ctk.CTkFrame(janela_principal, fg_color=COR_TOPO, corner_radius=0)
cabecalho.pack(fill="x", pady=(0, 10))

ctk.CTkLabel(cabecalho, text="SISTEMA DE SENHAS", font=("Arial", 20, "bold"), text_color=COR_BRANCO).pack(side="left", padx=16, pady=10)

num_na_fila = ctk.CTkLabel(cabecalho, text="Fila: 0", font=("Arial", 14), text_color=COR_CINZA)
num_na_fila.pack(side="right", padx=8, pady=10)

num_chamados = ctk.CTkLabel(cabecalho, text="Chamados: 0", font=("Arial", 14), text_color=COR_CINZA)
num_chamados.pack(side="right", padx=8, pady=10)

corpo = ctk.CTkFrame(janela_principal, fg_color=COR_FUNDO, corner_radius=0)
corpo.pack(fill="both", expand=True, padx=12, pady=(0, 10))
corpo.columnconfigure(0, weight=1)
corpo.columnconfigure(1, weight=1)
corpo.rowconfigure(0, weight=1)
corpo.rowconfigure(1, weight=1)

card_senha = ctk.CTkFrame(corpo, fg_color=COR_CARD, corner_radius=8)
card_senha.grid(row=0, column=0, sticky="nsew", padx=(0, 6), pady=(0, 6))

ctk.CTkLabel(card_senha, text="Senha Atual", font=("Arial", 14, "bold"), text_color=COR_CINZA).pack(pady=(10, 0))

label_senha_atual = ctk.CTkLabel(card_senha, text="---", font=("Arial", 72, "bold"), text_color=COR_CIANO)
label_senha_atual.pack()

label_tipo_func = ctk.CTkLabel(card_senha, text="", font=("Arial", 15, "bold"), text_color=COR_CINZA)
label_tipo_func.pack()

label_servico_func = ctk.CTkLabel(card_senha, text="", font=("Arial", 14), text_color=COR_CINZA)
label_servico_func.pack(pady=(0, 6))

ctk.CTkButton(
    card_senha, text="CHAMAR PROXIMA SENHA",
    font=("Arial", 14, "bold"), fg_color=COR_AZUL,
    text_color=COR_BRANCO, corner_radius=6, height=38,
    command=clicou_chamar
).pack(pady=(0, 10))

card_emitir = ctk.CTkFrame(corpo, fg_color=COR_CARD, corner_radius=8)
card_emitir.grid(row=0, column=1, sticky="nsew", padx=(6, 0), pady=(0, 6))

ctk.CTkLabel(card_emitir, text="Emitir Nova Senha", font=("Arial", 14, "bold"), text_color=COR_CINZA).pack(pady=(10, 4))

frame_nome = ctk.CTkFrame(card_emitir, fg_color=COR_CARD, corner_radius=0)
frame_nome.pack(fill="x", padx=12, pady=2)

ctk.CTkLabel(frame_nome, text="Nome:", font=("Arial", 14), text_color=COR_CINZA).pack(anchor="w")

campo_nome = ctk.CTkEntry(
    frame_nome, font=("Arial", 14),
    fg_color=COR_CARD2, text_color=COR_BRANCO,
    border_color=COR_BORDA, corner_radius=4,
    placeholder_text="Digite o nome...", placeholder_text_color=COR_CINZA
)
campo_nome.pack(fill="x", pady=4)

frame_prio = ctk.CTkFrame(card_emitir, fg_color=COR_CARD, corner_radius=0)
frame_prio.pack(fill="x", padx=12, pady=4)

ctk.CTkLabel(frame_prio, text="Prioridade:", font=("Arial", 14), text_color=COR_CINZA).pack(anchor="w")

linha_btns = ctk.CTkFrame(frame_prio, fg_color=COR_CARD, corner_radius=0)
linha_btns.pack(fill="x", pady=4)

botao_urg = ctk.CTkButton(
    linha_btns, text="URGENTE", font=("Arial", 13, "bold"),
    corner_radius=4, height=36, command=lambda: escolher_tipo("URGENTE")
)
botao_urg.pack(side="left", fill="x", expand=True, padx=2)

botao_pref = ctk.CTkButton(
    linha_btns, text="PREFERENCIAL", font=("Arial", 13, "bold"),
    corner_radius=4, height=36, command=lambda: escolher_tipo("PREFERENCIAL")
)
botao_pref.pack(side="left", fill="x", expand=True, padx=2)

botao_norm = ctk.CTkButton(
    linha_btns, text="NORMAL", font=("Arial", 13, "bold"),
    corner_radius=4, height=36, command=lambda: escolher_tipo("NORMAL")
)
botao_norm.pack(side="left", fill="x", expand=True, padx=2)

escolher_tipo("NORMAL")

frame_svc = ctk.CTkFrame(card_emitir, fg_color=COR_CARD, corner_radius=0)
frame_svc.pack(fill="x", padx=12, pady=4)

ctk.CTkLabel(frame_svc, text="Servico:", font=("Arial", 14), text_color=COR_CINZA).pack(anchor="w")

combo_servico = ctk.CTkComboBox(
    frame_svc, values=servicos, font=("Arial", 13),
    fg_color=COR_CARD2, text_color=COR_BRANCO,
    button_color=COR_BORDA, button_hover_color=COR_AZUL,
    dropdown_fg_color=COR_CARD2, dropdown_text_color=COR_BRANCO,
    border_color=COR_BORDA, corner_radius=4, state="readonly"
)
combo_servico.set(servicos[0])
combo_servico.pack(fill="x", pady=4)

ctk.CTkButton(
    card_emitir, text="GERAR SENHA",
    font=("Arial", 14, "bold"), fg_color=COR_VERDE,
    text_color=COR_BRANCO, corner_radius=6, height=38,
    command=clicou_gerar
).pack(pady=8)

card_fila = ctk.CTkFrame(corpo, fg_color=COR_CARD, corner_radius=8)
card_fila.grid(row=1, column=0, sticky="nsew", padx=(0, 6), pady=(6, 0))

topo_fila = ctk.CTkFrame(card_fila, fg_color=COR_BORDA, corner_radius=0)
topo_fila.pack(fill="x")

ctk.CTkLabel(topo_fila, text="Fila de Espera", font=("Arial", 14, "bold"), text_color=COR_BRANCO).pack(side="left", padx=10, pady=6)

label_qtd_fila = ctk.CTkLabel(topo_fila, text="0 pessoas", font=("Arial", 13), text_color=COR_CIANO)
label_qtd_fila.pack(side="right", padx=10)

area_fila = ctk.CTkScrollableFrame(card_fila, fg_color=COR_CARD, corner_radius=0)
area_fila.pack(fill="both", expand=True, padx=4, pady=4)

card_hist = ctk.CTkFrame(corpo, fg_color=COR_CARD, corner_radius=8)
card_hist.grid(row=1, column=1, sticky="nsew", padx=(6, 0), pady=(6, 0))

topo_hist = ctk.CTkFrame(card_hist, fg_color=COR_BORDA, corner_radius=0)
topo_hist.pack(fill="x")

ctk.CTkLabel(topo_hist, text="Historico", font=("Arial", 14, "bold"), text_color=COR_BRANCO).pack(side="left", padx=10, pady=6)

ctk.CTkLabel(topo_hist, text="ultimas 20 senhas", font=("Arial", 12), text_color=COR_CINZA).pack(side="right", padx=10)

cab_hist = ctk.CTkFrame(card_hist, fg_color=COR_CARD2, corner_radius=0)
cab_hist.pack(fill="x", padx=4, pady=(2, 0))

ctk.CTkLabel(cab_hist, text="Senha",      font=("Arial", 13, "bold"), text_color=COR_CINZA, width=120, anchor="center").pack(side="left", padx=4, pady=4)
ctk.CTkLabel(cab_hist, text="Nome",       font=("Arial", 13, "bold"), text_color=COR_CINZA, width=110, anchor="center").pack(side="left", padx=4, pady=4)
ctk.CTkLabel(cab_hist, text="Prioridade", font=("Arial", 13, "bold"), text_color=COR_CINZA, width=120, anchor="center").pack(side="left", padx=4, pady=4)
ctk.CTkLabel(cab_hist, text="Servico",    font=("Arial", 13, "bold"), text_color=COR_CINZA, anchor="w").pack(side="left", padx=8, pady=4, fill="x", expand=True)

area_historico = ctk.CTkScrollableFrame(card_hist, fg_color=COR_CARD, corner_radius=0)
area_historico.pack(fill="both", expand=True, padx=4, pady=4)

ctk.CTkLabel(area_historico, text="Nenhuma senha chamada", font=("Consolas", 16), text_color=COR_CINZA).pack(pady=20)

janela_principal.mainloop()