from setuptools import setup, find_packages

# Opening files
with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

with open('requirements.txt', 'r') as requirements_file:
    REQUIREMENTS = requirements_file.readlines()

# Package details
setup_args = dict(
    name = 'sentimentaltools',
    version = '0.1.0',
    description = 'A  tool to analyze an emotional state of a person useing computer vision',
    long_description_content_type = "text/markdown",
    long_description = README + '\n\n' + HISTORY,
    license = 'MIT',
    packages = find_packages(),
    author = 'Casper Ung, Aleksander mosekjær',
    author_email = 'wonger1324@gmail.com, REMEMBER TO ADD',
    keywords=['Sentimental', 'SentimentalAnalysis', 'NaturalLanguageProcessing'],
    url='https://github.com/Echono/FinalProject',
    download_url='REMEMBER TO ADD'
)

# Installing required libraries
install_requires = []
for line in REQUIREMENTS:
    install_requires.append(line.strip())

# Main detection
if __name__ == '__main__':
    setup(**setup_args, install_requires = install_requires)