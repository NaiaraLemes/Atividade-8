from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)

SECRET_KEY = 'minha_senha' 
app.config['SECRET_KEY'] = SECRET_KEY

class Formulario(FlaskForm):
    altura = FloatField('altura', validators=[DataRequired()])
    largura = FloatField('largura', validators=[DataRequired()])
    tipoCortina =  SelectField(u'Tipo Curtina', choices=[('oxford','Oxford'), ('tergal','Tergal'), ('gabardine', 'Gabardine')])

@app.route("/", methods=["GET", "POST"])
def home():
    formulario = Formulario()
    if formulario.validate_on_submit():
        largura = formulario.largura.data
        altura = formulario.altura.data
        tipoCortina = formulario.tipoCortina.data
        return "Sua cortina de" + " Tipo de Curtina " + str(tipoCortina) + "Largura: " + str(largura) +" Altura: " + str(altura) +  " Custará R$ " + str(altura * largura * 100)
    return render_template('home.html', form=formulario)