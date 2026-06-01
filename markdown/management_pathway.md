<!--
title: "Math in Management"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/management_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Management
    </h1>
  </div>

</div>

<br>

###  What will I be doing?
- Analyzing business performance data using Excel, SQL, and business intelligence tools  
- Building financial and operational models to forecast revenue, costs, and efficiency  
- Using project management software (e.g., Jira, Asana, Microsoft Project) to coordinate workflows  
- Interpreting KPIs and performance metrics to guide decision-making  
- Optimizing resource allocation and operational processes across teams and departments  
- Applying risk analysis and scenario modeling to support strategic planning  
- Communicating data-driven insights to stakeholders and executive leadership  


<br>

###  What are the most common jobs?
- General Manager  
- Operations Manager  
- Project Manager  
- Business Manager  
- Human Resources Manager  
- Supply Chain Manager  
- Financial Manager  
- Administrative Manager  


<br>

###  What math concepts do I need to know?
- Statistics  
- Data Analysis  
- Algebra  
- Financial Mathematics  
- Optimization  
- Graphing and Trends  
- Probability  
- Budgeting Calculations  
- Linear Programming  


--- PAGE ---

## Revenue, Costs, and Profit Modeling

In management and business decision-making, understanding how revenue, costs, and profit interact is essential for evaluating performance, pricing strategies, and long-term sustainability. Mathematical modeling provides a structured way to describe these relationships and make informed predictions about business outcomes.

At its core, a business is governed by three key quantities:

- **Revenue (R):** The total income generated from selling goods or services  
- **Cost (C):** The total expense incurred in producing and selling those goods or services  
- **Profit (P):** The financial gain after subtracting costs from revenue  

These relationships can be expressed mathematically to analyze business performance under different conditions.

<br>

### Revenue Modeling

Revenue is typically modeled as the product of price and quantity sold:

$$
R(q)=pq
$$

Where:
- $p$ = price per unit
- $q$ = quantity of units sold

This simple model shows that revenue increases either by selling more units or by increasing the price, though in real-world scenarios these two factors often influence each other.

<br>

### Cost Modeling

Costs are usually divided into two categories:

1. **Fixed Costs (F):** Costs that do not change with production level (e.g., rent, salaries, equipment)
2. **Variable Costs:** Costs that change depending on output (e.g., materials, shipping, labor per unit)

A common linear cost model is:

$$
C(q)=F+vq
$$

Where:
- $F$ = fixed cost
- $v$ = variable cost per unit
- $q$ = quantity produced

This model shows that total cost increases as production increases, but fixed costs remain constant regardless of output.

<br>

### Profit Modeling

Profit is defined as the difference between revenue and cost:

$$
P(q)=R(q)-C(q)
$$

Substituting the basic models gives:

$$
P(q)=pq-(F+vq)
$$

This can be simplified to:

$$
P(q)=(p-v)q-F
$$

This equation is especially important in management because it shows how profit depends on:
- The margin between price and variable cost ($p-v$)
- The scale of production ($q$)
- The burden of fixed costs ($F$)

<br>

### Break-Even Analysis

The break-even point occurs when profit equals zero:

$$
R(q)=C(q)
$$

Substituting the models:

$$
pq=F+vq
$$

Solving for $q$:

$$
q=\frac{F}{p-v}
$$

This value represents the minimum number of units that must be sold to cover all costs. Any sales beyond this point result in profit, while anything below results in a loss.

--- PAGE ---

## Fixed Costs vs Variable Costs

In management and business operations, costs are commonly divided into two major categories: **fixed costs** and **variable costs**. Understanding the difference between these two is essential for pricing decisions, budgeting, and predicting how profit changes as production levels change.

This distinction is important because not all costs behave the same way when a business scales up or down. Some costs remain constant regardless of output, while others change directly with production.


<br>

###  Fixed Costs

**Fixed costs** are expenses that remain constant over a given time period, regardless of how much a business produces or sells.

