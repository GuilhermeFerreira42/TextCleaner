import tkinter as tk
from tkinter import ttk

# Função para processar o texto
def processar_texto():
    caracteres_remover = entry_remover.get()
    texto = entry_texto.get("1.0", tk.END)
    texto_processado = ''.join([char for char in texto if char not in caracteres_remover])
    entry_resultado.delete("1.0", tk.END)  # Limpa o campo de resultado
    entry_resultado.insert(tk.END, texto_processado)  # Exibe o texto processado

# Função para criar menu de contexto
def criar_menu_contexto(widget):
    menu_contexto = tk.Menu(widget, tearoff=0)
    menu_contexto.add_command(label="Copiar", command=lambda: widget.event_generate("<<Copy>>"))
    menu_contexto.add_command(label="Colar", command=lambda: widget.event_generate("<<Paste>>"))
    menu_contexto.add_command(label="Cortar", command=lambda: widget.event_generate("<<Cut>>"))
    menu_contexto.add_command(label="Selecionar Tudo", command=lambda: widget.event_generate("<<SelectAll>>"))

    def exibir_menu(event):
        menu_contexto.tk_popup(event.x_root, event.y_root)

    widget.bind("<Button-3>", exibir_menu)

# Configuração da janela principal
root = tk.Tk()
root.title("Remover Caracteres Especiais")
root.geometry("600x500")  # Aumentando o tamanho da janela principal

# Rótulo e campo para informar os caracteres a serem removidos
label_remover = ttk.Label(root, text="Caracteres para remover:")
label_remover.pack(pady=5)
entry_remover = ttk.Entry(root, width=70)  # Aumentando a largura do campo de entrada
entry_remover.pack(pady=5)

# Adicionando menu de contexto ao campo entry_remover
criar_menu_contexto(entry_remover)

# Rótulo e campo para inserir o texto a ser processado
label_texto = ttk.Label(root, text="Insira o texto:")
label_texto.pack(pady=5)
entry_texto = tk.Text(root, height=15, width=70)  # Aumentando a altura e largura do campo de texto
entry_texto.pack(pady=5)

# Adicionando menu de contexto ao campo entry_texto
criar_menu_contexto(entry_texto)

# Botão "Processar"
botao_processar = ttk.Button(root, text="Processar", command=processar_texto)
botao_processar.pack(pady=10)

# Rótulo e campo para mostrar o texto processado
label_resultado = ttk.Label(root, text="Texto processado:")
label_resultado.pack(pady=5)
entry_resultado = tk.Text(root, height=15, width=70)  # Aumentando a altura e largura do campo de resultado
entry_resultado.pack(pady=5)

# Adicionando menu de contexto ao campo entry_resultado
criar_menu_contexto(entry_resultado)

# Iniciar o loop da interface gráfica
root.mainloop()
