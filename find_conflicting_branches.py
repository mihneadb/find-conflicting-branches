import sys
import subprocess

import fire
from git import Repo, Git


def get_merged_branches(repo, branch):
    branches_txt = repo.git.branch('-a', '--merged', branch)
    return [clean_branch_name(b) for b in branches_txt.split('\n')]


def clean_branch_name(b):
    return b.strip('*').strip()


def has_conflict(g, source_branch, to_merge_branch):
    g.execute(['git', 'checkout', source_branch])

    status, out, _ = g.execute(['git', 'merge', '--no-commit', '--no-ff', to_merge_branch],
                                with_extended_output=True, with_exceptions=False)

    if status != 0 and 'CONFLICT' in out:
        ret = True
    else:
        ret = False

    g.execute(['git', 'merge', '--abort'])

    return ret


def find_conflicting_branches(repo_path, target_branch, my_branch):
    repo = Repo(repo_path)
    g = Git(repo_path)

    # Find the branches that are merged into our branches of interest.
    branches_into_target = get_merged_branches(repo, target_branch)
    branches_into_mine = get_merged_branches(repo, my_branch)

    # Potential conflicting branches are the ones that are in the target branch but not in ours.
    potential_branches = set(branches_into_target).difference(branches_into_mine).difference([target_branch])

    # Find the conflicting ones.
    conflicting_branches = [b for b in potential_branches if has_conflict(g, b, my_branch)]
    return conflicting_branches


if __name__ == '__main__':
    fire.Fire(find_conflicting_branches)