Examples include:
- Rent or lease payments
- Salaries of permanent staff
- Insurance premiums
- Equipment purchases (often treated as fixed over time)
- Property taxes

Mathematically, fixed costs are represented as a constant:

$$
F = \text{constant}
$$

Or as part of a cost function:

$$
C(q) = F + \text{(variable component)}
$$

The key idea is that fixed costs do not depend on the quantity produced ($q$). Even if production drops to zero, these costs still exist.


<br>

###  Variable Costs

**Variable costs** change directly with the level of production or sales. The more units produced, the higher the total variable cost.

Examples include:
- Raw materials
- Packaging
- Hourly labor tied to production
- Shipping per unit
- Utilities tied to machine usage

Variable costs are often modeled as proportional to output:

$$
VC(q) = vq
$$

Where:
- $v$ = variable cost per unit
- $q$ = quantity produced

This means each additional unit adds a consistent cost to total expenses.


<br>

###  Total Cost Function

Combining both components gives the standard cost model:

$$
C(q) = F + vq
$$

Where:
- $F$ = fixed costs
- $vq$ = total variable costs

This linear model is widely used because it provides a simple but powerful approximation of real-world cost behavior.


<br>

###  Cost Behavior Comparison

The key difference between fixed and variable costs can be summarized as:

- Fixed costs remain constant: $F = \text{constant}$
- Variable costs scale with output: $vq$ increases as $q$ increases

Graphically:
- Fixed costs appear as a horizontal line when plotted against quantity
- Variable costs appear as a line starting at zero and increasing with slope $v$
- Total cost combines both into a line starting at $F$ with slope $v$


<br>

###  Average Cost Per Unit

Another useful measure is the average cost per unit:

$$
AC(q) = \frac{C(q)}{q} = \frac{F + vq}{q}
$$

This simplifies to:

$$
AC(q) = \frac{F}{q} + v
$$

This expression shows an important management insight:
- As production increases, $\frac{F}{q}$ decreases
- This means fixed costs are spread across more units
- Variable cost per unit remains constant

This is one reason businesses aim for higher production volumes: to reduce average cost per unit.


--- PAGE ---

## Break-Even Analysis

Break-even analysis is a fundamental tool in management that determines the exact point at which a business neither makes a profit nor a loss. At this point, total revenue equals total costs, and any sales beyond it contribute to profit while anything below it results in a loss.

It is widely used for pricing decisions, feasibility studies, and risk assessment because it translates business uncertainty into a clear mathematical threshold.


<br>

###  Core Condition

The break-even point occurs when:

$$
R = C
$$

Using standard revenue and cost models:

$$
pq = F + vq
$$

Where:
- $p$ = price per unit  
- $q$ = quantity sold  
- $F$ = fixed costs  
- $v$ = variable cost per unit  


<br>

###  Solving for Break-Even Quantity

Rearranging the equation:

$$
pq - vq = F
$$

$$
q(p - v) = F
$$

$$
q = \frac{F}{p - v}
$$

This formula gives the number of units that must be sold to cover all fixed and variable costs.


<br>

###  Interpretation of the Formula

Each part of the equation has a direct business meaning:

- $F$ (fixed costs): increases the break-even point; higher fixed costs require more sales to recover expenses  
- $p - v$ (contribution margin): represents how much each unit contributes toward covering fixed costs  
- $q$: the required sales volume to reach financial neutrality  

A higher contribution margin reduces the break-even point, making the business less risky. A lower margin increases the required sales volume and financial pressure.


<br>

###  Contribution Margin Concept

The term $p - v$ is often called the **contribution margin per unit**:

$$
\text{Contribution Margin} = p - v
$$

It represents how much each unit sold contributes toward fixed costs and eventual profit. Once fixed costs are fully covered, all remaining contribution becomes profit.


<br>

###  Break-Even in Graphical Terms

Break-even occurs at the intersection of:
- Revenue line: $R(q) = pq$
- Cost line: $C(q) = F + vq$

At low production levels, costs exceed revenue due to fixed costs. As production increases, revenue grows faster (assuming $p > v$), eventually crossing the cost line at the break-even point.


