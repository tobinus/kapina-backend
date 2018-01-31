from sorl.thumbnail import get_thumbnail


class Thumbnail:
    def __init__(self, image):
        self.image = image

    def generate_crop(self, thumb_size):
        thumb_image = get_thumbnail(
            self.image, thumb_size,
            crop='center', quality=99
        )
        return thumb_image.url

    @property
    def large(self):
        return self.generate_crop('1024x576')

    @property
    def medium_large(self):
        return self.generate_crop('768x432')

    @property
    def medium(self):
        return self.generate_crop('300x168')

    @property
    def thumbnail(self):
        return self.generate_crop('150x84')
