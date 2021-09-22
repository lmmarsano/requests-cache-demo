# `str` `Mapping` Error Demo
Error treating `str` as `Mapping` appears to result from an abstract base class that attempts to define immutable, hashable mappings.
This abstract base class registers as virtual subclasses all classes implementing [the required abstract methods for abstract base classes `Hashable`, `Collection`, & `Mapping`](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes).
Coincidentally, `str` also has these required methods.

## Runtime Options
[`.env.defaults`](.env.defaults) documents environment variables (including file paths for secrets) and sets runtime defaults.
Set these environment variables in a `.env` file with a single assignment per line.
Add secret files to specified locations.
**IMPORTANT**: Do not check `.env` or secrets into version control.

## Development
### Requirements
- [poetry][poetry]

### Setup
1. Set [runtime options](#runtime-options).

	``` bash
	editor .env
	```
2. Run setup & follow on-screen instructions: creates virtual environment, configures pyright, installs dependencies & `pre-commit` hooks.

	``` bash
	redo setup
	```

	For those without `redo`, a less functional `do` script exists.

	``` bash
	./do setup
	```

### Automated Tests
```bash
redo check
```

## Redo Files
To overcome `make` limitations, this repository uses the [`redo` system][redo].
An equivalent though less performant [`do` script](local-setup/do) is included for those without the system.
Some `.do` files accept parameters as environment variables.
For example, to preview clean with a dry-run by passing the `-n` flag to `git clean`,

``` bash
ARGS=-n redo clean
```

Parameters may be discovered by reading the `.do` files.

[poetry]: https://python-poetry.org/
[redo]: https://redo.readthedocs.io/
[betamax]: https://betamax.readthedocs.io/
