from PIL import Image

# Buka citra RGB
rgb_image = Image.open('mawar.jpg')

# Konversi citra RGB ke grayscale
grayscale_image = rgb_image.convert('L')

# Konversi citra grayscale ke biner
threshold = 128
binary_image = grayscale_image.point(lambda x: 0 if x < threshold else 255, '1')

# Penskalaan citra
scale = 0.5
scaled_image = binary_image.resize((int(binary_image.width*scale), int(binary_image.height*scale)))

# Simpan citra hasil pengolahan
grayscale_image.save('grayscale_image.jpg')
binary_image.save('binary_image.jpg')
scaled_image.save('scaled_image.jpg')
