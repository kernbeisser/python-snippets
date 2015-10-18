#!/usr/bin/env python

import os
import sys
import hashlib


# read file content in 2k chunks
_BLOCKSIZE = 2048


def compute_sha1(file):
    digester = hashlib.sha1()
    return _compute_digest(file, digester)


def _compute_digest(file, digest_algorithm):
    while 1:
        chunk = file.read(_BLOCKSIZE)
        if not chunk:
            break
        digest_algorithm.update(chunk)
        file.close()
        return digest_algorithm.hexdigest()


def get_sizes(topdir):
    same_size = {}
    for root, dirs, files in os.walk(topdir):
        if '.git' in dirs:
            dirs.remove('.git')
        for f in files:
            full = os.path.join(root, f)
            if os.path.islink(full):
                continue
            size = os.path.getsize(full)
            if size == 0:
                continue
            same_size[full] = size
    return same_size


# TODO output elsewhere
def compare_dict_items(a_dict):
    import itertools

    for x, y in itertools.combinations(a_dict.items(), 2):
        hashes = {}
        if x[1] == y[1]:
            hashes[x[0]] = compute_sha1(open(x[0]))
            hashes[y[0]] = compute_sha1(open(y[0]))
            print "%-64s: %5d" % (x[0], x[1]), hashes[x[0]]
            print "%-64s: %5d" % (y[0], y[1]), hashes[y[0]]
            print "--------"


def main():
    if len(sys.argv) < 2:
        print "i need smore ..."
        sys.exit(1)
    else:
        topdir = sys.argv[1]

	found = get_sizes(topdir)
    compare_dict_items(found)


if __name__ == '__main__':
	main()
