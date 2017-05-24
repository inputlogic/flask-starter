# Make `app` available to the `flask run` command
from app import create_app
app = create_app()


# Only used if this file is run directly, the `make run` command does not
# execute this block
#
# Example: python run.py
if __name__ == '__main__':
    app.run()
