import MainRepo
import NgoModel,NgoRepo,DonorModel,DonorRepo
from flask import Flask, render_template, redirect, request
from flask.helpers import url_for

import os

app = Flask(__name__)


if(os.environ.get('ENV') == "Production"):
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = MainRepo.Repo(app.config)
ngoRepo = NgoRepo.Repo(db)
donorRepo = DonorRepo.Repo(db)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')



@app.route('/donation-form', methods=['GET','POST'])
def donation():
    if(request.method == "POST"):
        form = request.form
        donor = DonorModel.Donor(form.get('name'),form.get('mobile'),form.get('email'),form.get('address'),form.get('donation_Item_Name'),form.get('donation_Item_Number'),form.get('timeSlot'),form.get('date'),)
        success = donorRepo.addDonor(donor)
        if(success):
            return "Form Information Recorded"
        else:
            return "Database Error"
    if(request.method == "GET"):
        return render_template('donation-form.html')



@app.route('/ngo-registration', methods=['GET','POST'])
def ngo():
    if(request.method == "POST"):
        form = request.form
        ngo = NgoModel.Ngo(form.get("name"),form.get("email"),form.get("address"))
        success = ngoRepo.addNgo(ngo)
        if(success):
            return "Ngo Registered Successfully"
        else:
            return "Databse Error"
    if(request.method == "GET"):
        return render_template('ngo-registration-form.html')



@app.route('/inner-page', methods=['GET'])
def inner_page():
    if(request.method == "GET"):
        return render_template('inner-page.html')



@app.route('/', methods=['GET'])
@app.route('/Home', methods=['GET'])
def redir():
    return redirect(url_for('home'))


@app.before_request
def beforeRequest():
    if(app.config["ENV"] == "production"):
        if not request.url.startswith('https'):
            return redirect(request.url.replace('http', 'https', 1))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
