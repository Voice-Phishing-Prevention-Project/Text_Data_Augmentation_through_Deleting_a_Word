import os
import random

def remove_random_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()

        if len(words) > 1:  # Ensure there's at least one word to remove
            index_to_remove = random.randint(0, len(words) - 1)
            words.pop(index_to_remove)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(' '.join(words))

def process_files(folder_path):
    for i in range(1, 2233):
        print("완료")
        file_name = f"file ({i}).txt"
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            remove_random_word(file_path)

if __name__ == "__main__":
    folder_path = r"C:\Users\USER\Desktop\Data Augmentation_단어 삭제(수사기관 사칭형)"
    process_files(folder_path)
