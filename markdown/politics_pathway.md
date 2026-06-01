<!--
title: "Math in Politics"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/politics_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Politics
    </h1>
  </div>

</div>

<br>

###  What will I be doing?
- Analyzing polling, demographic, and voting datasets using Excel, R, Python, SPSS, and SQL databases  
- Using GIS software such as ArcGIS and QGIS to study districts, voter distribution, gerrymandering, and regional political trends  
- Building forecasting and probability models using statistical tools to predict election outcomes and voter behavior  
- Managing campaign outreach and communication data using CRM platforms, voter databases, and analytics dashboards  
- Producing policy reports, statistical summaries, and visualizations using Tableau, Power BI, and presentation software  
- Interpreting economic, census, and public opinion datasets to guide campaign strategy, legislation, and policy decisions  


<br>

###  What are the most common jobs?
- Politician  
- Policy Analyst  
- Political Scientist  
- Legislative Assistant  
- Diplomat  
- Campaign Manager  
- Public Administrator  
- International Relations Specialist  


<br>

###  What math concepts do I need to know?
- Statistics  
- Probability  
- Data Analysis  
- Game Theory  
- Algebra  
- Graphing and Trends  
- Voting Systems  
- Optimization  
- Logic  


--- PAGE ---

## Voting Systems and Social Choice Theory

Voting systems and social choice theory study how individual preferences are combined into collective decisions. These systems attempt to transform many separate rankings, approvals, or votes into a single societal outcome, but mathematical analysis shows that this process can produce paradoxes, inconsistencies, and trade-offs between fairness criteria.

Social choice theory therefore examines both the structure of voting systems and the limitations of collective decision-making. It combines mathematics, political science, economics, and logic to analyze representation, strategic behavior, and the aggregation of preferences across populations.

Common goals of voting systems include:
- Representing voter preferences fairly
- Reducing strategic manipulation
- Producing stable collective outcomes
- Preserving majority rule
- Avoiding dictatorial control

<br>

### Preference Aggregation

Preference aggregation refers to the process of combining individual rankings or choices into a collective decision.

For a voting population:

$$
P = \{p_1, p_2, p_3, \dots , p_n\}
$$

Where:
- $P$ = set of voter preferences
- $p_i$ = preference ordering of voter $i$

A social choice function maps these individual preferences into a final outcome:

$$
F(P) \rightarrow O
$$

Where:
- $F$ = aggregation rule or voting system
- $O$ = collective outcome

Different voting systems define $F$ differently, leading to different election results even when voter preferences remain unchanged.

<br>

### Ranked-Choice Voting

Ranked-choice voting (RCV) allows voters to rank candidates in order of preference rather than selecting only one option.

If no candidate receives a majority of first-choice votes:
- The candidate with the fewest votes is eliminated
- Votes are redistributed according to next-ranked preferences
- The process repeats until a majority winner emerges

RCV attempts to:
- Reduce vote splitting
- Encourage broader candidate support
- Reduce incentives for strategic “lesser evil” voting

However, outcomes may still depend on elimination order and voter distribution.

<br>

### Approval Voting

Approval voting allows voters to approve of as many candidates as they wish.

The winning candidate maximizes total approvals:

$$
A_i = \sum_{k=1}^{n} a_{ik}
$$

Where:
- $A_i$ = total approvals for candidate $i$
- $a_{ik} \in \{0,1\}$ = approval from voter $k$

This system:
- Simplifies voting strategy
- Encourages compromise candidates
- Reduces vote splitting

but may also incentivize tactical approval behavior.

<br>


### Median Voter Theorem

The Median Voter Theorem states that in a one-dimensional ideological space, the candidate or policy closest to the median voter will win under majority rule, assuming voters vote sincerely.

Let voter ideal points be ordered along a line:

$$
x_1 \leq x_2 \leq \cdots \leq x_n
$$

The median voter is:

$$
x_m
$$

Under standard assumptions, equilibrium policy converges toward $x_m$.

This result implies:
- Political competition tends toward moderation
- Extreme positions are disadvantaged in simple majority systems
- Policy outcomes reflect central voter preferences

<br>

### Condorcet Voting Systems

A Condorcet voting system selects the candidate who would defeat every other candidate in pairwise head-to-head comparisons.

For candidates $A$ and $B$:

$$
A \succ B
$$

means a majority prefers $A$ over $B$.

A Condorcet winner satisfies:

