<!--
title: "Math in Marketing"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/marketing_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Marketing
    </h1>
  </div>

</div>

<br>

###  What will I be doing?
- Analyzing consumer and behavioral data using SQL, Python, and analytics platforms  
- Running A/B tests and experimental designs to evaluate campaign performance  
- Building predictive models for customer segmentation, churn, and conversion rates  
- Using data visualization tools (e.g., Tableau, Power BI) to communicate marketing insights  
- Managing digital advertising platforms and tracking performance metrics (CTR, ROI, CAC)  
- Applying statistical analysis to evaluate market trends and consumer behavior  
- Interpreting large-scale customer data to optimize targeting and campaign strategy  


<br>

###  What are the most common jobs?
- Marketing Manager  
- Digital Marketer  
- Brand Strategist  
- Market Research Analyst  
- SEO Specialist  
- Content Marketer  
- Social Media Manager  
- Advertising Specialist  


<br>

###  What math concepts do I need to know?
- Statistics  
- Probability  
- Data Analysis  
- Algebra  
- Graphing and Trends  
- Percentages  
- A/B Testing  
- Optimization  
- Correlation and Regression  

--- PAGE ---

## Target Audience Segmentation

In marketing, **target audience segmentation** is the process of dividing a broad population of potential customers into smaller, more specific groups based on shared characteristics. The goal is to understand how different types of people think, behave, and make decisions so that messages, products, and strategies can be tailored more effectively.

Rather than treating “everyone” as a single market, segmentation recognizes that people respond differently depending on factors like age, income, interests, location, and psychological traits. This allows businesses to avoid generic messaging and instead create targeted strategies that are more likely to result in engagement and conversion.

At its core, segmentation is about reducing complexity. A large population can be modeled as a collection of subgroups, each with distinct needs and behaviors. For example, a fitness company might identify segments such as beginners looking for weight loss, athletes focused on performance, and older adults seeking low-impact exercise options. Each group requires a different approach.


<br>

###  Main Types of Segmentation

1. **Demographic Segmentation**  
   This divides audiences based on measurable population characteristics such as:
   - Age
   - Gender
   - Income level
   - Education
   - Occupation  
   
   Demographics are often the starting point because they are easy to measure and strongly correlate with purchasing behavior.

2. **Geographic Segmentation**  
   This organizes audiences based on location:
   - Country
   - Region or state
   - City
   - Climate zone  
   
   Geographic differences can influence needs significantly. For instance, winter clothing is marketed differently in colder climates than in tropical regions.

3. **Psychographic Segmentation**  
   This focuses on internal characteristics such as:
   - Lifestyle
   - Values
   - Interests
   - Personality traits  
   
   Psychographics help explain *why* people make decisions, not just who they are.

4. **Behavioral Segmentation**  
   This is based on how customers interact with a product or brand:
   - Purchase history
   - Brand loyalty
   - Usage frequency
   - Response to promotions  
   
   Behavioral data is especially powerful because it reflects actual actions rather than assumed traits.


--- PAGE ---

## Conversion Rates and Funnel Modeling

In marketing, **conversion rates** measure how effectively a group of potential customers moves from one stage of engagement to another, usually ending in a desired action such as a purchase, sign-up, or subscription. A **funnel model** is the structured representation of this process, showing how a large initial audience narrows step-by-step into a smaller group of converted users.

The term “funnel” is used because the structure typically narrows at each stage, much like a physical funnel. Many users enter at the top, but only a fraction reach the bottom where conversion occurs.


<br>

###  Basic Structure of a Marketing Funnel

A simplified funnel often includes:

1. **Awareness** – Users first become aware of a product or service.
2. **Interest** – Users show curiosity or engage with content.
3. **Consideration** – Users evaluate options and compare alternatives.
4. **Conversion** – Users complete a desired action (purchase, signup, etc.).

At each stage, some users drop off, which is why tracking conversion rates is essential for understanding performance.


<br>

###  Conversion Rate Definition

The **conversion rate** is the proportion of users who complete a desired action out of the total number of users at a given stage:

