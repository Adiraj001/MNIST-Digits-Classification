# 🧠 MNIST Digits Classification

A Deep Learning project for handwritten digit recognition using the **MNIST dataset**.  
This project trains a neural network using TensorFlow/Keras and allows prediction on custom digit images using OpenCV.

---

## 📌 Project Overview

This project builds and trains a neural network model to classify handwritten digits (0–9) from the MNIST dataset.  
It also includes a custom prediction script that allows testing the trained model on external digit images.

The goal of this project is to understand:
- Image preprocessing
- Neural network training
- Model evaluation
- Real-world prediction using custom input images

---

## 🛠️ Technologies Used

- Python 🐍  
- TensorFlow / Keras 🤖  
- OpenCV 👁️  
- NumPy  
- Matplotlib  

---

## 📂 Project Structure
MNIST-Digits-Classification/
│
├── ModelTraining.ipynb # Jupyter Notebook for training the model
├── app.py # Script for predicting custom digit images
├── mnistmodel.keras # Saved trained model
├── requirements.txt # Project dependencies
└── digits/ # Folder containing sample digit images



---

## 📊 Dataset

The project uses the **MNIST Handwritten Digits Dataset**, which contains:
- 60,000 training images
- 10,000 testing images
- Grayscale images (28x28 pixels)
- 10 output classes (digits 0–9)

---

## 🧠 Model Architecture

The model is built using Keras Sequential API and includes:
- Input layer (Flatten)
- Dense hidden layers with ReLU activation
- Output layer with Softmax activation

Loss Function: `SparseCategoricalCrossentropy`  
Optimizer: `Adam`  
Evaluation Metric: `Accuracy`

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Adiraj001/MNIST-Digits-Classification.git
cd MNIST-Digits-Classification
```

### 2️⃣ Create Environment
```bash
conda create --name mnist-ml python=3.10
conda activate mnist-ml

pip install -r requirements.txt
```

### 3️⃣ Train the Model
```bash
ModelTraining.ipynb
```

### 4️⃣ Run Prediction on Custom Images
```bash
python app.py
```

### 🎯 Future Improvements

- Improve model accuracy using CNN
- Build a GUI for digit drawing
- Deploy as a web application
- Add real-time webcam digit recognition
