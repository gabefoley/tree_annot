import pandas as pd
import argparse
import tree_code as tc
import sys
import random

def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--tree", help="Path to tree", required=True)
    parser.add_argument("-a", "--align", help="Path to alignment", required=True)
    parser.add_argument("-c", "--csv", help="Path to csv", required=True)
    parser.add_argument("-col", "--col", help="Column to annotate based on")
    parser.add_argument("-r", "--random_seed", help="Set the random seed to an integer to make colour selection "
                                                    "reproducible")

    parser.add_argument("-o", "--outpath", help="Outpath", default="tree_annot.png")

    return parser.parse_args(args)


if __name__ == "__main__":

    print ("\nRunning tree_annot")

    # Parse the arguments
    parser = parse_args(sys.argv[1:])

    df = pd.read_csv(parser.csv, index_col=0)

    annot_dict = df.to_dict(orient='index')

    col = parser.col.strip() if parser.col else df.columns[0]

    random_seed = parser.random_seed if parser.random_seed else random.randint(0, 999)

    print ("\nTo reproduce this colour scheme set the random seed as " + str(random_seed))
    color_dict = tc.get_color_dict(annot_dict, col, random_seed)

    # Load tree
    tree = tc.load_tree(parser.tree, parser.align)

    tree, ts = tc.get_example_tree(tree = tree, color_dict = color_dict, annot_dict=annot_dict, annot_index=col)

    # Write to out path

    print ("\nTree image has been written to " + parser.outpath)
    tree.render(parser.outpath, tree_style=ts, dpi=300)