<br>

###  Margin of Safety

Once the break-even point is known, managers often evaluate the **margin of safety**, which measures how far actual or expected sales are above break-even:

$$
\text{Margin of Safety} = q_{\text{actual}} - q_{\text{break-even}}
$$

A larger margin indicates lower financial risk, while a smaller margin indicates vulnerability to demand fluctuations.


--- PAGE ---

## Supply Chains and Network Optimization

In management, supply chains represent the flow of goods, services, and information from raw material sources to final consumers. These systems are often modeled as networks to analyze efficiency, reduce costs, and improve delivery performance. Mathematical tools from graph theory and optimization are used to design and control these networks.

A **supply chain network** consists of interconnected components such as:
- Suppliers (raw material sources)
- Manufacturers (production centers)
- Warehouses (storage nodes)
- Distribution centers (logistics hubs)
- Retailers or customers (end points)

These components can be represented as a graph, where:
- **Nodes (vertices)** represent locations or facilities
- **Edges (links)** represent transportation routes or flows of goods


<br>

###  Flow Representation in Networks

In a simplified model, each edge in the network carries a **flow** representing the quantity of goods transported between nodes.

Let:
- $x_{ij}$ = flow from node $i$ to node $j$
- $c_{ij}$ = cost per unit transported along that route

The total transportation cost in a network is:

$$
C = \sum c_{ij} x_{ij}
$$

This expression forms the basis of many supply chain optimization problems.


<br>

###  Network Optimization Goal

The primary goal in supply chain optimization is to:

- Minimize total cost
- Subject to demand and supply constraints
- While ensuring all customer requirements are satisfied

This can be written as a general optimization problem:

Minimize:

$$
C = \sum c_{ij} x_{ij}
$$

Subject to:
- Supply constraints (production limits at source nodes)
- Demand constraints (requirements at destination nodes)
- Flow conservation at intermediate nodes


<br>

###  Flow Conservation Principle

At intermediate nodes (such as warehouses), the total incoming flow must equal the total outgoing flow:

$$
\sum x_{\text{in}} = \sum x_{\text{out}}
$$

This ensures that goods are neither created nor lost within the network, only transferred.


<br>

###  Transportation Problem

A common special case of supply chain optimization is the **transportation problem**, where goods must be shipped from multiple suppliers to multiple consumers at minimum cost.

It typically involves:
- A set of supply nodes with fixed capacities
- A set of demand nodes with fixed requirements
- A cost matrix defining transportation costs between each pair

The objective is to determine the optimal shipment plan $x_{ij}$ that minimizes total cost while satisfying all constraints.


<br>

###  Shortest Path and Routing

In logistics, another key problem is finding the most efficient route between two points. This is modeled using shortest path optimization, where:

- Nodes represent locations
- Edges represent travel routes
- Weights represent distance, time, or cost

The goal is to minimize total path weight from origin to destination.


--- PAGE ---

## Pricing Strategies and Elasticity

Pricing strategies in management focus on how businesses set and adjust prices to maximize revenue, profit, or market share. A key mathematical idea underlying pricing decisions is **price elasticity of demand**, which measures how sensitive customer demand is to changes in price.

Understanding elasticity allows managers to predict how changing a price will affect total revenue and to choose optimal pricing strategies under different market conditions.

<br>

###  Price Elasticity of Demand

Price elasticity of demand measures the responsiveness of quantity demanded to changes in price:

$$
E = \frac{dQ}{dP}\cdot\frac{P}{Q}
$$

Where:
- $E$ = price elasticity of demand  
- $\frac{dQ}{dP}$ = rate of change of quantity with respect to price  
- $P$ = price level  
- $Q$ = quantity demanded  


<br>

###  Interpreting Elasticity

The value of $E$ determines how sensitive demand is to price changes:

- **Elastic demand ($|E| > 1$):**  
  Small price changes cause large changes in quantity demanded. Revenue is sensitive to pricing.

