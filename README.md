# tree_annot #

<p align="center">
	<img src="/examples/tree_annot.png?raw=true" alt="tree_annot example"/>

</p>

Simple program for creating an image of a phylogenetic tree coloured by a user-provided annotations file.

User provides -

1. A phylogenetic tree

2. An alignment file

3. A csv file where the first column is a list of sequence names and the next columns can be any categorical
information

The user then selects which column they wish to colour on (default is the first column) and a filename to write the
image to.

## Installation ##

Currently this is just provided as a Python script. Easiest way to use it right now is -

1. Clone this repository to your desktop

```
git clone https://github.com/gabefoley/tree_annot.git
```

2. Install the required Python modules as specified in requirements.txt (we assume Python>=3.5)

```
pip install -r requirements.txt
```


## Usage ##

### Basic usage ###

```
usage: tree_annot.py [-h] -t TREE -a ALIGN -c CSV [-col COL] [-r RANDOM_SEED]
                     [-o OUTPATH]
```



You can call tree_annot from the command line.

The paths to the tree, alignment, and csv file must be provided.

```
python tree_annot.py -t ./examples/CYP2U_165.nwk -a ./examples/CYP2U_165.aln -c ./examples/CYP2U_165.csv
```

Example files showing expected format of all three are given in the `examples` folder

The alignment file can be an alignment with or without ancestral sequences

### Specify a column ###

To specify a particular column to colour based on, use the `col` flag. By default, the first column (after the
seq_name column) is used.

```
python tree_annot.py -t ./examples/CYP2U_165.nwk -a ./examples/CYP2U_165.aln -c ./examples/CYP2U_165.csv -col "tag2"
```

### Specifying the colour scheme ###
If you don't set a random seed, the colours will be automatically chosen for you (using a method designed to give
contrasting colours). When the program runs, it will tell you the random seed used to generate the colour scheme

```
To reproduce this colour scheme set the random seed as 90
```

Which you can then provide to tree_annot as an argument to use this colour scheme

```
python tree_annot.py -t ./examples/CYP2U_165.nwk -a ./examples/CYP2U_165.aln -c ./examples/CYP2U_165.csv -col "tag2" -r 90

