# Init — auditoria e documentação inicial

1. Identifique a prioridade do usuário, stack e materiais existentes. Levante arquivos e pastas por nomes (lista limitada), sem abrir conteúdo massivamente. Identifique pontos de entrada, configurações, modelos, transformações, scripts, testes e eventuais Graphify/Diagram Design. Eles são pistas: valide contra o código.
2. Leia primeiro manifests, entradas e o código que conecta os componentes. Expanda por dependência real. Exclua node_modules, .git, .venv, binários, logs, imagens, dumps, exports de emuladores e dados de produção; não leia segredos e PII. Não dispare ações mutáveis do sistema. Se informação de Sheets ou sites não estiver no repo, indique claramente.
3. Identifique **o fluxo real**: fonte, entidade/aba/campo de origem, transformação e regra, etapa automática/acionada/revisada/preenchida manualmente, destino/campo, consumidor. Documente quais dados são preservados e sobrescritos. Para operações de fila, aprovação, classificação, reprocessamento e idempotência, explicite o comportamento verificável. Use matriz de decisão para regras tabeladas (estados, precedência, fallback, lacunas). Cite caminhos de arquivos/símbolos, sem copiar toda a implementação.
4. Documente arquitetura no nível adequado: repositório pequeno = pastas, componentes, arquivo e função principal por arquivo; não faça inventário de todas as funções. Mostre diagrama Mermaid e execução local conforme código. Distinga implementado de planejado.
5. Crie `docs/index.md` (guia curto), `docs/data-lineage.md` (prioritário), `docs/architecture.md` e `docs/technical-review.md` (problemas comprovados, riscos potenciais, melhorias opcionais, evidência, impacto, recomendação, esforço aproximado). Não corrija produção. Reaproveite o conteúdo anterior que estiver válido.
6. Crie `docs/documentation-map.json` com grupos de arquivos relevantes, globs *específicos*, documentos correspondentes, decisão `review_ai` ou `manual_review`, e explicações. Use `skip` exclusivamente em caminhos comprovadamente irrelevantes; não use `skip` para todo CSS, código interno ou testes. Documentos Markdown alterados manualmente serão detectados como `regenerate` (geração do HTML) pelo script.
7. Configure `mkdocs.yml` para HTML local, sem deploy público, com Mermaid. Não crie frontend próprio. Valide com `scripts/validate_docs.py`; execute `--build` somente se MkDocs instalado. Explique que abrir `mkdoc-site/index.html` diretamente pode não oferecer busca/navegação completas: use `mkdocs serve`.
8. Entregue resumo conciso, caminhos, achados com evidência, lacunas e comandos. Não apresente inferências como fatos.

## Exemplo de mapeamento por domínio

- Firebase: Sheets → revisão de schema → normalização → Firestore, Storage e Cloud Functions; mapear aba/coluna → campo destino.
- Scraping: páginas → seletores → regras estratégicas → planilha anterior/final, separando automático e manual.
- Apps Script: planilha origem → aba intermediária → aprovação/reprovação → processamento manual → Base, documentando campos modificados, regras tabeladas e limites.

Esses são exemplos de escopo, não afirmações sobre um repositório específico.
