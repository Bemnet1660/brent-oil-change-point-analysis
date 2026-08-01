# Final Report: Change Point Analysis of Brent Oil Prices

Author: BEMNET MULACHEW 
Date: 14 July 2026  
Course: KAIM 9 – Week 10 Challenge  
Institution: 10 Academy

---

## 1. Executive Summary

This report presents a Bayesian change point analysis of Brent oil prices from May 20, 1987 to September 30, 2022. Using PyMC, we identified structural breaks in the price series and associated them with major geopolitical events, OPEC decisions, and economic shocks.

Our key finding is a single dominant change point around 1990 , where the average price shifted from $[before] to $[after] , a [±X]% change. This break aligns with the [insert event name] , providing statistical evidence of its market impact.

The interactive dashboard (built with Flask + React) allows stakeholders to explore historical trends, filter by date, and highlight event-driven price movements.

---

## 2. Methodology

### 2.1 Data
- Source: Daily Brent oil prices (USD/barrel) from 1987-05-20 to 2022-09-30.
- Preprocessing: Converted to datetime, handled missing values via forward fill, computed log returns for stationarity.

### 2.2 Bayesian Change Point Model
We used PyMC to fit a single-change-point model:

- Prior for tau (change point index): DiscreteUniform(0, N)
- Prior for means: Normal(μ=0, σ=10) for μ₁ and μ₂
- Prior for sigma: HalfCauchy(β=1)
- Likelihood: Normal(μ = switch(tau > t, μ₁, μ₂), σ)

MCMC sampling: 2000 draws, 1000 tune, 4 chains (r_hat < 1.01).

### 2.3 Event Association
We compiled 17 major events (from historical research). Each detected change point was matched to events within ±30 days to infer plausible causal links.

---

## 3. Results

### 3.1 Change Point Detection
The model identified a change point at **[insert date]** (index [idx]).

| Metric | Before Change | After Change | Change |
|--------|---------------|--------------|--------|
| Mean Price | $[before] | $[after[±X]%]%** |
| Std Dev | $[std1] | $[std2] | — |Interpretationon**: There is a 95% posterior probability that the price shift lies betw[lower]r]** [upper]r]** USD.

### 3.2 Associated Events
The change point aligns closely with:

| Event Name | Date | Offset (days) | Impact Estimate |
|------------|------|---------------|-----------------|
| [Event]    | [date] | [±n]        | [High/Medium]  Conclusionon**: The statistical break is consistent with the market reaction[event]t]** , suggesting a causal impact.

### 3.3 Dashboard FeaturePrice chartrt** with overlayed event markersDate range filterer** to zoom into periods of interestEvent listst** with impact badgesVolatility metricscs** (rolling std, max drawdown).

---

## 4. Limitations
Single‑change‑point assumptionon** – Real oil markets undergo multiple breaks. Future work should use multi‑change‑point models.Causation vs. correlationon** – Coincidence does not imply causation; other unobserved factors may have contributed.Limited covariateses** – Only price data used. Including GDP, inflation, and exchange rates could improve explanatory power.Daily datata** – Does not capture intra‑day or high‑frequency effects.

---

## 5. Future Work

- Implemmultiple change point detectionon** (e.g., using pm.ChangePoint or Bayesian online changepoint detection).
- Incorpormacroeconomic variableses** via Vector Autoregression (VAR).
- ExplMarkov‑switchingng** models to capture volatility regimes.
- real‑time data feedsds** to make the dashboard dynamic.

---

## 7. Conclusion

---This analysis successfully demonstrates how Bayesian change point detection can quantify the impact of major events on Brent oil prices. The identified change point aligns with [event] , providing a statistically grounded estimate of its price effect. The accompanying dashboard offers an intuitive way for decision‑makers to explore these insights.

---

## 8. References

- PyMC Documentation: https://www.pymc.io
- Change Point Detection in Time Series (Forecastegy)
- Bayesian Inference and MCMC (Towards Data Science)
- OPEC historical announcements

---

Appendix: All code and data are available in the GitHub repository:  
[https://github.com/Bemnet1660/brent-oil-change-point-analysis](https://github.com/Bemnet1660/brent-oil-change-point-analysis


