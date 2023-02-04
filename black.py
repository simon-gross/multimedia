

from PIL import Image

# Create a new image with the desired resolution
image = Image.new('RGB', (4096, 2048), color = (0, 0, 0))

# Save the image to a file
image.save(r'D:\ucloud\Multi\Projekt_2\finished_material_kapitel4\ende_schwarz\black_image.jpg')