import pandas as pd
from django.contrib.auth.models import User
from .models import Citations

def run(*args, **kwargs):
    # Read CSV file into a DataFrame
    csv_file_path = 'C:/Users/hiba6/quotes/citat/citat/spiders/citations_data.csv'
    df = pd.read_csv(csv_file_path, delimiter=';')

    # Iterate through the DataFrame and create model instances
    for index, row in df.iterrows():
        # Create or update a Citations object with the values from the CSV file
        citation, created = Citations.objects.get_or_create(
            texte=row['texte'],
            auteur=row['auteur'],
            thèmes=row['thèmes'],
            defaults={
                'texte': row['texte'],
                'auteur': row['auteur'],
                'thèmes': row['thèmes'],
            }
        )

        if created:
            # If the object was created, print a message to the console
            print(f'Created a new Citations object for "{citation.auteur}" with text: "{citation.texte}" and themes: {citation.thèmes}')
        else:
            # If the object was updated, print a message to the console
            print(f'Updated an existing Citations object for "{citation.auteur}" with text: "{citation.texte}" and themes: {citation.thèmes}')