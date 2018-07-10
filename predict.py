import tensorflowjs as tfjs

model = tfjs.converters.load_keras_model("static/spaceinvaders/model/model.json")
print(model)