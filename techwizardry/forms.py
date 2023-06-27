import wtforms.validators
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from techwizardry.models import Usuario
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[wtforms.validators.DataRequired()])
    email = StringField('E-mail', validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    senha = PasswordField('Senha', validators=[wtforms.validators.DataRequired(), wtforms.validators.Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[wtforms.validators.DataRequired(), wtforms.validators.EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise wtforms.validators.ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça o login para continuar.')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    senha = PasswordField('Senha', validators=[wtforms.validators.DataRequired(), wtforms.validators.Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField("Fazer Login")

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[wtforms.validators.DataRequired()])
    email = StringField('E-mail', validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    foto_perfil = FileField('Foto de Perfil', validators=[FileAllowed(['jpg','png'])])
    curso_python = BooleanField('Python')
    curso_javascript = BooleanField('JavaScript')
    curso_java = BooleanField('Java')
    curso_go = BooleanField('Go')
    curso_rust = BooleanField('Rust')
    curso_php = BooleanField('PHP')
    curso_angular = BooleanField('Angular')
    curso_kotlin = BooleanField('Kotlin')
    curso_sql = BooleanField('SQL')
    curso_c = BooleanField('C#')
    curso_swift = BooleanField('Swift')
    curso_ruby = BooleanField('Ruby')
    curso_typescript = BooleanField('TypeScript')
    curso_html = BooleanField('Html')
    curso_css = BooleanField('CSS')

    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise wtforms.validators.ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail.')




class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[wtforms.validators.DataRequired(), wtforms.validators.Length(min=5, max=140)])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[wtforms.validators.DataRequired()])
    botao_submit = SubmitField('Confirmar Post')

