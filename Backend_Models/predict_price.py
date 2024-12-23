import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load data from CSV file
data = pd.read_csv('data.csv')

@app.route('/predict_price', methods=['POST'])
def prediction():
    data_json = request.json
    location = data_json.get('location')
    date = data_json.get('date')
    home = data_json.get('hometype')
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

    # Extract values dynamically from CSV file
    row = data[(data['Location'] == location) & (data['HomeType'] == home)]

    if not row.empty:
        index_value = row[f'{home}Index'].values[0]
        benchmark_value = row[f'{home}Benchmark'].values[0]
        yoy_change_value = row[f'{home}YoYChange'].values[0]
    else:
        # Fallback default values if no match is found
        index_value = 100 if home == 'Comp'
        index_value = 280 if home == 'SFDetach'
        index_value = 480 if home == 'SFAttach'
        index_value = 350 if home == 'THouse'
        index_value = 500 if home == 'Apart'
        benchmark_value = 850000 if home == 'Comp'
        benchmark_value = 1400000 if home == 'SFDetach' 
        benchmark_value = 1100000 if home == 'SFAttach' 
        benchmark_value = 800000 if home == 'THouse' 
        benchmark_value = 600000 if home == 'Apart' 
        yoy_change_value = 100 if home == 'Comp' 
        yoy_change_value = 10 if home == 'SFDetach' 
        yoy_change_value = 20 if home == 'SFAttach' 
        yoy_change_value = 50 if home == 'THouse' 
        yoy_change_value = 0.13 if home == 'Apart' 

    new_data = pd.DataFrame({
        'Date': [date],
        'Location': [location],
        f'{home}Index': [index_value],
        f'{home}Benchmark': [benchmark_value],
        f'{home}YoYChange': [yoy_change_value],
    })

    # Encode 'Date' column
    new_data['Date'] = date_encoder.transform(new_data[['Date']])

    # encode the Location column
    new_data = new_data.join(pd.get_dummies(new_data['Location'], dtype=int)).drop(['Location'], axis=1)

    # Reindex columns to match the training data
    if home == 'Comp':
        new_data = new_data.reindex(columns=x_train_comp_columns, fill_value=0)
        predictions = forest_comp.predict(new_data)
    elif home == 'SFDetach':
        new_data = new_data.reindex(columns=x_train_SFDetach_columns, fill_value=0)
        predictions = forest_SFDetach.predict(new_data)
    elif home == 'SFAttach':
        new_data = new_data.reindex(columns=x_train_SFAttach_columns, fill_value=0)
        predictions = forest_SFAttach.predict(new_data)
    elif home == 'THouse':
        new_data = new_data.reindex(columns=x_train_THouse_columns, fill_value=0)
        predictions = forest_THouse.predict(new_data)
    elif home == 'Apart':
        new_data = new_data.reindex(columns=x_train_Apart_columns, fill_value=0)
        predictions = forest_Apart.predict(new_data)
    else:
        return jsonify({'error': 'Invalid home type specified'}), 400

    predictions = int(predictions[0])
    print(predictions)

    # Return the prediction as JSON
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(debug=True)
