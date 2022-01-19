from app import app
import views
import management.commands

if __name__ == '__main__':
    app.run(debug=True)
