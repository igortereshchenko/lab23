from flask import render_template, request, redirect, url_for, Flask
from forms.CharacteristicForm import CharacteristicForm
from forms.EditCharacteristicForm import EditCharacteristicForm
from forms.EditGoodsForm import EditGoodsForm
from forms.EditStoreForm import EditStoreForm
from forms.GoodsForm import GoodsForm
from forms.StoreForm import StoreForm
from forms.UserForm import UserForm


import plotly
import json
from flask_sqlalchemy import SQLAlchemy
import plotly.graph_objs as go
from sqlalchemy.sql import func


app = Flask(__name__)
app.secret_key = 'key'

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:vlad16tank@localhost/NoSQL'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eqbfekyniuxapz:c2752077ab182298d4641a87b1516e2072c4ceb7ddb45e3064f3bbf463baf601@ec2-54-221-214-3.compute-1.amazonaws.com:5432/deuqr23i61d257'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Store_Have_Goods(db.Model):
    __tablename__  = 'store_have_goods'
    good_id_fk = db.Column(db.Integer, db.ForeignKey('goods.good_id'), primary_key=True)
    store_id_fk = db.Column(db.Integer, db.ForeignKey('store.store_id'), primary_key=True)

class User_Have_Goods(db.Model):
    __tablename__  = 'user_have_goods'
    good_id_fk = db.Column(db.Integer, db.ForeignKey('goods.good_id'), primary_key=True)
    user_name_fk = db.Column(db.String(20), db.ForeignKey('user.user_name'), primary_key=True)

class User(db.Model):

    __tablename__ = 'user'
    user_name = db.Column(db.String(20), primary_key=True)
    user_birthday= db.Column(db.Date, info={'min': '2000-01-01'}, nullable=False)
    user_salary = db.Column(db.Integer, nullable=False)
    user_position = db.Column(db.String(100), nullable=False)
    u_good_id = db.relationship("Goods",secondary="user_have_goods")

class Characteristic(db.Model):

    __tablename__ = 'characteristic'
    charac_name = db.Column(db.String(20), primary_key=True)
    charac_description= db.Column(db.String(100),primary_key=True)
    c_good_id_fk = db.Column(db.Integer, db.ForeignKey('goods.good_id'))


class Goods(db.Model):

    __tablename__ = 'goods'
    good_id = db.Column(db.Integer, primary_key=True)
    good_name = db.Column(db.String(45))
    good_model = db.Column(db.String(100))

    store_id_fk = db.relationship("Store", secondary="store_have_goods")
    results = db.relationship("Result")
    characters = db.relationship("Characteristic")
    users=db.relationship("User",secondary="user_have_goods")

class Result(db.Model):

    __tablename__ = 'result'

    result_id = db.Column(db.Integer, primary_key=True)
    r_good_id_fk = db.Column(db.Integer, db.ForeignKey('goods.good_id'))


class Store(db.Model):

    __tablename__ = 'store'
    store_id = db.Column(db.Integer, primary_key=True)
    store_name= db.Column(db.String(20), unique=True, nullable=False)
    store_link = db.Column(db.String(40), unique=True)
    good_id_store_fk = db.relationship("Goods", secondary="store_have_goods")
