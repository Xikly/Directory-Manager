from deep_translator import GoogleTranslator
import os

def file_translator(directory):
    first_loop = True

    while True:
        if first_loop is False:
            option = int(input("1 to go again, 0 to main menu\n\nOption: "))
            if option == 0: main_menu(directory)

        files = []

        for file in os.listdir(directory):
            if not os.path.isdir(file): files.append(f"{file}")

        translated_files = 0

        for file in files:
            translate_file = GoogleTranslator(source='auto', target='en').translate(file)
            os.rename(f"{directory}\\{file}", f"{directory}\\{translate_file}")
            translated_files += 1
            print(f"TRANSLATED | {file} TO {translate_file}")
        
        print(f"------------------\nTRANSLATED {translated_files} FILES\n------------------")

        first_loop = False

def file_word_remover(directory):
    first_loop = True

    while True:
        if first_loop is False:
            option = int(input("1 to go again, 0 to main menu\n\nOption: "))
            if option == 0: main_menu(directory)

        word_to_remove = input("Word to remove: ")

        files_changed = 0

        for file in os.listdir(directory):
            if not os.path.isdir(f"{directory}\\{file}"):
                new_name = file.replace(word_to_remove, '')
                os.rename(f"{directory}\\{file}", f"{directory}\\{new_name}")
                files_changed += 1
                print(f"RENAMED | {file} -> {new_name}")
        
        print(f"------------------\nChanged {files_changed} files...\n------------------")

        first_loop = False

def main_menu(directory):
    option = int(input(f"\n----------------------\n1. File Translator\n2. File Word Remover\n\nOption: "))

    if option == 1: file_translator(directory)
    if option == 2: file_word_remover(directory)

if __name__ == "__main__":
    directory = input("Directory to work with: ")
    main_menu(directory)