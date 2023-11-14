
# bibliotecas necessárias:
# pip install Pillow
# pip install rembg
# pip install easygui

#usei easygui para ficar mais dinâmico

from rembg import remove
from PIL import Image
import easygui as eg

input_path = eg.fileopenbox(title='Selecionar imagem')

output_path = eg.filesavebox(title='Salvar arquivo em..')

input = Image.open(input_path)

output = remove(input)

output.save(output_path)