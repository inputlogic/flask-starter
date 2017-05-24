from .. import app


handler = app()


@handler.template_filter()
def reverse(text):
    return text[::-1]
