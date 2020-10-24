from flask import Flask,render_template,redirect,url_for,request,session,flash
import numpy as np
from joblib import load,dump
rf=load("myiplmodel.pkl")
app=Flask(__name__)
app.secret_key="lucky"
@app.route("/")
def home():
        return render_template("home.html")
@app.route('/predict',methods=['POST'])
def predict():
     if request.method == "POST":
         session.permanent = True
         name_month = request.form["month"]
         bat_name=request.form["bat_team"]
         bowl_name=request.form["bowl_team"]
         overs=request.form["overs"]
         extras=request.form["extras"]
         runs=request.form["runs"]
         wickets=request.form["wickets"]
         last_runs=request.form["last_runs"]
         last_wickets=request.form["last_wickets"]
         bats_runs=request.form["bats_runs"]
         if int(runs) < int(last_runs):
             flash("Last five over score can't be greater than current score","info")
             return render_template('home.html')
         if int(wickets) < int(last_wickets):
             flash("Last five over wickets fallen can't be greater than total wicket fallen","info")
             return render_template('home.html')
         if int(runs) < int(bats_runs):
             flash("Batsman run can't be greater than current score","info")
             return render_template('home.html')
         try:
            if name_month == "January":
             a = np.array([[1]])
            elif name_month== "February":
             a = np.array([[2]])
            elif name_month == "March":
             a = np.array([[3]])
            elif name_month == "April":
             a = np.array([[4]])
            elif name_month == "May":
             a = np.array([[5]])
            elif name_month == "June":
             a = np.array([[6]])
            elif name_month== "July":
             a = np.array([[7]])
            elif name_month == "August":
             a = np.array([[8]])
            elif name_month == "September":
             a = np.array([[9]])
            elif name_month == "October":
             a = np.array([[10]])
            elif name_month == "November":
             a = np.array([[11]])
            elif name_month == "December":
             a = np.array([[12]])
            else:
                raise Exception
         except:
             flash("Some Error in Month Name","info")
             return render_template("home.html")
         try:
           if bat_name == "Delhi Capitals":
             a = np.concatenate((a, [[1, 0, 0, 0, 0, 0, 0]]), axis=1)
           elif bat_name == "Kings XI Punjab":
             a = np.concatenate((a, [[0, 1, 0, 0, 0, 0, 0]]), axis=1)
           elif bat_name == "Kolkata Knight Riders":
             a = np.concatenate((a, [[0, 0, 1, 0, 0, 0, 0]]), axis=1)
           elif bat_name == "Mumbai Indians":
             a = np.concatenate((a, [[0, 0, 0, 1, 0, 0, 0]]), axis=1)
           elif bat_name == "Rajasthan Royals":
             a = np.concatenate((a, [[0, 0, 0, 0, 1, 0, 0]]), axis=1)
           elif bat_name == "Royal Challengers Bangalore":
             a = np.concatenate((a, [[0, 0, 0, 0, 0, 1, 0]]), axis=1)
           elif bat_name == "Sunrisers Hyderabad":
             a = np.concatenate((a, [[0, 0, 0, 0, 0, 0, 1]]), axis=1)
           elif bat_name == "Chennai Super Kings":
             a = np.concatenate((a, [[0, 0, 0, 0, 0, 0, 0]]), axis=1)
           else:
             raise Exception
           if bowl_name == "Delhi Capitals":
             a = np.concatenate((a, [[1, 0, 0, 0, 0, 0, 0]]), axis=1)
           elif bowl_name == "Kings XI Punjab":
             a = np.concatenate((a, [[0, 1, 0, 0, 0, 0, 0]]), axis=1)
           elif bowl_name == "Kolkata Knight Riders":
             a = np.concatenate((a, [[0, 0, 1, 0, 0, 0, 0]]), axis=1)
           elif bowl_name == "Mumbai Indians":
             a = np.concatenate((a, [[0, 0, 0, 1, 0, 0, 0]]), axis=1)
           elif bowl_name == "Rajasthan Royals":
             a = np.concatenate((a, [[0, 0, 0, 0, 1, 0, 0]]), axis=1)
           elif bowl_name == "Royal Challengers Bangalore":
             a = np.concatenate((a, [[0, 0, 0, 0, 0, 1, 0]]), axis=1)
           elif bowl_name == "Sunrisers Hyderabad":
             a = np.concatenate((a, [[0, 0, 0, 0, 0, 0, 1]]), axis=1)
           elif bowl_name == "Chennai Super Kings":
             a = np.concatenate((a, [[0, 0, 0, 0, 0, 0, 0]]), axis=1)
           else:
             raise Exception
         except:
             flash("Some Error in Team Name","info")
             return  render_template("home.html")

         if bat_name==bowl_name:
             flash("Both Team Can't be Same","info")
             return  render_template("home.html")

         a = np.concatenate((a, [[overs]]), axis=1)
         a = np.concatenate((a, [[extras]]), axis=1)
         a = np.concatenate((a, [[runs]]), axis=1)
         a = np.concatenate((a, [[wickets]]), axis=1)
         a = np.concatenate((a, [[last_runs]]), axis=1)
         a = np.concatenate((a, [[last_wickets]]), axis=1)
         a = np.concatenate((a, [[bats_runs]]), axis=1)
         res = rf.predict(a)
         if res > runs:
           for val in res:
             flash(f"The first innings score will be around {int(val)}","info")
         else:
              flash(f"The first innings score will be around {int(runs)}","info")

         return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)
