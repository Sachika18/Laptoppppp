from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and label encoders
model = joblib.load("laptop_price_regression.pkl")
le_dict = joblib.load("label_encoders.pkl")

# Function to convert ROM to GB
def convert_rom(value):
    value = str(value).upper().strip()
    if 'TB' in value:
        return int(float(value.replace('TB','').strip()) * 1024)
    elif 'GB' in value:
        return int(float(value.replace('GB','').strip()))
    else:
        return int(value)

@app.route('/')
def home():
    # Send label encoder classes to HTML to dynamically populate dropdowns
    return render_template(
        'index.html',
        brands=le_dict['brand'].classes_,
        processors=le_dict['processor'].classes_,
        cpus=le_dict['CPU'].classes_,
        gpus=le_dict['GPU'].classes_,
        os_list=le_dict['OS'].classes_
    )

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form input
        brand = request.form.get('brand')
        processor = request.form.get('processor')
        cpu = request.form.get('cpu')
        ram = int(request.form.get('ram', 0))
        rom = convert_rom(request.form.get('rom', '0GB'))
        gpu = request.form.get('gpu')
        os_val = request.form.get('os')

        # Transform using LabelEncoders with fallback for unseen labels
        def safe_transform(le, value):
            if value in le.classes_:
                return le.transform([value])[0]
            else:
                return -1  # Unknown label

        data = {
            'brand': safe_transform(le_dict['brand'], brand),
            'processor': safe_transform(le_dict['processor'], processor),
            'CPU': safe_transform(le_dict['CPU'], cpu),
            'Ram': ram,
            'ROM': rom,
            'GPU': safe_transform(le_dict['GPU'], gpu),
            'OS': safe_transform(le_dict['OS'], os_val)
        }

        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]

        return render_template(
            'index.html',
            brands=le_dict['brand'].classes_,
            processors=le_dict['processor'].classes_,
            cpus=le_dict['CPU'].classes_,
            gpus=le_dict['GPU'].classes_,
            os_list=le_dict['OS'].classes_,
            prediction_text=f"💻 Estimated Laptop Price: ₹ {round(prediction,2):,}"
        )

    except Exception as e:
        return render_template(
            'index.html',
            brands=le_dict['brand'].classes_,
            processors=le_dict['processor'].classes_,
            cpus=le_dict['CPU'].classes_,
            gpus=le_dict['GPU'].classes_,
            os_list=le_dict['OS'].classes_,
            prediction_text=f"⚠ Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)
