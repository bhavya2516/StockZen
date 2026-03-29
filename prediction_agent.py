import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from tensorflow.keras.layers import LSTM, Dense

def predict_price(data):
    prices = data['Close'].values.reshape(-1,1)
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(prices)

    X = [scaled[i-60:i] for i in range(60, len(scaled))]
    X = np.array(X)

    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(X.shape[1],1)),
        LSTM(50),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, scaled[60:], epochs=2, verbose=0)

    last = scaled[-60:].reshape(1,60,1)
    pred = scaler.inverse_transform(model.predict(last, verbose=0))

    return float(pred[0][0])