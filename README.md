# Processing a debate transcript from video removing timestamps, setting colors per speaker and text cleanup.

![colorized-preview](https://github.com/user-attachments/assets/0c54bbc4-ea23-40de-a891-35764a384353)

# Transcript processing
A quick exercise in processing a debate transcript with ChatGPT using Python to generate multi-speaker HTML colorized text. 

Transcript.txt - The input transcript that has video timecodes, duplication of speaker names. 
transcript_cleaned.txt - The intermediate text file that removes the timestamps, duplicate speaker names, and trims the whitespace/newlines around the colons ":" to make it more readable
transcript.html - The output HTML with the speaker names bolded, and unique color for each speaker. 

process_transcript.py - The generated script used to run.
process-debate-chatlog-light.pdf - The chatlog between myself and ChatGPT to generate the code. (light mode)
process-debate-chatlog-dark.pdf - The chatlog between myself and ChatGPT to generate the code. (dark mode)

# Usage instructions

`python process_transcript.py Transcript.py transcript_cleaned.txt transcript.html`

# Credits

Original source transcript provided by Rev.com
https://www.rev.com/blog/transcripts/harris-vs-trump-presidential-debate
