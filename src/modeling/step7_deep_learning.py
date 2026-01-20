import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dense, Concatenate, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

DATA_PATH = Path("data/processed/step4_features.csv")

def main():
    df = pd.read_csv(DATA_PATH)

    # Encode chromosome as integer
    le = LabelEncoder()
    df["chrom_enc"] = le.fit_transform(df["Chromosome"])

    # Numeric features
    num_features = ["ref_len", "alt_len", "len_diff", "position_norm"]
    X_num = df[num_features].values

    scaler = StandardScaler()
    X_num = scaler.fit_transform(X_num)

    X_chr = df["chrom_enc"].values
    y = df["label"].values

    X_chr_train, X_chr_test, X_num_train, X_num_test, y_train, y_test = train_test_split(
        X_chr, X_num, y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    # Inputs
    chr_input = Input(shape=(1,), name="chromosome")
    num_input = Input(shape=(X_num.shape[1],), name="numeric")

    # Embedding for chromosome
    embed = Embedding(
        input_dim=df["chrom_enc"].nunique(),
        output_dim=8
    )(chr_input)

    embed = Flatten()(embed)

    # Combine
    x = Concatenate()([embed, num_input])
    x = Dense(64, activation="relu")(x)
    x = Dropout(0.3)(x)
    x = Dense(32, activation="relu")(x)

    output = Dense(1, activation="sigmoid")(x)

    model = Model(inputs=[chr_input, num_input], outputs=output)

    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    model.summary()

    es = EarlyStopping(
        monitor="val_loss",
        patience=3,
        restore_best_weights=True
    )

    model.fit(
        [X_chr_train, X_num_train],
        y_train,
        validation_split=0.1,
        epochs=20,
        batch_size=4096,
        callbacks=[es],
        verbose=2
    )

    y_prob = model.predict([X_chr_test, X_num_test]).ravel()
    y_pred = (y_prob >= 0.5).astype(int)

    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)

    print("\nDeep Learning Results")
    print(f"Accuracy : {acc:.4f}")
    print(f"ROC-AUC  : {auc:.4f}")

if __name__ == "__main__":
    main()
