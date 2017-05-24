def setup(app):
    app.add_template_filter(reverse)


def reverse(text):
    return text[::-1]
