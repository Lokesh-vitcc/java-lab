import sys
from pygments import highlight
from pygments.lexers import JavaLexer
from pygments.formatters import TerminalFormatter
from termcolor import cprint
import docx
def highlight_java_code(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    # Highlight the code using Pygments
    lexer = JavaLexer()
    formatter = TerminalFormatter()
    highlighted_code = highlight(code, lexer, formatter)
    doc = docx.Document()
    doc.add_paragraph(highlighted_code)
    doc.save("test.docx")
    # Print the highlighted code to the terminal
    cprint(highlighted_code, 'white', 'on_black')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python highlight_java.py <path_to_java_file>")
        sys.exit(1)

    java_file_path = sys.argv[1]
    highlight_java_code(java_file_path)

# https://stackoverflow.com/questions/41979095/write-text-in-particular-font-color-in-ms-word-using-python-docx