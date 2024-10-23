from app import create_app

# Create the application
app = create_app()

# Run the application if the file is called directly
if __name__ == "__main__":
    app.run(debug=False)