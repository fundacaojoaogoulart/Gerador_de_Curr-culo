# Avaliação técnica

## Método e evidências

Auditoria estática de 23/09/2026. Fontes lidas: `Gerador_de_Curriculo.py`, `README.md`, `requeriments.txt` e instruções/templates da skill de documentação. O inventário versionado contém esses três arquivos e um guia PDF, identificado apenas por nome. O aplicativo não foi importado nem executado. Não houve acesso a fotos, conversão ou leitura de dados pessoais.

Os achados abaixo distinguem comportamento confirmado no código de impactos potenciais. Esforço indicativo: pequeno (ajuste localizado), médio (mudança de fluxo e testes); nenhuma correção de produção faz parte desta entrega.

## Achados

| Achado confirmado / evidência | Impacto ou risco potencial | Recomendação | Esforço |
| --- | --- | --- | --- |
| Caminhos relativos, constantes 17–18 e gravação 175–184 | Iniciar de outra pasta pode impedir leitura ou deslocar saídas | Definir diretório de dados/saída explicitamente, inclusive no executável | Pequeno a médio |
| Carga captura toda exceção e retorna `None`, 28–37 | Falta de arquivo, schema inválido e erros de engine ficam indistinguíveis | Validar schema e distinguir causas de falha | Pequeno |
| Busca converte código para texto e usa primeira correspondência, 31–44 | Inferência de tipos pode afetar códigos; duplicatas selecionam pessoa inesperada | Definir contrato de código e política de unicidade | Médio |
| `NOME` é acessado sem validação, 165 e 172 | Ausência da coluna interrompe a geração; ausência de valor não recebe tratamento específico | Validar campos necessários antes da geração | Pequeno |
| Substituição depende de run e percurso limitado, 53–91 | Tags fragmentadas ou em partes não percorridas podem ficar no currículo | Estabelecer contrato do modelo e detectar tags residuais | Médio |
| Erros de foto são suprimidos, 58–69 | Sucesso pode ser informado para currículo sem foto | Definir foto obrigatória/opcional e reportar resultado parcial | Pequeno |
| Nome sanitiza somente duas barras, 172 | Caracteres inválidos do Windows ainda podem impedir gravação; nomes iguais colidem | Sanitizar nomes e definir política de colisão | Pequeno |
| DOCX salvo antes do PDF sem rollback, 179–199 | Resultado parcial e possível PDF antigo ao lado de DOCX novo | Distinguir sucesso parcial e usar estratégia de saída consistente | Médio |
| Operações síncronas na GUI, 131–184 | Interface pode ficar sem resposta durante I/O ou Word | Avaliar tarefa de fundo com atualização segura do Tkinter | Médio |
| Tema `vista` sem fallback, 102 | Portabilidade depende do tema disponível | Declarar plataforma suportada ou adicionar fallback | Pequeno |
| Dependências sem versões em `requeriments.txt` | Instalações futuras podem ter comportamento diferente | Registrar versões suportadas e verificar instalação limpa | Pequeno |

## Divergências da orientação existente

- O README descreve arquivos junto ao script, mas o código resolve caminhos pelo diretório de trabalho.
- O README declara `FOTO` obrigatória; o código aceita sua ausência. `NOME`, necessário na geração, não é destacado como obrigatório.
- O README descreve nome sem caracteres especiais; a implementação troca somente `/` e `\`.
- O README associa a falha inicial à ausência do Excel; a implementação também suprime quaisquer outras falhas de carga.

Essas diferenças são documentadas conforme implementação. A regra de negócio pretendida exige confirmação do responsável antes de alterar código ou estabelecer obrigatoriedades novas.

## Lacunas

- Schema real, tipos de células, duplicatas, lista de colunas e conteúdo do template não inspecionados.
- Layout, foto e PDF não validados em execução; disponibilidade e versão do Word não verificadas.
- Executável relatado pelo usuário sem artefato ou receita de empacotamento versionados; equivalência com o fonte não comprovada.
- Guia PDF não lido por restrição de binários; consistência de seu conteúdo não avaliada.
- Testes e automação de empacotamento não encontrados no inventário versionado.
- Políticas de obrigatoriedade de foto, colisão de nomes, códigos duplicados e revisão humana não formalizadas nas fontes lidas.

## Validação documental

Os checks da skill verificam presença dos arquivos, estrutura básica do mapa, links locais e fechamento de cercas Markdown. Nesta execução, `python .agents/skills/system-documentation/scripts/validate_docs.py --repo . --build` passou com zero problemas, incluindo `mkdocs build --strict`, usando MkDocs e Material já instalados.

O build estrito valida a construção MkDocs, mas não comprova sozinho a renderização visual de Mermaid ou o funcionamento do gerador de currículos. A conferência visual foi tentada via servidor local, mas a ferramenta informou que não há navegador conectado à sessão. A renderização visual dos diagramas permanece pendente.

Validação funcional futura pode usar uma base e um modelo inteiramente sintéticos para exercitar código não encontrado, duplicatas, tags fragmentadas, ausência de foto e falha de conversão. Isso não foi executado nesta auditoria.
