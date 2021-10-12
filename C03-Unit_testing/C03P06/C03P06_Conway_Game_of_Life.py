from PIL import Image
import random


class ConwayGame:

    def __init__(self, height, width, white_pixels):
        self.height = height
        self.width = width
        self.white_pixels = white_pixels
        self.white = 1
        self.black = 0

    def structure(self):
        images = []

        first_image = {}
        for cell in range(self.height * self.width):
            first_image[cell] = self.black

        for cell in self.white_pixels:
            first_image[cell] = self.white

        images.append(first_image)

        # check if two consecutive images are equal, or if there is infinity loop of images
        while images[-1] != self.calculate_next_image(images[-1]):
            images.append(self.calculate_next_image(images[-1]))
            if len(images) > 2:
                if images[-1] == images[-3]:
                    break

        return self.construct_gif(images)

    def calculate_next_image(self, previous_image):

        next_image = {}

        directions = {
            'left': -1,
            'right': 1,
            'top': - self.width,
            'bottom': self.width,
            'top_left': - self.width - 1,
            'top_right': - self.width + 1,
            'bottom_left': self.width - 1,
            'bottom_right': self.width + 1
        }

        # make image_dict by calculating the previous one
        for key, val in previous_image.items():

            # if the pixel is alive(white), decides to live or not
            if val == 1:
                white_neighbours = 0

                for direction in directions.values():
                    if self.is_key_existing(previous_image, key + direction) and previous_image[key + direction] == 1:
                        white_neighbours += 1

                if white_neighbours in range(2, 4):
                    next_image[key] = 1
                else:
                    next_image[key] = 0

            # if it is dead(black), decides to revive it or not
            if val == 0:
                white_neighbours = 0

                for direction in directions.values():
                    if self.is_key_existing(previous_image, key + direction) and previous_image[key + direction] == 1:
                        white_neighbours += 1

                if white_neighbours == 3:
                    next_image[key] = 1
                else:
                    next_image[key] = 0

        return next_image

    def construct_gif(self, images):

        image_stack = []

        for image in images:
            im = Image.new('RGB', (self.height, self.width), self.black)
            pixel = im.load()
            for value in enumerate(image.values()):
                if value[1] == self.white:
                    pixel[value[0] // self.width, value[0] % self.width] = (255, 255, 255)
            image_stack.append(im)

        image_stack[0].save('out.gif',
                            save_all=True,
                            append_images=image_stack[1:],
                            optimize=False,
                            duration=300
                            )

    def is_key_existing(self, cells_map, key):

        try:
            if cells_map[key]:
                return True

        except KeyError:
            return False

    def run_app(self):
        return self.structure()


if __name__ == '__main__':
    app = ConwayGame(100, 100, [random.randint(5000, 7000) for n in range(300)])
    app.run_app()

