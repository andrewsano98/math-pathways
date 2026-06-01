<!--
title: "Math in Insurance"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/insurance_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Insurance
    </h1>
  </div>

</div>

<br>

###  What will I be doing?
- Evaluating financial risk using probability models, statistical analysis, and actuarial software  
- Working with spreadsheets, SQL databases, and analytics platforms to assess claims and customer data  
- Modeling premiums, payouts, and long-term financial outcomes using forecasting tools  
- Using data visualization and reporting software to communicate trends and business risks  
- Detecting fraud patterns and unusual claim behavior using predictive analytics and machine learning tools  
- Interpreting regulatory, demographic, and economic data to guide insurance policies and pricing decisions  


<br>

###  What are the most common jobs?
- Actuary  
- Insurance Underwriter  
- Risk Analyst  
- Claims Adjuster  
- Actuarial Analyst  
- Insurance Agent  
- Data Analyst
- Risk Manager  


<br>

###  What math concepts do I need to know?
- Probability  
- Statistics  
- Data Analysis  
- Algebra  
- Calculus  
- Financial Mathematics  
- Risk Modeling  
- Expected Value  
- Regression Analysis  

--- PAGE ---

## Mathematical Foundations

A strong quantitative foundation is essential for understanding insurance systems. Insurance is fundamentally a discipline of measuring uncertainty, and this requires fluency in probability, statistics, and financial mathematics. These tools allow risk to be quantified, compared, and ultimately priced.

<br>

### Probability Theory

Probability provides the language for describing uncertain events such as accidents, illness, or loss.

Key concepts include:
- Events and sample spaces  
- Independence of events  
- Conditional relationships between events  

If two events $A$ and $B$ are independent, their joint probability is given by:

$$
P(A \cap B) = P(A)P(B)
$$

This relationship is foundational in insurance, where independence assumptions often simplify large-scale risk modeling.

<br>

### Expected Value and Variance

Expected value represents the long-run average outcome of a random variable, while variance measures its variability or risk.

$$
E[X] = \sum x_i p_i
\quad,\quad
\mathrm{Var}(X) = E[X^2] - (E[X])^2
$$

In insurance contexts:
- $E[X]$ represents the average expected loss  
- $\mathrm{Var}(X)$ represents uncertainty around that loss  

Together, they form the basis for pricing and risk assessment.

<br>

### Conditional Probability

Conditional probability describes how the likelihood of an event changes when additional information is known.

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

This is critical in insurance underwriting, where risk estimates are adjusted based on observable characteristics such as age, behavior, or medical history.

<br>

### Financial Mathematics

Insurance contracts involve payments over time, making financial mathematics essential. Future values must be discounted to present value to account for time and interest.

$$
PV = \frac{FV}{(1+r)^t}
$$

Where:
- $PV$ = present value  
- $FV$ = future value  
- $r$ = interest rate  
- $t$ = time period  

This equation underlies premium pricing, reserve calculation, and long-term policy valuation.


--- PAGE ---

## Risk and Uncertainty

Risk and uncertainty form the conceptual foundation of insurance. While many financial systems deal with known quantities, insurance is concerned with outcomes that are inherently unpredictable. The purpose of insurance is not to eliminate uncertainty, but to structure and manage it in a measurable and financially stable way.

<br>

### Deductibles, Copays, and Coverage Limits

Insurance contracts often include mechanisms that determine how losses are shared between insurer and policyholder:

- **Deductible**: the amount paid by the policyholder before insurance coverage begins  
- **Copay**: a shared percentage of loss  
- **Coverage Limit**: the maximum payout the insurer will provide  

These features reduce moral hazard and help distribute risk more efficiently.

<br>

### Premium Construction

The premium is the price paid by the policyholder in exchange for risk coverage. It is not arbitrary; rather, it is derived from expected losses and adjusted for administrative costs and profit.

$$
\text{Premium} = E[L] + \text{Loading}
$$

Where:
- $E[L]$ = expected loss  
- $\text{loading}$ = administrative costs, capital reserves, and profit margin  

This structure ensures that insurers remain financially solvent while covering anticipated claims.

<br>

### Risk vs. Uncertainty

A key distinction in insurance theory is between *risk* and *uncertainty*:

- **Risk** refers to situations where outcomes are unknown but their probabilities can be estimated.  
- **Uncertainty** refers to situations where probabilities themselves are unknown or cannot be reliably quantified.  

Insurance primarily operates in the domain of risk, where historical data and statistical modeling allow probability estimation.

