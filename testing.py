from process_temporal_text import TemporalTextAnalysis


# textlist = ['11 weeks down the line', '101th day for me', '16 weeks for me', 'eleven weeks','asdfgjhuytreqwerju 16 days']
textlist = ['tsdfnkdjnkjzdnvkxjdnvkjx', '12 days', 'week 4']
t = TemporalTextAnalysis()

for i in textlist:
    output = t.text_cleaning(i)
    print(output)