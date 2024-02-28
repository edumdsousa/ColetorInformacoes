import tkinter as tk
from tkinter import messagebox
import wmi
import psutil
import getpass
import math

def obter_informacoes_sistema():
    # Inicializa o objeto WMI
    c = wmi.WMI()

    # Obtém o modelo da placa mãe
    for board in c.Win32_BaseBoard():
        modelo_placa_mae = board.Product

    # Verifica se há uma bateria presente para determinar se é um notebook
    for battery in c.Win32_Battery():
        tipo = "LAPTOP"
        break
    else:
        tipo = "DESKTOP"

    # Obtém o fabricante do sistema
    for system in c.Win32_ComputerSystem():
        fabricante = system.Manufacturer

    # Obtém o nome do usuário atual
    usuario = getpass.getuser()

    # Obtém informações sobre a memória RAM
    mem = psutil.virtual_memory()
    ram = math.ceil(mem.total / (1024 ** 3))  # Arredonda para cima e converte bytes para gigabytes

    # Obtém informações sobre os discos (HDD e SSD)
    ssd = 0
    hdd = 0
    for disco in c.Win32_LogicalDisk(DriveType=3):  # DriveType 3 corresponde a discos fixos
        if 'C:' in disco.DeviceID.upper():
            ssd += psutil.disk_usage(disco.DeviceID).total
        else:
            hdd += psutil.disk_usage(disco.DeviceID).total

    # Convertendo de bytes para gigabytes com arredondamento para uma casa decimal
    ssd = round(ssd / (1024 ** 3), 1)
    hdd = round(hdd / (1024 ** 3), 1)

    return tipo, fabricante, modelo_placa_mae, ram, hdd, ssd, usuario

def obter_informacoes():
    tipo, fabricante, modelo_placa_mae, ram, hdd, ssd, usuario = obter_informacoes_sistema()

    # Preencher automaticamente os campos
    entradas["TIPO"].insert(0, tipo)
    entradas["MARCA"].insert(0, fabricante)
    entradas["MODELO"].insert(0, modelo_placa_mae)
    entradas["RAM"].insert(0, f"{ram} GB")
    entradas["HDD"].insert(0, f"{hdd} GB")
    entradas["SSD"].insert(0, f"{ssd} GB")
    entradas["USUARIO"].insert(0, usuario)

def escrever_dados():
    dados = ";".join([entradas[campo].get() for campo in entradas]) + "\n"  # Adiciona uma quebra de linha ao final do texto
    with open("dados.txt", "a") as arquivo:  # Modo "a" para adicionar ao arquivo
        arquivo.write(dados)
    messagebox.showinfo("Dados Escritos", "Os dados foram escritos com sucesso!")

# Criar janela principal
janela = tk.Tk()
janela.title("Obter Informações do Sistema")
janela.geometry("300x600")

# Botão Obter Informações
btn_obter_info = tk.Button(janela, text="Pesquisar", command=obter_informacoes)
btn_obter_info.pack(pady=20)

# Dicionário para armazenar as entradas
entradas = {}

# Exibir campos para preencher manualmente
campos = [
    "TIPO",
    "MARCA",
    "MODELO",
    "RAM",
    "SSD",
    "HDD",
    "RESPONSAVEL",
    "MATRICULA",
    "USUARIO",
    "EMAIL",
    "LOCALIDADE"
]

for campo in campos:
    lbl = tk.Label(janela, text=campo)
    lbl.pack()
    
    entrada = tk.Entry(janela)
    entrada.pack()
    
    # Adicionar entrada ao dicionário
    entradas[campo] = entrada

# Botão Escrever
btn_escrever = tk.Button(janela, text="Escrever", command=escrever_dados)
btn_escrever.pack(pady=20)

# Iniciar loop da janela principal
janela.mainloop()
