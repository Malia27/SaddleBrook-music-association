from flask import Flask, render_template, request, redirect, url_for, flash, app

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route('/send_inquiry', methods=['GET', 'POST'])
def send_inquiry():
    if request.method == 'POST':
        contact_name = request.form.get('contact_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        event_title = request.form.get('event_title')
        description = request.form.get('description')
        estimated_cost = request.form.get('estimated_cost')
        
        flash('Inquiry submitted successfully! The team will review your inquiry and contact you soon.', 'success')
        return redirect(url_for('send_inquiry'))
        
    return render_template('send_inquiry.html')

if __name__ == "__main__":
    app.run(debug=True)