<br>

### Frequency and Severity of Loss

Insurance systems typically decompose loss into two components:

- **Frequency**: how often an event occurs  
- **Severity**: how large the loss is when it occurs  

This decomposition allows insurers to model risk more effectively:

$$
E[L] = \sum p_i L_i
$$

Where:
- $p_i$ represents the probability of a loss event  
- $L_i$ represents the magnitude of the loss  

Expected loss provides the baseline for pricing and capital allocation.

<br>

### Risk Pooling and Diversification

Insurance works by combining many individual risks into a shared pool. While each individual outcome is uncertain, the *aggregate behavior of the pool becomes predictable*.

This produces a key stabilizing effect:

- Individual losses are highly variable  
- Aggregate losses become increasingly stable as the pool grows  
- Variability is reduced through diversification across independent risks  

Mathematically, risk pooling reduces relative variability:

$$
\mathrm{Var}\left(\frac{1}{n}\sum X_i\right) = \frac{\sigma^2}{n}
$$

Where:
- $X_i$ represents individual losses  
- $\sigma^2$ is the variance of individual loss  

This shows that as the number of insured units increases, the variance of average loss decreases, improving predictability and financial stability.

<br>

### Law of Large Numbers

The Law of Large Numbers explains why insurance systems become more stable and predictable as the number of policyholders increases. While individual losses are random and can vary widely, the average outcome across a large group becomes much more consistent.

Instead of focusing on individual outcomes, we define the sample average loss as:

$$
\bar{X}_n = \frac{X_1 + X_2 + \cdots + X_n}{n}
$$

The Law of Large Numbers states that as the number of observations grows, this sample average approaches the true expected value:

$$
\bar{X}_n \to E[X] \quad \text{as } n \to \infty
$$

Where:
- $\bar{X}_n$ is the average loss across $n$ policyholders  
- $X_1, X_2, \dots, X_n$ are individual losses  
- $E[X]$ is the expected (long-run average) loss  

As $n$ increases, the influence of individual randomness decreases, allowing insurers to predict total claims with increasing accuracy and set premiums more reliably.


--- PAGE ---

## Actuarial Science Basics

Actuarial science forms the mathematical core of insurance. It provides the tools used to model uncertainty over time, estimate future liabilities, and determine fair pricing for insurance products. Unlike basic probability, actuarial methods explicitly incorporate time, risk structure, and financial discounting.

<br>

### Mortality Tables and Survival Models

Mortality tables and survival models describe how long individuals or systems are expected to remain in a given state (e.g., alive, healthy, or active policyholders). A central concept is the survival function:

$$
S(t) = P(T > t)
$$

Where:
- $T$ = time until an event occurs (such as death or claim)  
- $S(t)$ = probability the event has not occurred by time $t$

<br>

Imagine a dataset of 1,000 individuals being tracked over time. Each individual has a recorded time at which a specific event occurs (for example, death, failure, or policy termination). Instead of starting with formulas, we begin by counting outcomes directly.

| Time (t) | Individuals Remaining (N) | Survival Value S(t) |
|---|---|---
| 0 | 1000 | 1.00 |
| 10 | 980 | 0.98 |
| 20 | 940 | 0.94 |
| 30 | 880 | 0.88 |
| 40 | 750 | 0.75 |

<br>

From this perspective, the survival function is computed as:

$$
S(t)=\frac{\text{number of individuals without event at time } t}{\text{total initial population}}
$$

These models are essential in life insurance and pension systems, where timing is as important as probability.

<br>

Computationally, the survival function can be built using a simple procedure:

1. Start with a dataset of individuals  
2. Record the time at which each individual experiences the event  
3. For each time point $t$, count how many individuals have NOT yet experienced the event  
4. Divide this count by the total number of individuals  

This produces a stepwise survival curve directly from data.

<br>

### Loss Distributions and Tail Risk

Insurance losses are not uniformly distributed; they often exhibit heavy tails, meaning rare but extreme events dominate total risk.

Key ideas include:
- Most claims are small and frequent  
- Large claims are rare but financially significant  
- Tail risk represents extreme outcomes in the distribution  

Understanding the shape of loss distributions is critical for maintaining insurer solvency.

<br>

### Pricing Models for Policies

Policy pricing is based on the principle of expected present value, adjusted for uncertainty and administrative costs.

A foundational actuarial quantity is:

$$
EPV = E[L \cdot e^{-rt}]
$$

