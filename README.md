# VS Code Extensions Management Scripts

Ce dépôt contient deux scripts Python pour gérer les extensions de Visual Studio Code :

1. `generate_vscode_extensions_list.py` : Génère une liste des extensions installées avec des liens vers le Visual Studio Marketplace.
2. `generate_vscode_install_script.py` : Crée un fichier `.cmd` contenant des commandes pour réinstaller toutes les extensions actuellement installées.

## Prérequis

- Python 3.x
- Visual Studio Code

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers sur votre machine.
2. Ouvrez un terminal et naviguez vers le dossier contenant le script.

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers sur votre machine.
2. Ouvrez un terminal et naviguez vers le dossier contenant les scripts.

## Utilisation

### Générer la liste des extensions

Exécutez le script suivant pour générer une liste Markdown des extensions installées :

```bash
python generate_vscode_extensions_list.py
```

Cela créera un fichier `extensions_list.md` avec la liste des extensions et des liens vers le Visual Studio Marketplace.

### Générer le script d'installation

Exécutez le script suivant pour générer un fichier `.cmd` pour réinstaller les extensions :

```bash
python generate_vscode_install_script.py
```

Cela générera un fichier `vscode_install.cmd` que vous pourrez exécuter pour installer toutes les extensions en une seule fois.

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
