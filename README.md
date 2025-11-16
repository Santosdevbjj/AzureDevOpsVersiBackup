### Github e Azure Devops para Versionamento e Backups

![Azure_Databricks01](https://github.com/user-attachments/assets/6ba56dfe-a8ea-40db-8529-209cbfb1437d) 



**Bootcamp Microsoft AI for Tech - Azure Databricks**

---

**DESCRIÇÃO:**

Este projeto demonstra como integrar o Azure Data Factory ao Azure DevOps, permitindo versionamento, controle de mudanças e backups automáticos de pipelines e artefatos de dados.

A integração garante maior governança e rastreabilidade no desenvolvimento de soluções de dados.

O processo inclui a criação de uma organização e projeto no DevOps, configuração do repositório Git, definição de branches e conexão direta com o Data Factory.

Também são abordadas boas práticas para configurar essa integração durante ou após a criação do recurso, além da visualização e gerenciamento dos arquivos versionados diretamente dentro do repositório.

Com essa estrutura, é possível manter históricos de alterações, padronizar ambientes de desenvolvimento e preparar a esteira para futuras automações de CI/CD no Azure.

---


Este guia te leva do zero à integração completa entre Azure Data Factory e Azure DevOps (Git) para versionamento, rastreabilidade e backups automatizados de artefatos (pipelines, datasets e linked services).

Também inclui um projeto Python pronto para automatizar exportações e commits no repositório. 


---


**Visão geral do projeto**

Este projeto demonstra como configurar Azure DevOps com Git, criar e vincular um Azure Data Factory ao repositório, e manter um fluxo de backup automatizado com Python. 

Com isso, você garante governança, histórico de mudanças e prepara a base para uma esteira de CI/CD no Azure. 


> **Observação:** Para este projeto, consideramos uma conta gratuita de estudante no Azure, priorizando recursos com camadas gratuitas e custos mínimos.


---

**Estrutura do repositório**

<img width="875" height="1670" alt="repo-structure" src="https://github.com/user-attachments/assets/77a1ee64-1280-4968-897b-0b8faf742f1d" />


---

- **README.md:** Documentação principal do projeto, guia completo de uso.
- **LICENSE:** Licença do repositório (ex.: MIT).
- **docs/:** Evidências visuais com prints de configuração e diagramas do fluxo.
- **src/:** Código-fonte dos scripts Python para backup e sincronização.
- **backups/:** Exportações versionadas dos artefatos do Data Factory e snapshots.
- **.github/workflows/:** Pipeline opcional do GitHub Actions para automatizar backups.
- **config/settings.example.json:** Exemplo de configuração local.

---



**Tecnologias utilizadas**

- **Azure Data Factory:** Orquestração de dados em pipelines visuais e artefatos versionáveis.
- **Azure DevOps + Git:** Controle de versão, branches, PRs e integração direta com Data Factory.
- **Python 3.10+:** Automação de export e commit dos artefatos.
- **Azure SDK for Python (azure-mgmt-datafactory, azure-identity):** Acesso aos recursos do Data Factory via API.
- **GitPython:** Interação programática com repositórios Git locais.
- **GitHub Actions (opcional):** Automação de backups em cron.
- **JSON:** Formato de exportação dos artefatos.
- **MIT License:** Licenciamento aberto para uso e modificação.

---

**Requisitos de hardware e software**

- **Hardware:**
  - CPU: Qualquer CPU moderna.
  - Memória: 4 GB RAM mínimo (8 GB recomendado).
  - Armazenamento: 2 GB livres para ambiente e backups.
- **Software:**
  - Sistema operacional: Windows, macOS ou Linux.
  - Python: Versão 3.10+ instalada.
  - Git: Versão 2.30+ instalada e configurada.
  - Azure CLI: Para login e contexto (recomendado).
  - Conta Azure: Estudante gratuita com acesso a Data Factory e DevOps.
  - Acesso ao Azure DevOps: Organização e projeto criados.
- **Bibliotecas Python:**
  - azure-identity
  - azure-mgmt-datafactory
  - GitPython
  - python-dotenv (opcional)
  - requests (opcional)

---


**Passo a passo detalhado no Azure e Azure DevOps**

**Preparação: organização e projeto no Azure DevOps**

**1. Criar organização no Azure DevOps**
   - Acessar: dev.azure.com
   - Criar organização: Defina nome único (ex.: org-nome-sobrenome).
   - Região: Selecione a região que melhor atende latência.
**2. Criar projeto**
   - Nome: data-platform-versioning (ou sua preferência).
   - Visibilidade: Privado (recomendado).
   - Version control: Git.
   - Work item process: Agile (padrão).

**3. Criar repositório Git**
   - Repos → New repository: adf-versioning.
   - Default branch: main.
   - Políticas (opcional): PR obrigatório para main, reviewers, build validação.

**Criação do recurso Azure Data Factory**

**1. Acessar o Portal do Azure**
   - Portal: portal.azure.com (login com conta de estudante).
**2. Criar Resource Group**
   - Nome: rg-data-platform-dev.
   - Região: Brazil South (ou próxima).
**3. Criar Data Factory**
   - Create → Data Factory:
     - Subscription: Sua assinatura de estudante.
     - Resource Group: rg-data-platform-dev.
     - Nome do Data Factory: adf-dev-{seu-sufixo}.
     - Região: Igual ao resource group (recomendado).
     - Version: Data Factory V2.
   - Review + create: Provisionar.

**Configurar o GIT do DevOps durante a criação (ou após)**

**1. Link do Git no Data Factory Studio**
   - Open data factory studio → Manage → Git configuration.
**2. Selecionar Azure DevOps**
   - Git repository type: Azure DevOps Git.
   - Azure Active Directory: Selecionar sua conta.
   - Organization: Sua organização DevOps.
   - Project: data-platform-versioning.
   - Repository: adf-versioning.
**3. Branch Mapping**
   - Collaboration branch: main ou develop (recomendado develop).
   - Publish branch: adf_publish (padrão do ADF).
   - Root folder: /adf/ (criar estrutura organizada).
**4. Salvar configuração**
   - O Data Factory passa a escrever no repositório os arquivos JSON de pipelines, datasets, linked services e triggers.

> Dica: Se já criou o ADF sem Git, conecte pelo Data Factory Studio em Manage → Git configuration. Isso permite versionar artefatos criados anteriormente.

**Boas práticas de branches e PRs**

- Branches:
  - main: Estável, somente via PR.
  - develop: Colaboração ativa.
  - feature/*: Uma feature por branch, PR para develop.
- PR checks:
  - Code owners: Assegura revisão por responsáveis.
  - Build validation: Pipeline CI para validar JSON do ADF e diffs.
- Publish branch (adf_publish):
  - Usado pelo ADF ao publicar, gera ARM templates e artefatos compilados.

**Visualização dos arquivos versionados**

- Local no repo: /adf/
  - pipelines: /adf/pipelines/*.json
  - datasets: /adf/datasets/*.json
  - linkedServices: /adf/linkedServices/*.json
  - triggers: /adf/triggers/*.json
- Publish artifacts: /adf_publish/ (gerado pela ação de Publish no Studio).

> O repositório de referência “AzureDevOpsVersiBackup” traz uma descrição compatível com estes objetivos de versionamento e governança para Data Factory.

---

**Scripts Python para backups e commits**

**Configuração inicial**

**- Clonar seu repositório:**
  - git clone https://github.com/<seu-usuario>/azure-devops-datafactory-backups.git
- Criar ambiente Python e instalar dependências:
  - python -m venv .venv && source .venv/bin/activate (Windows: .\.venv\Scripts\activate)
  - pip install azure-identity azure-mgmt-datafactory GitPython python-dotenv
- Azure login (recomendado via Azure CLI):
  - az login
  - Se necessário, az account set --subscription "<ID OU NOME>"

    
---
**Autor:**
Sergio Santos 

---

