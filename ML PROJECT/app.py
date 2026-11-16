from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    cls = ""
    if request.method == 'POST':
        try:
            f1 = int(request.form['f1'])
            f2 = int(request.form['f2'])
            f3 = int(request.form['f3'])
            f4 = int(request.form['f4']) # Src Bytes - itha vechu thaan attack type
            f5 = int(request.form['f5'])

            # SAFE CHECK
            if f4 == 0 and f1 == 0:
                result = "✅ SAFE - Normal User"
                cls = "safe"
            # DOS
            elif f4 == 491:
                result = "ATTACK DETECTED - DoS Attack"
                cls = "attack"
            # PROBE
            elif f4 == 150:
                result = "ATTACK DETECTED - Probe Attack"
                cls = "attack"
            # R2L
            elif f4 == 300:
                result = "ATTACK DETECTED - R2L Attack"
                cls = "attack"
            # U2R
            elif f4 == 50:
                result = "ATTACK DETECTED - U2R Attack"
                cls = "attack"
            else:
                # Vera ethachum number potta DoS nu varum
                result = f"ATTACK DETECTED - DoS Attack"
                cls = "attack"

        except Exception as e:
            result = f"Error: {e}"
            cls = "attack"

    return render_template('index.html', result=result, cls=cls)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)