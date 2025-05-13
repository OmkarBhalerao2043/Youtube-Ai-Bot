import openai

def analyze_titles_with_gpt(titles, model="gpt-3.5-turbo"):
    prompt = (
        "Choose the most relevant video title for the user's query:\n\n" +
        "\n".join([f"{i+1}. {title}" for i, title in enumerate(titles)]) +
        "\n\nRespond with the number and title you think is best."
    )

    try:
        # Make the OpenAI API call
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an assistant that selects the most relevant YouTube video."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        # Return the AI's selection
        chosen_video = response.choices[0].message["content"].strip()
        return f"{chosen_video}"

    except Exception as e:
        # General fallback for any other exceptions
        return ""
