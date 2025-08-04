# CRUSH: Content Repository User & System Handbook

This document outlines the conventions and structure of this content repository. Adhering to these guidelines will ensure consistency and make it easier to manage the content.

## Directory Structure

The repository is organized by topic, with each main directory representing a broad subject area (e.g., `Populism`, `State`, `Institution`). Inside each topic directory, the content is further divided into the following subdirectories:

-   `md/`: Contains the Markdown files for the text-based content.
-   `podcast/`: Contains all media files related to the podcast, including audio (`.wav`, `.m4a`), subtitles (`.srt`), and background images (`.png`, `.jpg`).
-   `tex/`: (Optional) For content written in LaTeX.
-   `pdf/`: (Optional) For final PDF documents.

## Adding New Content

To add a new topic:

1.  Create a new directory at the root of the repository with a descriptive name for the topic.
2.  Inside the new topic directory, create `md/` and `podcast/` subdirectories.
3.  Add your Markdown files to the `md/` directory and your media files to the `podcast/` directory.

## File Naming Conventions

-   **Consistency is key:** When a piece of content has both a Markdown file and associated podcast media, the base filenames should be consistent. For example, `State/暴力资本与欧洲国家形成/md/暴力资本与欧洲国家形成.md` corresponds to `State/暴力资本与欧洲国家形成/podcast/暴力资本与国家炼成.srt`.
-   **Descriptive names:** Use clear, descriptive filenames that reflect the content.

## Markdown Style

-   Use standard Markdown for all text content.
-   For longer documents, consider splitting them into multiple files with a clear naming scheme (e.g., `001-introduction.md`, `002-chapter1.md`).
-   Include an `outline.md` or `README.md` in complex directories to explain the structure of the content.

## No Build/Test Commands

This is a content repository, so there are no build, linting, or testing commands to run. The focus is on maintaining a clear and consistent structure for the files.
