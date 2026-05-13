# hugepages

![hugepages — inspect and manage hugepages](assets/banner.svg)

Convenience tool to manage hugepages.

## Install

```
pipx install hugepages
```

Or standalone (single-file, stdlib only -- no pip needed):

```
curl -fsSL https://raw.githubusercontent.com/safl/hugepages/main/src/hugepages/hugepages.py \
  -o ~/.local/bin/hugepages && chmod +x ~/.local/bin/hugepages
```

## Shell completion

```
hugepages --print-completion bash > ~/.local/share/bash-completion/completions/hugepages
```

Open a new shell (or `source` the file) and tab-completion is live: `hugepages <TAB>` lists `info setup mount`.
