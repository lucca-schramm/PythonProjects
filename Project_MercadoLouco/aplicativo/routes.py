from aplicativo import app
from flask import render_template, redirect, url_for, flash, request
from aplicativo.models import User, Item
from aplicativo.forms import RegisterForm, LoginForm, PurchaseItem, SellItem, PostItem
from aplicativo import db
from flask_login import login_user,logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/dash',  methods=['GET', 'POST'])
@login_required
def dash_page():
    #Compra
    purchase_Form = PurchaseItem()
    selling_form = SellItem()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object=Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Parabéns! Você comprou {p_item_object.name} por {p_item_object.price}", category='success')
            else:
                flash("Infelizmente você não tem dinheiro suficiente para comprar este item.", category='danger')
        #Venda
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Parabéns! Você vendeu {s_item_object.name} por {s_item_object.price}", category='success')
            else:
                flash(f"Infelizmente você não conseguiu vender {s_item_object.name}.", category='danger')
                
        return redirect(url_for('dash_page'))
    
    if request.method == "GET":
        items=Item.query.filter_by(owner=None)
        owned_items=Item.query.filter_by(owner=current_user.id)
        return render_template('dashpage.html', items=items, 
                               purchase_Form = purchase_Form, owned_items=owned_items,
                               selling_form = selling_form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create=User(username=form.username.data,
                            email=form.email.data,
                            password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Conta criada com sucesso! Você está logado como {user_to_create.username}', category='success')
        return redirect(url_for('dash_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Ocorreu um erro registrando este usuário: {err_msg}", category='danger')
    return render_template('register.html', form=form)

@app.route('/registerItem', methods=['GET', 'POST'])
def register_item_page():
    form = PostItem()
    if form.validate_on_submit():
        item_to_create=Item(name = form.name.data,
                            price = form.price.data,
                            code = form.code.data,
                            description = form.description.data,
                            owner = current_user.id)
        db.session.add(item_to_create)
        db.session.commit()
        flash(f'Item {item_to_create.name} criado com sucesso!', category='Success')
        return redirect(url_for('dash_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Ocorreu um erro registrando este item! {err_msg}", category='danger')
    return render_template('registerItem.html', form=form)
        
        

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
            ):
            login_user(attempted_user)
            flash(f"Sucesso! Logado como: {attempted_user.username}.", category='success')
            return redirect(url_for('dash_page'))
        else:
            flash('Usuário ou senha errados. Tente novamente!', category='danger')
            
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'Você foi desconectado!', category='info')
    return redirect(url_for("home_page"))

