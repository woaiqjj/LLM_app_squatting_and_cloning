# LLM-app-squatting-and-cloning

## Project Overview

This repository contains **LLMappCrazy**, a tool developed to detect impersonation attacks in Large Language Model (LLM) app stores, specifically focusing on **app squatting** and **app cloning**. LLMappCrazy leverages 14 squatting generation techniques, combined with Levenshtein distance and BERT-based semantic analysis, to identify cloned apps through functional similarity analysis.

### Research Questions (RQs)

This project addresses the following research questions:

- **RQ1**: To what extent are squatting apps present? Do they primarily target popular apps?
- **RQ2**: How widespread are cloning apps in LLM app stores, as another form of impersonation?
- **RQ3**: How many cases of potential cross-platform plagiarism exist? What are the situations in different stores?
- **RQ4**: How many impersonation (squatting and cloning) apps exhibit malicious behavior?
- **RQ5**: What is the impact of these impersonation apps on users and the LLM app ecosystem?

### Features

- **Squatting Name Variants**: Generates multiple variants of app names using techniques such as symbol expansion, character substitution, prefix/suffix addition, and emoji extension.
- **Levenshtein Distance Matching**: Detects minor textual differences between app names.
- **BERT-Based Semantic Analysis**: Identifies semantically similar apps, enabling detection of more nuanced cloning cases.
- **Cross-Platform Analysis**: Identifies potential cross-platform plagiarism by analyzing similarities across multiple LLM app platforms.

## Repository Structure

- `dataset/`: Contains the dataset used in this study, with application information gathered from major LLM app stores.
- `squatting/`: Stores data on detected squatting apps, including generated name variants and their matches.
- `cloning/`: Contains data on detected cloning apps, focusing on apps with high functional and semantic similarity.
- `LLMappCrazy/`: The core tool developed for detecting squatting and cloning, featuring modules for name generation, similarity matching, and cross-platform comparison.
- `top_1000.csv`: Lists the top 1000 apps identified with duplicated or squatting names, showing the extent of name conflicts and impersonation in the dataset.
- `README.md`: Project overview, research context, and usage instructions.

## Data Collection

Data for this project was gathered from six major LLM app stores: GPT Store, FlowGPT, Poe, Coze, Cici, and Character.AI. Key fields collected for each application include application ID, author, description, and instructions, forming a structured dataset for analysis.

## Key Findings

- **Distribution of Squatting Apps**: Of the 12,000 generated squatting name variations, 3,509 squatting apps were identified, with 40% exhibiting malicious behaviors such as phishing, malware distribution, and ad injection.
- **Prevalence of Cloning Apps**: Among the 9,575 detected cloned apps, there were significant instances of cross-platform plagiarism.
- **Impact on Users and Ecosystem**: The large presence of squatting and cloning apps negatively affects user experience and platform trust, presenting potential security risks.

## Contributing

Contributions to improve detection methods, expand datasets, or provide feedback are welcome. Please submit a pull request or reach out to the repository maintainers.