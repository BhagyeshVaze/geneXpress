# geneXpress

Python tool for querying UniGene databases to identify tissues where a given gene is expressed across multiple host organisms.

## Usage

```bash
python3 get_gene_level_information.py --host [HOST_NAME] --gene [GENE_NAME]
```

**Supported hosts:** Human, Mouse, Cow, Horse, Sheep, Rat

## Scripts

- **get_gene_level_information.py** — Main CLI script; resolves host names, locates UniGene files, and outputs a sorted list of tissues expressing the specified gene.
- **assignment5/config.py** — Host name mappings and configuration.
- **assignment5/io_utils.py** — File I/O utilities and gene file validation.

## Dependencies

Python 3
