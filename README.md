# DaysGen

DaysGen (Number of Days Generator) is a rule-based sentiment temporal text analysis tool that is *specifically attuned to temporal data expressed in social media*.. 

# Key Features


# Usage and Sample Output

- Install dependencies:
    - All the libraries used in this toolkit can be installed using the following command. 

        ```
        pip install -r requirements.txt
        ```


```python
from process_temporal_textme  import TemporalTextAnalysis
t = TemporalTextAnalysis()

textlist = ['tsdfnkdjnkjzdnvkxjdnvkjx', '12 days', 'week 4']

for i in textlist:
    output = t.text_cleaning(i)
    print(output)
```

- Output

| Text |Output| Notes|
|------|---|---------|
|asdfghhjkl|9999||
|12 days |12||
|mid march|	300 | 30 days per month and calculated for current date|
|5 weks|	35 | |




