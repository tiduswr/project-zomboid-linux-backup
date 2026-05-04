#!/usr/bin/env python3

import os
import zipfile
from datetime import datetime
import shutil
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

console = Console()

# Caminhos
HOME = os.path.expanduser("~")
SAVE_DIR = os.path.join(HOME, ".var/app/com.valvesoftware.Steam/Zomboid/Saves")
BACKUP_DIR = os.path.join(HOME, "temp/Zomboid/Saves")

os.makedirs(BACKUP_DIR, exist_ok=True)


def listar_backups(show_table=True):
    files = sorted(os.listdir(BACKUP_DIR))

    if not files:
        console.print("[red]Nenhum backup encontrado.[/red]")
        return []

    if show_table:
        table = Table(title="📦 Backups disponíveis")
        table.add_column("Arquivo", style="cyan")
        table.add_column("Tamanho", style="magenta")

        for f in files:
            size = os.path.getsize(os.path.join(BACKUP_DIR, f)) // 1024
            table.add_row(f, f"{size} KB")

        console.print(table)

    return files


def criar_backup():
    console.print(Panel("📦 Criando backup...", style="blue"))

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = f"zomboid_saves_{timestamp}.zip"
    zip_path = os.path.join(BACKUP_DIR, zip_name)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(SAVE_DIR):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, SAVE_DIR)
                zipf.write(full_path, rel_path)

    console.print(f"[green]✔ Backup criado:[/green] {zip_name}")


def restaurar_backup():
    backups = listar_backups()

    if not backups:
        return

    nome = Prompt.ask("\nDigite o nome do backup")

    if nome not in backups:
        console.print("[red]Arquivo não encontrado![/red]")
        return

    zip_path = os.path.join(BACKUP_DIR, nome)

    if os.path.exists(SAVE_DIR):
        if Confirm.ask("Deseja apagar os saves atuais?"):
            shutil.rmtree(SAVE_DIR)

    os.makedirs(SAVE_DIR, exist_ok=True)

    console.print(Panel("♻ Restaurando backup...", style="yellow"))

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(SAVE_DIR)

    console.print("[green]✔ Backup restaurado com sucesso![/green]")


def deletar_backup():
    backups = listar_backups()

    if not backups:
        return

    nome = Prompt.ask("Digite o nome do backup para deletar")

    if nome not in backups:
        console.print("[red]Arquivo não encontrado![/red]")
        return

    if Confirm.ask(f"Tem certeza que deseja deletar '{nome}'?"):
        os.remove(os.path.join(BACKUP_DIR, nome))
        console.print("[green]✔ Backup removido![/green]")


def menu():
    while True:
        console.print(Panel("🧟 Project Zomboid Backup Manager", style="bold cyan"))

        console.print("""
[1] Criar backup
[2] Restaurar backup
[3] Listar backups
[4] Deletar backup
[0] Sair
""")

        op = Prompt.ask("Escolha", default="0")

        if op == "1":
            criar_backup()
        elif op == "2":
            restaurar_backup()
        elif op == "3":
            listar_backups()
        elif op == "4":
            deletar_backup()
        elif op == "0":
            console.print("[bold]Saindo...[/bold]")
            break
        else:
            console.print("[red]Opção inválida![/red]")


if __name__ == "__main__":
    menu()