$$
CR = \frac{\text{Number of Conversions}}{\text{Total Users at Stage}}
$$

For example, if 200 people visit a landing page and 20 of them make a purchase, the conversion rate is:

$$
CR = \frac{20}{200} = 0.1 = 10\%
$$

This simple ratio allows marketers to quantify effectiveness at each step of the funnel.

<br>

###  Example Funnel Model

Suppose a funnel has the following structure:

- 10,000 users enter Awareness
- 4,000 move to Interest
- 1,200 move to Consideration
- 300 convert

We compute stage conversion rates:

- Awareness - Interest: $ \frac{4000}{10000} = 40\% $
- Interest - Consideration: $ \frac{1200}{4000} = 30\% $
- Consideration - Conversion: $ \frac{300}{1200} = 25\% $

Overall conversion:

$$
CR_{total} = \frac{300}{10000} = 3\%
$$

<br>

### Funnel KPIs and Practical Measurement

In real marketing systems, funnels are not only analyzed through probabilities, but through **observable performance metrics (KPIs)** that track user behavior at each stage. These metrics allow marketers to identify bottlenecks and optimize specific parts of the funnel.

<br>

### Impressions, Clicks, and CTR (Top of Funnel)

At the top of the funnel, exposure is measured using **impressions** and **click-through rate (CTR)**:

$$
CTR = \frac{\text{Clicks}}{\text{Impressions}}
$$

Where:
- Impressions = number of times content is shown
- Clicks = number of user interactions

CTR measures how effectively attention is converted into initial engagement.

<br>

### Click-to-Lead Conversion Rate

Once users click into a landing page or form, the next key metric is **lead conversion rate**:

$$
CVR_{lead} = \frac{\text{Leads Generated}}{\text{Clicks}}
$$

This captures how well traffic is being converted into identifiable interest (e.g., email signups, registrations).

<br>

### Lead-to-Customer Conversion Rate

A core funnel KPI is how many leads become paying customers:

$$
CVR_{sales} = \frac{\text{Customers}}{\text{Leads}}
$$

This is often the most important conversion metric for revenue-focused businesses.

<br>

### Overall Funnel Conversion Rate

The full funnel conversion is the product of stage conversions:

$$
CVR_{total} = \frac{\text{Customers}}{\text{Impressions}}
$$

Or equivalently:

$$
CVR_{total} = CTR \times CVR_{lead} \times CVR_{sales}
$$

This shows how each stage multiplicatively impacts final performance.

<br>

### Cost Per Funnel Stage

Funnel performance is often tied directly to cost efficiency:

#### Cost Per Click (CPC)

$$
CPC = \frac{\text{Ad Spend}}{\text{Clicks}}
$$

#### Cost Per Lead (CPL)

$$
CPL = \frac{\text{Ad Spend}}{\text{Leads}}
$$

#### Customer Acquisition Cost (CAC)

$$
CAC = \frac{\text{Ad Spend}}{\text{Customers}}
$$

These metrics map directly onto funnel stages:
- CPC - top-of-funnel efficiency
- CPL - mid-funnel efficiency
- CAC - bottom-funnel efficiency

<br>

### Revenue-Based Funnel Metrics

Funnels are ultimately evaluated in financial terms:

#### Revenue Per Visitor (RPV)

$$
RPV = \frac{\text{Total Revenue}}{\text{Total Visitors}}
$$

#### Average Order Value (AOV)

$$
AOV = \frac{\text{Revenue}}{\text{Number of Purchases}}
$$

#### Funnel Revenue Efficiency

$$
Funnel\ Efficiency = \frac{\text{Revenue}}{\text{Impressions}}
$$

This connects exposure directly to monetization.

<br>

### Drop-Off Rate by Stage

Each funnel stage has an associated loss rate:

$$
Dropoff_i = 1 - \frac{N_{i+1}}{N_i}
$$

Where:
- $N_i$ = users at stage i
- $N_{i+1}$ = users at next stage

This is one of the most actionable diagnostics in funnel optimization.

<br>

### Time-Based Funnel Metrics