'''
db.create_all()

db.session.query(Store_Have_Goods).delete()
db.session.query(Characteristic).delete()
db.session.query(Store).delete()
db.session.query(Result).delete()
db.session.query(Goods).delete()
db.session.query(User).delete()

Good1 = Goods(
    good_id=10,
    good_name ="Samsung",
    good_model ="S10")
Good2 = Goods(
    good_id=14,
    good_name="OnePlus",
    good_model="7 PRO")
Good3 = Goods(
    good_id=11,
    good_name="IPhone",
    good_model="11")
Good4 = Goods(
    good_id=12,
    good_name="Huawei",
    good_model="P30 PRO")
Good5 = Goods(
    good_id=13,
    good_name="Xiaomi",
    good_model="Mi9")


Charc1 = Characteristic(

    charac_name="RAM",
    charac_description="4Gb"
)
Charc6 = Characteristic(

    charac_name="RAM",
    charac_description="8Gb"
)
Charc2 = Characteristic(

    charac_name="Color",
    charac_description="black")
Charc7 = Characteristic(

    charac_name="Color",
    charac_description="yellow")

Charc3 = Characteristic(
    charac_name="Capacity",
    charac_description="64Gb")

Charc4 = Characteristic(

    charac_name="Display",
    charac_description="16:9")

Charc5 = Characteristic(

    charac_name="Front Camera",
    charac_description="12MP")


Store1 = Store(
    store_id = 12,
    store_name="Rozetka",
    store_link="https://rozetka.com.ua")
Store2 = Store(
    store_id = 11,
    store_name="Comfy",
    store_link="https://comfy.com.ua")
Store3 = Store(
    store_id = 14,
    store_name="Citrus",
    store_link="https://citrus.com.ua")
Store4 = Store(
    store_id = 13,
    store_name="Hotline",
    store_link="https://hotline.com.ua")
Store5 = Store(
    store_id = 0,
    store_name="Allo",
    store_link="https://allo.com.ua")

Result1 = Result(
    result_id =4,

)

Result2 = Result(
    result_id =0,
    )

Result3 = Result(
    result_id =3,
    )

Result4 = Result(
    result_id =2,
    )
Result5 = Result(
    result_id =1,
    )



# create relations
Good1.results.append(Result1)
Good2.results.append(Result2)
Good3.results.append(Result3)
Good4.results.append(Result4)
Good5.results.append(Result5)

Good1.store_id_fk.append(Store1)
Good1.store_id_fk.append(Store2)
Good1.store_id_fk.append(Store3)

Good2.store_id_fk.append(Store2)
Good2.store_id_fk.append(Store3)
Good2.store_id_fk.append(Store4)

Good3.store_id_fk.append(Store1)
Good3.store_id_fk.append(Store3)

Good4.store_id_fk.append(Store4)

Good5.store_id_fk.append(Store5)



Good1.characters.append(Charc1)
Good1.characters.append(Charc2)
Good1.characters.append(Charc3)
Good1.characters.append(Charc4)
Good1.characters.append(Charc5)


Good2.characters.append(Charc6)
Good2.characters.append(Charc7)
Good2.characters.append(Charc3)
Good2.characters.append(Charc4)
Good2.characters.append(Charc5)


Good3.characters.append(Charc3)
Good4.characters.append(Charc4)
Good5.characters.append(Charc5)


# insert into database
db.session.add_all([Result1,Result2,Result3,Result4,Result5])
db.session.add_all([Charc1,Charc2,Charc3,Charc4,Charc5])
db.session.add_all([Good1,Good2,Good3,Good4,Good5])
db.session.add_all([Store1,Store2,Store3,Store4,Store5])


db.session.commit()
'''

@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def user():
    result = db.session.query(User).all()

    return render_template('all_users.html', result=result)

@app.route('/add', methods=['GET'])
def user_add():
    db.session.query(User).delete()
    User1=User(
        user_name = "Vlad",
        user_birthday= "2001-01-01",
        user_salary = 999,
        user_position = "manager"
    )

    User2=User(
        user_name = "Dima",
        user_birthday= "2002-01-01",
        user_salary = 888,
        user_position = "full-stack"
    )
    User3=User(
        user_name = "Anya",
        user_birthday= "2003-01-01",
        user_salary = 777,
        user_position = "junior"
    )
    db.session.add_all([User1,User3,User2])
    db.session.commit()
    return redirect('/get')


@app.route('/insert', methods=['GET', 'POST'])
def new_user():
    form = UserForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('new_user_form.html', form=form, form_name="New user",
                                   action="new_user")
        else:
            new_user = User(

            user_name=form.user_name.data,
            user_birthday = form.user_birthday.data,
            user_salary = form.user_salary.data,
            user_position = form.user_position.data,

            )

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('user'))

    return render_template('new_user_form.html', form=form, form_name="New user",
                           action="new_user")



@app.route('/all_characteristic', methods=['GET'])
def characteristic():
    result = db.session.query(Characteristic).all()

    return render_template('all_characteristic.html', result=result)


@app.route('/new_characteristic', methods=['GET', 'POST'])
def new_characteristic():
    form = CharacteristicForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('new_charactersitic_form.html', form=form, form_name="New characteristic",
                                   action="new_characteristic")
        else:
            new_characteristic = Characteristic(

                charac_name=form.charac_name.data,
                charac_description=form.charac_description.data

            )

            db.session.add(new_characteristic)
            db.session.commit()

            render_template('all_users.html', form=form, form_name="all_users",
                           action="all_users")

    return render_template('new_charactersitic_form.html', form=form, form_name="New characteristic",
                           action="new_characteristic")


