# src/devops_sync.py
import os
import json
from datetime import datetime
from git import Repo

from utils.logger import get_logger

# Inicializa logger
log = get_logger("devops_sync")

def load_settings():
    with open(os.path.join('src', 'config', 'settings.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def commit_and_push():
    settings = load_settings()
    repo = Repo(settings['repo_path'])

    log.info("Preparando commit e push para o repositório remoto...")

    repo.git.add(all=True)
    msg = f"{settings.get('commit_message_prefix', '[ADF Backup]')} {datetime.utcnow().isoformat()}Z"

    if repo.is_dirty(untracked_files=True):
        repo.index.commit(msg)
        log.info(f"Commit realizado: {msg}")

        try:
            origin = repo.remote(name='origin')
            origin.push()
            log.info("Push realizado com sucesso para o repositório remoto.")
        except Exception as e:
            log.error(f"Erro ao realizar push: {e}", exc_info=True)
    else:
        log.warning("Nenhuma alteração detectada. Commit não realizado.")

if __name__ == '__main__':
    try:
        commit_and_push()
    except Exception as e:
        log.error(f"Erro durante commit/push: {e}", exc_info=True)
