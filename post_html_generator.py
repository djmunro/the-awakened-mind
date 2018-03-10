import os

from jinja2 import FileSystemLoader, Environment


class PostHtmlGenerator(object):

    def __init__(self, post):
        self.post = post

    def render_template(self, template):
        template_loader = FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), '_templates'))
        return Environment(loader=template_loader).get_template(template).render(post=self.post.headers)