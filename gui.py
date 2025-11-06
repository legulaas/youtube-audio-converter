"""
YouTube Audio Converter - Interface Gráfica
============================================
Interface gráfica básica para o conversor de áudio do YouTube.

Autor: Matheus Fragoso
Repositório: https://github.com/legulaas/youtube-audio-converter
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import sys
from main import baixar_audio


class YouTubeAudioConverterGUI:
    def __init__(self, root):
        """
        Inicializa a interface gráfica do YouTube Audio Converter.
        
        Args:
            root: Janela principal do tkinter
        """
        self.root = root
        self.setup_ui()
        self.download_thread = None
        
    def setup_ui(self):
        """Configura a interface do usuário."""
        # Configuração da janela principal
        self.root.title("YouTube Audio Converter")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Configurar ícone (se existir)
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass  # Ignora se não houver ícone
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar redimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="🎵 YouTube Audio Converter", 
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # URL do vídeo
        ttk.Label(main_frame, text="URL do vídeo:").grid(
            row=1, column=0, sticky=tk.W, pady=(0, 5)
        )
        
        self.url_var = tk.StringVar()
        url_entry = ttk.Entry(
            main_frame, 
            textvariable=self.url_var, 
            width=60,
            font=("Arial", 10)
        )
        url_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Pasta de destino
        ttk.Label(main_frame, text="Pasta de destino:").grid(
            row=3, column=0, sticky=tk.W, pady=(0, 5)
        )
        
        folder_frame = ttk.Frame(main_frame)
        folder_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        folder_frame.columnconfigure(0, weight=1)
        
        self.folder_var = tk.StringVar(value=os.getcwd())
        folder_entry = ttk.Entry(
            folder_frame, 
            textvariable=self.folder_var, 
            font=("Arial", 10)
        )
        folder_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        browse_button = ttk.Button(
            folder_frame, 
            text="Procurar", 
            command=self.browse_folder,
            width=12
        )
        browse_button.grid(row=0, column=1)
        
        # Botões de ação
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=3, pady=(0, 15))
        
        self.download_button = ttk.Button(
            button_frame,
            text="📥 Baixar Áudio",
            command=self.start_download,
            style="Accent.TButton"
        )
        self.download_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_button = ttk.Button(
            button_frame,
            text="🗑️ Limpar",
            command=self.clear_fields
        )
        self.clear_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.open_folder_button = ttk.Button(
            button_frame,
            text="📁 Abrir Pasta",
            command=self.open_destination_folder
        )
        self.open_folder_button.pack(side=tk.LEFT)
        
        # Barra de progresso
        ttk.Label(main_frame, text="Progresso:").grid(
            row=6, column=0, sticky=tk.W, pady=(15, 5)
        )
        
        self.progress = ttk.Progressbar(
            main_frame, 
            mode='indeterminate',
            length=400
        )
        self.progress.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Status
        ttk.Label(main_frame, text="Status:").grid(
            row=8, column=0, sticky=tk.W, pady=(0, 5)
        )
        
        self.status_text = scrolledtext.ScrolledText(
            main_frame,
            height=8,
            width=70,
            font=("Consolas", 9),
            wrap=tk.WORD
        )
        self.status_text.grid(row=9, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        main_frame.rowconfigure(9, weight=1)
        
        # Status inicial
        self.update_status("Pronto para download! 🎯")
        
    def browse_folder(self):
        """Abre o diálogo para selecionar pasta de destino."""
        folder = filedialog.askdirectory(
            title="Selecione a pasta de destino",
            initialdir=self.folder_var.get()
        )
        if folder:
            self.folder_var.set(folder)
    
    def clear_fields(self):
        """Limpa os campos da interface."""
        self.url_var.set("")
        self.status_text.delete(1.0, tk.END)
        self.update_status("Campos limpos! ✨")
    
    def open_destination_folder(self):
        """Abre a pasta de destino no explorador de arquivos."""
        folder = self.folder_var.get()
        if os.path.exists(folder):
            os.startfile(folder)
        else:
            messagebox.showerror("Erro", "A pasta de destino não existe!")
    
    def update_status(self, message):
        """
        Atualiza o texto de status na interface.
        
        Args:
            message (str): Mensagem para exibir
        """
        self.status_text.insert(tk.END, f"{message}\n")
        self.status_text.see(tk.END)
        self.root.update_idletasks()
    
    def validate_inputs(self):
        """
        Valida os campos de entrada.
        
        Returns:
            bool: True se válidos, False caso contrário
        """
        url = self.url_var.get().strip()
        folder = self.folder_var.get().strip()
        
        if not url:
            messagebox.showerror("Erro", "Por favor, insira a URL do vídeo!")
            return False
            
        if not folder:
            messagebox.showerror("Erro", "Por favor, selecione uma pasta de destino!")
            return False
            
        if not os.path.exists(folder):
            messagebox.showerror("Erro", "A pasta de destino não existe!")
            return False
            
        # Validação básica de URL do YouTube
        if "youtube.com" not in url.lower() and "youtu.be" not in url.lower():
            result = messagebox.askyesno(
                "Aviso", 
                "A URL não parece ser do YouTube. Deseja continuar mesmo assim?"
            )
            if not result:
                return False
        
        return True
    
    def start_download(self):
        """Inicia o processo de download em uma thread separada."""
        if not self.validate_inputs():
            return
            
        # Desabilitar botão durante o download
        self.download_button.config(state="disabled")
        self.progress.start(10)
        
        # Limpar status anterior
        self.status_text.delete(1.0, tk.END)
        self.update_status("Iniciando download... 🚀")
        
        # Executar download em thread separada
        self.download_thread = threading.Thread(
            target=self.download_worker,
            daemon=True
        )
        self.download_thread.start()
    
    def download_worker(self):
        """Worker thread para realizar o download."""
        try:
            url = self.url_var.get().strip()
            folder = self.folder_var.get().strip()
            
            self.update_status(f"URL: {url}")
            self.update_status(f"Destino: {folder}")
            self.update_status("-" * 50)
            
            # Redirecionar saída para capturar mensagens do yt-dlp
            import io
            import contextlib
            
            # Capturar stdout
            output_buffer = io.StringIO()
            
            with contextlib.redirect_stdout(output_buffer):
                # Chamar função de download
                baixar_audio(url, folder)
            
            # Obter saída capturada
            captured_output = output_buffer.getvalue()
            if captured_output:
                for line in captured_output.split('\n'):
                    if line.strip():
                        self.update_status(line)
            
            self.update_status("-" * 50)
            self.update_status("✅ Download concluído com sucesso!")
            
            # Perguntar se quer abrir a pasta
            self.root.after(0, self.ask_open_folder)
            
        except Exception as e:
            self.update_status(f"❌ Erro durante o download: {str(e)}")
            self.root.after(0, lambda: messagebox.showerror("Erro", f"Erro durante o download:\n{str(e)}"))
        
        finally:
            # Reabilitar interface
            self.root.after(0, self.download_finished)
    
    def ask_open_folder(self):
        """Pergunta se o usuário quer abrir a pasta de destino."""
        result = messagebox.askyesno(
            "Download Concluído", 
            "Download concluído com sucesso!\n\nDeseja abrir a pasta de destino?"
        )
        if result:
            self.open_destination_folder()
    
    def download_finished(self):
        """Chamado quando o download termina para reabilitar a interface."""
        self.progress.stop()
        self.download_button.config(state="normal")
        
    def on_closing(self):
        """Chamado quando a janela é fechada."""
        if self.download_thread and self.download_thread.is_alive():
            result = messagebox.askyesno(
                "Confirmar", 
                "Há um download em andamento. Deseja realmente fechar?"
            )
            if not result:
                return
        
        self.root.destroy()


def main():
    """Função principal da aplicação GUI."""
    # Criar janela principal
    root = tk.Tk()
    
    # Configurar estilo
    style = ttk.Style()
    
    # Tentar usar tema moderno se disponível
    try:
        style.theme_use('winnative')  # Windows
    except:
        try:
            style.theme_use('clam')  # Alternativa multiplataforma
        except:
            pass  # Usar tema padrão
    
    # Criar aplicação
    app = YouTubeAudioConverterGUI(root)
    
    # Configurar evento de fechamento
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Iniciar loop da interface
    root.mainloop()


if __name__ == "__main__":
    main()