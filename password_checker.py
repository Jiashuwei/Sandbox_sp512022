
def is_valid_password(text):
    return 8 <= len(text) <= 20

def main():
    new_password = "hello world"
    print(f"{new_password} is a valid password? {is_valid_password(new_password)}")


if __name__ == '__mian__':
    main()