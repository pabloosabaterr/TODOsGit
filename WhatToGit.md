# TODO / NEEDSWORK / FIXME / XXX markers in git

409 lines in total, at HEAD `93eec172` (v2.55.0-504-g93eec17209). Collected on 2026-08-08.

Dates come from `git blame -w` and refer to the last time the line was touched, which is not necessarily when the marker was added.

Links point at the tip of `master` on GitHub, so line numbers may drift as that branch moves ahead of the commit scanned here.

This file is generated. Run `deno task report` to rebuild it; do not edit it by hand.

## Count by marker

| Marker | Count |
| --- | --- |
| TODO | 207 |
| NEEDSWORK | 122 |
| FIXME | 40 |
| XXX | 41 |

## Count by top-level directory

| Directory | Count |
| --- | --- |
| (root) | 156 |
| builtin | 55 |
| compat | 8 |
| contrib | 11 |
| Documentation | 16 |
| git-gui | 7 |
| gitk-git | 4 |
| gitweb | 3 |
| odb | 1 |
| perl | 9 |
| po | 22 |
| refs | 5 |
| t | 104 |
| templates | 4 |
| tools | 3 |
| trace2 | 1 |

## Count by year of last modification

| Year | Count |
| --- | --- |
| 2005 | 4 |
| 2006 | 16 |
| 2007 | 7 |
| 2008 | 11 |
| 2009 | 6 |
| 2010 | 20 |
| 2011 | 5 |
| 2012 | 37 |
| 2013 | 24 |
| 2014 | 10 |
| 2015 | 10 |
| 2016 | 12 |
| 2017 | 10 |
| 2018 | 20 |
| 2019 | 20 |
| 2020 | 14 |
| 2021 | 45 |
| 2022 | 49 |
| 2023 | 17 |
| 2024 | 20 |
| 2025 | 19 |
| 2026 | 33 |

## Full listing

<details>
<summary><b>(root)</b> &mdash; 156 markers</summary>

`.clang-format` (1)

