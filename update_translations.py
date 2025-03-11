import json
import glob
import os

# Define the old and new slogans
old_slogans = [
    'Explore the cosmos',
    'Unlock mysteries',
    'Chart new frontiers',
    'Dive into knowledge',
    'Discover wonders',
    'Ignite curiosity',
    'Forge new paths',
    'Unravel secrets',
    'Pioneer insights',
    'Embark on adventures'
]

new_slogans = [
    'Challenge AI perspectives',
    'Shape the future of AI',
    'Join the AI conversation',
    'Debate with intelligence',
    'Explore AI frontiers',
    'Question. Discuss. Evolve.',
    'Your voice in AI matters',
    'Think beyond AI limits',
    'Where AI meets human insight',
    'Be part of AI evolution'
]

# Find all translation files
translation_files = glob.glob('src/lib/i18n/locales/*/translation.json')

for file_path in translation_files:
    try:
        # Read the current translation file
        with open(file_path, 'r', encoding='utf-8') as f:
            translations = json.load(f)
        
        # Remove old slogans
        for slogan in old_slogans:
            if slogan in translations:
                del translations[slogan]
        
        # Add new slogans
        for slogan in new_slogans:
            translations[slogan] = ""  # Empty string for all languages except English
        
        # Sort the translations alphabetically
        sorted_translations = dict(sorted(translations.items()))
        
        # Write back the updated translations
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(sorted_translations, f, ensure_ascii=False, indent=2)
        
        print(f"Updated {file_path}")
    
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

print("\nDone updating translation files!") 