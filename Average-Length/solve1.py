with open("communications.docx") as file:
    for line in file: # Loop through each line 
        # Remove leading and trailing whitespace
        line = line.strip()
        # Find the length of each line
        line_length = len(line)
        # Add total of length
        line_length_sum += line_length
        # Find total number of lines
        line_count += 1
        # Find the average length of each line
        line_length_avg = line_length_sum / line_count

# Display the results
print("Total number of lines:", line_count)
print("Total length of lines: {line_length_sum}")
print("Average length of lines: {line_length_avg}")

