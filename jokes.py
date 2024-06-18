import pyjokes

# Get 5 neutral jokes
jokes = pyjokes.get_jokes(language='en', category='neutral')

# Print the jokes
for i, joke in enumerate(jokes[:5]):
    print(f"{i+1}. {joke}")
