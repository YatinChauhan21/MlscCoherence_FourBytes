def recognize_speech(language='en-US'):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        if language == 'en':
            text = recognizer.recognize_google(audio, language='en-US')
            print("English:", text)
        elif language == 'hi':
            text = recognizer.recognize_google(audio, language='hi-IN')
            print("Hindi:", text)
        else:
            print("Unsupported language. Please provide 'en' for English or 'hi' for Hindi.")
            return None
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None


# Example usage:
english_text = recognize_speech(language='en')
hindi_text = recognize_speech(language='hi')
