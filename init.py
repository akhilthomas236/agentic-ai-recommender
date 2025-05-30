"""
Initialization script to ensure proper folder structure and default files
"""
import os
import shutil

def ensure_directory_exists(dir_path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Created directory: {dir_path}")

def main():
    """Main initialization function"""
    # Ensure all required directories exist
    ensure_directory_exists("src")
    ensure_directory_exists("src/components")
    ensure_directory_exists("src/data")
    ensure_directory_exists("src/utils")
    
    # Check if the CSS file exists, if not create an empty one
    css_path = "src/components/styles.css"
    if not os.path.exists(css_path):
        with open(css_path, "w") as f:
            f.write("/* Custom styles for AI Agentic Tool Recommender */")
        print(f"Created empty CSS file: {css_path}")
    
    print("Initialization completed successfully!")

if __name__ == "__main__":
    main()
