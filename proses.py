from PIL import Image

# upload file gambar
rgb_image = Image.open('mawar.jpg')

# Konversi citra RGB => grayscale
grayscale_image = rgb_image.convert('L')

# Konversi citra grayscale => biner
threshold = 128
binary_image = grayscale_image.point(
    lambda x: 0 if x < threshold else 255, '1')

# Penskalaan
scale = 0.5
scaled_image = binary_image.resize(
    (int(binary_image.width*scale), int(binary_image.height*scale)))

# Simpan citra hasil pengolahan
grayscale_image.save('gambar_grayscale.jpg')
binary_image.save('gambar_binary.jpg')
scaled_image.save('gambar_scaled.jpg')
