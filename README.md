# Bigram_Experiment

This project explores the use of bigrams (pairs of words) in financial news headlines and tweets to detect patterns and events that may correlate with stock price movements. The experiments include data collection, preprocessing, sentiment analysis, and the relationship between sentiment and stock prices.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Introduction

This repository contains experiments with bigram analysis on financial news and social media data. The goal is to identify meaningful patterns and events by analyzing word pairs and their frequency, and to explore their relationship with stock market data.

## Features

- Collects and processes financial news headlines and tweets
- Extracts and analyzes bigrams from text data
- Performs sentiment analysis
- Correlates sentiment and bigram patterns with stock price movements
- Visualizes results with word clouds and data plots

## Getting Started

To initialize the environment:

```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Usage

- Data and results are stored in the `data/` directory.
- Source code for data collection, processing, and analysis is in the `src/` directory.
- Run scripts in `src/` as needed for your experiments.