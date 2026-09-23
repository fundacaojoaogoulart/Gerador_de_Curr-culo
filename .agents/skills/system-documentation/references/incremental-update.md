# Update — triagem e patch mínimo

1. Determine a base correta para comparar. Mudanças locais não commitadas: `--base HEAD` (inclui untracked não ignorados). Comparação de branch/PR: `--base origin/main --head HEAD`, usando merge-base; **não inclui alterações não commitadas** nesse modo. Não misture os dois silenciosamente.
2. Execute `scripts/detect_changes.py --repo <raiz> --map docs/documentation-map.json [--base ... --head ...] --output <arquivo opcional>` antes de ler código. O script não aciona IA e não lê conteúdo dos arquivos; produz somente nomes, classificação e documentos prováveis.
3. `skip`: nada a fazer. `regenerate`: alterações somente nos próprios documentos ou geradores determinísticos; valide e gere HTML se for útil, sem análise semântica. `review_ai`: leia *somente* diffs relevantes e os arquivos/documentos atingidos, além de referências estritamente necessárias. `manual_review`: não invente conteúdo; esclareça o que requer validação humana. Se várias classificações ocorrerem, prevalece a mais cautelosa.
4. O agente deve confirmar se a mudança realmente afetou as docs antes de editar. Gerar um patch localizado, sem alterar títulos, IDs, sequência de regras ou terminologia desnecessariamente. Se não houver mudança semântica, não altere nada. Atualizar o mapa se um novo arquivo, rota, função ou aba passar a se relacionar a documentos.
5. Alterações diretas no Sheets, sites, banco e serviços remotos não estão cobertas pelo Git. Não validar fontes externas sem acesso e autorização. Mudanças apenas de registros/valores não exigem atualização narrativa se contrato e processo permanecem iguais.
6. Não tocar automaticamente em `docs/technical-review.md`, salvo pedido explícito de nova auditoria. Não executar scraper, filas, deploy nem mutações de banco/planilha para testar documentos.
7. Executar `scripts/validate_docs.py --repo <raiz> [--build]` e resumir diff; pedir revisão humana em conflitos de regra/semântica.

## Regras de classificação

- `skip`: padrão estreito explicitamente irrelevante ou artefato gerado ignorado.
- `regenerate`: somente `.md`/configuração do MkDocs afetados sem mudança em fonte do aplicativo; o HTML é opcional, sem LLM.
- `review_ai`: código/configurações relevantes do aplicativo, arquivos desconhecidos ou mudança que pode alterar dados/regras.
- `manual_review`: mapa ausente ou inválido, caminhos de segredo, regra externa que não pode ser checada com segurança.

Para segurança, caminho desconhecido **nunca é skip**. O mapa não é um parser semântico; globs são heurísticas conservadoras.
