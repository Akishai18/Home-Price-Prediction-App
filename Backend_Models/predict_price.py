import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/predict_price', methods=['POST'])
def prediction():
    data = request.json
    location = data.get('location')
    date = data.get('date')
    home = data.get('hometype')
    print(f"Location: {location}, Date: {date}, Home Type: {home}")

    # Load the models
    forest_comp = joblib.load('forest_comp_model.pkl')
    forest_SFDetach = joblib.load('forest_SFDetach_model.pkl')
    forest_SFAttach = joblib.load('forest_SFAttach_model.pkl')
    forest_THouse = joblib.load('forest_THouse_model.pkl')
    forest_Apart = joblib.load('forest_Apart_model.pkl')

    # Load the OrdinalEncoder used for encoding 'Date' column
    date_encoder = joblib.load('date_encoder.pkl')

    # Load the column names for each type
    x_train_comp_columns = joblib.load('x_train_comp_columns.pkl')
    x_train_SFDetach_columns = joblib.load('x_train_SFDetach_columns.pkl')
    x_train_SFAttach_columns = joblib.load('x_train_SFAttach_columns.pkl')
    x_train_THouse_columns = joblib.load('x_train_THouse_columns.pkl')
    x_train_Apart_columns = joblib.load('x_train_Apart_columns.pkl')


    if home == "Comp":
        new_data = pd.DataFrame({
            'CompIndex': [100],
            'CompBenchmark': [850000],
            'CompYoYChange': [100],
            'Date': [date],
            'Location': [location]
        })

        # Encode 'Date' column
        new_data['Date'] = date_encoder.transform(new_data[['Date']])

        # One-hot encode the Location column
        new_data = new_data.join(pd.get_dummies(new_data['Location'], dtype=int)).drop(['Location'], axis=1)

        # Reindex columns to match the training data
        new_data = new_data.reindex(columns=x_train_comp_columns, fill_value=0)

        predictions = forest_comp.predict(new_data)
        predictions = int(predictions[0] + 700000)
        print(predictions)

    elif home == "SFDetach":
        new_data = pd.DataFrame({
            'Date': [date],
            'Location': [location],
            'SFDetachIndex': [280],
            'SFDetachBenchmark': [1400000],
            'SFDetachYoYChange': [10],
        })

        # Encode 'Date' column
        new_data['Date'] = date_encoder.transform(new_data[['Date']])

        # One-hot encode the Location column
        new_data = new_data.join(pd.get_dummies(new_data['Location'], dtype=int)).drop(['Location'], axis=1)

        # Reindex columns to match the training data
        new_data = new_data.reindex(columns=x_train_SFDetach_columns, fill_value=0)

        predictions = forest_SFDetach.predict(new_data)
        predictions = int(predictions[0] * 100000 + 400000)
        print(predictions)

    elif home == "SFAttach":
        new_data = pd.DataFrame({
            'Date': [date],
            'Location': [location],
            'SFAttachIndex': [480],
            'SFAttachBenchmark': [1100000],
            'SFAttachYoYChange': [20],
        })

        # Encode 'Date' column
        new_data['Date'] = date_encoder.transform(new_data[['Date']])

        # One-hot encode the Location column
        new_data = new_data.join(pd.get_dummies(new_data['Location'], dtype=int)).drop(['Location'], axis=1)

        # Reindex columns to match the training data
        new_data = new_data.reindex(columns=x_train_SFAttach_columns, fill_value=0)

        predictions = forest_SFAttach.predict(new_data)
        predictions = int(predictions[0])
        print(predictions)
    elif home == "THouse":
        new_data = pd.DataFrame({
            'Date': [date],
            'Location': [location],
            'THouseIndex': [350],
            'THouseBenchmark': [800000],
            'THouseYoYChange': [50],
        })

        # Encode 'Date' column
        new_data['Date'] = date_encoder.transform(new_data[['Date']])

        # One-hot encode the Location column
        new_data = new_data.join(pd.get_dummies(new_data['Location'], dtype=int)).drop(['Location'], axis=1)

        # Reindex columns to match the training data
        new_data = new_data.reindex(columns=x_train_THouse_columns, fill_value=0)

        predictions = forest_THouse.predict(new_data)
        predictions = int(predictions[0])
        print(predictions)
    elif home == "Apart":
        new_data = pd.DataFrame({
            'Date': [date],
            'Location': [location],
            'ApartIndex': [500],
            'ApartBenchmark': [600000],
            'ApartYoYChange': [0.13],
        })

        # Encode 'Date' column
        new_data['Date'] = date_encoder.transform(new_data[['Date']])

        # One-hot encode the Location column
        new_data = new_data.join(pd.get_dummies(new_data['Location'], dtype=int)).drop(['Location'], axis=1)

        # Reindex columns to match the training data
        new_data = new_data.reindex(columns=x_train_Apart_columns, fill_value=0)

        predictions = forest_Apart.predict(new_data)
        predictions = int(predictions[0])
        print(predictions)
    else:
        return jsonify({'error': 'Invalid home type specified'}), 400

    # Return the prediction as JSON
    return jsonify({'predictions': predictions})


if __name__ == '__main__':
    app.run(debug=True)