Where:
- $L$ = future loss  
- $r$ = discount rate  
- $t$ = time until payment  

This equation ensures that future liabilities are expressed in present-day financial terms.

<br>

### Reserving

Reserving refers to the process of estimating the amount of money an insurance company must set aside to pay claims that have already occurred but have not yet been fully paid. These reserves ensure that the insurer can meet its future obligations even if payments are delayed over time.

In practice, reserves are updated regularly as new information becomes available, such as reported claims, revised damage estimates, or changes in claim status. This allows insurers to maintain financial stability as claims develop gradually rather than all at once. Accurate reserving is essential because underestimating liabilities can threaten the long-term financial health of an insurance company, while overestimating them can unnecessarily restrict available capital.


<br>

### Risk Loading in Pricing

Insurance premiums are not based solely on expected loss; they also include compensation for uncertainty.

$$
\text{Premium} = E[L] + \lambda \cdot \mathrm{Var}(L)
$$

Where:
- $E[L]$ = expected loss  
- $\mathrm{Var}(L)$ = variability of loss  
- $\lambda$ = risk loading coefficient  

This formulation reflects the idea that higher uncertainty demands higher premiums, even when expected losses are equal.


--- PAGE ---

## Insurance Types Overview

Insurance is a field that applies mathematical reasoning to the management of uncertain future losses. Although the specific products and industries vary, all forms of insurance share a common structure: they assess risk factors, estimate the likelihood and severity of future events, and translate those estimates into financial terms through pricing and contracts. By pooling large numbers of independent or partially independent risks, insurance systems reduce variability at the collective level, even when individual outcomes remain unpredictable. Different types of insurance—such as life, health, property, liability, and reinsurance—differ primarily in the nature of the risks they cover, the time horizon over which losses occur, and the mathematical models used to describe them. Understanding these differences provides a unified framework for analyzing how uncertainty is quantified, transferred, and managed in real-world financial systems.

<br>

| Insurance Type | What It Covers | Typical Risk Factors | Loss Pattern | Mathematical Focus |
|----------------|----------------|----------------------|--------------|--------------------------|
| Life Insurance | Payout upon death of insured | Age, health status, smoking, genetics, occupation | Low frequency, high severity | Survival models, present value, mortality tables |
| Health Insurance | Medical costs from illness/injury | Age, medical history, lifestyle, pre-existing conditions | High frequency, medium variability | Stochastic processes, utilization models, LLN |
| Auto Insurance | Vehicle damage, liability from accidents | Driving history, age, location, vehicle type, mileage | Moderate frequency, moderate severity | Poisson processes, risk scoring, regression models |
| Homeowners Insurance | Property damage, theft, natural disasters | Location, weather risk, construction type, claims history | Low frequency, high severity (catastrophic risk) | Catastrophe modeling, tail risk, CLT |
| Renters Insurance | Personal property loss in rented housing | Location, property value, theft risk, lifestyle factors | Low frequency, low–moderate severity | Basic risk pooling, expected value |
| Disability Insurance | Income replacement due to inability to work | Occupation, health status, age, industry risk level | Low frequency, long duration payouts | Survival analysis, present value, long-term cash flow modeling |
| Liability Insurance | Legal responsibility for damages or injury | Industry type, business size, behavior risk, exposure level | Low frequency, potentially extreme severity | Tail risk modeling, extreme value theory |
| Travel Insurance | Trip cancellation, medical emergencies abroad | Destination risk, trip cost, traveler age, health | Low frequency, short-term events | Short-horizon probability models, conditional risk |
| Reinsurance | Insurance for insurance companies | Portfolio composition, catastrophe exposure, correlation of risks | Very low frequency, extremely high severity | Aggregation models, dependence structures, tail dependence |


--- PAGE ---

## Data, Modeling, and Technology

Modern insurance systems rely heavily on data science and computational methods to evaluate and manage risk. Instead of depending only on historical averages or broad population assumptions, insurers now use large datasets and predictive models to estimate risk at both the individual and portfolio level.

This shift allows insurance pricing and decision-making to become more responsive to observed behavior, rather than fixed long-term averages.

<br>

### Predictive Modeling and Machine Learning

Predictive models are used to estimate the probability that a future insurance event will occur based on observable characteristics of a policyholder or situation. In general, a predictive model takes a set of inputs (features) and produces an estimated outcome:

$$
\text{Inputs (features)} \rightarrow \text{Model} \rightarrow \text{Predicted probability or loss}
$$

