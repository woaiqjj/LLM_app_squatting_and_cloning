# LLMappCrazy

## Overview

**LLMappCrazy** is a tool designed to detect impersonation attacks in Large Language Model (LLM) app stores by identifying **app squatting** and **app cloning**. By leveraging 14 squatting generation techniques along with Levenshtein distance and BERT-based semantic analysis, LLMappCrazy provides a comprehensive approach to detecting apps that mimic popular names or functionality.

### Key Features

- **Name Variant Generation**: Generates squatting name variants using techniques such as symbol expansion, character substitution, and emoji addition.
- **Similarity Analysis**: Uses Levenshtein distance and BERT-based semantic similarity to identify cloned apps.
- **Cross-Platform Detection**: Analyzes app names across multiple platforms to detect potential cross-platform impersonation.

## Usage

To run **LLMappCrazy** with a specific app name and output results to a CSV file, use the following command:

```bash
python LLMappCrazy.py --appname "ExampleAppName" --file "output.csv"
```

### Parameters

- `--appname` (required): The name of the application you want to analyze for squatting or cloning variations.
- `--file` (required): The output file path where the results will be saved in CSV format.

### Example

```bash
python LLMappCrazy.py --appname "GPTAssistant" --file "squatting_results.csv"
```

This command will analyze potential squatting or cloning variations of "GPTAssistant" and output the results to `squatting_results.csv`.

## Output

The output CSV file will include details of detected squatting and cloning apps, such as generated name variants, similarity scores, and potential impersonation risks.

## Requirements

Ensure Python is installed. The tool may use libraries such as `Levenshtein` and `transformers` for similarity analysis.

---

This `README.md` provides users with an overview of **LLMappCrazy** and clear instructions on how to use it with example commands. Let me know if you'd like any additional information included!