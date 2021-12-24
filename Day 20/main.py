with open('Day 20/input.txt') as f:
    enhancement_algo, image = f.read().strip().split('\n\n')

image = [row.replace('#', '1').replace('.', '0') for row in image.split('\n')]
enhancement_algo = enhancement_algo.replace('#', '1').replace('.', '0')

def get_enhanced_pixel(neighbor_pixels):
    return enhancement_algo[int(neighbor_pixels, 2)]

lit_pixels = set()
for i, row in enumerate(image):
    for j, pixel in enumerate(row):
        if pixel == '1': lit_pixels.add((i, j))

# if the 0th index is a lit pixel, then we can't track all lit pixels
# because after iteration 1 there will be an infinite amount
# so we set a toggle flag to know that we track lit, then unlit pixels
toggle = enhancement_algo[0] == '1'

def enhance_pixel(pixels, pixel, pixel_type_return):
    neighbor_string = ''
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor = (pixel[0] + i, pixel[1] + j)
            if neighbor in pixels: neighbor_string += str(1 - int(pixel_type_return))
            else: neighbor_string += pixel_type_return

    return get_enhanced_pixel(neighbor_string)

def enhance_image(pixels, pixel_type_return):
    enhanced_image = set()

    pixels_to_update = set()
    for pixel in pixels:
        for i in range(-1, 2):
            for j in range(-1, 2):
                pixels_to_update.add((pixel[0] + i, pixel[1] + j))

    for pixel in pixels_to_update:
        enhanced_pixel = enhance_pixel(pixels, pixel, pixel_type_return)
        if enhanced_pixel == pixel_type_return: enhanced_image.add(pixel)

    return enhanced_image

def print_image(lit_pixels):
    min_x = min(pixel[0] for pixel in lit_pixels)
    max_x = max(pixel[0] for pixel in lit_pixels)
    min_y = min(pixel[1] for pixel in lit_pixels)
    max_y = max(pixel[1] for pixel in lit_pixels)

    for i in range(min_x, max_x + 1):
        line = ''
        for j in range(min_y, max_y + 1):
            if (i, j) in lit_pixels: line += '#'
            else: line += '.'
        print(line)

enhanced = enhance_image(lit_pixels, '0')
double_enhanced = enhance_image(enhanced, '1')
print(len(double_enhanced))

lit_image = lit_pixels
for i in range(25):
    unlit_image = enhance_image(lit_image, '0')
    lit_image = enhance_image(unlit_image, '1')
print(len(lit_image))