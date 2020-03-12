from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('answer.html')

    elif request.method == 'POST':
        params = {}
        params['surname'] = request.form.get('surname')
        params['name'] = request.form.get('name')
        params['email'] = request.form.get('email')
        params['education'] = request.form.get('education')
        params['profession'] = []
        prof = {'prof_1': 'Инженер-исследователь', 'prof_2': 'Пилот',
                'prof_3': 'Строитель', 'prof_4': 'Экзобиолог',
                'prof_5': 'Врач', 'prof_6': 'Инженер по терраформированию',
                'prof_7': 'Климатолог',
                'prof_8': 'Специалист по радиационной защите',
                'prof_9': 'Астрогеолог', 'prof_10': 'Гляциолог',
                'prof_11': 'Инженер жизнеобеспечения',
                'prof_12': 'Метеоролог',
                'prof_13': 'Оператор марсохода', 'prof_14': 'Киберинженер',
                'prof_15': 'Штурман', 'prof_16': 'Пилот дронов'}
        for i in range(1, 17):
            if request.form.get('prof_' + str(i)) == 'on':
                params['profession'].append(prof['prof_' + str(i)])
        params['motivation'] = request.form.get('about')
        params['sex'] = request.form.get('sex')
        params['ready'] = 'True' if request.form.get(
            'accept') == 'on' else 'False'

        return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