$$
A \succ B,\quad A \succ C,\quad A \succ D,\dots
$$

against all competitors.

Condorcet systems attempt to identify the strongest majority-supported candidate, though a Condorcet winner does not always exist.

<br>

### Condorcet Paradox

The Condorcet paradox demonstrates that collective preferences can become cyclic even when individual voter preferences are internally consistent.

Example:

- Majority prefers $A$ over $B$
- Majority prefers $B$ over $C$
- Majority prefers $C$ over $A$

This creates a cycle:

$$
A \succ B \succ C \succ A
$$

meaning no stable majority ordering exists.

The paradox reveals that majority voting can produce logically inconsistent societal preferences even when every voter behaves rationally individually.

<br>

### Arrow’s Impossibility Theorem

Arrow’s Impossibility Theorem is one of the foundational results in social choice theory. It states that no ranked voting system can simultaneously satisfy all major fairness criteria once three or more options exist.

Arrow showed that no system can satisfy all of the following simultaneously:
- Non-dictatorship
- Pareto efficiency
- Independence of irrelevant alternatives
- Universal admissibility
- Transitive collective preferences

Symbolically:

$$
\text{No voting system satisfies all fairness axioms simultaneously}
$$

This theorem demonstrates that every voting system involves trade-offs between competing definitions of fairness.

<br>

### Fairness Criteria in Elections

Voting systems are often evaluated according to formal fairness criteria.

Common criteria include:

- **Majority Criterion**  
  A candidate preferred by a majority should win.

- **Condorcet Criterion**  
  A candidate who defeats all others head-to-head should win.

- **Monotonicity Criterion**  
  Ranking a candidate higher should not harm their chances of winning.

- **Independence of Irrelevant Alternatives (IIA)**  
  The relative ranking between two candidates should not depend on unrelated alternatives.

- **Non-Dictatorship**  
  No single voter should determine all outcomes regardless of others.

Because many fairness conditions conflict mathematically, electoral systems must balance competing priorities rather than satisfy all criteria perfectly.

<br>

### Strategic Voting and System Design

Many voting systems create incentives for strategic behavior, where voters do not vote honestly according to true preference.

Examples include:
- Tactical voting
- Vote splitting
- Bullet voting
- Coalition coordination

Strategic effects are studied using:
- Game theory
- Utility models
- Equilibrium analysis
- Behavioral simulations

As a result, election system design is not purely procedural but also mathematical, behavioral, and strategic.


--- PAGE ---

## Electoral Systems and Representation

Electoral systems determine how votes are translated into political representation. Different systems distribute political power in different ways, influencing party structure, coalition formation, voter behavior, and legislative outcomes. Because representation depends heavily on mathematical allocation rules, electoral systems are closely connected to statistics, optimization, and social choice theory.

Electoral systems attempt to balance competing goals such as:
- Fair representation
- Government stability
- Simplicity of voting
- Geographic representation
- Majority rule
- Minority inclusion

Different systems prioritize these goals differently, which can significantly alter political outcomes even when the underlying vote totals remain unchanged.

<br>

### Proportional Representation

Proportional representation (PR) systems allocate legislative seats approximately in proportion to the percentage of votes received by each party.

A simplified proportional allocation is:

$$
S_i \approx \frac{V_i}{V_T} \times S_T
$$

Where:
- $S_i$ = seats allocated to party $i$
- $V_i$ = votes received by party $i$
- $V_T$ = total votes cast
- $S_T$ = total available seats

PR systems tend to:
- Increase representation of smaller parties
- Encourage coalition governments
- Reduce disproportional outcomes

However, highly proportional systems may also produce fragmented legislatures with many competing parties.

<br>

### Plurality and Majority Systems

Plurality systems award victory to the candidate with the greatest number of votes, even without an absolute majority.

For candidate vote totals:

$$
V_A > V_B, V_C, V_D, \dots
$$

candidate $A$ wins under plurality rules.

Majority systems instead require:

$$
V_A > \frac{1}{2}V_T
$$

meaning the winning candidate must receive more than 50% of all votes cast.

Plurality systems:
- Are simple and fast
- Often favor larger parties
- Can produce vote splitting

Majority systems:
- Increase winner legitimacy
- Often require runoff elections or ranked-choice redistribution
- Reduce minority-rule outcomes

<br>

### Duverger’s Law

Duverger’s Law states that plurality voting systems tend to favor two-party political structures.