Funnels also depend on timing, not just conversion:

#### Time to Convert (TTC)

$$
TTC = \text{Average time from first touch to conversion}
$$

#### Stage Duration

$$
T_i = \text{Average time spent in stage } i
$$

Shorter or longer durations can indicate:
- friction (too slow)
- low intent (too fast without conversion)

<br>

### Cohort Funnel Analysis

Instead of analyzing all users together, funnels are often evaluated by cohort:

$$
CR_{cohort} = \frac{\text{Conversions from cohort}}{\text{Cohort size}}
$$

This helps compare:
- acquisition channels
- campaign performance
- time-based user quality differences

<br>

### Funnel Efficiency Summary Metric

A combined efficiency metric can be expressed as:

$$
FE = CTR \times CVR_{lead} \times CVR_{sales} \times AOV
$$

This produces a single number that approximates how well attention becomes revenue.


--- PAGE ---

## A/B Testing and Experimental Design

**A/B testing** is a method in marketing used to compare two versions of a variable (A and B) to determine which performs better based on a defined metric, such as conversion rate, click-through rate, or engagement. It is a core tool in **experimental design**, where controlled comparisons are used to make data-driven decisions rather than relying on intuition.

At its core, A/B testing treats marketing as a measurable experiment: one group experiences version A (the control), while another group experiences version B (the treatment). The difference in outcomes is then analyzed to determine whether one version is statistically superior.


<br>

###  Basic Structure of an A/B Test

An A/B test typically involves:

1. **Population** – The full set of users being studied.
2. **Random Assignment** – Users are randomly split into two groups:
   - Group A (control)
   - Group B (variant)
3. **Intervention** – Each group is exposed to a different version of a marketing element.
4. **Outcome Measurement** – A metric is recorded for each group.
5. **Analysis** – The results are compared using statistical methods.

Random assignment is critical because it ensures that differences in outcomes are caused by the variation itself, not by pre-existing differences between users.


<br>

###  Conversion Rate Comparison

A common goal in A/B testing is comparing conversion rates between two groups:

$$
CR_A = \frac{\text{Conversions in A}}{\text{Users in A}}
$$

$$
CR_B = \frac{\text{Conversions in B}}{\text{Users in B}}
$$

The observed effect size is:

$$
\Delta = CR_B - CR_A
$$

If $\Delta > 0$, version B appears better; if $\Delta < 0$, version A performs better.

However, a difference alone is not enough—we must determine whether the difference is statistically significant.


<br>

###  Statistical Significance

To evaluate whether results are meaningful, A/B testing uses hypothesis testing:

- **Null hypothesis ($H_0$):** There is no difference between A and B.
- **Alternative hypothesis ($H_1$):** There is a difference between A and B.

A common test statistic for comparing proportions is based on a z-score:

$$
z = \frac{CR_B - CR_A}{\sqrt{p(1 - p)\left(\frac{1}{n_A} + \frac{1}{n_B}\right)}}
$$

where:
- $p$ is the pooled conversion rate
- $n_A, n_B$ are sample sizes

If the absolute value of $z$ exceeds a critical threshold (based on confidence level, e.g., 95%), we reject the null hypothesis.

<br>

###  Experimental Design Principles

Good A/B testing relies on several key principles:

1. **Randomization**  
   Ensures unbiased group assignment and reduces confounding variables.

2. **Control vs Treatment**  
   One group remains unchanged while the other receives a modification.

3. **Sample Size Adequacy**  
   Larger samples reduce variance and increase confidence in results.

4. **Isolation of Variables**  
   Only one element should change between A and B to ensure causality.

5. **Replicability**  
   Results should be consistent if the experiment is repeated.


<br>

###  Example Experiment

Suppose a company tests two versions of a landing page:

- Version A: current design
- Version B: new call-to-action button

Results:

- A: 5,000 users, 250 conversions - $CR_A = 5\%$
- B: 5,000 users, 300 conversions - $CR_B = 6\%$

Difference:

$$
\Delta = 1\%
$$

Even though B performs better, statistical testing is needed to determine whether this 1% increase is meaningful or could have occurred by chance.


