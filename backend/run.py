from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)  # Solo útil para desarrollo; Heroku ignorará `debug=True`