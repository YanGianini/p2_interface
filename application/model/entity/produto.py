class Produto():
    def __init__(self, id=None, name=None, image=None, oldPrice=None, price=None, description=None, count=None, value=None):
        self._id = id
        self._name = name
        self._image = image
        self._oldPrice = oldPrice
        self._price = price
        self._description = description
        self._count = count
        self._value = value

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_image(self):
        return self._image

    def set_image(self, img):
        self._image = img

    def get_oldPrice(self):
        return self._oldPrice

    def set_oldPrice(self, oldprice):
        self._oldPrice = oldprice

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_count(self):
        return self._count

    def set_count(self, count):
        self._count = count

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value