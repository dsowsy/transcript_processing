import re
import argparse

# Define speaker colors with proper CSS class names
SPEAKER_COLORS = {
    'Kamala Harris': 'kamala-harris',
    'Donald Trump': 'donald-trump',
    'David Muir': 'david-muir',
    'Lindsey Davis': 'lindsey-davis',
    'Speaker 1': 'speaker-1',  # New speaker added with its own color
}

def deduplicate_speaker_names(text):
    # Regular expression pattern to match speaker names duplicated consecutively
    name_pattern = r'(\b\w+\s\w+\b)[ \n]*\1'
    deduplicated_text = re.sub(name_pattern, r'\1', text)
    return deduplicated_text

def remove_timestamps(text):
    # Regular expression pattern to match timestamps like (00:39) or (1:02:15)
    timestamp_pattern = r'\(\d{1,2}:\d{2}(?::\d{2})?\)'
    text_without_timestamps = re.sub(timestamp_pattern, '', text)
    return text_without_timestamps

def clean_colons_and_whitespace(text):
    # Remove any spaces around colons and ensure the text that may be on the next line follows the colon immediately.
    text = re.sub(r'\s*:\s*', ': ', text)
    text = re.sub(r':\s*\n\s*', ': ', text)
    return text

def generate_html(text, output_html_file):
    # Create the HTML structure with a white background and dark text
    html_content = """<html>
<head>
    <style>
        body {
            background-color: white;
            color: black;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        .kamala-harris {
            color: blue;
        }
        .donald-trump {
            color: red;
        }
        .david-muir {
            color: green;
        }
        .lindsey-davis {
            color: purple;
        }
        .speaker-1 {
            color: orange;
        }
        /* Add styles for other speakers here */
    </style>
</head>
<body>
"""

    # Add the colored speakers text with proper paragraph handling
    for speaker, color_class in SPEAKER_COLORS.items():
        # Use regex to find speaker name followed by a colon and apply the corresponding CSS class
        pattern = rf"({speaker}):"
        # Make the speaker name bold and ensure the following text stays the same color but not bold
        replacement = rf'<strong class="{color_class}">\1:</strong><span class="{color_class}">'
        text = re.sub(pattern, replacement, text)

    # Close the opened <span> for each speaker's line
    text = re.sub(r'(<strong.*?</strong>)', r'\1</span>', text)

    # Replace new lines with <br> for HTML readability
    text = text.replace("\n", "<br>\n")

    # Add the processed text into the body
    html_content += text
    html_content += "</body>\n</html>"

    # Write the HTML content to the output file
    with open(output_html_file, 'w') as file:
        file.write(html_content)

    print(f"HTML file has been generated and saved to '{output_html_file}'.")

def process_transcript(input_file, output_file, output_html_file):
    # Read the input file
    with open(input_file, 'r') as file:
        transcript = file.read()

    # Deduplicate speaker names
    deduplicated_text = deduplicate_speaker_names(transcript)
    
    # Remove timestamps
    cleaned_text = remove_timestamps(deduplicated_text)

    # Clean colons and fix whitespace issues
    final_text = clean_colons_and_whitespace(cleaned_text)

    # Write the cleaned text to the output file
    with open(output_file, 'w') as file:
        file.write(final_text)

    print(f"Processing complete. The cleaned transcript has been saved to '{output_file}'.")

    # Generate the HTML file with colored speakers
    generate_html(final_text, output_html_file)

if __name__ == "__main__":
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(description="Deduplicate speaker names, remove timestamps, clean up colons, and generate an HTML file with colored speakers.")
    parser.add_argument("input_file", help="The path to the input transcript file.")
    parser.add_argument("output_file", help="The path to save the processed transcript.")
    parser.add_argument("output_html_file", help="The path to save the generated HTML file.")

    args = parser.parse_args()

    # Process the transcript and generate HTML
    process_transcript(args.input_file, args.output_file, args.output_html_file)
