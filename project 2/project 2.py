from flask import Flask,render_template,request,url_for
from urllib.parse import unquote


app = Flask(__name__,static_url_path = "/Users/sea_fog/Desktop/hse/2 курс/колд/project 2", static_folder = "/Users/sea_fog/Desktop/hse/2 курс/колд/project 2")





#def make_dict(inputs):
#    for list in inputs:
#        for word in list:
#            word = word.lower()

#    for list in inputs:
#        nums = []
#        for i in list1:
#            nums.append(list.count(i))
#    inputstats = dict(zip(list(set(inputs)),list(set(nums))))

@app.route('/')
def main_page():
    if request.args:
        anorak = unquote(request.args['anorak'])
        dozhdevik = unquote(request.args['dozhdevik'])
        kosuxa = unquote(request.args['kosuxa'])
        parka = unquote(request.args['parka'])
        trench = unquote(request.args['trench'])
        bushlat = unquote(request.args['bushlat'])
        inputs = [anorak,dozhdevik,kosuxa,parka,trench,bushlat]
        f = open('inputs.txt','a',encoding='utf-8')
        for word in inputs:
                f.write(word + '\n')
        f.write('\n')
    return render_template('main_page.html')

#@app.route('/stats')
#def stats_page():
#    return render_template('stats.html',jsonlink=url_for())
#
#@app.route('/json')
#def json_page():


#@app.route('/search')
#def search_page(results_page):
#    return render_template('search_page.html',results_link=url_for(results_page())

#@app.route('/results')
#def results_page():
#    return





if __name__ == '__main__':
    app.run(debug=True)


