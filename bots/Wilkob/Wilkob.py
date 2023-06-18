from transformers import pipeline
import random
import re

class Bot:
    name = 'Wilkob'
    def __init__(self):
        self.text_generator = pipeline('text-generation', model='gpt2')
        self.joke_prefixe = "I know a great joke about "
        self.joke_topic = [
    "Animals",
    "Food",
    "Technology",
    "Sports",
    "School",
    "Puns",
    "Relationships",
    "Travel",
    "Knock-Knock",
    "Dad Jokes",
    "Doctor",
    "Music",
    "Movies",
    "Science",
    "Weather",
    "Politics",
    "History",
    "Math",
    "Space",
    "Books",
    "Money",
    "Work",
    "Holiday",
    "Law",
    "Art",
    "Fashion",
    "Cars",
    "Gardening",
    "Health",
    "Fitness",
    "Language",
    "Bar",
    "Psychology",
    "Random",
    "Video Games",
    "Social Media",
    "Internet",
    "Celebrities",
    "Marriage",
    "Wedding",
    "Gym",
    "Cooking",
    "Photography",
    "Fishing",
    "Shopping",
    "Dentist",
    "Police",
    "Firefighters",
    "Construction",
    "Farm",
    "Insects",
    "Fashion",
    "Knitting",
    "Running",
    "Camping",
    "Hiking",
    "Biking",
    "Swimming",
    "Singing",
    "Dancing",
    "Chess",
    "Soccer",
    "Basketball",
    "Baseball",
    "Tennis",
    "Golf",
    "Hockey",
    "Volleyball",
    "Cricket",
    "Rugby",
    "Boxing",
    "Wrestling",
    "Surfing",
    "Skating",
    "Skiing",
    "Snowboarding",
    "Painting",
    "Sculpture",
    "Drawing",
    "Poetry",
    "Theater",
    "Opera",
    "Architecture",
    "Comedy",
    "Musical",
    "Fashion",
    "Fantasy",
    "Thriller",
    "Horror",
    "Romance",
    "Documentary",
    "Action",
    "Adventure",
    "Science Fiction",
    "Mystery",
    "Biography",
    "Suspense",
    "Self-Help",
    "Cookbook",
    "Travel Guide",
    "History",
    "Art",
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology"
        ]

        
        

    def tell_joke(self):
        # Use the GPT-2 model to generate a joke
        # Choose a random prefix for the joke
        
        prefix = self.joke_prefixes + random.choice(self.joke_topic)
        joke = self.text_generator(f'{prefix}', max_length=25, do_sample=True)[0]['generated_text']
        return joke

    def rate_joke(self, joke):
        GPTMessage = "Please rate this joke " + joke
        ratingGPT = self.text_generator(f'{GPTMessage}', max_length=10, do_sample=True)[0]['generated_text']
        rating = self.extract_numbers(ratingGPT)[0]
        return rating
    
    def extract_numbers(string):
        numbers = re.findall(r'\d+', string)
        return [int(num) for num in numbers]
