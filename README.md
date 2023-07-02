ProjetoSiteFlask
Descrição
Este projeto é uma rede social para programadores, onde os usuários podem fazer posts, adicionar uma foto de perfil e cadastrar nome, e-mail e senha. As senhas são criptografadas com o algoritmo bcrypt para garantir a segurança dos usuários. O projeto foi desenvolvido utilizando Flask, Bootstrap e SQLAlchemy.

Tecnologias Utilizadas
Flask
Bootstrap
SQLAlchemy
bcrypt (para criptografia de senhas)
Pré-requisitos
Python 3.7 ou superior
Flask
SQLAlchemy
bcrypt
Instalação
Clone o repositório:

bash
Copy code
git clone https://github.com/HugoLeandro/ProjetoSiteFlask.git
Navegue até o diretório do projeto:

bash
Copy code
cd ProjetoSiteFlask
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copy code
python -m venv venv
source venv/bin/activate
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Configure as variáveis de ambiente. Crie um arquivo .env na raiz do projeto e defina as seguintes variáveis:

bash
Copy code
FLASK_APP=app.py
FLASK_ENV=development (ou production)
DATABASE_URL=sqlite:///database.db
Execute o aplicativo:

bash
Copy code
flask run
Acesse o aplicativo no seu navegador em http://localhost:5000.

Uso
Crie uma conta no site fornecendo seu nome, e-mail e senha.
Faça login no site com suas credenciais.
Após o login, você pode criar um novo post na página inicial.
Para adicionar uma foto de perfil, acesse a página de perfil e clique no botão "Adicionar Foto".
Explore as funcionalidades do site e interaja com outros usuários.
Contribuição
Se você deseja contribuir para este projeto, siga as etapas abaixo:

Faça um fork do repositório.

Crie uma nova branch com a sua contribuição:

bash
Copy code
git checkout -b minha-contribuicao
Faça as alterações necessárias e commit:

bash
Copy code
git commit -m "Descrição da minha contribuição"
Faça push para a branch:

bash
Copy code
git push origin minha-contribuicao
Abra um pull request no repositório original.

Licença
Este projeto está sob a licença MIT.

Contato
Para mais informações ou dúvidas sobre o projeto, entre em contato com Hugo Leandro através do e-mail leandrolimahugo@gmail.com
