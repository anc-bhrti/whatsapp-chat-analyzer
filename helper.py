def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    # Count words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # Count media files
    media_pattern = (
        r'<Media omitted>|'
        r'\.jpg \(file attached\)|'
        r'\.png \(file attached\)|'
        r'\.webp \(file attached\)|'
        r'\.pdf \(file attached\)|'
        r'\.xlsx \(file attached\)|'
        r'\.vcf \(file attached\)|'
        r'\.mp4 \(file attached\)|'
        r'\.mp3 \(file attached\)|'
        r'\.docx \(file attached\)|'
        r'\.txt \(file attached\)'
    )
    num_media_messages = df['message'].str.contains(media_pattern, case=False).sum()

    return num_messages, len(words), num_media_messages