Where:
- Inputs might include age, driving history, location, or health indicators  
- The model learns relationships between these inputs and past outcomes  
- The output is typically a probability of claim or an expected loss value  

Common modeling approaches include:
- Linear and logistic regression  
- Decision trees and ensemble methods  
- Neural networks and other machine learning models  

These tools allow insurers to move beyond broad group averages and toward more individualized estimates of risk.

<br>

### Claims Data Analysis

Claims data consists of historical records of insured events, including when they occurred, how often they occurred, and how severe the resulting losses were. This data forms the empirical foundation for most insurance models.

Some uses of claims data include:
- Estimating how frequently claims occur over time  
- Measuring the typical and extreme size of losses  
- Identifying patterns across different regions, time periods, or policy types  
- Improving the accuracy of pricing and reserve calculations  

In practice, claims databases are continuously updated, allowing models to be refined as new information becomes available.

<br>

### Risk Scoring Systems

Risk scoring is a practical method used in insurance to summarize many pieces of information about a person or policy into a single number that represents expected risk. This score is then used to help decide whether to insure someone and how much they should pay.

For example, an insurer might look at:
- Age of the policyholder  
- Driving history (for auto insurance)  
- Location (e.g., urban vs rural, weather risk)  
- Past claims history  
- Health indicators (for health or life insurance)  

Each of these factors contributes to the overall risk in a different way. Instead of evaluating them separately each time, insurers combine them into a single score.

A simplified way to represent this idea is:

$$
\text{Risk Score} = w_1x_1 + w_2x_2 + \cdots + w_nx_n
$$

Where:
- $x_1, x_2, \dots, x_n$ are measurable risk factors (such as age, driving violations, or location risk level)  
- $w_1, w_2, \dots, w_n$ are weights that represent how important each factor is in predicting risk  

In practice, higher weights are assigned to factors that have a stronger impact on the likelihood or cost of a claim. This type of structure makes risk scoring easier to interpret because it shows that the final score is built from a weighted combination of real-world variables, rather than an abstract black-box function.

<br>

### Poisson Distribution

The Poisson distribution is used to model the number of times an event occurs within a fixed period of time or space, especially when those events are rare and occur independently. It is commonly applied in insurance to represent counts of claims, such as the number of accidents per year or the number of claims filed by a policyholder. The probability of observing exactly $k$ events in a fixed interval is given by:

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

Where:
- $X$ is the number of events (e.g., claims)  
- $k$ is a specific number of observed events  
- $\lambda$ is the expected number of events in the interval  
- $e$ is the base of the natural logarithm  

In insurance applications, $\lambda$ represents the **average claim frequency** over the chosen time period. Applications include:
- Number of accidents per year for a driver or policyholder  
- Number of insurance claims filed within a portfolio  
- Modeling rare events such as natural disasters or system failures

<br>

### Stochastic Models in Insurance

Stochastic models describe systems that evolve over time with randomness built into the process. In insurance, this is necessary because events like claims or accidents do not occur in a perfectly predictable pattern, even if long-term averages are stable.

Instead of a single deterministic formula for what happens at time $t$, we describe a quantity that changes over time in a way that depends on random outcomes:

$$
X(t)
$$

In this context, $X(t)$ should be read as:
> “the value of a quantity after randomness has accumulated up to time $t$”

For example:
- $X(t)$ = total number of claims that have occurred by time $t$  
- $X(t)$ = total dollars paid out in claims by time $t$  
- $X(t)$ = number of active policies at time $t$

The important idea is that if you ran the system twice under the same conditions, you would not get the same $X(t)$. Instead, you would get different possible outcomes that follow a predictable statistical pattern.

Common stochastic models in insurance include:
- **Poisson processes** (counting how often events occur over time)  
- **Markov models** (systems that move between states such as healthy → sick → recovered)  
- **Continuous-time models** (for variables like interest rates that fluctuate continuously)

These models are used to study not just what is expected to happen, but how outcomes can vary under uncertainty.


--- PAGE ---

## How the Insurance Model Applies to Different Roles in the Industry

Insurance is often described as a single industry, but in practice it is a collection of specialized roles that each operate on different parts of the same underlying system. Every role is connected to the same core workflow: collect data, estimate risk, price uncertainty, manage contracts, and respond to claims. The difference is in where each job sits in that cycle and what tools are used to carry it out.

<br>

### Actuaries

