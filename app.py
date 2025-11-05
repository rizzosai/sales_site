from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# Main packages page (HTML content will be inserted here)
with open('packages.html', 'r', encoding='utf-8') as f:
    packages_html = f.read()

@app.route('/')
def packages():
    return render_template_string(packages_html)

@app.route('/thank-you')
def thank_you():
    # Redirect to backoffice after 5 seconds
    return '''
    <html><head><meta http-equiv="refresh" content="5;url=https://backoffice.rizzosai.com/login">
    <title>Thank You!</title></head>
    <body style="font-family:sans-serif;text-align:center;padding-top:60px;">
    <h1>Thank you for your purchase!</h1>
    <p>You will be redirected to your backoffice shortly.<br>If not, <a href="https://backoffice.rizzosai.com/login">click here</a>.</p>
    </body></html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
