# src/utils/logger.py
import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

def get_logger(
    name: str = "adf_backup",
    log_level: int = logging.INFO,
    log_dir: str = "logs",
    log_file: str = None,
    max_bytes: int = 5 * 1024 * 1024,  # 5 MB
    backup_count: int = 5
) -> logging.Logger:
    """
    Cria e retorna um logger configurado para console e arquivo.

    Args:
        name (str): Nome do logger.
        log_level (int): Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        log_dir (str): Diretório onde os arquivos de log serão armazenados.
        log_file (str): Nome do arquivo de log. Se None, usa timestamp.
        max_bytes (int): Tamanho máximo do arquivo antes da rotação.
        backup_count (int): Número de arquivos de backup mantidos.

    Returns:
        logging.Logger: Instância configurada do logger.
    """
    # Cria diretório de logs se não existir
    os.makedirs(log_dir, exist_ok=True)

    if log_file is None:
        log_file = f"{name}_{datetime.utcnow().strftime('%Y%m%d')}.log"

    log_path = os.path.join(log_dir, log_file)

    # Configuração básica
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.propagate = False  # evita duplicação em root logger

    # Formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # Handler para arquivo com rotação
    file_handler = RotatingFileHandler(
        log_path, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # Evita adicionar handlers duplicados
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


# Exemplo de uso
if __name__ == "__main__":
    log = get_logger("example")
    log.debug("Mensagem de debug")
    log.info("Mensagem informativa")
    log.warning("Aviso importante")
    log.error("Erro encontrado")
    log.critical("Erro crítico")
