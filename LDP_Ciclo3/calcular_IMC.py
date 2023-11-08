# Este programa calcula o IMC do usuário de acordo com o peso e a altura e classifica.

import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        altura = float(entrada_altura.get()) / 100
        peso = float(entrada_peso.get())
        imc = peso / (altura ** 2)
        entrada_imc.delete(0, tk.END)
        entrada_imc.insert(tk.END, str(imc))
        if imc < 17:
            messagebox.showinfo("Resultado", "Muito abaixo do peso")
        elif 17 <= imc < 18.5:
            messagebox.showinfo("Resultado", "Abaixo do peso")
        elif 18.5 <= imc < 25:
            messagebox.showinfo("Resultado", "Peso normal")
        elif 25 <= imc < 30:
            messagebox.showinfo("Resultado", "Acima do peso")
        elif 30 <= imc < 35:
            messagebox.showinfo("Resultado", "Obesidade I")
        elif 35 <= imc < 40:
            messagebox.showinfo("Resultado", "Obesidade II - Severa")
        else:
            messagebox.showinfo("Resultado", "Obesidade mórbida")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para altura e peso.")

def reiniciar():
    entrada_nome.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)
    entrada_peso.delete(0, tk.END)
    entrada_imc.delete(0, tk.END)

janela = tk.Tk()
janela.title("Calculadora de IMC")

tk.Label(janela, text="Nome do Paciente:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Endereço do Paciente:").pack()
entrada_endereco = tk.Entry(janela)
entrada_endereco.pack()

tk.Label(janela, text="Altura do Paciente (cm):").pack()
entrada_altura = tk.Entry(janela)
entrada_altura.pack()

tk.Label(janela, text="Peso do Paciente (kg):").pack()
entrada_peso = tk.Entry(janela)
entrada_peso.pack()

tk.Label(janela, text="IMC:").pack()
entrada_imc = tk.Entry(janela)
entrada_imc.pack()

tk.Button(janela, text="Calcular IMC", command=calcular_imc).pack()
tk.Button(janela, text="Reiniciar", command=reiniciar).pack()
tk.Button(janela, text="Sair", command=janela.quit).pack()

janela.mainloop()