Symbolically:

$$
\text{Plurality systems} \rightarrow \text{two-party equilibrium}
$$

This occurs because:
- Voters avoid “wasting” votes on smaller parties
- Smaller parties struggle to win geographically concentrated districts
- Strategic voting incentivizes consolidation

In contrast, proportional systems often support multi-party competition because smaller vote shares can still produce representation.

<br>

### Gerrymandering Metrics

Gerrymandering refers to the manipulation of electoral district boundaries to favor particular political groups.

One commonly used metric is the efficiency gap:

$$
EG = \frac{W_A - W_B}{V_T}
$$

Where:
- $EG$ = efficiency gap
- $W_A, W_B$ = wasted votes for each party
- $V_T$ = total votes cast

Wasted votes include:
- Votes beyond what was needed to win
- Votes cast for losing candidates

Large efficiency gaps may indicate systematic representational imbalance.

Other districting measures examine:
- Compactness
- Geographic continuity
- Population equality
- Partisan asymmetry

<br>

### Electoral District Modeling

Electoral district modeling studies how geographic boundaries influence political representation.

District systems attempt to satisfy:
- Equal population distribution
- Geographic coherence
- Legal representation requirements
- Community preservation

Population equality is often modeled as:

$$
D_i \approx \frac{P_T}{N}
$$

Where:
- $D_i$ = district population
- $P_T$ = total population
- $N$ = number of districts

District design strongly influences:
- Electoral competitiveness
- Minority representation
- Party advantage
- Voter influence

Because district boundaries alter representation mathematically, districting is both a political and computational optimization problem.

<br>

### Apportionment Methods

Apportionment methods determine how legislative seats are distributed among states, regions, or parties when representation must remain discrete.

Because seats cannot be divided fractionally, allocation systems must approximate proportional fairness.

<br>

#### Hamilton Method

The Hamilton method:
1. Assigns each group its lower quota
2. Distributes remaining seats according to largest fractional remainders

Quota is calculated as:

$$
Q_i = \frac{P_i}{P_T}S
$$

Where:
- $Q_i$ = quota for group $i$
- $P_i$ = population or vote total
- $P_T$ = total population or votes
- $S$ = total seats available

<br>

#### Jefferson Method

The Jefferson method uses a divisor system with downward rounding:

$$
Q_i = \left\lfloor \frac{P_i}{d} \right\rfloor
$$

Where:
- $d$ = adjusted divisor
- $\lfloor x \rfloor$ = floor function

Jefferson’s method tends to slightly favor larger populations or parties.

<br>

#### Huntington–Hill Method

The Huntington–Hill method uses geometric mean thresholds to determine seat assignment.

A seat is awarded when:

$$
P > \sqrt{n(n+1)}
$$

Where:
- $P$ = priority value
- $n$ = current seat count

This method is currently used for apportioning seats in the United States House of Representatives.

<br>

### Electoral College Systems

Electoral college systems use indirect voting structures in which electors formally select political leaders on behalf of voters.

A simplified representation is:

$$
E_i = H_i + S_i
$$

Where:
- $E_i$ = electoral votes for state $i$
- $H_i$ = number of representatives
- $S_i$ = number of senators

Electoral college systems:
- Combine population and regional representation
- Emphasize state-level outcomes
- Can produce outcomes differing from the national popular vote

This creates strategic emphasis on competitive regions often called “swing states.”

<br>

### Weighted Voting Systems

Weighted voting systems assign different voting strengths to different participants.

Total voting influence can be modeled as:

$$
W = \sum_{i=1}^{n} w_i
$$

Where:
- $w_i$ = voting weight of participant $i$

A proposal passes when:

$$
\sum w_i \geq q
$$

Where:
- $q$ = required quota or threshold

Weighted voting systems are used in:
- Federal systems
- International organizations
- Corporate governance
- Legislative coalitions

Importantly, voting weight does not always equal actual political power, which motivates the study of power indices such as the Banzhaf and Shapley–Shubik indices.


--- PAGE ---

## Political Statistics and Forecasting

Political statistics and forecasting use probability, statistical inference, and computational modeling to estimate political behavior and predict electoral outcomes. Because elections involve uncertainty, incomplete information, and changing human behavior, forecasting systems rely on both mathematical models and continuously updated observational data.

Modern political forecasting combines:
- Polling data
- Demographic analysis
- Historical voting patterns
- Economic indicators
- Geographic trends
- Behavioral modeling

