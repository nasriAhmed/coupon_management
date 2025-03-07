from app.app import create_app

# Creating the Flask application
app = create_app()

# Display registered routes
print("\n List of registered Flask routes:")
for rule in app.url_map.iter_rules():
    print(rule)
print("\n")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
