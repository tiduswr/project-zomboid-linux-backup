# 🧟 Project Zomboid Backup Manager (Linux)

Um gerenciador de backups simples e elegante para os saves do **Project Zomboid**, feito em Python e com interface de terminal amigável.

> ⚠️ Este projeto é **exclusivo para Linux**, com suporte focado na versão Flatpak da Steam.

---

## 📦 Funcionalidades

* ✔ Criar backup dos saves
* ✔ Restaurar backups facilmente
* ✔ Listar backups disponíveis
* ✔ Deletar backups antigos
* ✔ Interface bonita no terminal (usando Rich)
* ✔ Caminhos corrigidos (sem problemas de path absoluto)

---

## 🐧 Compatibilidade

Este script foi desenvolvido para:

* Sistemas Linux
* Instalação via Flatpak da Steam

Caminho padrão dos saves:

```bash
~/.var/app/com.valvesoftware.Steam/Zomboid/Saves
```

Backups são armazenados em:

```bash
~/temp/Zomboid/Saves
```

---

## ⚙️ Requisitos

* Python 3.8+
* Biblioteca `rich`

Instale com:

```bash
pip install rich
```

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/zomboid-backup.git
cd zomboid-backup
```

---

### 2. Dê permissão de execução

```bash
chmod +x zomboid_backup.py
```

---

### 3. Execute o programa

```bash
./zomboid_backup.py
```

---

## 🎮 Interface

O programa apresenta um menu interativo no terminal:

```
🧟 Project Zomboid Backup Manager

[1] Criar backup
[2] Restaurar backup
[3] Listar backups
[4] Deletar backup
[0] Sair
```

---

## 🧠 Como funciona

O script:

* Compacta apenas o conteúdo da pasta `Saves`
* Remove caminhos absolutos (evita erros na restauração)
* Permite restaurar diretamente no diretório correto

Estrutura do backup:

```
Sandbox/
Survival/
Multiplayer/
```

---

## ⚠️ Importante

* ❌ Não use `sudo` para rodar o script
* ✔ Execute como usuário normal
* ⚠️ O restore pode sobrescrever seus saves atuais (há confirmação)

---

## 💡 Possíveis melhorias futuras

* Backup automático (cron)
* Detecção de múltiplas instalações (Steam normal vs Flatpak)
* CLI estilo `git` (`backup`, `restore`, etc.)
* Barra de progresso

---

## 📄 Licença

MIT

---

## 🤝 Contribuição

Pull requests são bem-vindos!

Se encontrar bugs ou quiser sugerir melhorias, abra uma issue 🚀
