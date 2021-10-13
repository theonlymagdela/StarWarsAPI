from flask import Flask, render_template, request, redirect, session, flash
import requests
from util import json_response
import json
import data_handler as dh
import user
import sql


app = Flask(__name__)
app.secret_key = '#@_fu•ka_@!'

# --------------------------------------------- pages ---------------------------------------------


@app.route('/')
def main_page():

    return render_template('main.html')


def data_get_all(url):
    page = 1
    new_data = []

    for n in range(9):
        data_base = requests.get(f'{url}/?page={page}').json()['results']
        for data in data_base:
            new_dict = {'name': data['name'],
                        'height': data['height'],
                        'mass': data['mass'],
                        'hair_color': data['hair_color'],
                        'skin_color': data['skin_color'],
                        'eye_color': data['eye_color'],
                        'birth_year': data['birth_year'],
                        'gender': data['gender'],
                        'homeworld': data['homeworld']}
            new_data.append(new_dict)
        page += 1

    return new_data


@app.route('/planets')
@app.route('/planets/<int:page_number>')
def planets_all(page_number):
    column_names = ["Name", "Diameter", "Climate", "Terrain", "Surface Water", "Population", "Residents", ""]
    contents = ['name', 'diameter', 'climate', 'terrain', 'surface_water', 'population', 'residents']
    planets = requests.get(f'https://swapi.dev/api/planets/?page={page_number}').json()['results']
    ppl = data_get_all('https://swapi.dev/api/people')

    return render_template('index.html',
                           column_names=column_names,
                           contents=contents,
                           data_base=planets,
                           residents=ppl,
                           page_number=page_number,
                           page='/planets',
                           title="Planets")


@app.route('/residents')
@app.route('/residents/<int:page_number>')
def residents_all(page_number):
    column_names = ["Name", "Height", "Mass", "Hair color", "Skin color", "Eye color", "Birth year", "Gender", ""]
    contents = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender']
    people = requests.get(f'https://swapi.dev/api/people/?page={page_number}').json()['results']

    return render_template('table.html',
                           column_names=column_names,
                           contents=contents,
                           data_base=people,
                           page_number=page_number,
                           page='/residents',
                           title="Characters",
                           last_page=9)


@app.route('/films')
def films_all():
    column_names = ["Title", "Episode", "Director", "Release Date", "Opening", ""]
    contents = ['title', 'episode_id', 'director', 'release_date', 'opening_crawl']
    episodes = requests.get('https://swapi.dev/api/films/?page=1').json()['results']
    page_number = 1

    return render_template('table.html',
                           column_names=column_names,
                           contents=contents,
                           data_base=episodes,
                           page_number=page_number,
                           title="Films",
                           last_page=1)


@app.route('/stillFighting')
def still_fighting():

    return render_template('still-fighting.html')

# --------------------------------------------- user ---------------------------------------------


@app.route('/user/<int:user_id>')
def user_page(user_id):
    user_this = sql.user_get_by_id(user_id)

    return render_template('user.html', user=user_this)


@app.route('/registration', methods=['POST'])
@json_response
def registration():
    body = json.loads(request.data)
    mail = body['mail']
    password = user.password_hash(body['password'])
    name = body['name']
    surname = body['surname']

    if mail not in sql.users_get_mail():
        new_user = [mail, password, name, surname]
        flash("Registration was a success. Now, You can now login In")
        return dh.user_add(new_user)
    else:
        flash(f"It seams {mail} already exists in the system. Maybe you already have an account")


@app.route('/login', methods=['POST'])
def login_data_process():
    if user.is_logged():
        return redirect('/')

    body = json.loads(request.data)
    mail = body['mail']
    password = body['password']

    if not user.valid_login(mail, password):
        flash('Invalid username or password!')
        return redirect('/login')

    session['id'] = sql.user_id_get_by_mail(mail)
    session['username'] = mail
    flash('You were successfully logged in!')

    return redirect('/')


@app.route('/logout')
def logout_data_process():
    if user.is_logged():
        session.pop('id', None)
        session.pop('username', None)
        flash('You were successfully logged out!')

    return redirect('/')


# --------------------------------------------- main ---------------------------------------------


def main():
    app.run(
        host='0.0.0.0',
        port=20000,
        debug=True
    )


if __name__ == '__main__':
    main()