<br>

###  P-Values and Decision Making

The **p-value** represents the probability of observing a result at least as extreme as the one obtained, assuming the null hypothesis is true.

- If $p < 0.05$, results are typically considered statistically significant.
- If $p \geq 0.05$, results are considered inconclusive.

This does not measure the size of the effect—only the likelihood that it is due to random variation.

<br>

### One-Proportion Z-Test (Single Variant Testing)

Used when comparing a variant against a known baseline:

$$
z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}
$$

Where:
- $\hat{p}$ = observed conversion rate  
- $p_0$ = baseline conversion rate  
- $n$ = sample size  

This is commonly used in pre/post marketing comparisons.

<br>

### T-Test for Continuous Metrics

When measuring non-binary outcomes (e.g., revenue per user), a t-test is used:

$$
t = \frac{\bar{x}_A - \bar{x}_B}{\sqrt{\frac{s_A^2}{n_A} + \frac{s_B^2}{n_B}}}
$$

Where:
- $\bar{x}$ = sample mean  
- $s^2$ = sample variance  
- $n$ = sample size  

This applies to metrics like:
- average order value
- revenue per user
- session duration

<br>

### Chi-Square Test for Contingency Tables

For categorical outcomes, A/B tests can be framed as:

$$
\chi^2 = \sum \frac{(O - E)^2}{E}
$$

Where:
- $O$ = observed frequency  
- $E$ = expected frequency  

This is useful when comparing multiple categories (e.g., click vs no click across multiple variants).

<br>

### Confidence Interval for Lift

A confidence interval for the difference in conversion rates:

$$
CI_{\Delta} = (p_B - p_A) \pm z \cdot \sqrt{\frac{p_A(1-p_A)}{n_A} + \frac{p_B(1-p_B)}{n_B}}
$$

This provides a range of plausible values for the true effect size.

<br>

### Relative Lift and Percentage Change

A common marketing metric is relative improvement:

$$
\text{Lift} = \frac{p_B - p_A}{p_A}
$$

or equivalently:

$$
\text{Lift} \% = \left(\frac{p_B}{p_A} - 1\right) \times 100
$$

This normalizes improvements relative to baseline performance.

<br>

### Minimum Detectable Effect (MDE)

A key experimental design constraint:

$$
MDE \approx z \cdot \sqrt{\frac{2p(1-p)}{n}}
$$

Rearranged for sample size:

$$
n \approx \frac{2p(1-p)z^2}{MDE^2}
$$

This shows that detecting smaller improvements requires exponentially more users.

<br>

### Statistical Power Function

Power is the probability of detecting a true effect:

$$
\text{Power} = \Phi\left(\frac{|\Delta|}{\sigma} - z_{\alpha}\right)
$$

Where:
- $\Phi$ = normal CDF  
- $\Delta$ = true effect size  
- $\sigma$ = standard error  
- $z_{\alpha}$ = significance threshold  

<br>

### Bayesian A/B Testing Update Rule

Using a Beta prior for conversion rates:

$$
p \sim \text{Beta}(\alpha, \beta)
$$

After observing:
- successes = $x$
- failures = $n - x$

Posterior becomes:

$$
\text{Beta}(\alpha + x, \beta + n - x)
$$

Probability that B is better than A:

$$
P(p_B > p_A)
$$

This replaces p-values with direct probability estimates.

<br>

### Sequential Testing

When running multiple tests, significance must be adjusted:

$$
\alpha' = \frac{\alpha}{k}
$$

Where:
- $k$ = number of simultaneous tests  

This prevents inflated false-positive rates.

<br>

### Expected Value of Experiment Outcome

A/B testing decisions can be framed as expected value:

$$
EV = (p_B - p_A) \cdot N \cdot V - C
$$

Where:
- $N$ = number of users affected  
- $V$ = value per conversion  
- $C$ = cost of implementing change  

This connects statistical significance directly to business impact.

<br>

### Conversion Rate Variance

Conversion rates follow a binomial distribution:

