import re
import pandas as pd


def preprocess(data):
    # Match date formats like "12/07/25, 8:02 pm -"
    pattern = r'\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\u202f[ap]m -'

    # Split messages using the pattern
    messages = re.split(pattern, data)[1:]
    original_dates = re.findall(pattern, data)

    # Replace narrow no-break space with normal space in dates
    dates = [d.replace('\u202f', ' ') for d in original_dates]

    # Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Convert message_date to datetime
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p -')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Separate users and messages
    users = []
    msgs = []

    for message in df['user_message']:
        entry = re.split(r'([^:]+):\s', message, maxsplit=1)
        if len(entry) > 2:
            users.append(entry[1])
            msgs.append(entry[2])
        else:
            users.append('group_notification')
            msgs.append(entry[0])

    df['user'] = users
    df['message'] = msgs

    # Drop the combined column
    df.drop(columns=['user_message'], inplace=True)

    # Extract date-time features
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df
