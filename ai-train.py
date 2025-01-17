import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# 데이터 생성 (예시 데이터)
np.random.seed(42)
data = pd.DataFrame({
    'area': np.random.randint(50, 200, 500),
    'rooms': np.random.randint(1, 6, 500),
    'year_built': np.random.randint(1990, 2024, 500),
    'income': np.random.randint(3000, 12000, 500),
    'school_rating': np.random.randint(1, 10, 500),
    'transit_score': np.random.randint(1, 10, 500),
    'price': np.random.randint(20000, 100000, 500)
})

# 독립 변수와 종속 변수 설정
X = data[['area', 'rooms', 'year_built', 'income', 'school_rating', 'transit_score']]
y = data['price']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 1: 선형 회귀
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# 선형 회귀 예측
y_pred_lin = lin_reg.predict(X_test)

# 선형 회귀 평가
mse_lin = mean_squared_error(y_test, y_pred_lin)
r2_lin = r2_score(y_test, y_pred_lin)
print("Linear Regression - Mean Squared Error:", mse_lin)
print("Linear Regression - R2 Score:", r2_lin)

# 모델 2: 랜덤 포레스트 회귀
rf_reg = RandomForestRegressor(random_state=42, n_estimators=100)
rf_reg.fit(X_train, y_train)

# 랜덤 포레스트 예측
y_pred_rf = rf_reg.predict(X_test)

# 랜덤 포레스트 평가
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
print("Random Forest Regression - Mean Squared Error:", mse_rf)
print("Random Forest Regression - R2 Score:", r2_rf)

# 예측 예시 (테스트 데이터 중 일부를 사용)
sample_data = X_test.iloc[:5]
predictions_lin = lin_reg.predict(sample_data)
predictions_rf = rf_reg.predict(sample_data)

print("Sample Data Predictions (Linear Regression):", predictions_lin)
print("Sample Data Predictions (Random Forest Regression):", predictions_rf)

#모델 저장
joblib.dump(lin_reg, 'house_price_model.pkl')
joblib.dump(rf_reg, 'house_price_model_rf.pkl')

