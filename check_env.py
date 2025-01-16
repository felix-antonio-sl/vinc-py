import os

def main():
    database_url = os.getenv('DATABASE_URL')
    print(f"DATABASE_URL: {database_url}")

if __name__ == "__main__":
    main() 