- **Inelastic demand ($|E| < 1$):**  
  Quantity demanded changes little when price changes. Revenue is less sensitive to pricing.

- **Unit elastic demand ($|E| = 1$):**  
  Revenue remains relatively stable when price changes.


<br>

###  Revenue and Elasticity

Total revenue is given by:

$$
R = P \cdot Q
$$

Price changes affect both variables:
- Increasing price raises $P$ but may reduce $Q$
- Decreasing price lowers $P$ but may increase $Q$

Elasticity determines which effect dominates:
- If demand is elastic, lowering price increases revenue
- If demand is inelastic, raising price increases revenue


<br>

###  Pricing Strategy Types

Managers use elasticity insights to guide different pricing strategies:

1. **Penetration Pricing**
   - Low initial price to increase demand
   - Works best in elastic markets

2. **Skimming Pricing**
   - High initial price for premium segments
   - Works when demand is relatively inelastic

3. **Competitive Pricing**
   - Prices set relative to competitors
   - Common in markets with similar products

4. **Dynamic Pricing**
   - Prices change based on demand conditions
   - Used in airlines, hotels, and ride-sharing systems


<br>

###  Optimal Pricing Insight

In more advanced models, firms aim to set prices where marginal revenue equals marginal cost:

$$
MR = MC
$$

This condition ensures profit maximization, and elasticity plays a key role in determining marginal revenue behavior.

--- PAGE ---

## Inventory Management and Optimization

Inventory management focuses on determining how much stock a business should hold, when it should reorder, and how to minimize total costs while meeting customer demand. It is a balancing act between avoiding shortages (stockouts) and avoiding excessive holding costs.

Mathematical models are widely used to optimize inventory decisions by minimizing total cost under demand constraints.

<br>

###  Key Components of Inventory Systems

Inventory decisions are typically driven by three main cost factors:

- **Ordering costs:** fixed cost each time an order is placed (shipping, setup, processing)
- **Holding costs:** cost of storing inventory over time (warehousing, insurance, depreciation)
- **Shortage costs:** cost of running out of stock (lost sales, delays, customer dissatisfaction)


<br>

###  Total Inventory Cost Structure

A general cost model can be written as:

$$
TC(Q) = \text{Ordering Cost} + \text{Holding Cost} + \text{Purchase Cost}
$$

Where:
- $Q$ = order quantity

Each component behaves differently:
- Ordering cost decreases when order size increases (fewer orders needed)
- Holding cost increases when order size increases (more inventory stored)
- Purchase cost is often constant per unit in basic models


<br>

###  Economic Order Quantity (EOQ)

One of the most important models in inventory optimization is the **Economic Order Quantity (EOQ)**, which determines the optimal order size that minimizes total cost.

$$
Q^* = \sqrt{\frac{2DS}{H}}
$$

Where:
- $Q^*$ = optimal order quantity  
- $D$ = annual demand  
- $S$ = fixed ordering cost per order  
- $H$ = holding cost per unit per year  


<br>

###  Interpretation of EOQ

The EOQ formula balances two competing forces:

- Larger orders reduce ordering frequency but increase storage costs  
- Smaller orders reduce storage costs but increase ordering frequency  

The optimal point occurs when these two effects are equalized.


<br>

###  Reorder Point

While EOQ determines how much to order, the **reorder point** determines when to order:

$$
R = dL
$$

Where:
- $R$ = reorder point  
- $d$ = demand rate per time period  
- $L$ = lead time (time between ordering and receiving stock)

This ensures that new inventory arrives before stock runs out.

<br>

###  Safety Stock

To account for uncertainty in demand or delivery delays, businesses often maintain **safety stock**:

$$
SS = R - dL
$$

Safety stock acts as a buffer against variability in supply and demand.

<br>

###  Inventory Trade-Offs

Inventory systems involve several key trade-offs:

- Higher inventory reduces stockout risk but increases holding costs  
- Lower inventory reduces storage costs but increases risk of shortages  
- Faster ordering cycles improve responsiveness but increase operational cost  

