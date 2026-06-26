Passo a Passo para Instalação e Execução

1. Preparar o Diretório
Reúna os arquivos do projeto (código principal, requirements.txt, logo e CSS) em uma mesma pasta no seu computador. Abra o terminal (ou Prompt de Comando) e navegue até esse diretório.

2. Criar um Ambiente Virtual (Opcional, mas Recomendado)
Para evitar conflito de pacotes com outros projetos Python, crie e ative um ambiente virtual:

No Windows:

Bash
python -m venv venv
venv\\Scripts\\activate
No Linux / macOS:

Bash
python3 -m venv venv
source venv/bin/activate
3. Instalar as Dependências
Com o terminal aberto na pasta do projeto e o ambiente virtual ativado, instale as bibliotecas necessárias:

Bash
pip install -r requirements.txt
4. Configurar a Chave da API (Groq)
O aplicativo necessita de uma chave de API da Groq para utilizar o modelo Llama 3.1.

Crie uma pasta chamada .streamlit na raiz do projeto.

Dentro da pasta .streamlit, crie um arquivo de texto chamado secrets.toml.

Adicione sua chave de API gerada na plataforma Groq dentro do arquivo, exatamente neste formato:

Ini, TOML
GROQ_API_KEY = "SUA_CHAVE_AQUI"
5. Adicionar Documentos de Suporte
O sistema depende de documentos para formar a base de conhecimento.

Crie uma pasta chamada documentos_FJG na raiz do projeto (se ela ainda não existir).

Coloque nela os materiais de boas-vindas, relatórios, checklists e tutoriais da fundação.

Aviso: A aplicação não irá inicializar o índice de busca corretamente se a pasta documentos_FJG estiver vazia ou não existir.

6. Executar a Aplicação
Inicie a interface web utilizando o Streamlit:

Bash
streamlit run atendimento_estagiarios.py
