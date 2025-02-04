from Include.app import create_app, db
from flask_migrate import Migrate

app = create_app()

# Inicializar Flask-Migrate
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)  # Solo útil para desarrollo; Heroku ignorará `debug=True`