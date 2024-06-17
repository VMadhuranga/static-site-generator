# Static site generator

A static site generator built with Python. It takes Markdown files and turns them into a static website of HTML.

## Prerequisites

- You need to have [Python](https://www.python.org/) installed in your PC.

> Note: This project was built and tested in Debian 12 using Python version 3.12.3.

## Run Locally

- [Fork and clone](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the repo.
- Go to the repo directory.
- Add your static files (like CSS and Images) to the `static/` directory.
- Add your markdown files to the `content/` directory.
- Inside repo's root directory run the `./main.sh` command in the terminal.
- Go to http://localhost:8888 to view the web site.

> Note: Example files are provided in `content/` and `static/` directories.

## Running Tests

Inside repo's root directory run the `./test.sh` command in the terminal to run tests.

## Features

Supported markdown syntaxes:

- Heading
- Bold texts
- Italic texts
- Blockquote
- Unordered list
- Ordered list
- Inline code
- Code block
- Link
- Image

> Note: Currently, nesting inline elements (like "**bold _italic_**" word) does not work.

## Acknowledgment

This project is a part of [BOOT.DEV](https://www.boot.dev/), an online course to learn back-end development.
