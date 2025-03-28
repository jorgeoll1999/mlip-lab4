import pandas as pd

# Crear los ejemplos sintéticos como un DataFrame
synthetic_tweets = [
    "Great, another inspirational speech by Trump. My IQ just dropped 10 points.",
    "So glad we have leaders like Putin to show us the way. 🙃",
    "Kim Jong-un for Nobel Peace Prize 2025, please!",
    "Nothing says democracy like censorship. Go China!",
    "Biden’s speeches are the perfect cure for insomnia.",
    "Elon Musk should totally run for president. What could possibly go wrong?",
    "Fidel Castro really knew how to throw a party – ask anyone in prison.",
    "So proud of our government. Always looking out for... themselves.",
    "Another successful year of economic growth — if you’re a billionaire.",
    "Can’t wait for the next inspiring quote from a corrupt senator."
]

df_synthetic = pd.DataFrame({
    "text": synthetic_tweets,
    "label": ["negative"] * 10,  # Suponiendo que todos tienen un tono sarcástico/negativo
    "output": ["positive"] * 10  # Suponiendo que el modelo predice mal
})

# Guardar como archivo CSV para cargar en Zeno
csv_path = "synthetic_political_tweets.csv"
df_synthetic.to_csv(csv_path, index=False)

csv_path
