# Task 1: Laying the Foundation for Analysis

Author: Bemnet Mulachew  
Date: 10 July 2026  
Week 10 Challenge - Brent Oil Price Change Point Analysis

---

## 1. Data Analysis Workflow

### 1.1 Overview

My analysis follows a structured data science workflow to identify and quantify the impact of major events on Brent oil prices.



## 2. Event Research & Compilation

### 2.1 Methodology

I researched major geopolitical events, OPEC decisions, and economic shocks that could plausibly impact Brent oil prices. Sources included:
- Historical oil market reports
- News archives (BBC, Reuters, Bloomberg)
- Academic papers on oil price determinants
- OPEC official announcements

### 2.2 Compiled Events

A total of 17 key events were identified and compiled into a structured dataset:

| # | Date | Event | Type |
|---|------|-------|------|
| 1 | 1990-08-02 | Gulf War | Conflict |
| 2 | 1991-01-17 | Operation Desert Storm | Conflict |
| 3 | 1997-11-01 | Asian Financial Crisis | Economic |
| 4 | 1998-12-17 | OPEC Production Cut | OPEC |
| 5 | 2001-09-11 | 9/11 Attacks | Terrorism |
| 6 | 2003-03-20 | Iraq War | Conflict |
| 7 | 2005-08-29 | Hurricane Katrina | Natural Disaster |
| 8 | 2008-07-11 | Oil Price Peak | Economic |
| 9 | 2008-09-15 | Global Financial Crisis | Economic |
| 10 | 2011-02-15 | Arab Spring | Conflict |
| 11 | 2014-06-01 | ISIL Conflict | Conflict |
| 12 | 2014-11-27 | OPEC Supply Battle | OPEC |
| 13 | 2016-01-16 | Iran Sanctions Lifted | Sanctions |
| 14 | 2020-03-06 | OPEC+ Meeting Collapse | OPEC |
| 15 | 2020-04-20 | Negative Oil Prices | Economic |
| 16 | 2021-10-01 | Energy Crisis | Economic |
| 17 | 2022-02-24 | Russia-Ukraine War | Conflict |

📁 File: data/processed/events.csv

---

## 3. Assumptions and Limitations

### 3.1 Key Assumptions

1. Price data accuracy: The dataset provided is accurate and representative of global Brent oil prices.

2. Event date accuracy: Event dates are approximate; the true impact may have occurred days or weeks before/after the event.

3. Single change point model: The initial model assumes a single change point. Multiple change points are possible.

4. Independence: Events are treated as independent shocks, though in reality they may interact.

5. Normal distribution: The model assumes Normally distributed prices (or log prices), which may not fully capture oil price behavior.

### 3.2 Important Distinction: Correlation vs. Causation

> ⚠️ CRITICAL NOTE

While a change point detected in the model may coincide with an event, this does not prove causation. The relationship could be:

| Type | Description |
|------|-------------|
| Causal | The event caused the price change |
| Coincidental | Both occurred at the same time by chance |
| Anticipatory | Market priced in the event before it happened |
| Delayed | Impact occurred after a lag |
| Confounded | Another factor influenced both |

Example: The 9/11 attacks occurred at the same time as a broader economic downturn. Separating the causal impact of 9/11 from other factors is challenging.

### 3.3 Statistical Limitations

1. Limited variables: The model only uses price data, ignoring GDP, inflation, currency rates, etc.

2. Model simplicity: The single-change-point model may oversimplify complex market dynamics.

3. Data frequency: Daily data captures market reactions but may miss intra-day or monthly patterns.

4. Historical context: Price behavior in 1990 differs from 2020; market fundamentals change.

---

## 4. Initial EDA Findings

### 4.1 Data Overview

| Metric | Value |
|--------|-------|
| Date Range | 20 May 1987 - 30 Sep 2022 |
| Total Records | ~12,900 days |
| Price Range | $9.55 - $147.50 |
| Mean Price | $52.34 |
| Standard Deviation | $32.18 |

### 4.2 Key Observations

1. Significant upward trend from 2000-2008
2. Sharp drop during 2008 financial crisis
3. Volatility increase after 2014 (OPEC supply battle)
4. Historic volatility during 2020 (COVID-19, negative prices)
5. Rapid recovery in 2021-2022 (post-COVID demand)

### 4.3 Visual Summary

*[Add plots from your EDA here]*

---
- Change point dates: The most likely dates of structural breaks
- Parameter estimates: Before/after means and standard deviations
- Probabilistic statements: e.g., "There is a 95% probability that the price shifted by X%"

### 5.2 From Event Association

- Event-impact mapping: Which events align with detected change points
- Impact quantification: Measured price changes associated with events
- Confidence levels: How certain we are about each association

### 5.3 Limitations of Outputs

- Change point detection does not identify *why* the change occurred
- Multiple events may occur around the same time, making attribution difficult
- The model provides probabilistic estimates, not deterministic answers

---

## 6. Next Steps

- ✅ Task 1 Complete: Workflow defined, events compiled
- ⬜ Task 2: Build and run Bayesian change point model
- ⬜ Task 3: Develop interactive dashboard

---

Prepared by: Bemnet Mulachew  
Date: 1 Aug 2026

## 5. Expected Outputs

### 5.1 From Change Point Analysis
