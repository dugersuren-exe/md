import os

def find_md_files(directory='.'):
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and file != 'README.md':
                path = os.path.relpath(os.path.join(root, file), directory)
                md_files.append(path)
    return md_files

def generate_menu(md_files):
    menu = '# Автомат меню\n\n'
    for md in md_files:
        title = os.path.splitext(os.path.basename(md))[0].replace('_', ' ').capitalize()
        menu += f'- [{title}]({md})\n'
    return menu

def main():
    md_files = find_md_files()
    menu = generate_menu(md_files)
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(menu)
        f.write('\n---\n')
        f.write('## Төслийн тухай\nТайлбар хэсэг...')

if __name__ == "__main__":
    main()