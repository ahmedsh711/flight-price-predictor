from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from catboost import CatBoostRegressor

def get_preprocessing():
    scaling_cols = ['Duration_Minutes', 'Route_Frequency', 'Route_Competition', 'Airline_Route_Dominance']
    passthrough_cols = ['Total_Stops', 'Flight_Hour', 'Arrival_Hour', 'Is_Night_Flight', 'Arrives_Next_Day', 
                        'Is_Weekend', 'Is_Direct', 'Day_sin', 'Day_cos', 'Month_sin', 'Month_cos']
    ohe_cols = ['Airline', 'Source', 'Destination', 'Departure_Period', 'Duration_Category']
    
    num_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', RobustScaler())
    ])
    
    cat_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ohe', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'))
    ])
    
    preprocessing = ColumnTransformer(
        transformers=[
            ('num', num_pipeline, scaling_cols),
            ('cat', cat_pipeline, ohe_cols),
            ('pass', 'passthrough', passthrough_cols)
        ],
        remainder='drop'
    )
    
    return preprocessing

def build_pipeline():
    preprocessing = get_preprocessing()
    
    model = CatBoostRegressor(
        bagging_temperature=0.348666,
        depth=6,
        iterations=1500,
        l2_leaf_reg=5,
        learning_rate=0.085242,
        min_data_in_leaf=40,
        random_strength=0.386735,
        verbose=0,
        random_state=42
    )
    
    pipeline = Pipeline(steps=[
        ('preprocessing', preprocessing),
        ('model', model)
    ])
    
    return pipeline