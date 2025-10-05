# Laptop Price Predictor with 3D Visualization

This project is a web application that predicts laptop prices based on user input features and displays a 3D interactive laptop model. Built with Python (Flask), HTML/CSS, JavaScript, and Three.js.

## Features
- Predicts laptop prices using a trained regression model
- User-friendly form for inputting laptop specifications
- Interactive 3D laptop model (GLB format) rendered with Three.js
- Modern, responsive UI

## Project Structure
```
├── app.py                  # Flask application entry point
├── main.py                 # (Optional) Additional Python logic
├── data.csv                # Dataset used for training
├── laptop_price_model.pkl  # Trained regression model (pickle)
├── label_encoders.pkl      # Encoders for categorical features
├── laptop.glb              # 3D model of a laptop (GLB format)
├── img.jpeg                # Reference UI image
├── static/
│   ├── style.css           # Main stylesheet
│   ├── 3d-animations.js    # JS for 3D model rendering
│   ├── laptop.glb          # (Copy of 3D model for web access)
│   └── img.jpeg            # (Copy of reference image for web access)
├── templates/
│   └── index.html          # Main HTML template
```

## How to Run
1. **Install dependencies:**
   - Python 3.x
   - Flask
   - (Other dependencies as required by your model)

2. **Start the Flask server:**
   ```bash
   python app.py
   ```

3. **Open your browser:**
   - Go to `http://localhost:5000`

4. **Usage:**
   - Fill in the laptop specs in the form and click "Predict Price".
   - View the interactive 3D laptop model beside the form.

## 3D Model
- The 3D laptop is rendered using [Three.js](https://threejs.org/) and loaded from `laptop.glb`.
- The model rotates slowly and can be further enhanced for interactivity.

## Customization
- To change the 3D model, replace `laptop.glb` in the project root and static folder.
- To update the UI, edit `templates/index.html` and `static/style.css`.
- To improve predictions, retrain the model and update `laptop_price_model.pkl` and `label_encoders.pkl`.

## Credits
- 3D model: Your own or sourced from a free 3D asset site
- UI/UX: Inspired by the reference image (`img.jpeg`)

## License
This project is for educational/demo purposes. Please check licenses for any third-party assets you use.