<br>

###  Just-In-Time (JIT) Systems

Some businesses use **Just-In-Time inventory systems**, where inventory is kept as low as possible and materials arrive exactly when needed.

Advantages:
- Reduced holding costs  
- Less waste and overproduction  

Disadvantages:
- High sensitivity to supply chain disruptions  
- Requires highly reliable suppliers  


--- PAGE ---

## Market Structure and Competition Models

Market structure describes how firms in an industry compete with one another and how that competition affects prices, output, and profitability. Different structures create different strategic environments, and mathematical models help explain how firms behave under each one.

The main idea is that market outcomes depend on:
- Number of firms in the market  
- Degree of product differentiation  
- Barriers to entry  
- Strategic interaction between firms  

<br>

###  Perfect Competition

In perfect competition, many small firms sell identical products, and no single firm can influence market price.

Key characteristics:
- Many buyers and sellers  
- Homogeneous products  
- Free entry and exit  

In this model:
- Firms are price takers  
- Market price is determined by supply and demand  

Profit is maximized when:

$$
P = MC
$$

Where:
- $P$ = market price  
- $MC$ = marginal cost  

In the long run, economic profit tends toward zero due to free entry.

<br>

### Monopoly

A monopoly is a market with a single firm controlling supply.

The monopolist chooses output to maximize profit:

$$
\max_q \; \pi(q) = R(q) - C(q)
$$

Where revenue depends on the demand curve:

$$
R(q) = P(q)\cdot q
$$

Unlike perfect competition, the monopolist faces a downward-sloping demand curve, meaning:
- Increasing output lowers price  
- Output and price are jointly determined  

Profit maximization occurs where:

$$
MR = MC
$$

Where:
- $MR$ = marginal revenue  
- $MC$ = marginal cost  

<br>

###  Oligopoly

An oligopoly consists of a small number of firms whose decisions are interdependent. Each firm must consider how competitors will respond to its actions.

This creates a strategic environment best modeled using game theory.

A key concept is **strategic equilibrium**, where each firm chooses the best response to others' decisions.

<br>

###  Cournot Competition

In Cournot models, firms choose quantities simultaneously.

Each firm solves:

$$
\max_{q_i} \; \pi_i(q_i, q_{-i})
$$

Where:
- $q_i$ = output of firm $i$  
- $q_{-i}$ = output of competing firms  

Market price depends on total output:

$$
P = P(q_1 + q_2 + \dots + q_n)
$$

Firms adjust output based on expectations of rivals' production levels.

<br>

###  Bertrand Competition

In Bertrand models, firms compete by setting prices rather than quantities.

Key outcome:
- If products are identical and firms have similar costs, competition can drive price down to marginal cost:

$$
P = MC
$$

This leads to very low profits or even zero economic profit, despite having only a few firms.

<br>

###  Monopolistic Competition

Monopolistic competition lies between monopoly and perfect competition.

Characteristics:
- Many firms  
- Differentiated products  
- Some pricing power  

Each firm faces a downward-sloping demand curve:

$$
P = f(q)
$$

Firms compete through:
- Pricing  
- Branding  
- Product differentiation  
- Marketing  


--- PAGE ---

## Return on Investment (ROI)

Return on Investment (ROI) is a fundamental performance metric in management used to evaluate the efficiency or profitability of an investment. It measures how much return a business gains relative to the cost of the investment, allowing comparison across different projects, strategies, or assets.

<br>

###  Basic ROI Formula

ROI is defined as:

$$
ROI = \frac{\text{Net Profit}}{\text{Investment Cost}} \times 100\%
$$

Where:
- Net Profit = total gains minus total costs  
- Investment Cost = total amount invested  

<br>

###  Interpreting ROI

- A positive ROI means the investment generates profit  
- A negative ROI means the investment results in a loss  
- A higher ROI indicates better efficiency of capital usage  

For example:
- ROI = 0.20 means a 20% return on the original investment  
- ROI = -0.10 means a 10% loss  

<br>

