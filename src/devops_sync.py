# src/devops_sync.py
import os
import json
from datetime import datetime
from git import Repo

def load_settings():
    with open(os.path.join('src', 'config', 'settings.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def commit_and_push():
    settings = load_settings()
    repo = Repo(settings['repo_path'])
    repo.git.add(all=True)
    msg = f"{settings.get('commit_message_prefix', '[ADF Backup]')} {datetime.utcnow().isoformat()}Z"
    if repo.is_dirty(untracked_files=True):
        repo.index.commit(msg)
        origin = repo.remote(name='origin')
        origin.push()
        print(f'Commit e push realizados: {msg}')
    else:
        print('Sem mudanças para commit.')

if __name__ == '__main__':
    commit_and_push()
