### Azure Data Factory + Azure DevOps**

**Versionamento, Governança e Backups Automatizados de Pipelines de Dados**


![Azure_Databricks01](https://github.com/user-attachments/assets/6ba56dfe-a8ea-40db-8529-209cbfb1437d) 



**Bootcamp Microsoft AI for Tech - Azure Databricks**

---


📌 **Visão Geral**

Este projeto demonstra como integrar Azure Data Factory (ADF) ao Azure DevOps (Git) para garantir versionamento, rastreabilidade e backups automatizados de pipelines e artefatos de dados.

A solução foi projetada para simular ambientes corporativos regulados, onde histórico de mudanças, rollback seguro e governança técnica são requisitos fundamentais — e não opcionais.

O repositório inclui tanto a configuração nativa de integração ADF + DevOps, quanto scripts em Python para automação de backups e commits, ampliando o controle sobre os artefatos.


---

🎯 **Problema que o Projeto Resolve**

Em ambientes corporativos de dados, especialmente os regulados, é comum encontrar:

Pipelines sem histórico claro de alterações

Dependência excessiva do publish manual do Data Factory

Ausência de backups versionados de artefatos críticos

Dificuldade de auditoria e rollback em caso de falhas


Com base na minha experiência em sistemas críticos bancários, projetei esta solução para mitigar riscos de perda de metadados, garantir rastreabilidade completa e facilitar processos de rollback, mesmo em ambientes de alta conformidade regulatória.

O projeto demonstra como tratar pipelines de dados com o mesmo rigor aplicado a software corporativo.


---

🎯 **Objetivo do Projeto**

Este projeto foi desenvolvido com os seguintes objetivos:

Demonstrar governança de dados aplicada ao Azure Data Factory

Implementar versionamento real de pipelines, datasets e linked services

Criar uma base sólida para futuras esteiras de CI/CD em dados

Automatizar backups de artefatos com Python

Simular práticas comuns em ambientes bancários e corporativos



---

🛠 **Decisões Técnicas**

Integração Nativa ADF + Azure DevOps

Optei pela integração oficial do Data Factory com Azure DevOps Git para garantir:

Versionamento automático de artefatos

Colaboração via branches e pull requests

Histórico auditável de mudanças


**Scripts Python para Backups**

Embora o ADF já escreva no repositório, implementei scripts em Python para:

Exportações controladas de artefatos

Snapshots adicionais

Automação de commits e versionamento independente do publish


Uso de Git como Fonte de Verdade

Toda a configuração considera o repositório Git como fonte oficial de versionamento, reduzindo riscos operacionais.

Essas decisões refletem práticas adotadas em ambientes críticos, onde rastreabilidade e controle são mandatórios.


---

🚀 **Tecnologias Utilizadas**

Azure Data Factory (V2): Orquestração de pipelines e artefatos

Azure DevOps (Git): Controle de versão, branches e PRs

Python 3.10+: Automação de exportações e commits

Azure SDK for Python:

azure-identity

azure-mgmt-datafactory


GitPython: Integração programática com repositórios Git

GitHub Actions (opcional): Automação de backups

JSON: Formato dos artefatos versionados

MIT License: Licenciamento aberto



---


---

**Estrutura do repositório**

<img width="875" height="1670" alt="repo-structure" src="https://github.com/user-attachments/assets/77a1ee64-1280-4968-897b-0b8faf742f1d" />


---



📂 Estrutura do Repositório

.
├── README.md
├── LICENSE
├── docs/
│   ├── imagens/
│   └── diagramas/
├── src/
│   ├── export_adf_artifacts.py
│   ├── git_commit_backup.py
│   └── utils/
│       └── auth.py
├── backups/
│   ├── pipelines/
│   ├── datasets/
│   ├── linkedServices/
│   └── triggers/
├── config/
│   └── settings.example.json
└── .github/
    └── workflows/
        └── backup-adf.yml

**Descrição das Pastas**

**docs/**
Evidências visuais, prints de configuração e diagramas de arquitetura.

**src/**
Scripts Python responsáveis por exportar artefatos do ADF e versioná-los no Git.

**backups/**
Armazena snapshots versionados dos pipelines, datasets, linked services e triggers.

**config/**
Arquivo de configuração de exemplo para credenciais e parâmetros do projeto.

**.github/workflows/**
Pipeline opcional para automação de backups via GitHub Actions.



---

▶️ **Como Executar o Projeto**

Pré-requisitos

Python 3.10 ou superior

Git instalado e configurado

Azure CLI (recomendado)

Conta Azure (estudante ou trial)

Azure Data Factory criado

Organização e projeto no Azure DevOps


**Execução Local**

```
git clone https://github.com/Santosdevbjj/AzureDevOpsVersiBackup.git
cd AzureDevOpsVersiBackup
```

```
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
```

```
pip install azure-identity azure-mgmt-datafactory GitPython python-dotenv
az login
```

Após configurar o arquivo config/settings.json, execute:

```
python src/export_adf_artifacts.py
python src/git_commit_backup.py
```


---

🧠 **Aprendizados**

Como o Azure Data Factory organiza internamente seus artefatos

Diferença entre publish branch e versionamento colaborativo

Importância do Git como mecanismo de governança em dados

Aplicação de conceitos de engenharia de software em pipelines analíticos



---

🔮 **Próximos Passos**

Integração com Azure Key Vault para segredos

Validação automática dos JSONs do ADF em CI

Deploy entre ambientes (Dev → Test → Prod)

Monitoramento e alertas de falhas



---

📌 **Conclusão**

Este projeto demonstra como engenharia de dados, governança e versionamento podem (e devem) caminhar juntos.
Mesmo em contexto educacional, a solução foi estruturada para refletir cenários reais de mercado, especialmente ambientes corporativos regulados.






    
---
**Autor:**
Sergio Santos 

---

**Contato:**

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://santosdevbjj.github.io/portfolio/)
[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz) 


---


