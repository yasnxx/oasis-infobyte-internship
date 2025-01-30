import ipywidgets as widgets
import string
import random
import pyperclip
from IPython.display import display

def generate_password(change):
    length = length_var.value
    if length <= 0:
        output_label.value = "Please enter a valid password length."
        return

    character_set = ''
    if uppercase_var.value:
        character_set += string.ascii_uppercase
    if lowercase_var.value:
        character_set += string.ascii_lowercase
    if digits_var.value:
        character_set += string.digits
    if symbols_var.value:
        character_set += string.punctuation

    if not character_set:
        output_label.value = "Please select at least one character set."
        return

    password = ''.join(random.choice(character_set) for _ in range(length))
    password_entry.value = password
    output_label.value = ""

def copy_password(change):
    password = password_entry.value
    if password:
        pyperclip.copy(password)
        output_label.value = "Password copied to clipboard successfully!"
    else:
        output_label.value = "No password to copy!"

length_label = widgets.Label(value="Password Length:")
length_var = widgets.IntText(value=8, description="Length:", min=1)

uppercase_var = widgets.Checkbox(value=True, description="Uppercase")
lowercase_var = widgets.Checkbox(value=True, description="Lowercase")
digits_var = widgets.Checkbox(value=True, description="Digits")
symbols_var = widgets.Checkbox(value=True, description="Symbols")

generate_button = widgets.Button(description="Generate Password", button_style="success")
generate_button.on_click(generate_password)

password_entry = widgets.Text(description="Generated Password:", disabled=True)
copy_button = widgets.Button(description="Copy Password", button_style="info")
copy_button.on_click(copy_password)

output_label = widgets.Label(value="")

display(length_label, length_var, uppercase_var, lowercase_var, digits_var, symbols_var, generate_button, password_entry, copy_button, output_label)
