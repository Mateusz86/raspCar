from flask import Flask, render_template
import RPi.GPIO as GPIO
import time


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led')
def led():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4,GPIO.OUT)
    print "LED ON"
    GPIO.output(4,GPIO.HIGH)
    time.sleep(1)
    print "LED OF"
    GPIO.output(4,GPIO.LOW)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