###  ROI as a Percentage

ROI is often expressed as a percentage for easier interpretation:

$$
ROI\% = \frac{\text{Net Profit}}{\text{Investment Cost}} \times 100
$$

This format is widely used in business reporting because it allows quick comparison across investments of different sizes.

<br>

###  ROI in Decision Making

Managers use ROI to evaluate:
- Whether to approve new projects  
- How to allocate limited capital between competing options  
- Which products or divisions are performing best  
- Whether marketing campaigns are financially effective  

<br>

###  ROI vs Profit

It is important to distinguish ROI from raw profit:

- **Profit** measures absolute gain  
- **ROI** measures efficiency relative to cost  

A small project may have low profit but high ROI, while a large project may have high profit but low ROI. This distinction is critical for comparing investments of different scales.

<br>

###  Time-Adjusted ROI

Basic ROI ignores time, but investments often occur over different time horizons. To account for this, managers use annualized or time-adjusted measures.

A simple annualized approximation is:

$$
ROI_{annual} = \frac{ROI}{t}
$$

Where:
- $t$ = number of years

More advanced models incorporate discounting and use metrics like Net Present Value (NPV), but ROI remains a quick heuristic.

<br>

###  Limitations of ROI

While useful, ROI has important limitations:

- Ignores time value of money  
- Does not account for risk or uncertainty  
- Can be manipulated by changing accounting methods  
- Does not reflect cash flow timing  

Because of these limitations, ROI is often used alongside other metrics rather than as a standalone decision rule.

<br>

###  ROI and Opportunity Cost

Every investment has an opportunity cost—the return that could have been earned elsewhere. A rational decision requires comparing ROI across alternatives:

- Choose the investment with the highest acceptable ROI  
- Ensure ROI exceeds the cost of capital or required return  


--- PAGE ---

## Scaling and Exponential Growth

Scaling and exponential growth describe how systems change as they expand in size, particularly when growth is not linear but accelerates over time. In management, these concepts are essential for understanding business expansion, technology adoption, network effects, and long-term forecasting.

Unlike linear growth, where change happens at a constant rate, exponential growth increases at a rate proportional to the current size of the system. This leads to rapid acceleration once a system reaches a certain threshold.

<br>

###  Linear vs Exponential Growth

Linear growth follows a constant additive pattern:

$$
y = a + bt
$$

Exponential growth follows a multiplicative pattern:

$$
y = ae^{kt}
$$

Where:
- $y$ = quantity at time $t$  
- $a$ = initial value  
- $k$ = growth rate  
- $t$ = time  

The key difference is:
- Linear growth adds the same amount each period  
- Exponential growth multiplies by a constant factor each period  

<br>

###  Interpreting Exponential Growth

In the model $y = a e^{kt}$:
- If $k > 0$, the system grows exponentially  
- If $k < 0$, the system decays exponentially  
- Larger $k$ values indicate faster growth or decay  

Even small values of $k$ can lead to large long-term effects due to compounding.

<br>

###  Doubling Time

A useful concept in exponential systems is **doubling time**, which estimates how long it takes for a quantity to double:

$$
t_d = \frac{\ln 2}{k}
$$

This shows that:
- Higher growth rates lead to shorter doubling times  
- Even small increases in $k$ significantly accelerate growth  

<br>

###  Scaling Effects in Business

Scaling refers to how a system behaves as it grows in size. In management, scaling effects determine whether growth is efficient or costly.

There are three main types:

- **Economies of scale:** Costs per unit decrease as output increases  
- **Constant returns to scale:** Costs per unit remain stable  
- **Diseconomies of scale:** Costs per unit increase as the system grows  

<br>

###  Network Effects

Some systems exhibit **network effects**, where the value of the system increases as more users join.

A simple representation:

$$
V \propto n
$$

Or in stronger cases:

$$
V \propto n^2
$$

Where:
- $V$ = value of the network  
- $n$ = number of users  

This creates exponential-like growth in value, common in platforms, social networks, and digital ecosystems.

<br>

