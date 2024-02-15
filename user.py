from observer import Subject, Observer
from post_factory import PostFactory
from queue import Queue

"""
here we will use design pattern Observer with the help of our observer.py
"""
class User(Observer, Subject):
    def __init__(self, user_name, password):
        super(User, self).__init__()
        self.user_name = user_name
        self.following = {}  # users that this user follow
        self.posts = {}      # all the posts of this user
        self.notifications = Queue()
        self.connected = True
        self.password = password

    def __str__(self):
        return f"User name: {self.user_name}, Number of posts: {len(self.posts)}, Number of followers: {len(self.observers)}"

    def display(self):
        string = f"User name: {self.user_name}, Number of posts: {len(self.posts)}, Number of followers: {len(self.observers)}"
        return string

    def follow(self, user):
        """
        Follow a new user.
        """
        if user.user_name not in self.following:
            self.following[user.user_name] = user
            user.attach(self)
            print(f"{self.user_name} started following {user.user_name}")

    def unfollow(self, user):
        """
        Unfollow someone
        """
        if user.user_name in self.following:
            del self.following[user.user_name]
            user.detach(self)
            print(f"{self.user_name} unfollowed {user.user_name}")

    def update(self, message):
        self.notifications.put(message)  # new notif

    """
    here we create a new post with post factory and post and send notifs to the observers
    """
    def publish_post(self, type, description, price=0, localisation="", available=True):
        post = PostFactory.create_post(type, description, self, price, localisation, available)
        self.posts[description] = post
        self.notify_observers(f"{self.user_name} has a new post")
        print(post)
        return post

    def like(self, post):
        post.new_like(self)
        self.notify("like", post.author)

    def comment(self, post, the_comment):
        post.add_comment(self, the_comment)
        self.notify("comment", post.author, the_comment)

    def notify(self, type, user, comment=""):
        if self != user:        # don't send notif to himself
            if type == "like":
                str = f"{self.user_name} liked your post"
                user.notifications.put(str)
                print(f"notification to {user.user_name}: {str}")
            if type == "comment":
                str = f"{self.user_name} commented on your post"
                user.notifications.put(str)
                print(f"notification to {user.user_name}: {str}: {comment}")

    def print_notifications(self):      # print all the notifs of the user
        print(f"{self.user_name}'s notifications:")
        h = ""
        length = self.notifications.qsize()
        for i in range(length):
            h = self.notifications.get()
            print(h)
            self.notifications.put(h)

