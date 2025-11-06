"""
Gerador de Ícone para YouTube Audio Converter
============================================
Este script cria um ícone simples usando PIL (Pillow) para o executável.
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    def create_icon():
        """Cria um ícone simples para o YouTube Audio Converter."""
        
        # Tamanhos padrão para ícones do Windows
        sizes = [16, 32, 48, 64, 128, 256]
        
        # Criar ícone principal (256x256)
        size = 256
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Cores
        bg_color = (220, 38, 38)  # Vermelho YouTube-like
        text_color = (255, 255, 255)  # Branco
        border_color = (153, 27, 27)  # Vermelho escuro
        
        # Desenhar círculo de fundo
        margin = 10
        circle_coords = [margin, margin, size-margin, size-margin]
        draw.ellipse(circle_coords, fill=bg_color, outline=border_color, width=4)
        
        # Desenhar símbolo de música (nota musical simplificada)
        center_x, center_y = size // 2, size // 2
        
        # Haste da nota
        stem_width = 8
        stem_height = size // 3
        stem_x = center_x + 20
        stem_y1 = center_y - stem_height // 2
        stem_y2 = center_y + stem_height // 2
        
        draw.rectangle([stem_x - stem_width//2, stem_y1, stem_x + stem_width//2, stem_y2], 
                      fill=text_color)
        
        # Cabeça da nota
        note_radius = 25
        note_x = center_x - 15
        note_y = center_y + 15
        
        draw.ellipse([note_x - note_radius, note_y - note_radius//2, 
                     note_x + note_radius, note_y + note_radius//2], 
                    fill=text_color)
        
        # Adicionar texto "MP3" pequeno
        try:
            # Tentar usar uma fonte do sistema
            font_size = size // 8
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            # Fallback para fonte padrão
            font = ImageFont.load_default()
        
        text = "MP3"
        # Calcular posição do texto
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = (size - text_width) // 2
        text_y = size - 50
        
        draw.text((text_x, text_y), text, fill=text_color, font=font)
        
        # Salvar como ICO
        icon_path = "app_icon.ico"
        
        # Criar múltiplas versões em tamanhos diferentes
        icon_images = []
        for icon_size in sizes:
            resized = img.resize((icon_size, icon_size), Image.Resampling.LANCZOS)
            icon_images.append(resized)
        
        # Salvar como arquivo .ico
        img.save(icon_path, format='ICO', sizes=[(s, s) for s in sizes])
        
        print(f"✅ Ícone criado com sucesso: {icon_path}")
        print(f"📏 Tamanhos incluídos: {sizes}")
        
        return icon_path
    
    if __name__ == "__main__":
        create_icon()
        
except ImportError:
    print("❌ Pillow não está instalado!")
    print("💡 Instale com: pip install Pillow")
    print("🔄 Ou use um ícone existente renomeando para 'app_icon.ico'")