###  Feedback Loops

Exponential growth often arises from feedback mechanisms:

- **Positive feedback loop:** Growth accelerates itself (e.g., viral marketing)  
- **Negative feedback loop:** Growth is stabilized or slowed (e.g., market saturation)  

Positive feedback is what drives exponential scaling in successful systems.

<br>

###  Logistic Growth

In reality, exponential growth cannot continue indefinitely due to resource constraints. This leads to **logistic growth**, where growth slows as the system approaches a maximum capacity.

While exponential growth is:

- Unbounded  
- Rapidly accelerating  

Logistic growth introduces a saturation point (carrying capacity), making long-term predictions more realistic.


--- PAGE ---

## Behavioral Economics in Consumer Choice

Behavioral economics studies how real human decision-making deviates from the idealized rational models used in classical economics. In management, this is especially important because consumers do not always act logically—they are influenced by cognitive biases, emotions, and context.

Instead of assuming perfectly rational agents who always maximize utility, behavioral economics models decision-making as a combination of rational evaluation and psychological influence.

<br>

###  Utility vs Perceived Utility

Classical economics assumes consumers maximize utility:

$$
U(x)
$$

Where:
- $U$ = utility function  
- $x$ = choice or bundle of goods  

Behavioral economics introduces the idea that consumers act based on **perceived utility**, which can differ from actual utility due to biases:

$$
U_{perceived}(x) \neq U(x)
$$

This gap explains many real-world inconsistencies in consumer behavior.

<br>

###  Prospect Theory and Loss Aversion

One of the most important models in behavioral economics is **prospect theory**, which describes how people evaluate gains and losses relative to a reference point rather than absolute outcomes.

A key insight is **loss aversion**: losses feel more significant than equivalent gains.

This is often modeled as:

- Losses weighted more heavily than gains  
- Steeper utility curve for losses than for gains  

Mathematically, a simplified value function is:

$$
v(x)=\begin{cases}x^\alpha & \text{if } x \geq 0 \\ -\lambda(-x)^\beta & \text{if } x<0 \end{cases}
$$

Where:
- $x$ = gain or loss relative to a reference point  
- $\lambda > 1$ = loss aversion coefficient  
- $\alpha, \beta$ = curvature parameters  

<br>

###  Framing Effects

Consumer choices are influenced not only by outcomes but by how choices are presented (framed).

For example:
- “90% survival rate” vs “10% mortality rate”  
- Same information, different emotional impact  

<br>

###  Anchoring Effect

Anchoring occurs when individuals rely heavily on an initial reference value when making decisions.

A simple representation:

$$
\hat{x} = x_0 + \alpha(x - x_0)
$$

Where:
- $x_0$ = anchor value  
- $x$ = actual value  
- $\alpha$ = adjustment factor  

Consumers often fail to fully adjust away from anchors, leading to systematic bias in pricing perception and valuation.

<br>

###  Time Inconsistency and Present Bias

Consumers tend to overweight immediate rewards relative to future rewards. This is modeled using discounting:

$$
U = \sum_{t} \delta^t u_t
$$

Where:
- $\delta < 1$ represents time discounting  

Behavioral models modify this with stronger present bias:

- Immediate rewards are disproportionately preferred  
- Long-term planning becomes inconsistent over time  

This explains behaviors like overspending or under-saving.

<br>

###  Heuristics in Decision Making

Instead of full optimization, consumers often use shortcuts (heuristics):

- **Availability heuristic:** decisions based on easily recalled examples  
- **Representativeness heuristic:** judging probability based on similarity  
- **Satisficing:** choosing the first acceptable option rather than the optimal one  

These reduce cognitive effort but introduce predictable errors.

<br>

###  Nudging and Choice Architecture

Managers and policymakers use behavioral insights to design “nudges,” which guide decisions without restricting choice.

Examples include:
- Default enrollment in retirement plans  
- Simplified pricing structures  
- Strategic product placement  

The idea is to influence behavior by adjusting the decision environment rather than changing incentives directly.