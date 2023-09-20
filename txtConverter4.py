import os

# Set this to True if you want to surround the numbers with double quotes 
is_text = False 


def convert_text_file_to_string(input_file_path, output_file_path, isText=False, encoding='utf-8'):
    try:
        if not os.path.exists(input_file_path):
            return f'Error: Input file "{input_file_path}" not found.'

        with open(input_file_path, 'r', encoding=encoding) as input_file:
            lines = input_file.readlines()

        line_count = len(lines)
        if line_count == 0:
            return f'Error: Input file "{input_file_path}" is empty.'

        # Remove leading and trailing whitespace, and optionally add double quotes
        lines = [line.strip() if not isText else '"' + line.strip() + '"' for line in lines]

        first_10000_lines = lines[:10000]
        remaining_lines = lines[10000:]

        # Join the lines into two strings
        output_string1 = ', '.join(first_10000_lines)
        output_string2 = ', '.join(remaining_lines)

        # Write the two strings to the output file
        with open(output_file_path, 'w', encoding=encoding) as output_file:
            output_file.write(output_string1 + '\n')
            output_file.write(output_string2 + '\n')

        return f'Success: Output saved to {output_file_path}.'
    except Exception as e:
        return str(e)

# Example usage:
input_file_path = 'input.txt'
output_file_path = 'output.txt'

result = convert_text_file_to_string(input_file_path, output_file_path, is_text)

print(result)
