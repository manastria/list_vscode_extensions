import subprocess

def get_installed_extensions():
    result = subprocess.run('code --list-extensions', shell=True, stdout=subprocess.PIPE)
    extensions = result.stdout.decode('utf-8').strip().split('\n')
    return extensions

def generate_install_script(extensions):
    with open("vscode_install.cmd", "w") as f:
        for ext in extensions:
            f.write(f"call code --install-extension {ext}\n")

if __name__ == '__main__':
    extensions = get_installed_extensions()
    generate_install_script(extensions)
