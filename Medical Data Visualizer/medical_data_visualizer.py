import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess_data():
    df = pd.read_csv('medical_examination.csv')

    df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = (df['BMI'] > 25).astype(int)

    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    return df

def draw_cat_plot():
    df = preprocess_data()
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='bar', height=5, aspect=1.2).fig
    plt.show()
    return fig

def draw_heat_map():
    df = preprocess_data()
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', center=0)
    plt.show()
