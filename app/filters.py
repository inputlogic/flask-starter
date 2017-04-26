from . import app


# Example
# {{ 'hello'|reverse }} -> olleh
@app.template_filter()
def reverse(text):
    return text[::-1]
