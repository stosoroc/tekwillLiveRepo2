def self_correct_number_input():
    text = None
    try:
        text = input('Input Number')
        return float(text)
    except ValueError:
        print('Value is not a number')
        if text:
            # Try to remove all non number characters from text
            maybe_number = ''.join(a for a in text if a.isdigit() or a == '.')
            return float(maybe_number)



if __name__ == '__main__':
    print(self_correct_number_input())