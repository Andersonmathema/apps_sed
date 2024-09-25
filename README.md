# Removedor de Prazos do Tarefas SP

Este projeto é uma aplicação automatizada que utiliza Selenium e Streamlit para realizar o login na plataforma Tarefas SP e remover prazos de atividades de forma automatizada. O objetivo é facilitar a gestão de atividades, economizando tempo ao automatizar o processo de remoção de prazos.

## Funcionalidades

- **Login Automático:** A aplicação realiza o login na plataforma Tarefas SP utilizando credenciais fornecidas pelo usuário.
- **Remoção de Prazos:** A ferramenta navega automaticamente pelas atividades e remove prazos definidos.
- **Feedback em Tempo Real:** A aplicação fornece uma barra de progresso e mensagens de status para informar o usuário sobre o andamento do processo.
- **Encerramento Seguro:** Garantia de fechamento seguro do navegador após o término do processamento.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal do projeto.
- **Streamlit**: Framework para criar a interface web da aplicação.
- **Selenium**: Biblioteca para automação do navegador.
- **ChromeDriver**: Ferramenta necessária para que o Selenium controle o navegador Google Chrome.

## Pré-requisitos

- **Python 3.x** instalado.
- **Google Chrome** instalado.
- **ChromeDriver** compatível com a versão do Google Chrome instalada. [Download do ChromeDriver](https://chromedriver.chromium.org/downloads).
- Biblioteca **Streamlit** instalada.
- Biblioteca **Selenium** instalada.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

2. **Instale as dependências:**

   Certifique-se de que o ambiente Python está configurado corretamente e instale as dependências listadas no `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   Caso o arquivo `requirements.txt` não exista, instale manualmente as bibliotecas:

   ```bash
   pip install streamlit selenium
   ```

3. **Configure o ChromeDriver:**

   - Baixe o ChromeDriver compatível com a sua versão do Chrome: [ChromeDriver](https://chromedriver.chromium.org/downloads).
   - Extraia o ChromeDriver para uma pasta de fácil acesso e certifique-se de que está no PATH do sistema.

## Como Executar

1. **Inicie a aplicação Streamlit:**

   Execute o comando abaixo para iniciar o aplicativo:

   ```bash
   streamlit run home.py
   ```

2. **Acesse a aplicação:**

   - O Streamlit abrirá uma janela no navegador ou fornecerá um link local (e.g., `http://localhost:9090`).
   - Insira o RG com dígito e a senha nos campos apropriados e clique em **Entrar**.

3. **Monitoramento do Progresso:**

   - Após o login bem-sucedido, o aplicativo processará as atividades e mostrará uma barra de progresso.
   - Mensagens informativas guiarão o usuário durante o processo.

4. **Acesse o Tarefas SP:**

   - Após o processamento, um botão de acesso ao Tarefas SP será exibido para continuar gerenciando as atividades manualmente, se necessário.

## Problemas Comuns e Soluções

- **Erro de Login:** Verifique se as credenciais foram inseridas corretamente. Caso o erro persista, tente novamente.
- **ChromeDriver não encontrado:** Certifique-se de que o ChromeDriver está instalado corretamente e está no PATH do sistema.
- **Processos não encerrados:** Garanta que o navegador seja fechado corretamente após a execução. Caso contrário, feche manualmente pelo Gerenciador de Tarefas (Windows) ou Monitor de Atividade (Mac).

## Contribuindo

Contribuições são bem-vindas! Se desejar melhorar o projeto ou corrigir bugs, siga os passos abaixo:

1. **Fork o projeto.**
2. **Crie uma branch com sua feature:** `git checkout -b minha-feature`.
3. **Commit suas mudanças:** `git commit -m 'Minha nova feature'`.
4. **Push para a branch:** `git push origin minha-feature`.
5. **Abra um Pull Request.**

## Licença

Este projeto é licenciado sob a Licença GNU General Public License v3.0. Consulte o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato:

- **Nome:** Anderson
- **Email:** andersonandrades@prof.educacao.sp.gov.br
- **GitHub:** [Prof Anderson Andrade](https://github.com/ProfAndersonAndrade)
