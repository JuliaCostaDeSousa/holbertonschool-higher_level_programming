#!/usr/bin/env python3

# Main file content
from task_00_intro import generate_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)


# 1. Template vide
try:
    generate_invitations("", [{"name": "Test"}])
except Exception as e:
    print("Test 1 (template vide):", e)

# 2. Liste d'attendees vide
try:
    with open("template.txt", "r") as file:
        template_content = file.read()
    generate_invitations(template_content, [])
except Exception as e:
    print("Test 2 (liste vide):", e)

# 3. Mauvais type pour le template
try:
    generate_invitations(12345, [{"name": "Test"}])
except Exception as e:
    print("Test 3 (template non str):", e)

# 4. Mauvais type pour les attendees
try:
    with open("template.txt", "r") as file:
        template_content = file.read()
    generate_invitations(template_content, "not a list")
except Exception as e:
    print("Test 4 (attendees non list):", e)
