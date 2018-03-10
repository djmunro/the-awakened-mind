from post import Post
from post_html_generator import PostHtmlGenerator


def post_content():
    return '''
        ---
        title: Why the minimal-blog is there?
        foo: bar
        ---

        Name of the post
        '''


def generate():
    return PostHtmlGenerator(Post(post_content())).render_template('template.html')


if __name__ == '__main__':
    print generate()