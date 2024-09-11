import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected string but got {type(template).__name__}.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries but got {type(attendees).__name__}.")
        return
    
    # Handle empty inputs
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")
        
        invitation = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )
        
        # Write to output file
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(invitation)
        print(f"Invitation for {name} written to {filename}")

# Example usage:
if __name__ == "__main__":
    # Read the template from a file
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: The template file 'template.txt' does not exist.")
        exit()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
