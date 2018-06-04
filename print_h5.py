#!/usr/bin/env python
"""Print the contents of an HDF5 file"""

import h5py


def print_node(node, indent: int = 4) -> None:
    """Print a indented representation of node

    Args:
        node: The node to print
        indent: How many spaces per indent level

    Returns:
        None

    Examples:
        >>> print_node("a/b/c", indent=4)
                c
        >>> print_node("a")
        a
        >>> print_node("a/b", indent=3)
        b
    """
    *first, last = str(node).split("/")
    print(" " * indent * len(first) + last)


def print_h5(h5filename, indent=4):
    """For a given HDF5 file, print its contents"""
    with h5py.File(h5filename) as h5file:
        h5file.visit(lambda node: print_node(node, indent=indent))


print_h5("/Users/dijkema/Desktop/test.h5")
