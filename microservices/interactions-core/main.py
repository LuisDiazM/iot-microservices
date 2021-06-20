from app.appRoutes import app
# from dotenv import load_dotenv
app_run = app
if __name__ == "__main__":
    # load_dotenv()
    app.run(debug=True)
    
