# CodePlagerismDetector
for boomers who dont know to detect on their own
The provided Python code demonstrates a plagiarism check using the difflib module. The purpose of this code is to compare the similarity between two text files and calculate a similarity ratio.

The code begins by importing the difflib module, which provides classes and functions for performing string comparisons. The check_plagiarism function is defined, which takes two file paths as input: file1 and file2.

Inside the function, the with statement is used to open the two files in read mode. The contents of file1 and file2 are then read and stored in the variables text1 and text2, respectively.

Next, the similarity ratio is calculated using the SequenceMatcher class from the difflib module. The SequenceMatcher compares the two texts and determines the ratio of similarity between them. The ratio represents the degree of similarity, with 1.0 indicating identical texts.

Finally, the function returns the similarity ratio, and an example usage is provided. In the example usage, file1 and file2 are set to 'original_code.py' and 'suspected_plagiarism.py', respectively. These placeholders should be replaced with the actual file paths of the code files you want to compare.

To obtain the similarity ratio, the check_plagiarism function is called with the appropriate file paths, and the result is stored in the similarity variable. The code then prints the similarity ratio using f-string formatting.

By running this code with the desired file paths, you can determine the degree of similarity between the two code files. This can be useful in detecting potential plagiarism or identifying similarities between different versions of a program.

Please ensure that the necessary files exist and are accessible at the specified paths for the code to execute successfully.
