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
