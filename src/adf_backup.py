# src/adf_backup.py
import os
import json
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient

from utils.logger import get_logger

# Inicializa logger
log = get_logger("adf_backup")

def load_settings():
    with open(os.path.join('src', 'config', 'settings.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def ensure_dirs(base):
    for d in ['pipelines', 'datasets', 'linkedServices', 'triggers']:
        os.makedirs(os.path.join(base, d), exist_ok=True)

def write_json(base, subdir, name, content):
    path = os.path.join(base, subdir, f'{name}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(content.as_dict() if hasattr(content, 'as_dict') else content, f, indent=2)
    log.debug(f"Arquivo exportado: {path}")
    return path

def export_adf():
    settings = load_settings()
    cred = DefaultAzureCredential()
    client = DataFactoryManagementClient(cred, settings['subscription_id'])

    rg = settings['resource_group']
    adf_name = settings['data_factory_name']

    log.info(f"Iniciando exportação do Data Factory: {adf_name} no resource group {rg}")

    # diretório atual e snapshot
    base_current = os.path.join(settings['backup_root'], settings['workspace_name'])
    ts = datetime.utcnow().strftime('%Y-%m-%d_%H%M%S')
    base_snapshot = os.path.join(settings['backup_root'], 'snapshots', ts)

    for base in [base_current, base_snapshot]:
        ensure_dirs(base)

    # pipelines
    for p in client.pipelines.list_by_factory(rg, adf_name):
        pipeline = client.pipelines.get(rg, adf_name, p.name)
        write_json(base_current, 'pipelines', p.name, pipeline)
        write_json(base_snapshot, 'pipelines', p.name, pipeline)
        log.info(f"Pipeline exportado: {p.name}")

    # datasets
    for d in client.datasets.list_by_factory(rg, adf_name):
        dataset = client.datasets.get(rg, adf_name, d.name)
        write_json(base_current, 'datasets', d.name, dataset)
        write_json(base_snapshot, 'datasets', d.name, dataset)
        log.info(f"Dataset exportado: {d.name}")

    # linked services
    for ls in client.linked_services.list_by_factory(rg, adf_name):
        linked_service = client.linked_services.get(rg, adf_name, ls.name)
        write_json(base_current, 'linkedServices', ls.name, linked_service)
        write_json(base_snapshot, 'linkedServices', ls.name, linked_service)
        log.info(f"Linked Service exportado: {ls.name}")

    # triggers
    for t in client.triggers.list_by_factory(rg, adf_name):
        trigger = client.triggers.get(rg, adf_name, t.name)
        write_json(base_current, 'triggers', t.name, trigger)
        write_json(base_snapshot, 'triggers', t.name, trigger)
        log.info(f"Trigger exportado: {t.name}")

    log.info(f"Exportação concluída em {base_current} e snapshot {base_snapshot}")

if __name__ == '__main__':
    try:
        export_adf()
    except Exception as e:
        log.error(f"Erro durante exportação: {e}", exc_info=True)
