from sklearn.model_selection import train_test_split, cross_val_score, KFold
import time
import optuna

studies = {}

# scores a model with the five folds and returns the mean CV RMSE
def cv_rmse(model, X_train, y_train, kfold):
    """Mean CV RMSE over the five folds."""
    return -cross_val_score(model, X_train, y_train, cv=kfold,
                            scoring="neg_root_mean_squared_error").mean()

# runs an Optuna study and prints the best score and settings
def run_study(name, objective, n_trials):
    start = time.time()
    study = optuna.create_study(direction="minimize", sampler=optuna.samplers.TPESampler(seed=42, n_startup_trials=3))
    study.optimize(objective, n_trials=n_trials)
    studies[name] = study
    print(f"{name}: best CV RMSE {study.best_value:.1f} after {n_trials} tries "
          f"({(time.time() - start) / 60:.1f} min)")
    print("best parameters:", {k: round(v, 3) if isinstance(v, float) else v
                               for k, v in study.best_params.items()})
    return study