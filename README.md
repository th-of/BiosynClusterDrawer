# BiosynClusterDrawer
![](gif.gif)

This tool takes a list of open reading frames (ORFs) and draws the gene cluster using the python turtle package.

```python
# Explanation:

# [offset, ["label", start, stop, "color", "P"], ["label2", start, stop, "color", "P"]]
# Offset: length of sequence before the first ORF and after the last.
# Label: Name of gene/ORF, text to be added below.
# Start, stop: Real start and stop positions in the genome. 
# Color: "green", "red", "blue", "grey" etc.
# Promoters and terminators are identified by a string of "P" or "T" in the list of the reading frame with a 
# promoter ("P") upstream or a termintor ("T") downstream.
# P = promoter, T = terminator

# Sample input (gif above)
gak = [-50, ["gakA", 4231, 4335, "blue", "P"], ["gakB", 4422, 4526, "blue"], ["gakC", 4561, 4659, "blue", "T"],  ["gakI", 5333, 4881, "red", "T"], ["cro", 5517, 5290, "grey", "P"], ["gakT", 5600, 7339, "green", "P", "T"]]

```
