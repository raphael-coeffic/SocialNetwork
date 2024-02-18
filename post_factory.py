from post import Post, TextPost, ImagePost, SalePost


class PostFactory:

    """
    We use design pattern Factory for implement the creation of post.
    """
    @staticmethod
    def create_post(post_type, description, user, price=0, localisation="", available=True):
        if post_type == "Text":
            return TextPost(description, user)
        elif post_type == "Image":
            return ImagePost(description, user)
        elif post_type == "Sale":
            return SalePost(description, user, price, localisation, available)
        else:
            raise ValueError("")
