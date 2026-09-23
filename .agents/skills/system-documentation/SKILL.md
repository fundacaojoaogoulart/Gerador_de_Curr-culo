---
name: system-documentation
description: Documenta e mantém repositórios existentes em modo init/update, com auditoria técnica, data lineage, regras de negócio, MkDocs local e triagem determinística de Git diff para minimizar tokens. Use ao criar ou atualizar documentação de sistemas.
compatibility: Python 3.9+, Git; MkDocs opcional para geração HTML. Compatível com agentes que suportam Agent Skills.
metadata:
  version: "1.0.0"
  language: pt-BR
---

# System Documentation

Skill reutilizável. **Procedimento aqui; fatos do sistema no repositório.** Escolha um modo sem carregar os dois manuais.

## Antes de agir

- Confirme o modo pedido: `init` (primeira auditoria e documentação) ou `update` (mudança incremental).
- Leia `AGENTS.md` do projeto, se existir, e as pistas de localização fornecidas pelo usuário. Preserve e não sobrescreva instruções existentes.
- Use o mínimo de contexto necessário, evite segredos e dados pessoais, não execute operações externas ou mutáveis do aplicativo.
- Priorize fluxo de dados e regras de negócio quando o usuário assim pedir. Adapte profundidade da arquitetura ao tamanho do sistema.

## Modo init

Leia `references/initial-audit.md`, não `references/incremental-update.md`. Inventarie antes de ler. Produza, salvo justificativa explícita, `docs/index.md`, `docs/architecture.md`, `docs/data-lineage.md`, `docs/technical-review.md`, `docs/documentation-map.json` e `mkdocs.yml`. O `docs/documentation-map.json` é o mapa por repositório: use o modelo `templates/documentation-map.example.json` como estrutura, substituindo todos os caminhos e motivos pelos reais. Não trate o modelo como mapa pronto.

Para o MkDocs, reutilize `templates/mkdocs.yml`, adaptando o `site_name` e mantendo `site_dir: mkdoc-site`. Use Mermaid como código nos `.md`; valide o renderer no ambiente disponível. `mkdocs build` só gera HTML; não publica nada. Para navegação/busca completas, abra via `mkdocs serve` em localhost.

Execute `scripts/validate_docs.py --repo .` e, se MkDocs estiver instalado, `scripts/validate_docs.py --repo . --build`.

## Modo update

Leia `references/incremental-update.md`, não o manual init. Faça primeiro **triagem sem LLM**:

```bash
# Após instalar a skill localmente no repositório:
python .agents/skills/system-documentation/scripts/detect_changes.py --repo . --base HEAD --map docs/documentation-map.json
# PR/branch: use --base origin/main --head HEAD para comparar com merge-base.
```

Decisões: `skip`, `regenerate`, `review_ai`, `manual_review`. `review_ai` é suspeita de impacto, **não** ordem para reescrever. Leia diff restrito, fontes e trechos impactados; se informação ainda correta, produza **zero patch**. Atualize `docs/documentation-map.json` quando as relações código → docs mudarem. Registre conflitos sem inventar regras.

Após validar o init, recomende registrar a documentação inicial em commit para criar a linha de base. Se não houver mapa, não classifique como seguro: peça inicialização do mapa ou marque revisão. O script **não** chama LLM: num fluxo CLI, cabe ao invocador ler seu JSON e decidir chamar o agente. Não afirme que CI, cron ou integração programática existem quando não forem configurados.

Após qualquer modificação: valide e apresente diff mínimo.

## Quando ler arquivos de apoio

- `references/initial-audit.md`: apenas na inicialização.
- `references/incremental-update.md`: apenas na atualização.
- `references/documentation-standards.md`: se precisar criar documentação ou dirimir inconsistências de formato.
- `templates/documentation-map.example.json`: ao construir mapa novo.
- `templates/mkdocs.yml`: ao inicializar o site local.
- `scripts/`: executáveis locais; leia o código deles apenas se precisar depurar ou adaptar.

## Segurança e economia

Ignorar `.git`, dependências, cache, binários, builds, exports, logs, fixtures volumosas e datasets inteiros. Verificar schema/cabeçalhos antes de dados de linha. Nunca reproduzir dados pessoais. Divergência código ↔ regra aprovada: `manual_review`. Mudanças externas (Sheets, web, Firestore) não aparecem no Git diff e exigem verificação complementar autorizada.
