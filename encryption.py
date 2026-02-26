from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    
    # Use max length to handle odd-length messages
    max_len = max(len(even_letters), len(odd_letters))
    for i in range(max_len):
        if i < len(odd_letters):
            letter_list.append(odd_letters[i])
        if i < len(even_letters):
            letter_list.append(even_letters[i])
    
    new_message = ''.join(letter_list)
    return new_message

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message


while True:
    task = get_task()
    if task is None:
        break
    task = task.lower()

    if task == 'encrypt':
        message = get_message()
        if message:
            encrypted = swap_letters(message)
            messagebox.showinfo('Ciphertext of the secret message is:', encrypted)

    elif task == 'decrypt':
        message = get_message()
        if message:
            decrypted = swap_letters(message)  # Works correctly now
            messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break

root = Tk()
root.mainloop()