These methods are used to estimate:
- Election outcomes
- Voter preferences
- Turnout rates
- Party support shifts
- Electoral uncertainty

<br>

### Polling Methodology

Polling attempts to estimate the preferences of an entire population using a smaller sample.

If:
- $n$ = sample size
- $\hat{p}$ = observed support proportion

then the estimated support level is:

$$
\hat{p} = \frac{x}{n}
$$

Where:
- $x$ = number of respondents supporting a candidate or issue

Poll accuracy depends on:
- Sample representativeness
- Randomization quality
- Response rates
- Survey wording
- Timing of data collection

Because only a subset of voters is surveyed, all polls contain uncertainty.

<br>

### Margin of Error

The margin of error estimates the expected sampling uncertainty in polling results.

A common approximation is:

$$
MOE \approx z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

Where:
- $MOE$ = margin of error
- $z$ = confidence multiplier
- $\hat{p}$ = estimated proportion
- $n$ = sample size

Larger samples generally reduce uncertainty because:

$$
MOE \propto \frac{1}{\sqrt{n}}
$$

A smaller margin of error indicates greater statistical precision, though it does not account for systematic polling errors.

<br>

### Sampling Bias

Sampling bias occurs when surveyed respondents do not accurately represent the target population.

Bias may arise from:
- Undercoverage of demographic groups
- Nonresponse effects
- Selection bias
- Survey access limitations
- Timing effects

If:
- $\mu_s$ = sample mean
- $\mu_p$ = true population mean

then sampling bias is:

$$
\text{Bias} = \mu_s - \mu_p
$$

Even very large polls can produce inaccurate forecasts if systematic biases remain uncorrected.

<br>

### Regression Analysis

Regression models estimate relationships between political variables and electoral outcomes.

A simple linear regression model is:

$$
y = \beta_0 + \beta_1 x + \epsilon
$$

Where:
- $y$ = predicted outcome
- $x$ = explanatory variable
- $\beta_0$ = intercept
- $\beta_1$ = regression coefficient
- $\epsilon$ = random error

Political forecasting commonly uses regression to study:
- Economic effects on elections
- Demographic voting trends
- Geographic voting behavior
- Approval rating impacts
- Policy preference relationships

More advanced models may involve multiple interacting variables simultaneously.

<br>

### Monte Carlo Election Simulation

Monte Carlo simulations estimate election outcomes by repeatedly sampling from probabilistic models.

A simplified expectation estimate is:

$$
E(X) \approx \frac{1}{N}\sum_{i=1}^{N} x_i
$$

Where:
- $N$ = number of simulations
- $x_i$ = outcome of simulation $i$

Forecast systems may run:
- Thousands of simulations
- State-by-state probability sampling
- Correlated polling error models
- Turnout variability scenarios

Simulation outputs estimate:
- Win probabilities
- Electoral vote distributions
- Outcome uncertainty
- Rare but possible scenarios

<br>

### Markov Transition Models

Markov models describe systems that transition probabilistically between states over time.

A transition matrix is:

$$
P =
\begin{bmatrix}
p_{11} & p_{12} \\
p_{21} & p_{22}
\end{bmatrix}
$$

Where:
- $p_{ij}$ = probability of moving from state $i$ to state $j$

Political applications include:
- Party-switching behavior
- Opinion evolution
- Voter alignment changes
- Legislative coalition transitions

Markov models assume future states depend primarily on the current state rather than the full historical path.

<br>

### Demographic Weighting

Demographic weighting adjusts polling samples to better reflect population structure.

Weighted estimates are computed as:

$$
\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}
$$

Where:
- $w_i$ = weight assigned to respondent $i$
- $x_i$ = response value

Weighting attempts to correct for:
- Age imbalance
- Geographic imbalance
- Education effects
- Race and ethnicity representation
- Gender representation

Without weighting, polling samples may systematically misrepresent actual electorates.

<br>

### Voter Turnout Models

Turnout models estimate which eligible voters are likely to participate in an election.

Turnout probability may be represented as:

$$
P(T=1|X)
$$

Where:
- $T=1$ indicates voting participation
- $X$ represents demographic or behavioral variables

Factors affecting turnout include:
- Age
- Education
- Income
- Political engagement
- Registration status
- Election competitiveness

Forecasting turnout is critical because:
- Polling accuracy depends on likely voters
- Different demographic groups vote at different rates
- Small turnout shifts can change election outcomes

