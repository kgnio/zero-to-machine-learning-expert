
# Stage 00 - Introduction to Machine Learning

def predict_house_price(size, price_per_sqm):
    predicted_price = size * price_per_sqm
    return predicted_price


house_size = 150
price_per_sqm = 25000

prediction = predict_house_price(
    house_size,
    price_per_sqm
)

print("=== House Price Calculator ===")
print(f"House size: {house_size} sqm")
print(f"Price per sqm: {price_per_sqm:,.0f}")
print(f"Predicted price: {prediction:,.0f}")