- 2025-07-02 `9e45fc6c` [L21](https://github.com/git/git/blob/master/.clang-format#L21) `# NEEDSWORK: It would be nice if we can find optimal settings to ensur`

`Makefile` (2)

- 2022-05-26 `b9832f7e` [L3201](https://github.com/git/git/blob/master/Makefile#L3201) `### TODO FIXME: Translating everything in these files is a bad`
- 2025-04-23 `04a13ed8` [L3476](https://github.com/git/git/blob/master/Makefile#L3476) `# TODO: deprecate 'hdr-check' in lieu of 'check-headers' in Git 2.51+`

`apply.c` (3)

- 2016-04-22 `13b5af22` [L864](https://github.com/git/git/blob/master/apply.c#L864) `* FIXME! The end-of-filename heuristics are kind of screwy. For existi`
- 2016-04-22 `13b5af22` [L3406](https://github.com/git/git/blob/master/apply.c#L3406) `/* XXX read_sha1_file NUL-terminates */`
- 2016-04-22 `13b5af22` [L3609](https://github.com/git/git/blob/master/apply.c#L3609) `* NEEDSWORK: shouldn't this be flagged`

`branch.c` (1)

- 2022-01-28 `961b130d` [L803](https://github.com/git/git/blob/master/branch.c#L803) `* NEEDSWORK If tracking was set up in the superproject but not the`

`bundle-uri.c` (1)

- 2025-05-14 `35cb1bb0` [L327](https://github.com/git/git/blob/master/bundle-uri.c#L327) `* TODO: Restricting newlines in the target paths may break valid`

`bundle.c` (1)

- 2023-01-31 `d9fd674c` [L260](https://github.com/git/git/blob/master/bundle.c#L260) `/* TODO: preserve this verbose language. */`

`color.c` (1)

- 2017-08-21 `6cdf8a79` [L421](https://github.com/git/git/blob/master/color.c#L421) `* NEEDSWORK: This function is sometimes used from multiple threads, an`

`combine-diff.c` (1)

- 2014-02-24 `7195fbfa` [L1536](https://github.com/git/git/blob/master/combine-diff.c#L1536) `* TODO some of the filters could be ported to work on`

`connect.c` (1)

- 2018-03-15 `1aa8dded` [L1454](https://github.com/git/git/blob/master/connect.c#L1454) `* NEEDSWORK: If we are trying to use protocol v2 and we are planning`

`diff-lib.c` (1)

- 2024-04-03 `86829f3f` [L139](https://github.com/git/git/blob/master/diff-lib.c#L139) `* NEEDSWORK:`

`diff.c` (8)

- 2017-06-29 `e6e045f8` [L869](https://github.com/git/git/blob/master/diff.c#L869) `* NEEDSWORK: Instead of storing a copy of the line, add an offset poin`
- 2017-08-15 `f0b8fb6e` [L1188](https://github.com/git/git/blob/master/diff.c#L1188) `* NEEDSWORK: This uses the same heuristic as blame_entry_score() in bl`
- 2017-06-29 `e6e045f8` [L2295](https://github.com/git/git/blob/master/diff.c#L2295) `* NEEDSWORK:`
- 2012-04-30 `dc801e71` [L2995](https://github.com/git/git/blob/master/diff.c#L2995) `/* "Bin XXX -> YYY bytes" */`
- 2012-04-30 `dc801e71` [L3031](https://github.com/git/git/blob/master/diff.c#L3031) `* Binary files are displayed with "Bin XXX -> YYY bytes"`
- 2012-04-30 `dc801e71` [L3060](https://github.com/git/git/blob/master/diff.c#L3060) `* strlen("Bin XXX -> YYY bytes") == bin_width, and the part`
- 2012-04-30 `dc801e71` [L3061](https://github.com/git/git/blob/master/diff.c#L3061) `* starting from "XXX" should fit in graph_width.`
- 2019-04-05 `7fbbcb21` [L7470](https://github.com/git/git/blob/master/diff.c#L7470) `* NEEDSWORK: Consider deduplicating the OIDs sent.`

`diffcore-rename.c` (1)

- 2021-06-22 `1aedd03a` [L849](https://github.com/git/git/blob/master/diffcore-rename.c#L849) `* TODO: The following loops mirror the code/logic from`

`dir.c` (3)

- 2015-03-24 `777c55a6` [L652](https://github.com/git/git/blob/master/dir.c#L652) `* FIXME: parse_pathspec should have eliminated`
- 2015-03-08 `5ebf79ad` [L1778](https://github.com/git/git/blob/master/dir.c#L1778) `* NEEDSWORK: when untracked cache is enabled, prep_exclude()`
- 2021-04-01 `d425f651` [L4080](https://github.com/git/git/blob/master/dir.c#L4080) `/* TODO: audit for interaction with sparse-index. */`

`entry.c` (1)

- 2021-04-01 `3450a304` [L454](https://github.com/git/git/blob/master/entry.c#L454) `/* TODO: audit for interaction with sparse-index. */`

`environment.h` (2)

- 2026-07-14 `1a6c84e9` [L92](https://github.com/git/git/blob/master/environment.h#L92) `* NEEDSWORK: It would be better if these definitions could be moved to`
- 2024-09-12 `673af418` [L212](https://github.com/git/git/blob/master/environment.h#L212) `* TODO: All the below state either explicitly or implicitly relies on`

`fsmonitor.c` (2)

- 2024-02-26 `29c139ce` [L246](https://github.com/git/git/blob/master/fsmonitor.c#L246) `* NEEDSWORK: We used the name-hash to find the correct`
- 2024-02-26 `29c139ce` [L285](https://github.com/git/git/blob/master/fsmonitor.c#L285) `* NEEDSWORK: Our caller already tried an exact match`

`git-archimport.perl` (4)

- 2005-09-11 `241b5967` [L23](https://github.com/git/git/blob/master/git-archimport.perl#L23) `=head1 TODO`
- 2005-11-23 `42f44b08` [L229](https://github.com/git/git/blob/master/git-archimport.perl#L229) `# FIXME see if we can find a more optimal way to do this by graphing`
- 2005-08-30 `d3968363` [L237](https://github.com/git/git/blob/master/git-archimport.perl#L237) `## TODO cleanup irrelevant patches`
- 2005-11-23 `6df896b5` [L474](https://github.com/git/git/blob/master/git-archimport.perl#L474) `# TODO: handle removed_directories and renamed_directories:`

`git-cvsexportcommit.perl` (1)

- 2006-01-06 `576cfc86` [L299](https://github.com/git/git/blob/master/git-cvsexportcommit.perl#L299) `# TODO:we need to handle removed in cvs`

`git-cvsimport.perl` (1)

- 2006-01-15 `8cd16211` [L85](https://github.com/git/git/blob/master/git-cvsimport.perl#L85) `# NEEDSWORK: Maybe warn on unrecognized lines?`

`git-cvsserver.perl` (27)

- 2006-02-22 `3fda8c4c` [L424](https://github.com/git/git/blob/master/git-cvsserver.perl#L424) `# TODO : re-enable this, currently it's not particularly useful`
- 2006-02-22 `3fda8c4c` [L663](https://github.com/git/git/blob/master/git-cvsserver.perl#L663) `# TODO : check we're not squashing an already existing file`
- 2008-05-14 `8a06a632` [L694](https://github.com/git/git/blob/master/git-cvsserver.perl#L694) `#TODO: Also have option to send warning to user?`
- 2006-02-22 `3fda8c4c` [L767](https://github.com/git/git/blob/master/git-cvsserver.perl#L767) `# TODO : not sure if the format of this message is quite correct.`
- 2012-10-13 `61717661` [L1118](https://github.com/git/git/blob/master/git-cvsserver.perl#L1118) `# || ( defined($state->{opt}{D}) && $state->{opt}{D} ne "" ) # TODO`
- 2012-10-13 `61717661` [L1122](https://github.com/git/git/blob/master/git-cvsserver.perl#L1122) `# TODO: Convert -D value into the form 2011.04.10.04.46.57,`
- 2012-10-13 `d8574ff2` [L1312](https://github.com/git/git/blob/master/git-cvsserver.perl#L1312) `# TODO: If it has been modified in the sandbox, error out`
- 2006-02-22 `3fda8c4c` [L1469](https://github.com/git/git/blob/master/git-cvsserver.perl#L1469) `# TODO : we should copy files in blocks`
- 2012-10-13 `61717661` [L1497](https://github.com/git/git/blob/master/git-cvsserver.perl#L1497) `# TODO?: OR sticky dir is different...`
- 2012-10-13 `61717661` [L1511](https://github.com/git/git/blob/master/git-cvsserver.perl#L1511) `# TODO?: Consider sending a final duplicate Sticky response`
- 2012-10-13 `61717661` [L1610](https://github.com/git/git/blob/master/git-cvsserver.perl#L1610) `#TODO: We could split the cvs commit into multiple`
- 2006-02-22 `3fda8c4c` [L1847](https://github.com/git/git/blob/master/git-cvsserver.perl#L1847) `# TODO : All possible statuses aren't yet implemented`
- 2012-10-13 `61717661` [L2152](https://github.com/git/git/blob/master/git-cvsserver.perl#L2152) `# TODO: Use --label instead of -L because -L is no longer`
- 2012-10-13 `61717661` [L2159](https://github.com/git/git/blob/master/git-cvsserver.perl#L2159) `# TODO: Real CVS seems to include a date in the label, before`
- 2006-02-22 `3fda8c4c` [L2329](https://github.com/git/git/blob/master/git-cvsserver.perl#L2329) `# TODO: if we got a revision from the client, use that instead`
- 2012-10-13 `eb5dcb2c` [L2760](https://github.com/git/git/blob/master/git-cvsserver.perl#L2760) `# || ( defined($stickyDate) && $stickyDate ne "" )   # TODO`
- 2012-10-13 `eb5dcb2c` [L2764](https://github.com/git/git/blob/master/git-cvsserver.perl#L2764) `# TODO: Convert -D value into the form 2011.04.10.04.46.57,`
- 2012-10-13 `eb5dcb2c` [L2808](https://github.com/git/git/blob/master/git-cvsserver.perl#L2808) `# TODO: When/if we actually pick versions by {date} properly,`
- 2006-02-22 `3fda8c4c` [L3861](https://github.com/git/git/blob/master/git-cvsserver.perl#L3861) `# TODO: log processing is memory bound`
- 2012-10-13 `ab07681f` [L4513](https://github.com/git/git/blob/master/git-cvsserver.perl#L4513) `# TODO: date, state, or by specific logins filters?`
- 2012-10-13 `ab07681f` [L4514](https://github.com/git/git/blob/master/git-cvsserver.perl#L4514) `# TODO: Handle comma-separated list of revFilter items, each item`
- 2012-10-13 `ab07681f` [L4517](https://github.com/git/git/blob/master/git-cvsserver.perl#L4517) `# TODO: Adjust $db_query WHERE clause based on revFilter, instead of`
- 2012-10-13 `bfdafa09` [L4561](https://github.com/git/git/blob/master/git-cvsserver.perl#L4561) `actual revision (one of the below).  TODO: Also allow it to`
- 2012-10-13 `bfdafa09` [L4635](https://github.com/git/git/blob/master/git-cvsserver.perl#L4635) `#   - FUTURE: TODO: Rework database somehow to make up and remember`
- 2012-10-13 `658b57ad` [L4738](https://github.com/git/git/blob/master/git-cvsserver.perl#L4738) `# TODO: Possible optimization strategies:`
- 2012-10-13 `658b57ad` [L4765](https://github.com/git/git/blob/master/git-cvsserver.perl#L4765) `# TODO: Include file hash in dirmap cache.`
- 2012-10-13 `51a7e6db` [L5015](https://github.com/git/git/blob/master/git-cvsserver.perl#L5015) `# TODO: Perhaps use git check-ref-format, with an in-process cache of`

`git-filter-branch.sh` (2)

- 2007-07-23 `dfd05e38` [L542](https://github.com/git/git/blob/master/git-filter-branch.sh#L542) `# TODO: This should possibly go, with the semantics that all positive `
- 2007-06-03 `6f6826c5` [L550](https://github.com/git/git/blob/master/git-filter-branch.sh#L550) `# XXX: Rewrite tagged trees as well?`

`git-p4.py` (4)

- 2007-05-23 `6a49f8e2` [L4071](https://github.com/git/git/blob/master/git-p4.py#L4071) `# TODO: should always look at previous commits,`
- 2022-04-01 `c785e202` [L4204](https://github.com/git/git/blob/master/git-p4.py#L4204) `# FIXME - what's a P4 projectName ?`
- 2022-04-01 `c785e202` [L4217](https://github.com/git/git/blob/master/git-p4.py#L4217) `# FIXME`
- 2022-04-01 `c785e202` [L4324](https://github.com/git/git/blob/master/git-p4.py#L4324) `# TODO: use common prefix of args?`

`git-svn.perl` (3)

- 2014-12-07 `83c9433e` [L1417](https://github.com/git/git/blob/master/git-svn.perl#L1417) `# TODO: handle combining properties better`
- 2014-12-07 `83c9433e` [L1437](https://github.com/git/git/blob/master/git-svn.perl#L1437) `# TODO: don't simply append here if $file already has svn-properties`
- 2007-01-13 `44320b9e` [L1870](https://github.com/git/git/blob/master/git-svn.perl#L1870) `# TODO: set *:merge properties or like...`

`git.c` (1)

- 2016-01-26 `441981bc` [L860](https://github.com/git/git/blob/master/git.c#L860) `* NEEDSWORK: if we can figure out cases`

`graph.c` (1)

- 2008-05-04 `c12172d2` [L47](https://github.com/git/git/blob/master/graph.c#L47) `* TODO:`

`grep.c` (2)

- 2020-01-15 `1d1729ca` [L1535](https://github.com/git/git/blob/master/grep.c#L1535) `* TODO: allowing text conversion to run in parallel with object`
- 2006-09-17 `83b5d2f5` [L1786](https://github.com/git/git/blob/master/grep.c#L1786) `/* NEEDSWORK:`

`grep.h` (1)

- 2021-08-16 `0693806b` [L128](https://github.com/git/git/blob/master/grep.h#L128) `* NEEDSWORK: See if we can remove this field, because the repository`

`hash.h` (1)

- 2026-02-07 `67e526c3` [L231](https://github.com/git/git/blob/master/hash.h#L231) `uint32_t algo;	/* XXX requires 4-byte alignment */`

`help.c` (1)

- 2020-04-16 `617d5719` [L797](https://github.com/git/git/blob/master/help.c#L797) `/* NEEDSWORK: also save and output GIT-BUILD_OPTIONS? */`

`http-push.c` (1)

- 2009-01-17 `20642801` [L1124](https://github.com/git/git/blob/master/http-push.c#L1124) `* NEEDSWORK: remote_ls() ignores info/refs on the remote side.  But it`

`imap-send.c` (1)

- 2013-01-15 `1efee7ff` [L770](https://github.com/git/git/blob/master/imap-send.c#L770) `* NEEDSWORK: Previously this case handled '<num> EXISTS'`

`khash.h` (1)

- 2013-12-21 `fff42755` [L184](https://github.com/git/git/blob/master/khash.h#L184) `} /* TODO: to implement automatically shrinking; resize() already supp`

`line-log.c` (4)

- 2013-03-28 `12da1d1f` [L933](https://github.com/git/git/blob/master/line-log.c#L933) `/* NEEDSWORK should apply some heuristics to prevent mismatches */`
- 2013-04-12 `1ddac3ff` [L977](https://github.com/git/git/blob/master/line-log.c#L977) `* NEEDSWORK not enough when we get around to`
- 2013-04-12 `1ddac3ff` [L982](https://github.com/git/git/blob/master/line-log.c#L982) `* NEEDSWORK tramples over data structures not owned here`
- 2013-03-28 `12da1d1f` [L1134](https://github.com/git/git/blob/master/line-log.c#L1134) `/* NEEDSWORK evil merge detection stuff */`

`list-objects-filter-options.c` (1)

- 2019-09-18 `627b8268` [L395](https://github.com/git/git/blob/master/list-objects-filter-options.c#L395) `/* NEEDSWORK: 'expand' result leaking??? */`

`list-objects.c` (1)

- 2017-11-15 `ce5b6f9b` [L416](https://github.com/git/git/blob/master/list-objects.c#L416) `* NEEDSWORK: Adding the tree and then flushing it here`

`match-trees.c` (1)

- 2008-06-30 `85e51b78` [L273](https://github.com/git/git/blob/master/match-trees.c#L273) `* NEEDSWORK: this limits the recursion depth to hardcoded`

`merge-ort.c` (6)

- 2021-01-01 `4204cd59` [L1797](https://github.com/git/git/blob/master/merge-ort.c#L1797) `/* FIXME: can't handle linked worktrees in submodules yet */`
- 2021-01-01 `62fdec17` [L2220](https://github.com/git/git/blob/master/merge-ort.c#L2220) `* FIXME: If opt->priv->call_depth && !clean, then we really`
- 2020-12-15 `53e88a03` [L3058](https://github.com/git/git/blob/master/merge-ort.c#L3058) `* TODO: For renames we normally remove the path at the`
- 2020-12-13 `6681ce5c` [L4632](https://github.com/git/git/blob/master/merge-ort.c#L4632) `unpack_opts.quiet = 0; /* FIXME: sequencer might want quiet? */`
- 2021-09-27 `04988c8d` [L4635](https://github.com/git/git/blob/master/merge-ort.c#L4635) `unpack_opts.preserve_ignored = 0; /* FIXME: !opts->overwrite_ignore */`
- 2022-08-04 `4057523a` [L4782](https://github.com/git/git/blob/master/merge-ort.c#L4782) `* NEEDSWORK: The steps to resolve these errors deserve a more`

`meson.build` (1)

- 2025-04-23 `04a13ed8` [L2278](https://github.com/git/git/blob/master/meson.build#L2278) `# TODO: deprecate 'hdr-check' in lieu of 'check-headers' in Git 2.51+`

`midx.c` (1)

- 2024-04-01 `748b88a0` [L1007](https://github.com/git/git/blob/master/midx.c#L1007) `display_progress(progress, 0); /* TODO: Measure QSORT() progress */`

`notes-merge.c` (1)

- 2010-11-09 `75ef3f4a` [L631](https://github.com/git/git/blob/master/notes-merge.c#L631) `/* TODO: How to handle multiple merge-bases? */`

`object-file.c` (1)

- 2026-07-10 `48d730a1` [L1326](https://github.com/git/git/blob/master/object-file.c#L1326) `* NEEDSWORK: This transaction flag is only used by the "files"`

`object.h` (1)

- 2018-05-15 `14ba97f8` [L14](https://github.com/git/git/blob/master/object.h#L14) `/* TODO: migrate alloc_states to mem-pool? */`

`odb.h` (1)

- 2025-07-01 `e989dd96` [L444](https://github.com/git/git/blob/master/odb.h#L444) `* TODO: odb_read_object_info_extended()'s call stack has a recursive b`

`oidmap.h` (2)

- 2019-10-06 `87571c3f` [L101](https://github.com/git/git/blob/master/oidmap.h#L101) `/* TODO: this API could be reworked to do compile-time type checks */`
- 2019-10-06 `87571c3f` [L109](https://github.com/git/git/blob/master/oidmap.h#L109) `/* TODO: this API could be reworked to do compile-time type checks */`

`pack-bitmap.c` (1)

- 2022-08-14 `28cd7306` [L1046](https://github.com/git/git/blob/master/pack-bitmap.c#L1046) `/* NEEDSWORK: cache misses aren't recorded */`

`path.c` (1)

- 2015-10-01 `b2a7123b` [L1108](https://github.com/git/git/blob/master/path.c#L1108) `* NEEDSWORK: This function doesn't perform normalization w.r.t. traili`

`pathspec.c` (1)

- 2013-07-14 `bd30c2e4` [L537](https://github.com/git/git/blob/master/pathspec.c#L537) `* FIXME: should we enable ONESTAR in _GLOB for`

`pkt-line.c` (1)

- 2011-02-24 `bbc30f99` [L73](https://github.com/git/git/blob/master/pkt-line.c#L73) `/* XXX we should really handle printable utf8 */`

`promisor-remote.h` (1)

- 2019-06-25 `fa3d1b63` [L11](https://github.com/git/git/blob/master/promisor-remote.h#L11) `* Information in its fields come from remote.XXX config entries or`

`read-cache.c` (4)

- 2022-09-28 `4a6ed30f` [L1844](https://github.com/git/git/blob/master/read-cache.c#L1844) `* NEEDSWORK: using 'offsetof()' is cumbersome and should be replaced`
- 2018-10-10 `77ff1127` [L2260](https://github.com/git/git/blob/master/read-cache.c#L2260) `/* TODO: does creating more threads than cores help? */`
- 2021-04-01 `0c18c059` [L2532](https://github.com/git/git/blob/master/read-cache.c#L2532) `/* TODO: audit for interaction with sparse-index. */`
- 2023-05-16 `1a40e7be` [L3816](https://github.com/git/git/blob/master/read-cache.c#L3816) `/* TODO: audit for interaction with sparse-index. */`

`ref-filter.c` (2)

- 2024-09-19 `20652956` [L2441](https://github.com/git/git/blob/master/ref-filter.c#L2441) `* NEEDSWORK: The following code might be unnecessary if all codepaths`
- 2015-07-07 `68411046` [L2835](https://github.com/git/git/blob/master/ref-filter.c#L2835) `* NEEDSWORK:`

`refs.c` (2)

- 2022-08-05 `b877e617` [L599](https://github.com/git/git/blob/master/refs.c#L599) `* NEEDSWORK: Special case other symrefs such as REBASE_HEAD,`
- 2026-02-25 `01dc8459` [L2345](https://github.com/git/git/blob/master/refs.c#L2345) `* TODO Send in a 'struct worktree' instead of a 'gitdir', and`

`remote-curl.c` (1)

- 2018-03-15 `a4d78ce2` [L495](https://github.com/git/git/blob/master/remote-curl.c#L495) `* NEEDSWORK: If we are trying to use protocol v2 and we are planning`

`remote.h` (2)

- 2022-05-16 `1d04e719` [L465](https://github.com/git/git/blob/master/remote.h#L465) `* NEEDSWORK: This works incorrectly on the domain and protocol part.`
- 2022-05-16 `1d04e719` [L475](https://github.com/git/git/blob/master/remote.h#L475) `* NEEDSWORK: Given how chop_last_dir() works, this function is broken`

`repack-promisor.c` (2)

- 2025-10-15 `29e93551` [L60](https://github.com/git/git/blob/master/repack-promisor.c#L60) `* NEEDSWORK: fetch-pack sometimes generates non-empty`
- 2026-01-05 `dd8c4e12` [L93](https://github.com/git/git/blob/master/repack-promisor.c#L93) `* NEEDSWORK: Giving pack-objects only the OIDs without any ordering`

`replay.c` (1)

- 2026-01-13 `6aeda3cf` [L94](https://github.com/git/git/blob/master/replay.c#L94) `char *sign_commit = NULL; /* FIXME: cli users might want to sign again`

`rerere.c` (4)

- 2015-06-30 `4b68c2a0` [L553](https://github.com/git/git/blob/master/rerere.c#L553) `* NEEDSWORK: we do not record or replay a previous "resolve by`
- 2015-06-30 `4b68c2a0` [L589](https://github.com/git/git/blob/master/rerere.c#L589) `* NEEDSWORK: we may want to fix the caller that implements "rerere`
- 2016-03-14 `3d730ed9` [L1013](https://github.com/git/git/blob/master/rerere.c#L1013) `* NEEDSWORK: handle conflicts from merges with`
- 2015-06-30 `e828de82` [L1290](https://github.com/git/git/blob/master/rerere.c#L1290) `* NEEDSWORK: shouldn't we be calling this from "reset --hard"?`

`reset.c` (1)

- 2021-09-27 `1b5f3733` [L169](https://github.com/git/git/blob/master/reset.c#L169) `unpack_tree_opts.preserve_ignored = 0; /* FIXME: !overwrite_ignore */`

`resolve-undo.c` (1)

- 2021-04-01 `dc26b23e` [L163](https://github.com/git/git/blob/master/resolve-undo.c#L163) `/* TODO: audit for interaction with sparse-index. */`

`revision.c` (2)

- 2010-04-20 `ebdc94f3` [L1388](https://github.com/git/git/blob/master/revision.c#L1388) `* NEEDSWORK: decide if we want to remove parents that are`
- 2021-04-01 `f5fed74f` [L1810](https://github.com/git/git/blob/master/revision.c#L1810) `/* TODO: audit for interaction with sparse-index. */`

`run-command.c` (1)

- 2015-12-15 `c553c72e` [L1861](https://github.com/git/git/blob/master/run-command.c#L1861) `* NEEDSWORK:`

`send-pack.c` (2)

- 2014-09-12 `a85b377d` [L342](https://github.com/git/git/blob/master/send-pack.c#L342) `* NEEDSWORK: perhaps move this to git-compat-util.h or somewhere and`
- 2014-08-12 `621b0599` [L637](https://github.com/git/git/blob/master/send-pack.c#L637) `* NEEDSWORK: why does delete-refs have to be so specific to`

`sequencer.c` (4)

- 2020-11-02 `14c4586c` [L785](https://github.com/git/git/blob/master/sequencer.c#L785) `* TODO: merge_switch_to_result will update index/working tree;`
- 2021-09-27 `1b5f3733` [L4106](https://github.com/git/git/blob/master/sequencer.c#L4106) `unpack_tree_opts.preserve_ignored = 0; /* FIXME: !overwrite_ignore */`
- 2020-11-02 `14c4586c` [L4399](https://github.com/git/git/blob/master/sequencer.c#L4399) `* TODO: Should use merge_incore_recursive() and`
- 2026-07-15 `42554b78` [L5023](https://github.com/git/git/blob/master/sequencer.c#L5023) `* NEEDSWORK: Do not record the commit as rewritten when`

`setup.c` (1)

- 2017-06-20 `73f192c9` [L2049](https://github.com/git/git/blob/master/setup.c#L2049) `* NEEDSWORK: currently we allow bogus GIT_DIR values to be set in some`

`shallow.c` (2)

- 2018-05-19 `58dbe58f` [L123](https://github.com/git/git/blob/master/shallow.c#L123) `* TODO: use "int" elemtype instead of "int *" when/if commit-slab`
- 2013-12-05 `8e277383` [L641](https://github.com/git/git/blob/master/shallow.c#L641) `/* XXX check "UNINTERESTING" from pack bitmaps if available */`

`sparse-index.c` (1)

- 2021-07-14 `fc6609d1` [L218](https://github.com/git/git/blob/master/sparse-index.c#L218) `* NEEDSWORK: If we have unmerged entries, then stay full.`

`submodule.c` (7)

- 2021-08-06 `a452128a` [L235](https://github.com/git/git/blob/master/submodule.c#L235) `* NEEDSWORK: Emit a warning if submodule.active exists, but is valuele`
- 2016-08-31 `fd47ae6a` [L684](https://github.com/git/git/blob/master/submodule.c#L684) `/* TODO: other options may need to be passed here. */`
- 2022-03-07 `b90d9f76` [L795](https://github.com/git/git/blob/master/submodule.c#L795) `* NEEDSWORK: Storing an arbitrary commit is undesirable because we can`
- 2022-03-07 `b90d9f76` [L1650](https://github.com/git/git/blob/master/submodule.c#L1650) `* NEEDSWORK: Submodules set/unset a value for`
- 2019-03-13 `bd5e567d` [L1784](https://github.com/git/git/blob/master/submodule.c#L1784) `* NEEDSWORK: This indicates that the overall fetch`
- 2021-09-27 `94b7f156` [L2110](https://github.com/git/git/blob/master/submodule.c#L2110) `/* TODO: determine if this might overwright untracked files */`
- 2017-03-08 `bf0231c6` [L2626](https://github.com/git/git/blob/master/submodule.c#L2626) `* FIXME:`

`tree-walk.c` (1)

- 2018-11-18 `5a0b97b3` [L1198](https://github.com/git/git/blob/master/tree-walk.c#L1198) `* FIXME: attributes _can_ match directories and we`

`unpack-trees.c` (1)

- 2023-02-27 `13e1fd6e` [L2288](https://github.com/git/git/blob/master/unpack-trees.c#L2288) `* TODO: We should actually invalidate o->internal.result, not src_inde`

`upload-pack.c` (1)

- 2007-01-08 `93822c22` [L193](https://github.com/git/git/blob/master/upload-pack.c#L193) `/* XXX: are we happy to lose stuff here? */`

`usage.c` (1)

- 2019-02-22 `ee4512ed` [L62](https://github.com/git/git/blob/master/usage.c#L62) `* TODO It would be nice to update the call sites to pass both`

`utf8.c` (2)

- 2022-12-01 `937b71cc` [L230](https://github.com/git/git/blob/master/utf8.c#L230) `* TODO: fix the interface of this function and 'utf8_strwidth()' to`
- 2013-03-07 `6cd3c053` [L685](https://github.com/git/git/blob/master/utf8.c#L685) `* TODO use iconv to decode one char and obtain its chrlen`

`worktree.c` (1)

- 2023-12-29 `465a22b3` [L180](https://github.com/git/git/blob/master/worktree.c#L180) `* NEEDSWORK: This function exists so that we can look up metadata of a`

`wt-status.c` (1)

- 2009-12-11 `3c588453` [L235](https://github.com/git/git/blob/master/wt-status.c#L235) `; /* NEEDSWORK: use "git reset --unresolve"??? */`

</details>

<details>
<summary><b>Documentation</b> &mdash; 16 markers</summary>

`Documentation/CodingGuidelines` (4)

- 2026-02-12 `aa94ba7d` [L36](https://github.com/git/git/blob/master/Documentation/CodingGuidelines#L36) `- A label "NEEDSWORK:" followed by a description of the things to`
- 2026-02-12 `aa94ba7d` [L38](https://github.com/git/git/blob/master/Documentation/CodingGuidelines#L38) `decisions yet to be made. 80% of the work to resolve a NEEDSWORK`
- 2026-02-12 `aa94ba7d` [L42](https://github.com/git/git/blob/master/Documentation/CodingGuidelines#L42) `NEEDSWORK comment without doing anything else, with the commit log`
- 2026-02-12 `aa94ba7d` [L44](https://github.com/git/git/blob/master/Documentation/CodingGuidelines#L44) `the thing the NEEDSWORK comment mentioned.`

`Documentation/MyFirstContribution.adoc` (1)

- 2019-05-17 `76644e32` [L983](https://github.com/git/git/blob/master/Documentation/MyFirstContribution.adoc#L983) `TODO https://github.com/gitgitgadget/gitgitgadget/issues/83`

`Documentation/git-range-diff.adoc` (1)

- 2018-08-13 `ba931edd` [L170](https://github.com/git/git/blob/master/Documentation/git-range-diff.adoc#L170) `-TODO: Describe a bug`

`Documentation/git-rebase.adoc` (2)

- 2010-08-10 `cd035b1c` [L946](https://github.com/git/git/blob/master/Documentation/git-rebase.adoc#L946) `pick deadbee Implement feature XXX`
- 2010-08-10 `cd035b1c` [L947](https://github.com/git/git/blob/master/Documentation/git-rebase.adoc#L947) `fixup f1a5c00 Fix to feature XXX`

`Documentation/gitprotocol-http.adoc` (6)

- 2013-08-21 `4c6fffe2` [L366](https://github.com/git/git/blob/master/Documentation/gitprotocol-http.adoc#L366) `TODO: Document this further.`
- 2014-01-26 `586aa786` [L443](https://github.com/git/git/blob/master/Documentation/gitprotocol-http.adoc#L443) `TODO: Define error if no "want" lines are requested.`
- 2013-08-21 `4c6fffe2` [L463](https://github.com/git/git/blob/master/Documentation/gitprotocol-http.adoc#L463) `TODO: Document the pack based response`
- 2013-08-21 `4c6fffe2` [L477](https://github.com/git/git/blob/master/Documentation/gitprotocol-http.adoc#L477) `TODO: Document the non-pack response`
- 2013-08-21 `4c6fffe2` [L480](https://github.com/git/git/blob/master/Documentation/gitprotocol-http.adoc#L480) `TODO: Document parsing response`
- 2013-08-21 `4c6fffe2` [L528](https://github.com/git/git/blob/master/Documentation/gitprotocol-http.adoc#L528) `TODO: Document this further.`

`Documentation/lint-manpages.sh` (2)

- 2024-06-06 `2dd100c5` [L8](https://github.com/git/git/blob/master/Documentation/lint-manpages.sh#L8) `@\$(foreach b,\$($1),echo XXX \$(b:\$X=) YYY;)`
- 2024-06-06 `2dd100c5` [L12](https://github.com/git/git/blob/master/Documentation/lint-manpages.sh#L12) `sed -n -e 's/.*XXX \(.*\) YYY.*/\1/p'`

</details>

<details>
<summary><b>builtin</b> &mdash; 55 markers</summary>

`builtin/am.c` (1)

- 2021-09-27 `1b5f3733` [L2017](https://github.com/git/git/blob/master/builtin/am.c#L2017) `opts.preserve_ignored = 0; /* FIXME: !overwrite_ignore */`

`builtin/checkout.c` (2)

- 2008-08-30 `0cf8581e` [L366](https://github.com/git/git/blob/master/builtin/checkout.c#L366) `* NEEDSWORK:`
- 2019-04-25 `183fb44f` [L705](https://github.com/git/git/blob/master/builtin/checkout.c#L705) `* NEEDSWORK: if --worktree is not specified, we`

`builtin/clone.c` (1)

- 2017-03-17 `bb62e0a9` [L1149](https://github.com/git/git/blob/master/builtin/clone.c#L1149) `* NEEDSWORK: In a multi-working-tree world, this needs to be`

`builtin/commit.c` (2)

- 2021-04-01 `cb8388df` [L272](https://github.com/git/git/blob/master/builtin/commit.c#L272) `/* TODO: audit for interaction with sparse-index. */`
- 2021-04-01 `cb8388df` [L1041](https://github.com/git/git/blob/master/builtin/commit.c#L1041) `/* TODO: audit for interaction with sparse-index. */`

`builtin/config.c` (1)

- 2011-01-30 `b09c53a3` [L558](https://github.com/git/git/blob/master/builtin/config.c#L558) `* NEEDSWORK: this naive pattern lowercasing obviously does not`

`builtin/difftool.c` (1)

- 2021-04-01 `48b3c7da` [L609](https://github.com/git/git/blob/master/builtin/difftool.c#L609) `/* TODO: audit for interaction with sparse-index. */`

`builtin/fast-export.c` (1)

- 2018-11-15 `fdf31b63` [L762](https://github.com/git/git/blob/master/builtin/fast-export.c#L762) `* FIXME: string_list_remove() below for each ref is overall`

`builtin/fast-import.c` (4)

- 2020-05-30 `d42a2fb7` [L1977](https://github.com/git/git/blob/master/builtin/fast-import.c#L1977) `* NEEDSWORK: perhaps check for reasonable values? For example, we`
- 2020-05-30 `d42a2fb7` [L1990](https://github.com/git/git/blob/master/builtin/fast-import.c#L1990) `* NEEDSWORK: check for brokenness other than num > 1400, such as`
- 2026-03-12 `ee66c793` [L2919](https://github.com/git/git/blob/master/builtin/fast-import.c#L2919) `* NEEDSWORK: To properly support interoperability mode`
- 2019-10-03 `3164e6bd` [L3304](https://github.com/git/git/blob/master/builtin/fast-import.c#L3304) `* NEEDSWORK: replace list of tags with hashmap for faster`

`builtin/fetch.c` (4)

- 2026-06-19 `7d00999b` [L1942](https://github.com/git/git/blob/master/builtin/fetch.c#L1942) `* NEEDSWORK: By the time this function executes, we have already parse`
- 2025-05-19 `0e358de6` [L2052](https://github.com/git/git/blob/master/builtin/fetch.c#L2052) `* TODO: if reference transactions gain logical conflict resolution, we`
- 2017-12-08 `aa57b871` [L2845](https://github.com/git/git/blob/master/builtin/fetch.c#L2845) `/* TODO should this also die if we have a previous partial-clone? */`
- 2022-01-18 `135a12bc` [L2886](https://github.com/git/git/blob/master/builtin/fetch.c#L2886) `* NEEDSWORK: as a future optimization, we can return early`

`builtin/fsck.c` (5)

- 2026-01-09 `f6b26258` [L532](https://github.com/git/git/blob/master/builtin/fsck.c#L532) `/* TODO: Maybe supplement with latest reflog entry info too? */`
- 2026-01-09 `f6b26258` [L539](https://github.com/git/git/blob/master/builtin/fsck.c#L539) `/* TODO: Consider also snapshotting the index of each worktree. */`
- 2026-01-09 `f6b26258` [L656](https://github.com/git/git/blob/master/builtin/fsck.c#L656) `* TODO: Could use refs_for_each_reflog(...) to find`
- 2023-02-24 `8840069a` [L884](https://github.com/git/git/blob/master/builtin/fsck.c#L884) `/* TODO: audit for interaction with sparse-index. */`
- 2026-01-09 `f6b26258` [L1115](https://github.com/git/git/blob/master/builtin/fsck.c#L1115) `* TODO: Consider first walking these indexes in snapshot_refs,`

`builtin/fsmonitor--daemon.c` (1)

- 2022-03-25 `518a522f` [L884](https://github.com/git/git/blob/master/builtin/fsmonitor--daemon.c#L884) `* NEEDSWORK: each batch contains a list of interned strings,`

`builtin/gc.c` (1)

- 2025-11-08 `28b83e6f` [L3494](https://github.com/git/git/blob/master/builtin/gc.c#L3494) `* TODO: this certainly is too eager, as some maintenance tasks may`

`builtin/grep.c` (2)

- 2020-01-15 `c441ea4e` [L467](https://github.com/git/git/blob/master/builtin/grep.c#L467) `* NEEDSWORK: repo_read_gitmodules() might call`
- 2022-09-22 `7cae7627` [L477](https://github.com/git/git/blob/master/builtin/grep.c#L477) `* NEEDSWORK: when reading a submodule, the sparsity settings in the`

`builtin/history.c` (1)

- 2026-04-27 `c6c22579` [L649](https://github.com/git/git/blob/master/builtin/history.c#L649) `* TODO: we don't yet have the ability to drop root`

`builtin/index-pack.c` (3)

- 2020-09-08 `f08cbf60` [L1170](https://github.com/git/git/blob/master/builtin/index-pack.c#L1170) `* NEEDSWORK: If parent data needs to be reloaded, this`
- 2011-02-02 `e337a04d` [L1760](https://github.com/git/git/blob/master/builtin/index-pack.c#L1760) `* NEEDSWORK: extract this bit from free_pack_by_name() in`
- 2025-11-19 `8dc22e87` [L2126](https://github.com/git/git/blob/master/builtin/index-pack.c#L2126) `* TODO: we may eventually set up an in-memory object database,`

`builtin/ls-remote.c` (1)

- 2024-08-02 `9e89dcb6` [L103](https://github.com/git/git/blob/master/builtin/ls-remote.c#L103) `* TODO: This is buggy, but required for transport helpers. When a`

`builtin/merge-index.c` (2)

- 2021-04-01 `299e2c45` [L68](https://github.com/git/git/blob/master/builtin/merge-index.c#L68) `/* TODO: audit for interaction with sparse-index. */`
- 2021-04-01 `299e2c45` [L100](https://github.com/git/git/blob/master/builtin/merge-index.c#L100) `/* TODO: audit for interaction with sparse-index. */`

`builtin/merge-tree.c` (1)

- 2006-02-15 `164dcb97` [L317](https://github.com/git/git/blob/master/builtin/merge-tree.c#L317) `*    NOTE NOTE NOTE! FIXME! We really really need to walk the index`

`builtin/merge.c` (1)

- 2021-09-27 `1b5f3733` [L759](https://github.com/git/git/blob/master/builtin/merge.c#L759) `opts.preserve_ignored = 0; /* FIXME: !overwrite_ignore */`

`builtin/mv.c` (1)

- 2022-08-09 `5784db1b` [L580](https://github.com/git/git/blob/master/builtin/mv.c#L580) `* NEEDSWORK: we are *not* paying attention to`

`builtin/patch-id.c` (1)

- 2024-05-20 `4a1c9593` [L255](https://github.com/git/git/blob/master/builtin/patch-id.c#L255) `* NEEDSWORK: This hack should be removed in favor of converting`

`builtin/pull.c` (1)

- 2015-06-18 `1678b81e` [L606](https://github.com/git/git/blob/master/builtin/pull.c#L606) `* FIXME: The current implementation assumes the default mapping of`

`builtin/read-tree.c` (1)

- 2014-06-13 `5a092ceb` [L194](https://github.com/git/git/blob/master/builtin/read-tree.c#L194) `* NEEDSWORK`

`builtin/receive-pack.c` (2)

- 2026-03-30 `8151f4fe` [L1419](https://github.com/git/git/blob/master/builtin/receive-pack.c#L1419) `* NEEDSWORK: is_null_oid() cannot know whether it's an`
- 2025-06-20 `5c697f0b` [L1917](https://github.com/git/git/blob/master/builtin/receive-pack.c#L1917) `* NEEDSWORK: Add conflict resolution between deletion and creation`

`builtin/replay.c` (1)

- 2023-11-24 `8259e415` [L154](https://github.com/git/git/blob/master/builtin/replay.c#L154) `* TODO: In the future we might want to either die(), or allow`

`builtin/reset.c` (1)

- 2021-09-27 `1b5f3733` [L83](https://github.com/git/git/blob/master/builtin/reset.c#L83) `opts.preserve_ignored = 0; /* FIXME: !overwrite_ignore */`

`builtin/rev-list.c` (1)

- 2025-07-21 `f31abb42` [L731](https://github.com/git/git/blob/master/builtin/rev-list.c#L731) `* NEEDSWORK: The next loop is utterly broken.  It tries to`

`builtin/shortlog.c` (1)

- 2024-10-17 `b3300164` [L413](https://github.com/git/git/blob/master/builtin/shortlog.c#L413) `* NEEDSWORK: Later on we'll call parse_revision_opt which relies on`

`builtin/show-branch.c` (1)

- 2018-05-19 `44cecbf8` [L38](https://github.com/git/git/blob/master/builtin/show-branch.c#L38) `* TODO: convert this use of commit->object.flags to commit-slab`

`builtin/show-index.c` (1)

- 2026-01-30 `ea39808a` [L46](https://github.com/git/git/blob/master/builtin/show-index.c#L46) `* TODO: If a future implementation of index file version encodes the h`

`builtin/stash.c` (1)

- 2021-09-27 `1b5f3733` [L363](https://github.com/git/git/blob/master/builtin/stash.c#L363) `opts.preserve_ignored = 0; /* FIXME: !overwrite_ignore */`

`builtin/submodule--helper.c` (7)

- 2018-05-10 `fc1b9243` [L360](https://github.com/git/git/blob/master/builtin/submodule--helper.c#L360) `* NEEDSWORK: the command currently has access to the variables $name,`
- 2017-03-17 `1f8d7115` [L592](https://github.com/git/git/blob/master/builtin/submodule--helper.c#L592) `* NEEDSWORK: In a multi-working-tree world, this needs to be`
- 2025-11-15 `dd8e8c78` [L2120](https://github.com/git/git/blob/master/builtin/submodule--helper.c#L2120) `* NEEDSWORK: audit and ensure that update_submodule() has right`
- 2024-03-26 `e8d06089` [L2952](https://github.com/git/git/blob/master/builtin/submodule--helper.c#L2952) `* TODO: allow exempting it via`
- 2021-08-06 `a452128a` [L3559](https://github.com/git/git/blob/master/builtin/submodule--helper.c#L3559) `* NEEDSWORK: In a multi-working-tree world this needs to be`
- 2021-08-06 `a452128a` [L3563](https://github.com/git/git/blob/master/builtin/submodule--helper.c#L3563) `* NEEDSWORK: In the longer run, we need to get rid of this`
- 2021-08-10 `a6226fd7` [L3605](https://github.com/git/git/blob/master/builtin/submodule--helper.c#L3605) `/* TODO: audit for interaction with sparse-index. */`

</details>

<details>
<summary><b>compat</b> &mdash; 8 markers</summary>

`compat/fsmonitor/fsm-listen-win32.c` (1)

- 2022-05-26 `39664e93` [L439](https://github.com/git/git/blob/master/compat/fsmonitor/fsm-listen-win32.c#L439) `* NEEDSWORK: We might try to check for the deleted directory`

`compat/regex/regex_internal.c` (1)

- 2010-08-17 `d18f76dc` [L749](https://github.com/git/git/blob/master/compat/regex/regex_internal.c#L749) `/* XXX Don't use mbrtowc, we know which conversion`

`compat/regex/regexec.c` (6)

- 2010-08-17 `d18f76dc` [L2434](https://github.com/git/git/blob/master/compat/regex/regexec.c#L2434) `/* TODO: This isn't efficient.`
- 2010-08-17 `d18f76dc` [L2854](https://github.com/git/git/blob/master/compat/regex/regexec.c#L2854) `TODO: This function isn't efficient...`
- 2010-08-17 `d18f76dc` [L3039](https://github.com/git/git/blob/master/compat/regex/regexec.c#L3039) `TODO: This function is similar to the functions transit_state*(),`
- 2010-08-17 `d18f76dc` [L3267](https://github.com/git/git/blob/master/compat/regex/regexec.c#L3267) `/* TODO: It is still inefficient...  */`
- 2010-08-17 `d18f76dc` [L3804](https://github.com/git/git/blob/master/compat/regex/regexec.c#L3804) `/* FIXME: I don't think this if is needed, as both '\n'`
- 2010-08-17 `d18f76dc` [L4112](https://github.com/git/git/blob/master/compat/regex/regexec.c#L4112) `/* XXX We have no indication of the size of this buffer.  If this`

</details>

<details>
<summary><b>contrib</b> &mdash; 11 markers</summary>

`contrib/buildsystems/CMakeLists.txt` (2)

- 2020-06-26 `f1f5dff9` [L98](https://github.com/git/git/blob/master/contrib/buildsystems/CMakeLists.txt#L98) `#TODO gitk git-gui gitweb`
- 2020-06-26 `f7adba41` [L99](https://github.com/git/git/blob/master/contrib/buildsystems/CMakeLists.txt#L99) `#TODO Enable NLS on windows natively`

`contrib/completion/git-completion.bash` (6)

- 2013-01-11 `fea16b47` [L592](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash#L592) `# XXX does not work when the directory prefix contains a tilde,`
- 2013-01-11 `fea16b47` [L1449](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash#L1449) `# XXX this can not be improved, since options can appear everywhere, a`
- 2013-01-11 `fea16b47` [L1816](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash#L1816) `# XXX should we check for -x option ?`
- 2013-01-11 `fea16b47` [L2165](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash#L2165) `# XXX ignore options like --modified and always suggest all cached`
- 2023-12-03 `a1fbe26a` [L3380](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash#L3380) `# NEEDSWORK:`
- 2021-03-24 `61318078` [L3488](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash#L3488) `# NEEDSWORK: can we somehow unify this with the options in _git_log() `

`contrib/credential/netrc/git-credential-netrc.perl` (1)

- 2013-02-25 `54829209` [L51](https://github.com/git/git/blob/master/contrib/credential/netrc/git-credential-netrc.perl#L51) `# TODO: maybe allow the token map $options{tmap} to be configurable.`

`contrib/libgit-rs/Cargo.toml` (1)

- 2025-01-29 `65c10aa8` [L6](https://github.com/git/git/blob/master/contrib/libgit-rs/Cargo.toml#L6) `rust-version = "1.63" # TODO: Once we hit 1.84 or newer, we may want t`

`contrib/libgit-sys/Cargo.toml` (1)

- 2025-01-28 `e7f8bf12` [L7](https://github.com/git/git/blob/master/contrib/libgit-sys/Cargo.toml#L7) `rust-version = "1.63" # TODO: Once we hit 1.84 or newer, we may want t`

</details>

<details>
<summary><b>git-gui</b> &mdash; 7 markers</summary>

`git-gui/git-gui.sh` (2)

- 2009-08-11 `dd6451f9` [L841](https://github.com/git/git/blob/master/git-gui/git-gui.sh#L841) `# TODO: this option should be added to the git-config documentation`
- 2010-01-24 `a9fa11fe` [L2100](https://github.com/git/git/blob/master/git-gui/git-gui.sh#L2100) `# TODO we could make life easier (start up faster?) for gitk`

`git-gui/lib/index.tcl` (2)

- 2007-07-21 `1ac17950` [L496](https://github.com/git/git/blob/master/git-gui/lib/index.tcl#L496) `# FIXME: Unfortunately, even that isn't enough in some languages`
- 2019-12-01 `fa38ab68` [L539](https://github.com/git/git/blob/master/git-gui/lib/index.tcl#L539) `# FIXME: Unfortunately, even that isn't enough in some languages`

`git-gui/lib/remote.tcl` (1)

- 2008-09-24 `ba6485e0` [L291](https://github.com/git/git/blob/master/git-gui/lib/remote.tcl#L291) `# XXX: Better re-read the config so that we will never get out`

`git-gui/lib/remote_add.tcl` (1)

- 2008-09-24 `ba6485e0` [L105](https://github.com/git/git/blob/master/git-gui/lib/remote_add.tcl#L105) `# XXX: We abuse check-ref-format here, but`

`git-gui/po/zh_cn.po` (1)

- 2008-01-06 `312fd92b` [L21](https://github.com/git/git/blob/master/git-gui/po/zh_cn.po#L21) `# FIXME: checkout 的标准翻译`

</details>

<details>
<summary><b>gitk-git</b> &mdash; 4 markers</summary>

`gitk-git/gitk` (2)

- 2008-11-18 `cdc8429c` [L9933](https://github.com/git/git/blob/master/gitk-git/gitk#L9933) `# XXX this isn't right if we have a path limit...`
- 2013-04-27 `8f3ff933` [L9993](https://github.com/git/git/blob/master/gitk-git/gitk#L9993) `# XXX this isn't right if we have a path limit...`

`gitk-git/po/fr.po` (2)

- 2010-01-12 `5cc0f821` [L42](https://github.com/git/git/blob/master/gitk-git/po/fr.po#L42) `# FIXME : améliorer la traduction de 'file limite'`
- 2010-01-12 `5cc0f821` [L938](https://github.com/git/git/blob/master/gitk-git/po/fr.po#L938) `# FIXME : Traduction standard de "pane"?`

</details>

<details>
<summary><b>gitweb</b> &mdash; 3 markers</summary>

`gitweb/gitweb.perl` (3)

- 2008-10-10 `1b2d297e` [L846](https://github.com/git/git/blob/master/gitweb/gitweb.perl#L846) `# XXX: Warning: If you touch this, check the search form for updating,`
- 2009-02-07 `7e1100e9` [L6666](https://github.com/git/git/blob/master/gitweb/gitweb.perl#L6666) `# TODO: Allow a readme in some safe format.`
- 2006-09-22 `cae1862a` [L7251](https://github.com/git/git/blob/master/gitweb/gitweb.perl#L7251) `# FIXME: Should be available when we have no hash base as well.`

</details>

<details>
<summary><b>odb</b> &mdash; 1 markers</summary>

`odb/source-loose.c` (1)

- 2026-06-01 `87af3bb4` [L972](https://github.com/git/git/blob/master/odb/source-loose.c#L972) `/* TODO: this is a known omission that we'll want to address eventuall`

</details>

<details>
<summary><b>perl</b> &mdash; 9 markers</summary>

`perl/Git.pm` (4)

- 2006-06-24 `d5c7721d` [L89](https://github.com/git/git/blob/master/perl/Git.pm#L89) `TODO: In the future, we might also do`
- 2006-09-23 `18b0fc1c` [L918](https://github.com/git/git/blob/master/perl/Git.pm#L918) `# TODO: Support for passing FILEHANDLE instead of FILENAME`
- 2008-05-23 `7182530d` [L934](https://github.com/git/git/blob/master/perl/Git.pm#L934) `# TODO: Support for passing FILEHANDLE instead of FILENAME`
- 2006-06-25 `a6065b54` [L1745](https://github.com/git/git/blob/master/perl/Git.pm#L1745) `# FIXME: This is probably horrible idea and the thing will explode`

`perl/Git/SVN.pm` (2)

- 2012-07-26 `29499c0b` [L762](https://github.com/git/git/blob/master/perl/Git/SVN.pm#L762) `# FIXME: Fragile, if SVN adds new public properties,`
- 2021-10-29 `412e4cae` [L2272](https://github.com/git/git/blob/master/perl/Git/SVN.pm#L2272) `# TODO: move this to Git.pm?`

`perl/Git/SVN/Editor.pm` (2)

- 2014-12-07 `83c9433e` [L303](https://github.com/git/git/blob/master/perl/Git/SVN/Editor.pm#L303) `# TODO: get existing properties to compare to`
- 2014-12-07 `83c9433e` [L307](https://github.com/git/git/blob/master/perl/Git/SVN/Editor.pm#L307) `# TODO: caching svn properties or storing them in .gitattributes`

`perl/Git/SVN/Log.pm` (1)

- 2012-07-26 `b74fda1c` [L32](https://github.com/git/git/blob/master/perl/Git/SVN/Log.pm#L32) `# TODO: make $c->{l} not have a trailing newline in the future`

</details>

<details>
<summary><b>po</b> &mdash; 22 markers</summary>

`po/AGENTS.md` (7)

- 2026-02-25 `6f8e885f` [L758](https://github.com/git/git/blob/master/po/AGENTS.md#L758) `TODO="po/review-todo.json"`
- 2026-02-25 `6f8e885f` [L764](https://github.com/git/git/blob/master/po/AGENTS.md#L764) `rm -f "$TODO"`
- 2026-02-25 `6f8e885f` [L770](https://github.com/git/git/blob/master/po/AGENTS.md#L770) `rm -f "$BATCH_FILE" "$TODO" "$DONE"`
- 2026-02-25 `6f8e885f` [L779](https://github.com/git/git/blob/master/po/AGENTS.md#L779) `rm -f "$TODO"`
- 2026-02-25 `6f8e885f` [L803](https://github.com/git/git/blob/master/po/AGENTS.md#L803) `git-po-helper msg-select --json --head "$NUM" -o "$TODO" "$PENDING"`
- 2026-02-25 `6f8e885f` [L834](https://github.com/git/git/blob/master/po/AGENTS.md#L834) `TODO="po/review-todo.json"`
- 2026-02-25 `6f8e885f` [L843](https://github.com/git/git/blob/master/po/AGENTS.md#L843) `rm -f "$TODO"`

`po/bg.po` (3)

- 2014-06-27 `642c7fab` [L281](https://github.com/git/git/blob/master/po/bg.po#L281) `# FIXME`
- 2023-08-05 `f42a8bb3` [L289](https://github.com/git/git/blob/master/po/bg.po#L289) `# TODO`
- 2022-06-12 `4ab81452` [L17547](https://github.com/git/git/blob/master/po/bg.po#L17547) `# FIXME - как да обърна реда на форматите? Нито %2$.*ls, нито %.*2$ls,`

`po/de.po` (5)

- 2022-06-19 `13608fdc` [L10560](https://github.com/git/git/blob/master/po/de.po#L10560) `msgstr "Konnte TODO-Liste nicht erzeugen."`
- 2022-06-19 `13608fdc` [L10728](https://github.com/git/git/blob/master/po/de.po#L10728) `msgstr "TODO-Liste während eines interaktiven Rebase bearbeiten"`
- 2022-06-19 `13608fdc` [L19914](https://github.com/git/git/blob/master/po/de.po#L19914) `"Sie bearbeiten gerade die TODO-Datei eines laufenden interaktiven Reb`
- 2022-06-19 `13608fdc` [L21904](https://github.com/git/git/blob/master/po/de.po#L21904) `"Konnte TODO-Befehl nicht ausführen\n"`
- 2022-06-19 `13608fdc` [L21909](https://github.com/git/git/blob/master/po/de.po#L21909) `"bearbeiten Sie bitte zuerst die TODO-Liste:\n"`

`po/es.po` (1)

- 2022-06-16 `69635e52` [L18367](https://github.com/git/git/blob/master/po/es.po#L18367) `"Estás editando el archivo TODO de un rebase interactivo.\n"`

`po/ko.po` (4)

- 2016-11-04 `de7011c1` [L3628](https://github.com/git/git/blob/master/po/ko.po#L3628) `# FIXME: "parent %d" 번호가 무슨 의미?`
- 2016-01-03 `c6cd2669` [L6348](https://github.com/git/git/blob/master/po/ko.po#L6348) `# FIXME: give twice?`
- 2016-01-03 `c6cd2669` [L7042](https://github.com/git/git/blob/master/po/ko.po#L7042) `# FIXME: 의미 불명`
- 2016-08-21 `ec584cd6` [L17005](https://github.com/git/git/blob/master/po/ko.po#L17005) `"진행 중인 대화형 리베이스의 TODO 파일을 편집하는 중입니다.\n"`

`po/sv.po` (1)

- 2026-06-25 `4de2e01d` [L16614](https://github.com/git/git/blob/master/po/sv.po#L16614) `# TODO: Hitta bättre översättning för "poll"`

`po/vi.po` (1)

- 2024-07-26 `db510450` [L67](https://github.com/git/git/blob/master/po/vi.po#L67) `# | ... TODO ...                      |                              |`

</details>

<details>
<summary><b>refs</b> &mdash; 5 markers</summary>

`refs/files-backend.c` (1)

- 2024-05-07 `644daf77` [L3164](https://github.com/git/git/blob/master/refs/files-backend.c#L3164) `* TODO: currently we skip creating reflogs for dangling`

`refs/reftable-backend.c` (4)

- 2025-04-08 `ca89c18d` [L1359](https://github.com/git/git/blob/master/refs/reftable-backend.c#L1359) `* TODO: it's dubious whether we should reload the stack that "HEAD"`
- 2024-05-07 `644daf77` [L1564](https://github.com/git/git/blob/master/refs/reftable-backend.c#L1564) `* TODO: currently we skip creating reflogs for dangling`
- 2024-11-26 `46b5f670` [L2213](https://github.com/git/git/blob/master/refs/reftable-backend.c#L2213) `* TODO: we should adapt this callsite to reload the stack. There is no`
- 2024-11-26 `46b5f670` [L2264](https://github.com/git/git/blob/master/refs/reftable-backend.c#L2264) `* TODO: we should adapt this callsite to reload the stack. There is no`

</details>

<details>
<summary><b>t</b> &mdash; 104 markers</summary>

`t/helper/test-chmtime.c` (1)

- 2022-03-25 `369f0f54` [L140](https://github.com/git/git/blob/master/t/helper/test-chmtime.c#L140) `* NEEDSWORK: The Windows version of 'utime()'`

`t/helper/test-trace2.c` (1)

- 2019-02-22 `a15860dc` [L174](https://github.com/git/git/blob/master/t/helper/test-trace2.c#L174) `* [] TODO talk about process replacement and how it affects SID.`

`t/helper/test-wildmatch.c` (2)

- 2012-11-20 `ef49841d` [L10](https://github.com/git/git/blob/master/t/helper/test-wildmatch.c#L10) `"pattern because Windows does not like it. Use 'XXX/' instead.");`
- 2012-11-20 `ef49841d` [L11](https://github.com/git/git/blob/master/t/helper/test-wildmatch.c#L11) `else if (!strncmp(argv[i], "XXX/", 4))`

`t/lib-gpg.sh` (1)

- 2025-10-13 `e204a167` [L77](https://github.com/git/git/blob/master/t/lib-gpg.sh#L77) `# NEEDSWORK: prepare_gnupghome() should definitely be`

`t/perf/p7527-builtin-fsmonitor.sh` (2)

- 2022-05-26 `7667f9d2` [L23](https://github.com/git/git/blob/master/t/perf/p7527-builtin-fsmonitor.sh#L23) `# NEEDSWORK: It would be nice if perf-lib had an option to`
- 2022-05-26 `7667f9d2` [L112](https://github.com/git/git/blob/master/t/perf/p7527-builtin-fsmonitor.sh#L112) `# NEEDSWORK: We assume that $GIT_PERF_REPEAT_COUNT > 1.  With`

`t/t0000-basic.sh` (18)

- 2021-09-22 `c3ff7be6` [L117](https://github.com/git/git/blob/master/t/t0000-basic.sh#L117) `test_expect_success 'subtest: a failing TODO test' '`
- 2012-12-16 `5ebf89e8` [L125](https://github.com/git/git/blob/master/t/t0000-basic.sh#L125) `> not ok 2 - pretend we have a known breakage # TODO known breakage`
- 2021-09-22 `c3ff7be6` [L132](https://github.com/git/git/blob/master/t/t0000-basic.sh#L132) `test_expect_success 'subtest: a passing TODO test' '`
- 2012-12-16 `b73d9a23` [L138](https://github.com/git/git/blob/master/t/t0000-basic.sh#L138) `> ok 1 - pretend we have fixed a known breakage # TODO known breakage `
- 2021-09-22 `c3ff7be6` [L144](https://github.com/git/git/blob/master/t/t0000-basic.sh#L144) `test_expect_success 'subtest: 2 TODO tests, one passin' '`
- 2012-12-16 `b73d9a23` [L152](https://github.com/git/git/blob/master/t/t0000-basic.sh#L152) `> not ok 1 - pretend we have a known breakage # TODO known breakage`
- 2012-12-16 `b73d9a23` [L154](https://github.com/git/git/blob/master/t/t0000-basic.sh#L154) `> ok 3 - pretend we have fixed another known breakage # TODO known bre`
- 2021-09-22 `c3ff7be6` [L162](https://github.com/git/git/blob/master/t/t0000-basic.sh#L162) `test_expect_success 'subtest: mixed results: pass, failure and a TODO `
- 2012-12-16 `5ebf89e8` [L173](https://github.com/git/git/blob/master/t/t0000-basic.sh#L173) `> not ok 3 - pretend we have a known breakage # TODO known breakage`
- 2012-12-16 `5ebf89e8` [L205](https://github.com/git/git/blob/master/t/t0000-basic.sh#L205) `> not ok 8 - pretend we have a known breakage # TODO known breakage`
- 2012-12-16 `5ebf89e8` [L206](https://github.com/git/git/blob/master/t/t0000-basic.sh#L206) `> not ok 9 - pretend we have a known breakage # TODO known breakage`
- 2012-12-16 `b73d9a23` [L207](https://github.com/git/git/blob/master/t/t0000-basic.sh#L207) `> ok 10 - pretend we have fixed a known breakage # TODO known breakage`
- 2022-07-28 `46fb057a` [L619](https://github.com/git/git/blob/master/t/t0000-basic.sh#L619) `not ok 2 - # TODO induced breakage (--invert-exit-code): failing test `
- 2022-07-28 `46fb057a` [L624](https://github.com/git/git/blob/master/t/t0000-basic.sh#L624) `# faked up failures as TODO & now exiting with 0 due to --invert-exit-`
- 2022-07-28 `46fb057a` [L634](https://github.com/git/git/blob/master/t/t0000-basic.sh#L634) `not ok 2 - # TODO induced breakage (--invert-exit-code): failing test `
- 2022-07-28 `46fb057a` [L637](https://github.com/git/git/blob/master/t/t0000-basic.sh#L637) `# faked up failures as TODO & now exiting with 0 due to --invert-exit-`
- 2022-07-28 `46fb057a` [L648](https://github.com/git/git/blob/master/t/t0000-basic.sh#L648) `not ok 2 - # TODO induced breakage (--invert-exit-code): failing test `
- 2022-07-28 `46fb057a` [L651](https://github.com/git/git/blob/master/t/t0000-basic.sh#L651) `# faked up failures as TODO & now exiting with 0 due to --invert-exit-`

`t/t0027-auto-crlf.sh` (2)

- 2016-04-25 `67e9bff0` [L582](https://github.com/git/git/blob/master/t/t0027-auto-crlf.sh#L582) `# currently the same as text, eol=XXX`
- 2016-04-25 `67e9bff0` [L597](https://github.com/git/git/blob/master/t/t0027-auto-crlf.sh#L597) `# text=auto + eol=XXX`

`t/t0080-unit-test-output.sh` (2)

- 2023-11-09 `e137fe3b` [L17](https://github.com/git/git/blob/master/t/t0080-unit-test-output.sh#L17) `not ok 5 - passing TEST_TODO() # TODO`
- 2024-07-30 `96c6304c` [L63](https://github.com/git/git/blob/master/t/t0080-unit-test-output.sh#L63) `not ok 22 - if_test passing TEST_TODO() # TODO`

`t/t0200-gettext-basic.sh` (1)

- 2011-11-18 `5e9637c6` [L42](https://github.com/git/git/blob/master/t/t0200-gettext-basic.sh#L42) `# TODO: When we have more locales, generalize this to test them`

`t/t0212/parse_events.perl` (3)

- 2019-02-22 `a15860dc` [L171](https://github.com/git/git/blob/master/t/t0212/parse_events.perl#L171) `# TODO decide what information we want to test from thread events.`
- 2019-02-22 `a15860dc` [L183](https://github.com/git/git/blob/master/t/t0212/parse_events.perl#L183) `# TODO decide what information we want to test from exec events.`
- 2022-07-18 `3a251bac` [L225](https://github.com/git/git/blob/master/t/t0212/parse_events.perl#L225) `# NEEDSWORK: Ignore due to`

`t/t0450-txt-doc-vs-help.sh` (1)

- 2022-10-13 `c39fffc1` [L166](https://github.com/git/git/blob/master/t/t0450-txt-doc-vs-help.sh#L166) `echo "=== TODO: $builtin ===" &&`

`t/t1006-cat-file.sh` (2)

- 2025-06-02 `9fd38038` [L186](https://github.com/git/git/blob/master/t/t1006-cat-file.sh#L186) `# FIXME: %(rest) is incompatible with object names that include whites`
- 2025-06-02 `b0b910e0` [L1248](https://github.com/git/git/blob/master/t/t1006-cat-file.sh#L1248) `# FIXME: this call to mktree is incompatible with compatObjectFormat`

`t/t1091-sparse-checkout-builtin.sh` (1)

- 2021-09-24 `49fdd51a` [L503](https://github.com/git/git/blob/master/t/t1091-sparse-checkout-builtin.sh#L503) `# NEEDSWORK: We are asking to update a file outside of the`

`t/t1092-sparse-checkout-compatibility.sh` (10)

- 2021-07-20 `70569fad` [L565](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L565) `# NEEDSWORK: sparse-checkout behaves differently from full-checkout wh`
- 2022-01-11 `e015d4d9` [L831](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L831) `# NEEDSWORK: '--remove', unlike the rest of 'update-index', does not i`
- 2021-09-24 `105e8b01` [L1106](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L1106) `# NEEDSWORK: Even though the merge conflict removed the`
- 2021-09-24 `105e8b01` [L1117](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L1117) `# NEEDSWORK: This mode now fails, because folder2/z is`
- 2021-07-14 `e5ca2910` [L1919](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L1919) `# NEEDSWORK: a sparse-checkout behaves differently from a full checkou`
- 2021-07-20 `70569fad` [L1954](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L1954) `# NEEDSWORK: 'git checkout' behaves incorrectly in the case of`
- 2021-07-20 `70569fad` [L2007](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L2007) `# NEEDSWORK: 'git checkout' behaves incorrectly in the case of`
- 2022-09-22 `7cae7627` [L2210](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L2210) `# NEEDSWORK: when running 'grep' in the superproject with --recurse-su`
- 2022-09-22 `7cae7627` [L2225](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L2225) `# NEEDSWORK: this test is not actually testing the code. The design pu`
- 2023-08-11 `4723ae10` [L2442](https://github.com/git/git/blob/master/t/t1092-sparse-checkout-compatibility.sh#L2442) `# NEEDSWORK: The 'diff --check' test is left as 'test_expect_failure' `

`t/t1700-split-index.sh` (1)

- 2018-11-19 `d8465500` [L48](https://github.com/git/git/blob/master/t/t1700-split-index.sh#L48) `# NEEDSWORK: Stop hard-coding checksums.`

`t/t1800-hook.sh` (1)

- 2023-06-10 `6b6fe8b4` [L569](https://github.com/git/git/blob/master/t/t1800-hook.sh#L569) `# TODO: We should emit the same (or at least a more similar)`

`t/t3070-wildmatch.sh` (5)

- 2018-01-30 `91061c44` [L278](https://github.com/git/git/blob/master/t/t3070-wildmatch.sh#L278) `match 1 1 1 1 'XXX/foo' '**/foo'`
- 2018-01-30 `91061c44` [L300](https://github.com/git/git/blob/master/t/t3070-wildmatch.sh#L300) `match 0 0 0 0 'XXX/\' '*/\'`
- 2018-01-30 `91061c44` [L301](https://github.com/git/git/blob/master/t/t3070-wildmatch.sh#L301) `match 1 1 1 1 'XXX/\' '*/\\'`
- 2018-01-30 `91061c44` [L394](https://github.com/git/git/blob/master/t/t3070-wildmatch.sh#L394) `match 1 1 1 1 'XXX/adobe/courier/bold/o/normal//12/120/75/75/m/70/iso8`
- 2018-01-30 `91061c44` [L395](https://github.com/git/git/blob/master/t/t3070-wildmatch.sh#L395) `match 0 0 0 0 'XXX/adobe/courier/bold/o/normal//12/120/75/75/X/70/iso8`

`t/t3430-rebase-merges.sh` (4)

- 2018-04-25 `8f6aed71` [L35](https://github.com/git/git/blob/master/t/t3430-rebase-merges.sh#L35) `mv "$1" "$(git rev-parse --git-path ORIGINAL-TODO)"`
- 2018-04-25 `8f6aed71` [L135](https://github.com/git/git/blob/master/t/t3430-rebase-merges.sh#L135) `grep -v "^#" <.git/ORIGINAL-TODO >output &&`
- 2026-07-06 `47f79f61` [L484](https://github.com/git/git/blob/master/t/t3430-rebase-merges.sh#L484) `test_grep "^label $third-" .git/ORIGINAL-TODO &&`
- 2026-07-06 `47f79f61` [L485](https://github.com/git/git/blob/master/t/t3430-rebase-merges.sh#L485) `test_grep ! "^label $third$" .git/ORIGINAL-TODO`

`t/t4107-apply-ignore-whitespace.sh` (1)

- 2009-08-04 `86c91f91` [L66](https://github.com/git/git/blob/master/t/t4107-apply-ignore-whitespace.sh#L66) `# because of the missing string at EOL. TODO: this testcase should be`

`t/t4205-log-pretty-formats.sh` (1)

- 2021-04-25 `3593ebd3` [L541](https://github.com/git/git/blob/master/t/t4205-log-pretty-formats.sh#L541) `# --date=[XXX] and corresponding %a[X] %c[X] format equivalency`

`t/t5300-pack-object.sh` (1)

- 2025-01-27 `fc62e033` [L715](https://github.com/git/git/blob/master/t/t5300-pack-object.sh#L715) `# TODO: Make these compatible in the future and replace this test with`

`t/t5515-fetch-merge-logic.sh` (1)

- 2019-02-25 `d790ee17` [L9](https://github.com/git/git/blob/master/t/t5515-fetch-merge-logic.sh#L9) `# NEEDSWORK: If the overspecification of the expected result is reduce`

`t/t5539-fetch-http-shallow.sh` (1)

- 2019-02-25 `d790ee17` [L75](https://github.com/git/git/blob/master/t/t5539-fetch-http-shallow.sh#L75) `# NEEDSWORK: If the overspecification of the expected result is reduce`

`t/t5550-http-fetch-dumb.sh` (1)

- 2020-04-18 `e7fab62b` [L442](https://github.com/git/git/blob/master/t/t5550-http-fetch-dumb.sh#L442) `# NEEDSWORK: Writing commands to git-remote-curl can race against the `

`t/t5551-http-fetch-smart.sh` (1)

- 2019-03-22 `3a9e1ad7` [L239](https://github.com/git/git/blob/master/t/t5551-http-fetch-smart.sh#L239) `# NEEDSWORK: When using HTTP(S), protocol v0 supports a "half-auth"`

`t/t5552-skipping-fetch-negotiator.sh` (1)

- 2019-12-26 `d6509da6` [L194](https://github.com/git/git/blob/master/t/t5552-skipping-fetch-negotiator.sh#L194) `# NEEDSWORK: The number of "have"s sent depends on whether the transpo`

`t/t5616-partial-clone.sh` (1)

- 2019-11-05 `6462d5eb` [L531](https://github.com/git/git/blob/master/t/t5616-partial-clone.sh#L531) `# NEEDSWORK: The tests beginning with "fetch lazy-fetches" below only`

`t/t5750-bundle-uri-parse.sh` (1)

- 2022-12-22 `ebc39479` [L75](https://github.com/git/git/blob/master/t/t5750-bundle-uri-parse.sh#L75) `# TODO: We would prefer if parsing a bundle list would not cause`

`t/t6020-bundle-misc.sh` (1)

- 2022-03-09 `86fdd94d` [L606](https://github.com/git/git/blob/master/t/t6020-bundle-misc.sh#L606) `# NEEDSWORK: 'git clone --bare' should be able to clone from a filtere`

`t/t6102-rev-list-unexpected-objects.sh` (1)

- 2022-07-28 `96ecf699` [L25](https://github.com/git/git/blob/master/t/t6102-rev-list-unexpected-objects.sh#L25) `test_expect_success 'TODO (should fail!): traverse unexpected non-blob`

`t/t6404-recursive-merge.sh` (1)

- 2024-10-24 `f56f9d6c` [L90](https://github.com/git/git/blob/master/t/t6404-recursive-merge.sh#L90) `# TODO: fragile test, relies on ambiguous merge-base resolution`

`t/t7012-skip-worktree-writing.sh` (6)

- 2010-04-19 `3d816767` [L191](https://github.com/git/git/blob/master/t/t7012-skip-worktree-writing.sh#L191) `#TODO test_expect_failure 'git-apply adds file' false`
- 2010-04-19 `3d816767` [L192](https://github.com/git/git/blob/master/t/t7012-skip-worktree-writing.sh#L192) `#TODO test_expect_failure 'git-apply updates file' false`
- 2010-04-19 `3d816767` [L193](https://github.com/git/git/blob/master/t/t7012-skip-worktree-writing.sh#L193) `#TODO test_expect_failure 'git-apply removes file' false`
- 2010-04-19 `3d816767` [L194](https://github.com/git/git/blob/master/t/t7012-skip-worktree-writing.sh#L194) `#TODO test_expect_failure 'git-mv to skip-worktree' false`
- 2010-04-19 `3d816767` [L195](https://github.com/git/git/blob/master/t/t7012-skip-worktree-writing.sh#L195) `#TODO test_expect_failure 'git-mv from skip-worktree' false`
- 2010-04-19 `3d816767` [L196](https://github.com/git/git/blob/master/t/t7012-skip-worktree-writing.sh#L196) `#TODO test_expect_failure 'git-checkout' false`

`t/t7401-submodule-summary.sh` (1)

- 2020-08-21 `2a0d1a5c` [L16](https://github.com/git/git/blob/master/t/t7401-submodule-summary.sh#L16) `# NEEDSWORK: This test script is old fashioned and may need a big clea`

`t/t7406-submodule-update.sh` (3)

- 2018-08-08 `65799fbc` [L992](https://github.com/git/git/blob/master/t/t7406-submodule-update.sh#L992) `sed "s/$H/XXX/" out >expect &&`
- 2018-08-08 `65799fbc` [L1002](https://github.com/git/git/blob/master/t/t7406-submodule-update.sh#L1002) `sed "s/$H2/XXX/" out >actual &&`
- 2022-06-30 `8fc36c39` [L1152](https://github.com/git/git/blob/master/t/t7406-submodule-update.sh#L1152) `# NEEDSWORK: Clean up the tests so that we can reuse the test setup.`

`t/t7501-commit-basic-functionality.sh` (1)

- 2024-01-17 `cab11f4e` [L6](https://github.com/git/git/blob/master/t/t7501-commit-basic-functionality.sh#L6) `# FIXME: Test the various index usages, test reflog`

`t/t7510-signed-commit.sh` (1)

- 2021-09-10 `1bfb57f6` [L369](https://github.com/git/git/blob/master/t/t7510-signed-commit.sh#L369) `# NEEDSWORK: This test relies on the test_tick commit/author dates fro`

`t/t7527-builtin-fsmonitor.sh` (1)

- 2022-03-25 `a00cdff8` [L671](https://github.com/git/git/blob/master/t/t7527-builtin-fsmonitor.sh#L671) `# NEEDSWORK: Repeat one of the "edit" tests on wt-secondary and`

`t/t7528-signed-commit-ssh.sh` (3)

- 2021-09-10 `3326a783` [L401](https://github.com/git/git/blob/master/t/t7528-signed-commit-ssh.sh#L401) `test_expect_failure GPGSSH 'detect fudged commit with double signature`
- 2021-09-10 `3326a783` [L417](https://github.com/git/git/blob/master/t/t7528-signed-commit-ssh.sh#L417) `test_expect_failure GPGSSH 'show double signature with custom format (`
- 2021-09-10 `3326a783` [L430](https://github.com/git/git/blob/master/t/t7528-signed-commit-ssh.sh#L430) `test_expect_failure GPGSSH 'verify-commit verifies multiply signed com`

`t/t9350-fast-export.sh` (1)

- 2009-03-23 `41a5c70f` [L725](https://github.com/git/git/blob/master/t/t9350-fast-export.sh#L725) `# NEEDSWORK: not just check return status, but validate the output`

`t/t9400-git-cvsserver-server.sh` (2)

- 2007-05-02 `b3b53439` [L341](https://github.com/git/git/blob/master/t/t9400-git-cvsserver-server.sh#L341) `#TODO: cvsserver doesn't support update w/o -d`
- 2008-02-01 `41ac414e` [L342](https://github.com/git/git/blob/master/t/t9400-git-cvsserver-server.sh#L342) `test_expect_failure "cvs update w/o -d doesn't create subdir (TODO)" '`

`t/t9402-git-cvsserver-refs.sh` (2)

- 2012-10-13 `aa7aab3b` [L510](https://github.com/git/git/blob/master/t/t9402-git-cvsserver-refs.sh#L510) `# TODO: Validate that the .# file was saved properly, and then`
- 2012-10-13 `aa7aab3b` [L532](https://github.com/git/git/blob/master/t/t9402-git-cvsserver-refs.sh#L532) `# TODO: test cvs status`

`t/t9806-git-p4-options.sh` (1)

- 2011-12-24 `09fca77b` [L212](https://github.com/git/git/blob/master/t/t9806-git-p4-options.sh#L212) `# XXX: should clone/sync just use the client spec exactly, rather`

`t/t9902-completion.sh` (4)

- 2013-04-27 `ddf07bdd` [L2814](https://github.com/git/git/blob/master/t/t9902-completion.sh#L2814) `: TODO .gitignore should not be here &&`
- 2013-04-27 `ddf07bdd` [L2822](https://github.com/git/git/blob/master/t/t9902-completion.sh#L2822) `: TODO .gitignore should not be here &&`
- 2013-04-27 `ddf07bdd` [L2835](https://github.com/git/git/blob/master/t/t9902-completion.sh#L2835) `: TODO .gitignore should not be here &&`
- 2013-04-27 `ddf07bdd` [L2846](https://github.com/git/git/blob/master/t/t9902-completion.sh#L2846) `: TODO .gitignore should not be here &&`

`t/test-lib.sh` (5)

- 2022-07-28 `46fb057a` [L811](https://github.com/git/git/blob/master/t/test-lib.sh#L811) `say_color warn "# faked up failures as TODO & now exiting with 0 due t`
- 2022-07-28 `46fb057a` [L820](https://github.com/git/git/blob/master/t/test-lib.sh#L820) `pfx="# TODO induced breakage (--invert-exit-code):"`
- 2022-07-28 `6d00680d` [L843](https://github.com/git/git/blob/master/t/test-lib.sh#L843) `say_color error "ok $test_count - $1 # TODO known breakage vanished"`
- 2022-07-28 `6d00680d` [L849](https://github.com/git/git/blob/master/t/test-lib.sh#L849) `say_color warn "not ok $test_count - $1 # TODO known breakage"`
- 2026-02-20 `68ac70b6` [L1783](https://github.com/git/git/blob/master/t/test-lib.sh#L1783) `# NEEDSWORK: We might eventually want to split this up into two`

`t/unit-tests/test-lib.c` (2)

- 2023-11-09 `e137fe3b` [L106](https://github.com/git/git/blob/master/t/unit-tests/test-lib.c#L106) `vprintf(format, ap); /* TODO: handle newlines */`
- 2023-11-09 `e137fe3b` [L244](https://github.com/git/git/blob/master/t/unit-tests/test-lib.c#L244) `printf(" # TODO");`

</details>

<details>
<summary><b>templates</b> &mdash; 4 markers</summary>

`templates/hooks/sendemail-validate.sample` (4)

- 2023-04-14 `3c8d3ade` [L22](https://github.com/git/git/blob/master/templates/hooks/sendemail-validate.sample#L22) `# Replace the TODO placeholders with appropriate checks according to y`
- 2023-04-14 `3c8d3ade` [L27](https://github.com/git/git/blob/master/templates/hooks/sendemail-validate.sample#L27) `# TODO: Replace with appropriate checks (e.g. spell checking).`
- 2023-04-14 `3c8d3ade` [L35](https://github.com/git/git/blob/master/templates/hooks/sendemail-validate.sample#L35) `# TODO: Replace with appropriate checks for this patch`
- 2023-04-14 `3c8d3ade` [L41](https://github.com/git/git/blob/master/templates/hooks/sendemail-validate.sample#L41) `# TODO: Replace with appropriate checks for the whole series`

</details>

<details>
<summary><b>tools</b> &mdash; 3 markers</summary>

`tools/check-builtins.sh` (2)

- 2015-02-05 `8c1e9f40` [L6](https://github.com/git/git/blob/master/tools/check-builtins.sh#L6) `$(foreach b,$(BUILT_INS),echo XXX $(b:$X=) YYY;)`
- 2006-11-05 `c74390e4` [L11](https://github.com/git/git/blob/master/tools/check-builtins.sh#L11) `sed -n -e 's/.*XXX \(.*\) YYY.*/\1/p' |`

`tools/coccinelle/the_repository.cocci` (1)

- 2026-01-15 `4eb105c1` [L5](https://github.com/git/git/blob/master/tools/coccinelle/the_repository.cocci#L5) `// TODO: remove the rules below and the macros from tree.h after the`

</details>

<details>
<summary><b>trace2</b> &mdash; 1 markers</summary>

`trace2/tr2_tgt_normal.c` (1)

- 2019-02-22 `ee4512ed` [L233](https://github.com/git/git/blob/master/trace2/tr2_tgt_normal.c#L233) `* TODO if (cmd->env) { Consider dumping changes to environment. }`

</details>
