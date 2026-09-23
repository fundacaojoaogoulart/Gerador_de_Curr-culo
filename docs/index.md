# Gerador de Currículos

Aplicação desktop Python/Tkinter que seleciona um profissional em uma planilha Excel, preenche um modelo Word e salva um currículo em DOCX e PDF. A geração é acionada pelo operador; não há geração em lote na interface implementada.

## Navegação

- [Arquitetura e uso](architecture.md): componentes, requisitos e sequência operacional.
- [Fontes, regras e destinos](data-lineage.md): campos manuais/automáticos, transformações e comportamento de falhas.
- [Avaliação técnica](technical-review.md): evidências, limitações e lacunas de validação.

## Escopo da documentação

Auditoria estática inicial em 23/09/2026, baseada em `Gerador_de_Curriculo.py`, `README.md` e `requeriments.txt`. O guia PDF foi identificado somente pelo nome. Não foram abertos binários, dependências, dados pessoais, planilhas ou modelos Word, nem executados o aplicativo, downloads de fotos ou conversões.

O uso de um executável foi informado pelo responsável. O repositório contém a interface em Python, mas não contém executável versionado nem receita de empacotamento. Seu funcionamento empacotado não foi verificado.

## Visualização local

Com MkDocs Material instalado, execute na raiz do repositório:

```powershell
mkdocs serve --dev-addr 127.0.0.1:8000
```

Acesse `http://127.0.0.1:8000`. Para gerar apenas HTML local:

```powershell
mkdocs build --strict
```

A saída fica em `mkdoc-site/`; não há configuração de deploy. Abrir o HTML diretamente pode limitar a busca e a navegação. Os diagramas usam Mermaid integrado ao tema Material; sua renderização no navegador pode depender de recursos externos do tema.

## Manutenção

`docs/documentation-map.json` relaciona alterações de fontes aos documentos que precisam de revisão. O workflow `.github/workflows/documentation.yml` executa triagem, validação e build no GitHub Actions, sem chamar IA ou publicar o site. Os prompts e o fluxo de manutenção estão em [documentation-maintenance.md](documentation-maintenance.md). Localmente, use os scripts da skill:

```powershell
python .agents/skills/system-documentation/scripts/detect_changes.py --repo .
python .agents/skills/system-documentation/scripts/validate_docs.py --repo . --build
```

Após validar, recomenda-se registrar os arquivos de documentação em commit para estabelecer a linha de base das próximas atualizações.
