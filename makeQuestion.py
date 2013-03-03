
f = open("input.txt")
line = f.readline();

# get output filename
output_filename = line
output_file = open(output_filename.strip() + '.csv', 'w')

# NewQuestion,MC,
output_file.write('NewQuestion,MC,\n');

line = f.readline();
# Title,User Visible Registers,
output_file.write('Title,' + line.strip() + ',\n');

#QuestionText,"
output_file.write('QuestionText,"\n')

line = f.readline();
question_lines = line.split('\\n')
for line in question_lines:
  output_file.write(line.strip() + '\n')

#",
output_file.write('",\n');

#Option,100,Address register,,"Correct."
lines = f.readlines();
for i in range(len(lines)-1):
  ans = 'Incorrect answer.'
  num = lines[i][0];
  if lines[i][0] == '5':
    ans = 'Not the most correct answer.'
    num = '50'
    lines[i] = lines[i][3:len(lines[i])]
  elif lines[i][0] == '1':
    ans = 'Correct.'
    num = '100'
    lines[i] = lines[i][4:len(lines[i])]
  else:
    lines[i] = lines[i][2:len(lines[i])]
  if i+1 != len(lines)-1 and not lines[i+1][0].isdigit():
    output_file.write('Option,' + num + ',"' + lines[i].strip() + '",,"' + ans + ' ' + lines[i+1].strip() + '"\n')
  elif num.isdigit():
    output_file.write('Option,' + num + ',"' + lines[i].strip() + '",,"' + ans + '"\n')
  
#Feedback,"It is essential to understand register usages and its availability to users.",,,,
output_file.write('Feedback,"' + lines[len(lines)-1].strip() + '",,,,')
f.close()
output_file.close
