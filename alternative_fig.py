import matplotlib.pyplot as plt
import pandas as pd


def create_seamless_barchart(df):
    df['start'] = pd.to_datetime(df['start'])
    df['ende'] = pd.to_datetime(df['ende'])

    fig, ax = plt.subplots(figsize=(10, 2))

    for i, row in df.iterrows():
        ax.barh(y=0, width=(row['ende'] - row['start']).total_seconds(), left=row['start'].to_pydatetime(),
                color=row['color'], edgecolor='none')

    ax.xaxis_date()
    ax.yaxis.set_visible(False)
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M'))
    plt.tight_layout()

    plt.show()


# Example Data
data = {
    'start': ['2024-08-27 00:00:00', '2024-08-27 06:00:00', '2024-08-27 12:00:00', '2024-08-27 18:00:00'],
    'ende': ['2024-08-27 06:00:00', '2024-08-27 12:00:00', '2024-08-27 18:00:00', '2024-08-28 00:00:00'],
    'color': ['#FF5733', '#FF5733', '#33FF57', '#33FF57']
}

df = pd.DataFrame(data)
create_seamless_barchart(df)
