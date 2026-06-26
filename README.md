Gerador de Currículos Automático
Este projeto consiste em uma aplicação desktop, construída em Python, projetada para automatizar a criação de currículos. A ferramenta utiliza uma interface gráfica simples para buscar dados de profissionais em uma planilha Excel e preencher automaticamente um modelo no Microsoft Word, gerando arquivos finais em .docx e .pdf.

 Principais Funcionalidades
Interface Gráfica (GUI): Interface acessível construída com a biblioteca tkinter, permitindo a interação simples do usuário.

Integração com Excel: Lê automaticamente os dados do arquivo Minibios_Base.xlsx.

Preenchimento de Modelo Word: Localiza placeholders no formato {{NOME_DA_VARIAVEL}} dentro do arquivo Curriculo.docx e os substitui pelos dados correspondentes da planilha.

Processamento de Imagens: Identifica a tag [FOTO] no texto, faz o download da imagem a partir de uma URL fornecida na planilha e a insere no currículo (com largura padrão de 4 cm).

Conversão Dupla: Salva o documento preenchido no formato .docx e o converte automaticamente para .pdf utilizando a biblioteca docx2pdf.

 Pré-requisitos e Dependências
Para executar este script, você precisará do Python instalado e das seguintes bibliotecas de terceiros:

pandas (Para manipulação da base de dados em Excel)

python-docx (Importado como docx, para manipulação do template Word)

requests (Para realizar o download das fotos via URL)

docx2pdf (Para a conversão final do arquivo)

Atenção: A biblioteca docx2pdf exige que o Microsoft Word esteja instalado no computador onde o script for executado.

 Estrutura de Arquivos Exigida
Para que o programa funcione corretamente, os seguintes arquivos devem estar no mesmo diretório que o script Gerador_de_Curriculo.py:

Minibios_Base.xlsx: A planilha Excel contendo a base de dados. É obrigatório ter uma coluna chamada CODIGO_LC para a busca e uma coluna FOTO com as URLs das imagens.

Curriculo.docx: O template base do currículo contendo os placeholders e a tag [FOTO].

 Passo a Passo para Utilização
Inicie a Aplicação: Execute o script Python. A janela "Gerador de Currículos" será aberta.

Aguarde o Carregamento: O sistema pré-carregará a base de dados do Excel. Aguarde a mensagem "Base de dados carregada. Pronto." na barra de status inferior.

Insira o Código: No campo de texto, digite o CODIGO_LC correspondente ao profissional desejado.

Gere o Documento: Clique no botão "Gerar Currículo" (ou pressione a tecla Enter).

Verifique os Arquivos: Após o processamento e a conversão, uma caixa de sucesso informará que os arquivos Curriculo_NOME.docx e Curriculo_NOME.pdf (onde "NOME" é o nome do profissional sem caracteres especiais) foram salvos com sucesso na mesma pasta.

 Tratamento de Erros Comuns
O programa possui alertas nativos para lidar com algumas situações:

Erro Crítico de Inicialização: Ocorre se o arquivo Minibios_Base.xlsx não for encontrado na inicialização.

Não Encontrado: Ocorre se o código digitado não existir na base do Excel.

Erro de Permissão: Ocorre se o Word ou um leitor de PDF estiver com o arquivo de saída aberto no momento da geração.

Erro de Conversão: Geralmente indica a ausência do Microsoft Word instalado na máquina local.