'''
@app.route('/edit_characteristic/<string:charac_name>', methods=['GET', 'POST'])
def edit_characteristic(charac_name):

    form = EditCharacteristicForm()
    result = db.session.query(Characteristic).filter(Characteristic.charac_name == charac_name).one()

    if request.method == 'GET':


        form.charac_name.data = result.charac_name
        form.charac_description.data = result.charac_description



        return render_template('edit_characteristic_form.html', form=form, form_name='edit characteristic')
    elif request.method == 'POST':
        result.charac_id = form.charac_id.data
        result.charac_name = form.charac_name.data
        result.charac_description = form.charac_description.data



        db.session.commit()
        return redirect('/all_characteristic')
'''


@app.route('/delete_characteristic/<string:charac_name>/<string:charac_description>', methods=['GET', 'POST'])
def delete_characteristic(charac_name, charac_description):
    result = db.session.query(Characteristic).filter(Characteristic.charac_name == charac_name).filter(
        Characteristic.charac_description == charac_description).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/all_characteristic')


@app.route('/all_goods', methods=['GET'])
def goods():
    result = db.session.query(Goods).all()

    return render_template('all_goods.html', result=result)


@app.route('/new_goods', methods=['GET', 'POST'])
def new_goods():
    form = GoodsForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('new_goods_form.html', form=form, form_name="New goods", action="new_goods")
        else:
            new_goods = Goods(
                good_id=form.good_id.data,
                good_name=form.good_name.data,
                good_model=form.good_name.data

            )

            db.session.add(new_goods)
            db.session.commit()

            return redirect(url_for('goods'))

    return render_template('new_goods_form.html', form=form, form_name="New goods", action="new_goods")


@app.route('/edit_goods/<string:good_name>', methods=['GET', 'POST'])
def edit_goods(good_name):
    form = EditGoodsForm()
    result = db.session.query(Goods).filter(Goods.good_name == good_name).one()

    if request.method == 'GET':

        form.good_id.data = result.good_id
        form.good_name.data = result.good_name
        form.good_model.data = result.good_model

        return render_template('edit_goods_form.html', form=form, form_name='edit goods')
    elif request.method == 'POST':

        result.good_id = form.good_id.data
        result.good_name = form.good_name.data
        result.good_model = form.good_model.data

        db.session.commit()
        return redirect('/all_goods')


@app.route('/delete_goods/<string:good_name>', methods=['GET', 'POST'])
def delete_goods(good_name):
    result = db.session.query(Goods).filter(Goods.good_name == good_name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/all_goods')


@app.route('/all_store', methods=['GET'])
def store():
    result = db.session.query(Store).all()

    return render_template('all_store.html', result=result)


@app.route('/new_store', methods=['GET', 'POST'])
def new_store():
    form = StoreForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('new_store_form.html', form=form, form_name="New store", action="new_store")
        else:
            new_store = Store(
                store_id=form.store_id.data,
                store_name=form.store_name.data,
                store_link=form.store_link.data

            )

            db.session.add(new_store)
            db.session.commit()

            return redirect(url_for('store'))

    return render_template('new_store_form.html', form=form, form_name="New store", action="new_store")


@app.route('/edit_store/<string:store_name>', methods=['GET', 'POST'])
def edit_store(store_name):
    form = EditStoreForm()
    result = db.session.query(Store).filter(Store.store_name == store_name).one()

    if request.method == 'GET':

        form.store_id.data = result.store_id
        form.store_name.data = result.store_name
        form.store_link.data = result.store_link

        return render_template('edit_store_form.html', form=form, form_name='edit store')
    elif request.method == 'POST':

        result.store_id = form.store_id.data
        result.store_name = form.store_name.data
        result.store_link = form.store_link.data

        db.session.commit()
        return redirect('/all_store')


@app.route('/delete_store/<string:store_name>', methods=['GET', 'POST'])
def delete_store(store_name):
    result = db.session.query(Store).filter(Store.store_name == store_name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/all_store')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    query2 = (
        db.session.query(
            User.user_position,
            User.user_salary).label('salary')
        )



    position, salary = zip(*query2)
    pie = go.Pie(
        labels=position,
        values=salary
    )


    data = {
        "pie": [pie]
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)


if __name__ == "__main__":
    app.run(debug=True)