Actuaries are responsible for translating uncertainty into financial estimates. Their primary focus is determining how much risk costs over time and ensuring that premiums are sufficient to cover future claims.

Core responsibilities:
- Estimating expected losses using historical data  
- Modeling claim frequency and severity  
- Building pricing models for insurance products  
- Calculating reserves for future liabilities  
- Stress-testing outcomes under extreme scenarios  

Mathematical tools used:
- Probability and statistics  
- Loss distributions  
- Poisson and frequency models  
- Survival models  
- Discounted cash flow methods  

Common tools used:
- Excel (especially for pricing and reserving work)  
- R and Python for statistical modeling  
- Actuarial software (e.g., AXIS, Prophet, Milliman tools)  

Actuaries sit at the center of the insurance model because they define the financial structure of risk.

<br>

### Underwriters

Underwriters decide whether an insurance company should accept a specific risk and under what conditions.

Core responsibilities:
- Evaluating applications for insurance coverage  
- Assessing individual or business-level risk  
- Adjusting premiums based on risk factors  
- Setting deductibles, exclusions, and coverage limits  
- Classifying policies into risk tiers  

Common tools used:
- Risk scoring systems  
- Rule-based underwriting platforms  
- Decision engines integrated into insurance systems  
- Basic statistical models and dashboards  

Underwriting is where theoretical risk models become enforceable contracts.

<br>

### Claims Adjusters

Claims adjusters handle the process of verifying and resolving insurance claims after a loss occurs.

Core responsibilities:
- Investigating reported claims  
- Verifying coverage and policy terms  
- Estimating the cost of damages or losses  
- Detecting fraud or inconsistencies  
- Approving or denying payouts  

Common tools used:
- Claims management systems  
- Image and document analysis tools  
- Fraud detection software  
- Rule-based evaluation systems  

Claims adjusters represent the cost-realization side of the insurance model.

<br>

### Data Scientists and Risk Modelers

Data scientists build predictive systems that support underwriting, pricing, and claims decisions.

Core responsibilities:
- Building models that predict claim probability and severity  
- Identifying risk factors in large datasets  
- Automating underwriting decisions  
- Detecting fraud patterns  
- Improving pricing accuracy through machine learning  

Mathematical tools used:
- Regression models  
- Classification models  
- Time-series models  
- Stochastic modeling techniques  

Common tools used:
- Python (pandas, scikit-learn, PyTorch)  
- SQL for data extraction  
- Cloud platforms (AWS, Snowflake, Databricks)  

Data scientists connect raw data directly to decision-making systems.

<br>

### Insurance Analysts

Insurance analysts focus on monitoring performance and helping decision-makers understand how the business is operating over time.

Core responsibilities:
- Tracking loss ratios and profitability  
- Analyzing claims trends  
- Monitoring portfolio performance  
- Supporting pricing and underwriting teams with reports  
- Identifying emerging risk patterns  

Key metrics:
- Loss ratio (claims ÷ premiums)  
- Combined ratio (claims + expenses ÷ premiums)  
- Frequency and severity trends  

Common tools used:
- Excel and dashboards (Power BI, Tableau)  
- SQL queries for reporting  
- Basic statistical analysis tools  

Analysts provide the feedback layer that connects operations to strategy.

<br>

### Insurance Operations and Systems Roles

Behind every insurance decision is a large technical system that stores data, processes transactions, and enforces rules.

Core responsibilities:
- Maintaining policy administration systems (PAS)  
- Managing claims processing infrastructure  
- Ensuring data integrity and compliance  
- Automating workflows across departments  
- Supporting integration between modeling and business systems  

Common tools used:
- Databases (SQL-based systems)  
- Cloud infrastructure (AWS, Azure, GCP)  
- API-based systems for integration  
- Workflow automation platforms  

These roles ensure that the insurance model functions reliably at scale.

<br>

### Unified View of Insurance Roles

Although these roles are different, they all operate on the same underlying structure:

- Actuaries define expected cost and uncertainty  
- Underwriters apply those models to individual decisions  
- Claims teams determine realized outcomes  
- Data scientists improve prediction and automation  
- Analysts monitor system performance  
- Operations teams maintain the infrastructure

Together, they form a continuous loop:

$$
\text{Data} \rightarrow \text{Modeling} \rightarrow \text{Pricing} \rightarrow \text{Contracts} \rightarrow \text{Claims} \rightarrow \text{New Data}
$$

Insurance is therefore not a single job or discipline, but a coordinated system where each role controls a different part of the same financial process.