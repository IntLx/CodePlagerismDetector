import difflib

def check_plagiarism(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()
    
    similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
    
    return similarity_ratio

# Example usage
file1 = 'original_code.py'
file2 = 'suspected_plagiarism.py'
similarity = check_plagiarism(file1, file2)
print(f"Similarity ratio: {similarity}")
