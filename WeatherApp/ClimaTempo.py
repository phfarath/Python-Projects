import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
from dotenv import load_dotenv

class AplicativoClima:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo do ClimaTempo")
        self.root.geometry("500x600")
        self.root.configure(bg='#f0f0f0')
        
        # Carrega variáveis de ambiente
        load_dotenv()
        
        # API KEY do arquivo .env
        self.api_key = os.getenv('CLIMA_API_KEY')
        
        if not self.api_key:
            messagebox.showerror("Erro", "API Key não encontrada no arquivo .env")
            self.root.destroy()
            return
        
        # Interface grafica
        self.configurar_interface()
        
    def configurar_interface(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(padx=30, pady=20, fill=tk.BOTH, expand=True)
        
        # Título
        titulo = tk.Label(main_frame, 
                         text="Previsão do Tempo",
                         font=('Helvetica', 24, 'bold'),
                         bg='#f0f0f0',
                         fg='#2c3e50')
        titulo.pack(pady=20)
        
        # Frame de busca
        busca_frame = tk.Frame(main_frame, bg='#f0f0f0')
        busca_frame.pack(fill=tk.X, pady=10)
        
        # Entrada da cidade
        self.cidade_entry = tk.Entry(busca_frame,
                                   font=('Helvetica', 14),
                                   width=20,
                                   bd=2,
                                   relief=tk.GROOVE)
        self.cidade_entry.pack(side=tk.LEFT, padx=5)
        self.cidade_entry.insert(0, "Digite a cidade...")
        self.cidade_entry.bind('<FocusIn>', lambda e: self.cidade_entry.delete(0, tk.END))
        
        # Botão de busca
        self.buscar_button = tk.Button(
            busca_frame,
            text="Buscar",
            command=self.obter_clima,
            font=('Helvetica', 12),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            padx=20,
            relief=tk.RAISED,
            cursor='hand2'
        )
        self.buscar_button.pack(side=tk.LEFT, padx=5)
        
        # Frame para informações do clima
        self.info_frame = tk.Frame(main_frame, bg='white', relief=tk.GROOVE, bd=2)
        self.info_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # Labels para informações
        self.temp_label = tk.Label(self.info_frame, 
                                 text="--°C",
                                 font=('Helvetica', 36, 'bold'),
                                 bg='white',
                                 fg='#2c3e50')
        self.temp_label.pack(pady=20)
        
        self.desc_label = tk.Label(self.info_frame,
                                 text="",
                                 font=('Helvetica', 18),
                                 bg='white',
                                 fg='#34495e')
        self.desc_label.pack(pady=10)
        
        # Frame para detalhes adicionais
        detalhes_frame = tk.Frame(self.info_frame, bg='white')
        detalhes_frame.pack(pady=20)
        
        self.umidade_label = tk.Label(detalhes_frame,
                                    text="Umidade: --%",
                                    font=('Helvetica', 14),
                                    bg='white',
                                    fg='#7f8c8d')
        self.umidade_label.pack(pady=5)
        
        self.vento_label = tk.Label(detalhes_frame,
                                  text="Vento: -- m/s",
                                  font=('Helvetica', 14),
                                  bg='white',
                                  fg='#7f8c8d')
        self.vento_label.pack(pady=5)
        
        self.hora_label = tk.Label(self.info_frame,
                                 text="",
                                 font=('Helvetica', 10),
                                 bg='white',
                                 fg='#95a5a6')
        self.hora_label.pack(pady=10)
    
    def obter_clima(self):
        cidade = self.cidade_entry.get()
        if not cidade or cidade == "Digite a cidade...":
            messagebox.showerror("Erro", "Por favor, digite o nome de uma cidade")
            return
            
        try:
            # Requisição da API
            url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={self.api_key}&units=metric"
            resposta = requests.get(url)
            dados = resposta.json()
            
            if resposta.status_code == 200:
                # Puxa os dados da API
                temp = dados['main']['temp']
                desc = dados['weather'][0]['description']
                umidade = dados['main']['humidity']
                velocidade_vento = dados['wind']['speed']
                
                # Atualiza os dados da interface
                self.temp_label.config(text=f"{temp:.1f}°C")
                self.desc_label.config(text=desc.capitalize())
                self.umidade_label.config(text=f"Umidade: {umidade}%")
                self.vento_label.config(text=f"Velocidade do Vento: {velocidade_vento} m/s")
                self.hora_label.config(text=f"Última Atualização: {datetime.now().strftime('%H:%M:%S')}")
            else:
                messagebox.showerror("Erro", f"Erro: {dados['message']}")
                
        except requests.exceptions.RequestException:
            messagebox.showerror("Erro", "Falha ao conectar ao serviço de clima")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoClima(root)
    root.mainloop()