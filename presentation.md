# Model Results

## Ensamble Models' Scores

### 1. Random Forest

**Best CV RMSE: 164.5**

- ⚙️ **Settings:** 8 trials · 0.3 min
- Params: `max_features=0.894`, `min_samples_leaf=3`, `max_depth=15`

### 2. XGBoost

**Best CV RMSE: 135.1**

- ⚙️ **Settings:** 30 trials · 3.8 min
- Params: `n_estimators=956`, `learning_rate=0.027`, `max_depth=10`, `subsample=0.678`, `colsample_bytree=0.936`, `min_child_weight=9`

### 3. CatBoost

**Best CV RMSE: 128.4**

- ⚙️ **Settings:** 5 trials · 0.7 min
- Params: `depth=10`, `learning_rate=0.089`, `l2_leaf_reg=3.423`

### 4. Voting and stacking Models

- **4.1. Voting CV RMSE:** 135.3
- **4.2. Stacking CV RMSE:** 127.3
- *Stacking weights:* `rf=-0.12`, `xgb=0.36`, `cat=0.77`

## Cross-Validation Scores

| Model | CV RMSE |
|---|---:|
| Stacking | 127.8 |
| CatBoost | 128.4 |
| Voting | 135.1 |
| XGBoost | 136.7 |
| Random Forest | 164.5 |

# ⭐ Final Test Evaluation

| Model | Train RMSE | CV RMSE | Test RMSE | Test MAE | Test R² |
|---|---:|---:|---:|---:|---:|
| Stacking | 42.0 | 127.8 | 121.7 | 72.9 | 0.963 |
| CatBoost | 49.0 | 128.4 | 122.9 | 73.9 | 0.962 |
| Voting | 57.6 | 135.1 | 127.8 | 75.7 | 0.959 |
| XGBoost | 38.2 | 136.7 | 127.1 | 76.1 | 0.959 |
| Random Forest | 102.7 | 164.5 | 154.3 | 94.7 | 0.940 |