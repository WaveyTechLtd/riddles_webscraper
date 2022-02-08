# riddles_webscraper
Upwork project pitch, client wanted to scrap a number of riddles from a popular wesbite.

Information required in the final output file was riddle number, question and answer.
Using a combination of Beautiful Soup and pandas, to scrap the info and collate into a dataframe, before finally publishing as a example_riddles.tsv file.

Changes required to use this file
- Input your own working directory filepath before use, via the n_pages variable, e.g. n_pages=list(range(1,5)).
- Input the catagory of riddles you wish to scrap, via the base_url variable, e.g. base_url = "https://www.riddles.com/best-riddles"
- Review the number of pages of riddles with wish to scrap. At the moment, the code runs through the first 5 pages of "best-riddles".

Example output file is also included in "example_riddles.tsv"