Modern turnout models often combine:
- Historical voting records
- Survey data
- Behavioral prediction models
- Machine learning techniques

to estimate electoral participation probabilities across populations.


--- PAGE ---

## Game Theory and Political Strategy

Game theory in political science analyzes how rational actors make strategic decisions when outcomes depend not only on their own choices but also on the choices of others. Political environments often involve competition, cooperation, negotiation, and deterrence, making game-theoretic models especially useful for understanding elections, legislative behavior, diplomacy, and coalition formation.

These models assume that political actors:
- Have defined preferences
- Make decisions strategically
- Respond to incentives and constraints
- Anticipate the behavior of others

The result is a framework for predicting equilibrium behavior in complex strategic environments.

<br>

### Prisoner’s Dilemma

The Prisoner’s Dilemma models situations where individually rational choices lead to collectively suboptimal outcomes.

A typical payoff structure is:

$$
T > R > P > S
$$

Where:
- $T$ = temptation payoff (defecting while other cooperates)
- $R$ = reward for mutual cooperation
- $P$ = punishment for mutual defection
- $S$ = sucker’s payoff

The key insight is that:
- Both players defecting is a Nash equilibrium
- Mutual cooperation yields a better collective outcome
- Rational self-interest can produce suboptimal social results

In political contexts, this appears in:
- Arms races
- Legislative gridlock
- International agreements
- Tax compliance behavior

<br>

### Nash Equilibrium

A Nash equilibrium occurs when no player can improve their outcome by unilaterally changing strategy. Formally, a strategy profile $(s_1, s_2, ..., s_n)$ is a Nash equilibrium if:

