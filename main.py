from flask import Flask, render_template, redirect, session, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import secrets
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.secret_key = secrets.token_hex(16)

db = SQLAlchemy(app)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    about = db.Column(db.String(300), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    photo_url = db.Column(db.String(300), nullable=False)
    add_date = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f"<Product {self.id}"


@app.route('/corzina')
def corzina():
        return render_template('corzina.html', products=Products.query.all())


@app.route('/delete_product')
def delete_product():
    if 'admin_status' in session and session['admin_status']:
        prod_id = request.args.get('id')
        filter_ = request.args.get("filter")
        try:
            product = Products.query.filter_by(id=prod_id).delete()
            db.session.commit()
        except:
            return "Ошибка БД"
        return redirect(f'/?search={filter_}')


@app.route("/")
def main():
    if 'cart' not in session:
        session['cart'] = []
    session['admin_status'] = True
    products = Products.query.order_by(Products.id.desc()).all()
    filters = request.args.get("search")
    if filters == None:
        filters = ''

    isAdmin = str('admin_status' in session and session['admin_status'])


    return render_template('index.html', products=products, filter=filters, admin=isAdmin, cart=session['cart'])


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == "GET":
        if 'admin_status' in session and session['admin_status']:
            return redirect(f"/add_product?admin=true&time={datetime.utcnow().strftime('%d_%m_%Y_%H_%M_%S')}")
        else:
            return render_template('auth.html')
    else:
        login = request.form['login']
        password = request.form['password']

        if login == "admin" and password == "ober":
            session['admin_status'] = True
            return redirect('/admin')
        else:
            return redirect('/')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if 'admin_status' in session and session['admin_status'] and request.args.get("admin") == 'true':
        if request.method == "GET":
            return render_template('add_product.html')
        else:
            name = request.form['name']
            about = request.form['description']
            price = request.form['price']
            image = request.files['image']

            add_date = str(request.args.get('time'))
            image_path = f'static/img/products/{name}_{add_date}.jpg'

            image.save(image_path)

            product = Products(name=name, about=about, cost=price, photo_url=image_path, add_date=add_date)

            try:
                db.session.add(product)
                db.session.commit()
                return redirect('/admin')
            except:
                return "Проищошла ошибка БД"
    else:
        return redirect('/')




@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    id = request.form.get('productId')
    add = False

    if int(id) not in session['cart']:

        session['cart'].append(int(id))
        add = True
    else:
        session['cart'].remove(int(id))

    session.modified = True

    response = {
        'status': "OK" if add else "REM",
        'cart_count': len(session['cart'])
    }
    return response





if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()