import pandas as pd
import plotly.graph_objects as go

def createBarChart(df):
    # Convert the columns 'start' and 'ende' into datetime objects
    df['start'] = pd.to_datetime(df['start'])
    df['ende'] = pd.to_datetime(df['ende'])

    # Adjust end time to match the next start time if the colors are the same
    for i in range(len(df) - 1):
        if df.loc[i, 'color'] == df.loc[i + 1, 'color']:
            df.loc[i, 'ende'] = df.loc[i + 1, 'start']

    # Create Diagram
    fig = go.Figure()

    for i, row in df.iterrows():
        fig.add_trace(go.Scatter(
            x=[row['start'], row['ende'], row['ende'], row['start']],
            y=[1, 1, 0, 0],
            fill='toself',
            fillcolor=row['color'],
            mode='none',
            showlegend=False,
        ))

    # Formatting the x-axis
    tickvals = pd.date_range(start=df['start'].min(), end=df['ende'].max(), freq='3H')
    ticktext = []
    previous_day = None

    for d in tickvals:
        if previous_day is None or d.day != previous_day:
            ticktext.append(f"<b>{d.strftime('%d.%m')}</b>")
        else:
            ticktext.append(d.strftime('%H:%M'))
        previous_day = d.day

    fig.update_layout(
        yaxis=dict(showticklabels=False),
        xaxis=dict(
            tickformat='%H:%M',
            tickvals=tickvals,
            ticktext=ticktext
        ),
        margin=dict(l=20, r=20, t=10, b=20),
        height=200,
    )

    return fig


# Example DataFrame
data = {
    'start': ['2024-08-27 08:00', '2024-08-27 09:00', '2024-08-27 10:00', '2024-08-27 11:00', '2024-08-27 12:00'],
    'ende':  ['2024-08-27 09:00', '2024-08-27 10:00', '2024-08-27 11:00', '2024-08-27 12:00', '2024-08-27 13:00'],
    'color': ['green', 'green','green', 'green', 'green']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create the bar chart
fig = createBarChart(df)

# Show the bar chart
fig.show()
