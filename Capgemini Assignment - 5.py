#writing into a new file
initial_lines = ["Line 1", "Line 2", "Line 3"]
with open('sample.txt', 'w') as f:
    for line in initial_lines:
        f.write(line)
        f.write('\n')

#appending into file
append_lines = ["Appended line 1", "Appended line 2"]
with open('sample.txt', 'a') as f:
    for line in append_lines:
        f.write(line)
        f.write('\n')

#reading from file
with open('sample.txt') as f:
    content = f.readlines()
print(f'Content from sample.txt\n {content}')

