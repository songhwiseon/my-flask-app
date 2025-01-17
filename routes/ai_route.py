from flask import render_template,request,jsonify,Blueprint
import pymysql
from db import get_db_connection
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import joblib
import os 

ai_route = Blueprint('ai', __name__)

# 모델 로드

# lin_reg = joblib.load('house_price_model.pkl')
# rf_reg = joblib.load('house_price_model_rf.pkl')
# cat_dog_model = tf.keras.models.load_model('mobilenet_cats_and_dogs_classifier.h5')

covid_model = tf.keras.models.load_model('covid-19.keras')

def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))  # 모델에 맞는 입력 크기
    img_array = image.img_to_array(img)  # 이미지를 배열로 변환
    img_array = np.expand_dims(img_array, axis=0)  # 배치를 추가 (모델은 배치 형태를 요구)
    img_array = img_array / 255.0  # 스케일 조정 (0~1로)
    return img_array    


@ai_route.route("/covid-19", methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']
    name = request.form.get('name', '익명')
    age = request.form.get('age', 0)

    # 파일 저장
    file_path = os.path.join("uploads", image_file.filename)
    os.makedirs("uploads", exist_ok=True)
    image_file.save(file_path)

    try:
        # 이미지 예측
        preprocessed_img = load_and_preprocess_image(file_path)
        prediction = covid_model.predict(preprocessed_img)

        # 결과 처리
        if prediction[0][0] > 0.5:
            label = "Pneumonia"
            confidence = float(prediction[0][0])
        else:
            label = "Normal"
            confidence = float(1 - prediction[0][0])

        # 데이터베이스에 저장
        conn = get_db_connection()
        with conn.cursor() as cursor:
            query = """
                INSERT INTO `covid-19` 
                (name, age, label, confidence, created_date)
                VALUES 
                (%s, %s, %s, %s, sysdate())
            """
            cursor.execute(query, (name, age, label, confidence))
            conn.commit()

        # 임시 파일 삭제
        if os.path.exists(file_path):
            os.remove(file_path)

        return jsonify({
            "name": name,
            "age": age,
            "label": label,
            "confidence": confidence,
            "message": "저장 완료"
        })

    except Exception as e:
        # 오류 발생시 파일 삭제
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({"error": str(e)}), 500

    finally:
        if 'conn' in locals():
            conn.close()
    









# # 이미지 전처리 함수
# def load_and_preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(150, 150))  # 모델에 맞는 크기로 조정
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)  # 배치 추가
#     img_array = img_array / 255.0  # 스케일 조정
#     return img_array

# # 고양이 강아지 이미지 예측 
# @ai_route.route("/cat-dog", methods=['POST'])
# def predict():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image file provided"}), 400

#     # 이미지 파일 저장
#     image_file = request.files['image']
#     file_path = os.path.join("uploads", image_file.filename)
#     os.makedirs("uploads", exist_ok=True)
#     image_file.save(file_path)

#     # 이미지 전처리 및 예측
#     try:
#         preprocessed_img = load_and_preprocess_image(file_path)
#         prediction = cat_dog_model.predict(preprocessed_img)

#         # 결과 반환
#         if prediction[0] > 0.5:
#             result = {
#                 "label": "Dog",
#                 "confidence": float(prediction[0][0])
#             }
#         else:
#             result = {
#                 "label": "Cat",
#                 "confidence": float(1 - prediction[0][0])
#             }

#         # 처리 후 임시 파일 삭제
#         os.remove(file_path)

#         return jsonify(result)

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
 
    






# # 예측 데이터 저장
# @ai_route.route("/add-predict", methods=['POST'])
# def addpredict():
   
#         data = request.json

#         # 입력 데이터 변환
#         feature = np.array([[
#             int(data['area']),
#             int(data['rooms']),
#             int(data['year_built']),
#             int(data['income']),
#             int(data['school_rating']),
#             int(data['transit_score'])
#         ]])

#         # 예측 수행
#         price_lin = lin_reg.predict(feature)[0]
#         price_rf = rf_reg.predict(feature)[0]

        
#         # 데이터베이스 연결 및 저장
#         conn = get_db_connection()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
            
#         query = """
#             INSERT INTO house
#             (area, rooms, year_built, income, school_rating, transit_score, price_lin, price_rf, created_date)
#             VALUES
#             (%s, %s, %s, %s, %s, %s, %s, %s, sysdate())
#             """

        
#         # values = (
#         #     data['area'],
#         #     data['rooms'],
#         #     data['year_built'],
#         #     data['income'],
#         #     data['school_rating'],
#         #     data['transit_score'],
#         #     price_lin,
#         #     price_rf
#         # )
            
#         cursor.execute(query, 
#                        (data['area'], 
#                         data['rooms'], 
#                         data['year_built'], 
#                         data['income'], 
#                         data['school_rating'], 
#                         data['transit_score'], 
#                         price_lin, price_rf))
        
#         conn.commit()
#         cursor.close()
#         conn.close()

#         return jsonify({
#                 "message": "ok",
#                 "price_lin": f"${price_lin:,.2f}",
#                 "price_rf": f"${price_rf:,.2f}"
#         })
        

# # 예측 데이터 조회
# @ai_route.route("/predict")
# def getpredict():

#     house_idx = request.args.get('house_idx')
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("SELECT * FROM house WHERE house_idx = %s", (house_idx))
#         data = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify(data)    
#     except Exception as e:
#         return jsonify({"error": str(e)})
#     finally:
#         cursor.close()
#         conn.close()