$$
Var(p) = \frac{p(1-p)}{n}
$$

This explains why small sample sizes produce unstable results.


--- PAGE ---

## Marketing Techniques

Marketing techniques refer to the set of structured methods used to influence consumer awareness, perception, and behavior in order to achieve specific business objectives such as acquisition, conversion, retention, and brand development. While these techniques vary widely in form—from data-driven digital systems to traditional broadcast advertising—they all operate on the same underlying principle: allocating attention and resources in a way that increases the probability of desired consumer action.

In practice, marketing is not a single strategy but a collection of interacting systems. Some techniques focus on generating attention, others on converting that attention into measurable outcomes, and others still on maintaining long-term customer relationships. Understanding these techniques in a unified framework allows us to analyze marketing not as isolated tactics, but as components of a broader optimization problem involving information, incentives, and human decision-making.

The table below summarizes the most commonly used marketing techniques, along with their primary goals, underlying logic, and key performance metrics.

<br>

| Technique | Primary Goal | Core Idea | Key Metric(s) |
|---|---|---|---|
| Search Engine Optimization (SEO) | Increase organic visibility | Rank content higher in search results through relevance + authority | Organic traffic, ranking position |
| Paid Search (SEM / PPC) | Immediate traffic acquisition | Pay for visibility in search results via bidding systems | Cost per click (CPC), conversion rate |
| Social Media Marketing | Attention + engagement | Use platform algorithms to distribute content | Engagement rate, reach |
| Content Marketing | Build trust and authority | Provide valuable information to attract users | Time on page, organic leads |
| Email Marketing | Customer retention + conversion | Direct messaging to known users | Open rate, click-through rate (CTR) |
| Influencer Marketing | Borrow audience trust | Use creators to transfer credibility | Engagement, conversion rate |
| Affiliate Marketing | Scalable sales | Pay partners per conversion | Cost per acquisition (CAC), ROI |
| Display Advertising | Awareness + retargeting | Visual ads across websites/apps | Impressions, CTR |
| A/B Testing | Optimize performance | Compare variants to measure causal impact | Conversion rate, statistical significance |
| Conversion Rate Optimization (CRO) | Improve funnel efficiency | Increase % of users who take action | Funnel conversion rates |
| Audience Segmentation | Improve targeting precision | Divide users into behavioral groups | Conversion rate by segment |
| Branding | Shape perception | Build emotional and identity-based value | Brand awareness, preference |
| Positioning Strategy | Differentiation | Define how product compares to competitors | Market share, perceived value |
| Pricing Strategy | Maximize revenue | Adjust price based on demand sensitivity | Revenue, elasticity |
| Discounting / Promotions | Short-term demand spikes | Temporarily lower price to increase volume | Sales lift, margin impact |
| Funnel Marketing | Guide user journey | Structured stages from awareness to purchase | Stage conversion rates |
| Retention Marketing | Increase lifetime value | Keep customers active longer | Churn rate, LTV |
| Loyalty Programs | Encourage repeat purchases | Reward continued engagement | Repeat purchase rate |
| Referral / Viral Marketing | Organic growth | Users bring in new users | Viral coefficient (K-factor) |
| Word-of-Mouth Marketing | Trust-based acquisition | Customers organically recommend product | Referral rate |
| Direct Sales | High-conversion deals | Human-to-human persuasion | Close rate, deal size |
| Cold Outreach | New customer acquisition | Unsolicited direct contact | Response rate, conversion rate |
| Traditional Advertising (TV/Print/Radio) | Broad awareness | Broadcast messaging to large audiences | Reach, brand lift |
| Outdoor Advertising (Billboards) | High-frequency exposure | Repeated visual impressions in physical space | Recall rate |
| Event Marketing | High engagement | Physical interaction with product/brand | Leads generated, engagement |
| Sponsorship Marketing | Brand association building | Attach brand to events/teams/creators | Brand lift, impressions |
| Market Positioning | Competitive differentiation | Define relative identity in market space | Market share, perception |
| Competitive Strategy | Market advantage | Respond to competitors structurally | Share of market, growth rate |