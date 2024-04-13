def justify(text, width):
    words = text.split() # List
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        # If adding the word would exceed the width, justify the current line
        if current_length + len(current_line) + len(word) > width:
            lines.append(justify_line(current_line, width))
            current_line = [] # Reset list of the line we are working with
            current_length = 0 #Reset the length of the sum of words.
        
        current_line.append(word) #add word to the current line list
        current_length += len(word) #add to the sum of the current length 
    
    # Justify and add the last line
    lines.append(' '.join(current_line))
    
    return '\n'.join(lines)

def justify_line(words, width):
    # If there's only one word, no need to justify
    if len(words) == 1:
        return words[0]
    
    num_spaces_needed = width - sum(len(word) for word in words) # Num of chacarters from the word minus the max width
    num_gaps = len(words) - 1 # Space between words
    base_spaces = num_spaces_needed // num_gaps
    extra_spaces = num_spaces_needed % num_gaps
    
    justified_line = '' #Declare an empty string
    for i, word in enumerate(words):
        justified_line += word
        if i < num_gaps:
            justified_line += ' ' * (base_spaces + (1 if i < extra_spaces else 0))
    
    return justified_line

# Example usage:
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci."
width = 40
justified_text = justify(text, width)
print(justified_text)