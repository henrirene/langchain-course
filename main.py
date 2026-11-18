from dotenv import load_dotenv
import os


load_dotenv()

def main():
    print("hello to linkchain")
    print(os.environ.get("OPEN_AI_API"))


if __name__ == "__main__":
    main()


