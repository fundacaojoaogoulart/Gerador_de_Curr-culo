# Convenções mínimas

- Páginas: `docs/index.md`, `docs/data-lineage.md`, `docs/architecture.md`, `docs/technical-review.md`.
- `index.md`: descrição e navegação concisas, sem repetir fluxo e regras.
- `data-lineage.md`: fontes, campos, transformações, destinos, modalidade (automático/acionado/revisado/manual), regras de negócio, limites e referências ao código. Para cada campo crítico: origem → regra → destino. Diferencie não verificado de confirmado.
- `architecture.md`: Mermaid, sistemas/partes, responsabilidades, ponto(s) de entrada, organização por pasta/arquivo sem catálogo desnecessário de funções.
- `technical-review.md`: retrato da auditoria com evidências e riscos; não mantenha este documento em toda alteração trivial.
- Diagrama Mermaid com cerca de 5–15 nós quando possível; dividir só se legibilidade exigir. Preserve IDs e nomes para reduzir diffs.
- Manter idioma e estilo existentes. Não incluir segredos, dados pessoais, screenshots ou planilhas completas.
- Markdown é a fonte, MkDocs é a apresentação: `mkdocs build` não publica; `mkdocs serve` disponibiliza em localhost.
