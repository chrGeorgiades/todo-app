import gkeepapi

# Initialize the client
keep = gkeepapi.Keep()

# Login (replace with your credentials)
try:
    keep.authenticate('kitosapoel@gmail.com', '758597099123-p7ghauvlg1i2uujgnsq3fqame80nmrfs.apps.googleusercontent.com')
    print("Successfully logged in!")
    
    # Sync with Google Keep
    keep.sync()
    print("Sync completed!")
    
except Exception as e:
    print(f"Error: {e}")