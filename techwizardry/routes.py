import bcrypt
import flask
from flask import flash, redirect, url_for, request, abort
from techwizardry import app, bcrypt
from techwizardry.forms import FormLogin, FormCriarConta, FormEditarPerfil, FormCriarPost
from techwizardry.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
from techwizardry import database, login_manager
import secrets
import os
from PIL import Image


#from models import Post, Usuario

@app.route('/')
def home():
    posts = Post.query.order_by(Post.id.desc())
    return flask.render_template('home.html', posts=posts)


@app.route('/contato')
def contato():
    return flask.render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
    return flask.render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in flask.request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha.encode('utf-8'), form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flask.flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-primary')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            return flask.redirect(flask.url_for('home'))
        else:
            flash("Falha no Login. E-mail ou senha incorretos.")

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in flask.request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data).decode('utf-8')
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flask.flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-primary')
        return flask.redirect(flask.url_for('home'))
    return flask.render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/sair')
@login_required
def sair():
    logout_user()
    flask.flash(f'Logout feito com sucesso', 'alert-warning')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for("static", filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return flask.render_template('perfil.html', foto_perfil=foto_perfil)


@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post Criado com Sucesso', 'alert-primary')
        return redirect(url_for('home'))
    return flask.render_template('criarpost.html', form=form)


def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if campo.data:
            if 'curso_' in campo.name:
                lista_cursos.append(campo.label.text)
    return ';'.join(lista_cursos)

def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
    tamanho = (400, 400)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)
    return nome_arquivo

@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.cursos = atualizar_cursos(form)
        database.session.commit()
        flask.flash(f'Perfil atualizado com Sucesso.', 'alert-primary')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.username.data = current_user.username
    foto_perfil = url_for("static", filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return flask.render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)



@app.route('/post/<post_id>',  methods=['GET', 'POST'])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        form = FormCriarPost()
        if request.method == 'GET':
            form.titulo.data = post.titulo
            form.corpo.data = post.corpo
        elif form.validate_on_submit():
            post.titulo = form.titulo.data
            post.corpo = form.corpo.data
            database.session.commit()
            flash('Post Atualizado com Sucesso', 'alert-primary')
            return redirect(url_for('home'))
    else:
        form = None
    return flask.render_template('post.html', post=post, form=form)


@app.route('/post/<post_id>/excluir',  methods=['GET', 'POST'])
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash('Post excluido com Sucesso', 'alert-danger')
        return redirect(url_for('home'))
    else:
        abort(403)
