from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_page1():

    country = request.args['Country']
    typeOfFood = request.args['type']

    if country == 'America':
        reply1 = "You would like food from America"
    elif country == 'Italy':
        reply1 = "You would like food from Italy"
    else:
        reply1 = "You would like food from Mexico"
        
    if typeOfFood == 'Main':
        reply2 = "You would like a Main Course"
    else: 
        reply2 = "You would like a dessert"
        
    if country == 'America' and typeOfFood == 'Main':
        reply3 = "Our recomendation would be a hotdog"
    elif country == 'America' and typeOfFood == 'Dessert':
        reply3 = "Our recomendation would be cake"
        
    if country == 'Italy' and typeOfFood == 'Main':
        reply3 = "Our recomendation would be a pizza"
    elif country == 'Italy' and typeOfFood == 'Dessert':
        reply3 = "Our recomendation would be cannoli"
        
    if country == 'Mexico' and typeOfFood == 'Main':
        reply3 = "Our recomendation would be a taco"
    elif country == 'Mexico' and typeOfFood == 'Dessert':
        reply3 = "Our recomendation would be tres leches cake"
        
    return render_template('page1.html', response1 = reply1, response2 = reply2, response3 = reply3)

"""@app.route("/p2")
def render_page2():

    country = request.args['Country']
    typeOfFood = request.args['type']

    if country == 'America' and typeOfFood == 'Main':
        reply3 = "Our reccomendation would be a hotdog"
    elif typeOfFood == 'Dessert':
        reply3 = "Our recomendation would be cake"
        
    return render_template('page2.html', response3 = reply3)"""
    
if __name__=="__main__":
    app.run(debug=False)
