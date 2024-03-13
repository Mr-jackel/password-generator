import string
import argparse
try:
    from secrets import choice
except ModuleNotFoundError:
    from random import choice


def generate_password(length=8, uppers=False, lowers=False, 
                      digits=False, symbols=False):
    all_charactors = ''
    
    if uppers:
        all_charactors += string.ascii_uppercase
    
    if lowers:
        all_charactors += string.ascii_lowercase
    
    if digits:
        all_charactors += string.digits
    
    if symbols:
        all_charactors += string.punctuation
    
    if all_charactors == '':
        all_charactors = string.ascii_letters
    
    return ''.join(choice(all_charactors) for _ in range(length))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This script for create password"
    )
    
    parser.add_argument("length", type=int, help="Length of password")
    parser.add_argument('-u', '--upper', help="Use uppercase charactors in password", action="store_true")
    parser.add_argument('-l', '--lower', help="Use lowercase charactors in password", action="store_true")
    parser.add_argument('-d', '--digit', help="Use number charactors in password", action="store_true")
    parser.add_argument('-s', '--symbol', help="Use symbol charactors in password", action="store_true")
    
    args = parser.parse_args()
    
    # Create password from arguments of user send it in terminal or cmd.
    print(generate_password(args.length, args.upper, args.lower, args.digit, args.symbol))
    
