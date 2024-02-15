import matplotlib.pyplot as plt
from matplotlib import image as mpimg


class Post:
    def __init__(self, author):
        self.author = author
        self.likes = 0
        self.liked_by = set()  # who liked the post
        self.comments = []

    def __str__(self):
        pass

    def new_like(self, author):
        if author.user_name not in self.liked_by:  # check that a user don't like a post twice
            self.likes += 1
            self.liked_by.add(author.user_name)

    def like(self, user):
        user.like(self)

    def unlike(self, author):
        if author.user_name in self.liked_by:
            self.likes -= 1 if self.likes > 0 else 0
            self.liked_by.remove(author.user_name)

    def add_comment(self, author, comment):  # for add the comment to the post himself
        self.comments.append((author, comment))

    def comment(self, user, comment):
        user.comment(self, comment)

    def display(self):
        pass


class TextPost(Post):
    def __init__(self, content, author):
        super().__init__(author)
        self.content = content

    def __str__(self):
        return f'{self.author.user_name} published a post:\n"{self.content}"\n'

    def display(self):
        print(f"{self.author.user_name} published a post:")
        print(f'"{self.content}"')


class ImagePost(Post):
    def __init__(self, image_path, author):
        super().__init__(author)
        self.image_path = image_path  # this is the path to the image
        self.author = author

    def __str__(self):
        return f"{self.author.user_name} posted a picture\n"

    def display(self):
        print("Shows picture")
        self.show_image()

    def show_image(self):
        try:
            img = mpimg.imread(self.image_path)  # try to load the image
            plt.figure()
            plt.imshow(img)
            plt.show()
        except FileNotFoundError:
            pass  # the path doesn't exist
        except Exception:
            pass  # the path doesn't exist


class SalePost(Post):

    def __init__(self, description, author, price=0, localisation="", available=True):
        super().__init__(author)
        self.description = description
        self.price = price
        self.localisation = localisation
        self.availablility = available   # bollean if the product was sold or not

    def __str__(self):
        status_availability = "For sale!" if self.availablility else "Sold!"
        result = (f"{self.author.user_name} posted a product for sale:\n{status_availability}"
                  f" {self.description}, price: {self.price}, pickup from: {self.localisation}")
        result += "\n"
        return result

    def set_availability(self):
        self.availablility = False

    def discount(self, x, password):
        if self.author.password == password:   # check the password for apply the discount
            self._apply_discount(x)
            print(f"Discount on {self.author.user_name} product! the new price is: {self.price}")

    def _apply_discount(self, x):
        if x <= 100:
            h = 100 - x
            self.price *= (h / 100)
        else:
            self.price = 0

    def sold(self, password):
        if self.author.password == password:   # check the password for apply the sold
            self._apply_sold()

    def _apply_sold(self):
        self.availablility = False
        str = f"{self.author.user_name}'s product is sold"
        print(str)

    def display(self):
        str = (f"{self.author.user_name} posted a product for sale:\n"
               f"For sale! {self.description}, price: {self.price}, pickup from: {self.localisation}")
        print(str)
