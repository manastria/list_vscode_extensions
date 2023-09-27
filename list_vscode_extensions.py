import subprocess

def get_installed_extensions():
    result = subprocess.run('code --list-extensions', shell=True, stdout=subprocess.PIPE)
    extensions = result.stdout.decode('utf-8').strip().split('\n')
    return extensions

def generate_markdown_links(extensions):
    with open("extensions_list.md", "w", encoding='utf-8') as f:
        f.write("# Liste des plugins installés avec lien vers le Marketplace\n\n")
        for ext in extensions:
            f.write(f"- [{ext}](https://marketplace.visualstudio.com/items?itemName={ext})\n")

if __name__ == '__main__':
    extensions = get_installed_extensions()
    generate_markdown_links(extensions)
