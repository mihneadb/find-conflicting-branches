# find-conflicting-branches
An easy way to find those annoying conflicting branches

Say you want to merge your `awesome-feature` branch into `staging`, but git complains
about some conflicts. Your colleagues have ten branches in `staging` themselves. What
are you going to do?

```bash
$ python find_conflicting_branches.py /path/to/repo staging awesome-feature
# perf-improvements
```

There, with one simple command you found out that your branch conflicts with the
`perf-improvements` branch!
