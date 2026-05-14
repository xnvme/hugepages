![hugepages: inspect and manage Linux hugepages](https://raw.githubusercontent.com/xnvme/hugepages/main/assets/banner.svg)

# hugepages

[![PyPI](https://img.shields.io/pypi/v/hugepages.svg)](https://pypi.org/project/hugepages/)
[![Python](https://img.shields.io/pypi/pyversions/hugepages.svg)](https://pypi.org/project/hugepages/)
[![Test](https://github.com/xnvme/hugepages/actions/workflows/test.yml/badge.svg)](https://github.com/xnvme/hugepages/actions/workflows/test.yml)

Inspect and manage Linux hugepages.

## Install

```
pipx install hugepages
```

Or standalone (single-file, stdlib only, no pip needed):

```
curl -fsSL https://raw.githubusercontent.com/xnvme/hugepages/main/src/hugepages/hugepages.py \
  -o ~/.local/bin/hugepages && chmod +x ~/.local/bin/hugepages
```

## Shell completion

```
hugepages --print-completion bash > ~/.local/share/bash-completion/completions/hugepages
```

Open a new shell (or `source` the file) and tab-completion is live: `hugepages <TAB>` lists `info setup mount`.

## Usage

```
hugepages info                                  # current pool state + supported sizes
sudo hugepages setup --count 512                # reserve 512 pages at the smallest supported size
sudo hugepages setup --size 1048576 --count 4   # reserve 4 x 1 GiB pages
sudo hugepages mount                            # mount hugetlbfs at /dev/hugepages
```

`hugepages info` sample output:

```
Hugepage Support:
  Size: 2048  Total: 512  Free: 512  Reserved: 0
  Size: 1048576  Total: 4  Free: 4  Reserved: 0
```

## Related

- [`devbind`](https://github.com/xnvme/devbind): inspect and control PCI device-driver binding in Linux.
- [`iommu`](https://github.com/safl/iommu): inspect and configure the IOMMU isolation level in Linux.
