elif index == 9:  # Crop image (center crop as an example)
            width, height = current_image.size
            left = (width - 300) / 2
            top = (height - 300) / 2
            right = (width + 300) / 2
            bottom = (height + 300) / 2
            res_image = current_image.crop((left, top, right, bottom))
            res_array = np.array(res_image)