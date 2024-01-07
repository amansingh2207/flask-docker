from app import create_app

#Entrypoint of code is here
app = create_app()

if __name__ == "__main__":
    app.run()