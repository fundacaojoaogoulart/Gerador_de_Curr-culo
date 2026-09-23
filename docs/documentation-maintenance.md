# Exemplos de prompts (OpenCode)

## Inicialização (`init`)

```text
Use o agente documentation-engineer e carregue a skill system-documentation em modo init.
Este repositório é um gerador desktop de currículos em Python/Tkinter. Ele busca dados de
profissionais em uma planilha Excel, preenche um modelo Word e gera arquivos DOCX e PDF.
Priorize arquitetura e lógica de uso.
Fontes relevantes, se conhecidas: Gerador_de_Curriculo.py, README.md e requeriments.txt.
Há documentação em docs/, dependências documentais em docs/documentation-map.json e
diagramas Mermaid em docs/architecture.md e docs/data-lineage.md.
Faça inventário e leitura seletiva (não abra dependências, builds, binários, dados pessoais ou segredos).
Crie ou atualize docs/index.md, docs/data-lineage.md, docs/architecture.md, docs/technical-review.md,
docs/documentation-maintenance.md, docs/documentation-map.json e mkdocs.yml para visualização local, sem deploy.
Documente fontes → transformações/regras → destinos, campos automáticos vs manuais e limitações verificadas.
Não execute operações reais nem altere o código de produção. Valide e informe lacunas.
```

## Atualização (`update`)

```text
Use o agente documentation-engineer e a skill system-documentation em modo update.
Compare minhas mudanças locais com HEAD. Execute primeiro .agents/skills/system-documentation/scripts/detect_changes.py.
Se não houver impacto, não abra arquivos adicionais nem altere a documentação.
Se houver review_ai, examine somente diff, trechos e seções afetadas e proponha patch mínimo.
Preserve a documentação anterior, regras aprovadas, diagramas e IDs. Rode .agents/skills/system-documentation/scripts/validate_docs.py.
Não atualize technical-review.md nem execute ações externas ou mutáveis.
```

## CI sem IA

O workflow `.github/workflows/documentation.yml` roda em pushes, pull requests e acionamento manual. Usa diretamente os scripts da skill; não há cópias em `scripts/`.

- Em pull requests, compara base e head pelo merge-base. Em pushes, usa o SHA anterior; se indisponível, e em execuções manuais, compara o último commit com seu pai. No commit raiz, não há base anterior e a triagem compara o commit consigo mesmo.
- Publica somente o relatório `impact.json` como artefato e apresenta a decisão no resumo do job.
- Sempre valida os documentos e executa build estrito, mesmo quando a triagem retorna `skip`. Erros de validação/build fazem o job falhar.
- `review_ai` e `manual_review` são indicações para revisão manual, não chamadas de agentes nem bloqueios automáticos. Um CI verde não comprova correção semântica da documentação.
- Não altera Markdown, não executa o gerador de currículos e não faz deploy. A revisão com IA é iniciada manualmente usando o prompt `update` acima.

Para funcionar no GitHub, o workflow, os scripts em `.agents/skills/system-documentation/scripts/`, o mapa, os documentos e `mkdocs.yml` precisam estar versionados no mesmo repositório.

## Caso especializado: histórico de movimentações de líderes

```text
Use documentation-engineer + system-documentation em modo init. É Google Apps Script
acionado pela planilha. Priorize fluxo origem → aba intermediária → aprovação/reprovação →
processamento manual da fila → aba Base. Para cada campo da Base, registre origem,
condição/regra, atualização automática ou manual e arquivo responsável.
Documente estados do líder, precedência e limitações de regras tabeladas.
Arquitetura apenas por pasta/arquivo .js e função principal, sem inventário de funções.
Não execute processamento real, não exponha registros pessoais, gere MkDocs local.
```