$$
u_i(s_i, s_{-i}) \geq u_i(s'_i, s_{-i})
$$

for all players $i$ and all alternative strategies $s'_i$.

Where:
- $u_i$ = utility of player $i$
- $s_{-i}$ = strategies of all other players

In political systems, Nash equilibria help explain:
- Stable voting blocs
- Party competition strategies
- Legislative bargaining outcomes
- Campaign positioning

<br>

### Bargaining Theory

Bargaining theory models how actors divide resources or reach agreements under negotiation. A common representation is:

$$
x_1 + x_2 = 1
$$

Where:
- $x_1, x_2$ = shares allocated to each player

Outcomes depend on:
- Relative bargaining power
- Outside options
- Time preferences
- Information asymmetry

In politics, bargaining appears in:
- Coalition governments
- Budget negotiations
- Treaty formation
- Legislative compromise

Stronger bargaining positions typically lead to more favorable allocations, though outcomes are constrained by mutual agreement requirements.

<br>

### Coordination Games

Coordination games occur when players benefit from making the same choices or aligning strategies. A simple coordination structure is:

|  | Player 2: Choice A | Player 2: Choice B |
|---|---|---|
| Player 1: Choice A | (2,2) | (0,0) |
| Player 1: Choice B | (0,0) | (1,1) |

Multiple equilibria may exist, and the challenge becomes selecting a shared outcome. Political examples include:

- Party alignment
- Policy standardization
- Electoral coalition formation
- International treaty compliance

Coordination failures can lead to inefficiency even when cooperation is mutually beneficial.

<br>

### Deterrence Theory

Deterrence theory explains how threats and incentives prevent unwanted actions by increasing their expected cost. A simplified deterrence condition is:

$$
\text{Cost of action} > \text{Expected benefit}
$$

Where expected cost may include:
- Probability of punishment
- Severity of punishment
- Political or economic retaliation

In political science, deterrence is central to:
- Military strategy
- Law enforcement policy
- International relations
- Regulatory compliance

Credibility is essential: threats only deter behavior if they are believed.

<br>

### Rational Choice Theory

Rational choice theory assumes that individuals act to maximize utility subject to constraints.

Formally:

$$
\max U(x)
$$

Subject to:
- Resource constraints
- Institutional constraints
- Information limitations

Where:
- $U(x)$ = utility derived from outcome $x$

In politics, this framework is used to model:
- Voting behavior
- Candidate strategy
- Legislative decision-making
- Policy preferences

While powerful, the model depends on assumptions about rationality that may not always hold in real-world behavior.

<br>

### Strategic Voting

Strategic voting occurs when voters choose a candidate other than their top preference to influence the outcome more effectively.

This arises when:

$$
\text{Expected utility of honest vote} < \text{Expected utility of strategic vote}
$$

Common forms include:
- Voting for a less-preferred but viable candidate
- Avoiding “wasted” votes
- Coordinating against undesirable outcomes

Strategic voting is especially prominent in:
- Plurality systems
- Closely contested elections
- Multi-candidate races

It can significantly alter election outcomes relative to sincere preference aggregation.

<br>

### Coalition Formation Models

Coalition formation models study how groups of actors form alliances to achieve collective goals.

A coalition $C$ is a subset of players:

$$
C \subseteq N
$$

Where:
- $N$ = set of all actors

Coalitions form based on:
- Shared interests
- Minimum winning size
- Power distribution
- Payoff allocation rules

Key concepts include:
- Stability (no incentive to defect)
- Minimal winning coalitions
- Superadditive payoffs

In political systems, coalition models explain:
- Parliamentary government formation
- Legislative voting blocs
- International alliances
- Party mergers and splits

Coalition stability often depends on whether members receive sufficient payoff relative to outside alternatives.


--- PAGE ---

## Power, Influence, and Coalition Analysis

Power and influence in political systems are not determined solely by the number of votes or seats an actor holds, but by how critical that actor is to forming winning coalitions. Coalition analysis uses mathematical tools from game theory and combinatorics to measure how influence is distributed among participants in weighted voting systems and legislative bodies.

These models help explain:
- Why small actors can have disproportionate influence
- How coalitions form and dissolve
- How legislative bargaining power is distributed
- Why nominal voting weight does not always equal actual power

<br>

### Coalition Power Analysis

A coalition is any subset of players that can jointly achieve a winning outcome.

Formally, for a set of players $N$:

$$
C \subseteq N
$$

A coalition is considered winning if it meets or exceeds a threshold:

$$
\sum_{i \in C} w_i \geq q
$$

Where:
- $w_i$ = weight of player $i$
- $q$ = required quota for victory

Coalition power analysis studies how often each player is essential to winning coalitions and how their presence changes outcomes.

<br>

### Banzhaf Power Index

The Banzhaf power index measures how often a player is pivotal in turning a losing coalition into a winning one.

A player is pivotal if:

$$
\sum w_i < q \quad \text{but} \quad \sum w_i + w_j \geq q
$$

Where:
- $w_j$ = weight of the player being tested

The normalized Banzhaf index is:

$$
\beta_j = \frac{\phi_j}{\sum_{k=1}^{n} \phi_k}
$$

Where:
- $\phi_j$ = number of coalitions where player $j$ is pivotal

This measure captures:
- Voting power beyond formal weight
- Marginal influence in coalition formation
- Sensitivity of outcomes to individual actors

<br>

### Shapley–Shubik Power Index

The Shapley–Shubik index measures power by considering all possible orderings of players and identifying who is pivotal in each ordering. For a permutation of players, a player is pivotal if they are the first to cause a coalition to become winning. The index is:

$$
\phi_i = \frac{\text{number of permutations where } i \text{ is pivotal}}{n!}
$$

Where:
- $n!$ = total number of possible orderings

This approach reflects:
- Sequential bargaining power
- Order-dependent influence
- Expected marginal contribution

Unlike the Banzhaf index, it incorporates ordering effects in coalition formation.

<br>

### Minimal Winning Coalitions

A minimal winning coalition is a coalition that is winning, but would become losing if any single member left.

Formally:

$$
\sum_{i \in C} w_i \geq q \quad \text{and} \quad \forall j \in C: \sum_{i \in C \setminus \{j\}} w_i < q
$$

Where:
- $C$ = coalition
- $q$ = winning threshold

Minimal winning coalitions are important because:
- Every member is critical
- They minimize “excess” power
- They are often stable bargaining structures

In political systems, actors prefer minimal winning coalitions to maximize efficiency while minimizing unnecessary partners.

<br>

### Legislative Influence Models

Legislative influence models study how power operates within decision-making bodies such as parliaments or councils.

Influence depends on:
- Voting weight
- Coalition positioning
- Agenda-setting power
- Negotiation leverage

A simplified influence representation is:

$$
I_i = f(w_i, C_i, A_i)
$$

Where:
- $I_i$ = influence of actor $i$
- $w_i$ = voting weight
- $C_i$ = coalition position
- $A_i$ = agenda control capacity

These models highlight that formal voting weight alone does not fully determine political power.

<br>

### Power Distribution in Legislative Systems

Power distribution in legislative systems describes how influence is spread across parties, factions, or individuals.

Key observations include:
- Majority groups may still rely on minority coalitions
- Small parties can hold “kingmaker” positions
- Bicameral systems distribute power asymmetrically
- Committee structures concentrate influence

Power is often non-linear with respect to seat share:

$$
\text{Power} \neq \text{Seat Proportion}
$$

This mismatch motivates the study of power indices and coalition stability.

Understanding power distribution is essential for analyzing:
- Coalition governments
- Legislative bargaining outcomes
- Policy formation processes
- Institutional design efficiency


--- PAGE ---

## Public Policy and Collective Action

Public policy and collective action theory examine how individuals and institutions make decisions regarding shared resources, public goods, and collective outcomes. These frameworks focus on the tension between individual incentives and group efficiency, especially in situations where rational individual behavior can lead to socially suboptimal results.

Key questions include:
- How should public resources be allocated?
- Why do collective inefficiencies emerge?
- How can incentives be structured to improve outcomes?
- How do institutions align individual and social objectives?

<br>

### Public Choice Theory

Public choice theory is the study of how political decisions are made when individuals within a system—such as voters, politicians, and bureaucrats—are assumed to act based on incentives rather than purely collective welfare. It treats political outcomes as the result of many individual decisions interacting under institutional constraints.

This framework is used to explain how different institutional structures can lead to different policy outcomes, even when the underlying preferences of individuals remain unchanged.

<br>

### Collective Action Problems

Collective action problems describe situations where a group would benefit from cooperation, but individuals have incentives to act in their own self-interest instead. Even when everyone would be better off if they coordinated, lack of trust, enforcement, or communication can prevent cooperation from forming.

These problems are central to understanding why certain socially beneficial outcomes—such as shared funding, regulation, or coordinated behavior—are difficult to achieve without formal institutions or rules.

<br>

### Free-Rider Problem

The free-rider problem is a specific type of collective action problem that occurs when individuals benefit from a shared resource or public good without contributing to its cost. Because the good is still available regardless of individual contribution, rational actors may choose not to participate, expecting others to bear the burden.

This leads to under-provision of the good, since total voluntary contributions are often lower than what is socially optimal.

<br>

### Pareto Efficiency

A state is Pareto efficient if it is impossible to improve the well-being of one individual without making at least one other individual worse off.

Formally:

$$
\not\exists \; x' \text{ such that } U_i(x') \geq U_i(x) \; \forall i \text{ and } U_j(x') > U_j(x) \text{ for some } j
$$

Where:
- $x$ = current allocation
- $x'$ = alternative allocation
- $U_i(x)$ = utility of individual $i$ under allocation $x$

This concept does not imply that the outcome is fair or equitable—only that no further mutually beneficial improvements are possible given the current distribution.

<br>

### Cost–Benefit Analysis

Cost–benefit analysis is a decision-making framework used to evaluate whether a policy or action produces more total benefits than costs. It involves comparing all expected positive outcomes against all expected negative outcomes, often expressed in monetary or standardized units.

If the total benefits outweigh the total costs, the policy is considered economically justified within the model. This approach is widely used in public policy, infrastructure planning, and regulatory decision-making.

<br>

### Resource Allocation

Resource allocation refers to the process of distributing limited resources among competing needs or groups. Because resources are finite, decisions must be made about how to divide them in a way that balances efficiency, fairness, and practical constraints.

In political systems, resource allocation often involves trade-offs between competing social goals, such as maximizing total welfare, ensuring equitable distribution, or satisfying political priorities.

<br>

### Principal–Agent Problem

The principal–agent problem occurs when one party (the principal) delegates decision-making authority to another party (the agent), but their interests are not perfectly aligned. Since the agent makes decisions on behalf of the principal, differences in incentives can lead to outcomes that do not fully reflect the principal’s goals.

This problem is common in political systems where voters delegate authority to elected officials, and it can be difficult to fully monitor or control the actions of those in power.

<br>

### Public Goods and Incentive Systems

Public goods are goods or services that can be consumed by multiple individuals without reducing availability for others, and from which it is difficult to exclude non-payers. Because of these characteristics, they are often underprovided in markets without collective funding mechanisms.

Incentive systems are therefore designed to encourage contribution and ensure that public goods are produced at socially desirable levels, often through taxation, regulation, or institutional enforcement.