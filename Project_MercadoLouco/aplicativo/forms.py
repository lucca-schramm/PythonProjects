from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from aplicativo.models import User, Item

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Usuário já utilizado. Por favor tente um diferente!')
        
    def validate_email(self, email_to_check):
        email=User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email já utilizado. Por favor tente um diferente!')   
    
    username = StringField(label='Usuário:', validators=[Length(min=2, max=30), DataRequired()])
    email=StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Senha:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirmar Senha:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Criar Conta')
    
class LoginForm(FlaskForm):
    username= StringField(label='Usuário:', validators=[DataRequired()])
    password= StringField(label='Senha:', validators=[DataRequired()])
    submit = SubmitField(label='Fazer Login')
    
class PurchaseItem(FlaskForm):
    submit = SubmitField(label='Comprar Item')
    
class SellItem(FlaskForm):
    submit = SubmitField(label='Vender Item')
    
class PostItem(FlaskForm):
    def validate_code(self, code_to_check):
        code=Item.query.filter_by(code=code_to_check.data).first()
        if code:
            raise ValidationError('Código já utilizado. Por favor tente um diferente!')
    name = StringField(label='Nome', validators=[Length(min=3, max=20), DataRequired()])
    price = StringField(label='Preço: ', validators=[Length(min=1, max=7), DataRequired()])
    code = StringField(label='Código: ', validators=[Length(min=1, max=12), DataRequired()])
    description = StringField(label='Descrição: ', validators=[Length(min=1, max=1024), DataRequired()])
    submit = SubmitField(label="Registrar Item")