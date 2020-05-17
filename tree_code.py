from ete3 import PhyloTree, TreeStyle, TextFace, add_face_to_node, SeqMotifFace, NodeStyle, faces, ImgFace, CircleFace, \
    AttrFace
import pandas as pd
import random


def load_tree(tree_path, aln_path=None):
    """
    Load a tree, associate an alignment with it if given
    """
    tree = PhyloTree(tree_path, alignment=aln_path, format=1, alg_format='fasta')
    return tree


def layout(node):
    if node.is_leaf():
        N = AttrFace("name", fsize=30)
        faces.add_face_to_node(N, node, 0, position="aligned")


def get_example_tree(tree, color_dict=None, annot_dict=None, annot_index=None):
    for n in tree.traverse():
        if n.is_leaf():
            n.img_style["bgcolor"] = color_dict[annot_dict[n.name][annot_index]]

            ts = TreeStyle()
            ts.layout_fn = layout
            ts.show_leaf_name = False
            ts.mode = "c"
            ts.arc_start = -180  # 0 degrees = 3 o'clock
            ts.arc_span = 180
            ts.root_opening_factor = 1
    return tree, ts


def get_random_color(pastel_factor=0.5):
    return [(x + pastel_factor) / (1.0 + pastel_factor) for x in [random.uniform(0, 1.0) for i in [1, 2, 3]]]


def color_distance(c1, c2):
    return sum([abs(x[0] - x[1]) for x in zip(c1, c2)])


def generate_new_color(existing_colors, pastel_factor=0.5):
    max_distance = None
    best_color = None
    for i in range(0, 100):
        color = get_random_color(pastel_factor=pastel_factor)
        if not existing_colors:
            return color
        best_distance = min([color_distance(color, c) for c in existing_colors])
        if not max_distance or best_distance > max_distance:
            max_distance = best_distance
            best_color = color
    return best_color


def get_color_dict(annot_dict, annot_index, random_val):
    random.seed(random_val)

    color_dict = {}

    unique_vals = list(set(val[annot_index] for val in annot_dict.values()))

    colors = []
    for uv in unique_vals:
        color = generate_new_color(colors, pastel_factor=0.9)
        colors.append(color)
        color_dict[uv] = '#%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
    return color_dict
