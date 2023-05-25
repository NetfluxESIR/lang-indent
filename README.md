# Template for python scripts

This is a template for python scripts. It is intended to be used as a starting point for new scripts for Netflux.
With this template, you can create a new repository with all the necessary actions and workflows to get started (automated testing, linting and docker image creation).

If you want to learn more about template repositories, check out [this article](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

## Requirements

- Python 3.6+
- Poetry should be installed (see [Poetry documentation](https://python-poetry.org/docs/#installation) for more information)

## Poetry

This template uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging.

## Image creation

On a push to the `main` branch, a new docker image will be created and pushed to the GitHub's package registry. 
The image will be tagged with the version corresponding to the latest workflow run and as `latest`.

For more information, check out the [GitHub's package registry documentation](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).
