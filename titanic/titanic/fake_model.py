def fake_predict(user_age):
    if prediction == 0:
        prediction = "Not survived"
    elif prediction == 1:
        prediction = "Survived"
    else:
        prediction = "Error"
    return prediction
