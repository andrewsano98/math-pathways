<!--
title: "Math in Finance"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/finance_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Finance
    </h1>
  </div>

</div>

<br>

### What will I be doing?
- Building financial and risk models using Excel, Python, R, and quantitative analysis tools  
- Applying statistical and probabilistic methods to evaluate investments, markets, and portfolio performance  
- Using SQL and financial databases to analyze market, economic, and transactional data  
- Running simulations and forecasting models to assess risk, pricing, and market behavior  
- Interpreting financial statements, economic indicators, and trading data to support decision-making  
- Using algorithmic and quantitative trading tools to automate market analysis and execution strategies  
- Evaluating investment strategies based on risk, return, volatility, and economic conditions  

### What are the most common jobs?
- Financial Analyst  
- Investment Banker  
- Accountant  
- Portfolio Manager  
- Financial Planner  
- Risk Analyst  
- Actuary  
- Corporate Finance Manager  

### What math concepts do I need to know?
- Algebra  
- Statistics  
- Probability  
- Calculus  
- Financial Mathematics  
- Compound Interest  
- Data Analysis  
- Optimization  
- Graphing and Trends  

--- PAGE ---

## Time Value of Money

The **time value of money (TVM)** is one of the foundational ideas in finance and economics. At its core, it formalizes a simple but powerful observation: a dollar today is not equivalent to a dollar received in the future. This difference arises because money can be invested to generate returns, and because future payments carry uncertainty.

Understanding TVM allows us to compare cash flows occurring at different points in time by converting them into a common basis—either present value or future value.

<br>

### Interest and Growth

Interest is the mechanism by which money grows over time. From a mathematical perspective, interest can be viewed as a growth process applied to capital. From an economic perspective, it represents compensation for delaying consumption, taking on risk, and providing capital to others.

There are two primary growth behaviors in financial systems:

- **Linear growth**, where returns accumulate only on the original investment
- **Exponential growth**, where returns themselves begin generating additional returns

This distinction is critical, because even small changes in how interest is applied can lead to dramatically different long-term outcomes.

<br>

### Simple Interest

Simple interest describes a linear accumulation of value over time. It assumes that interest is earned only on the initial principal, and not on previously earned interest.

$$
I = Prt
$$

Where:
- $P$ = principal  
- $r$ = interest rate  
- $t$ = time  

### Total Amount with Simple Interest

The total accumulated value under simple interest is:

$$
A = P(1 + rt)
$$

This model is most commonly used in short-term loans or simplified financial contexts. Because growth is linear, it does not capture reinvestment effects, and therefore tends to underestimate long-term accumulation compared to real-world investment behavior.

<br>

### Compound Interest

Compound interest introduces a fundamentally different growth structure. Instead of earning interest only on the original principal, interest is periodically added to the balance, and future interest is calculated on this updated amount.

This produces exponential growth behavior.

$$
A =
P
\left(
1 +
\frac{r}{n}
\right)^{nt}
$$

Where:
- $P$ = principal  
- $r$ = annual interest rate  
- $n$ = compounding frequency per year  
- $t$ = time (years)  

The key implication of compounding is that growth becomes path-dependent: the earlier returns occur, the more time they have to compound. This leads to accelerating growth over long horizons, which is why compounding is often described as one of the most powerful forces in finance.

<br>

### Continuous Compounding

Continuous compounding represents the limiting case of compound interest as the compounding frequency increases without bound. It models a situation in which interest is being added at every possible instant.

$$
A = Pe^{rt}
$$

Where:
- $P$ = principal  
- $r$ = interest rate  
- $t$ = time  

In practice, continuous compounding is an idealization, but it is widely used in theoretical finance because it simplifies analysis and closely approximates high-frequency compounding systems.

<br>

### Future Value (FV)

Future value represents the amount that a present sum of money will grow to over a specified time period given a constant rate of return.

$$
FV = PV(1 + r)^t
$$

Where:
- $PV$ = present value  
- $r$ = interest rate  
- $t$ = number of periods  

Future value calculations are used when the goal is to project current investments forward in time, such as retirement planning or investment growth forecasting.

<br>

### Present Value (PV)

Present value is the inverse of future value. It expresses how much a future cash flow is worth today after accounting for time and the required rate of return.

$$
PV = \frac{FV}{(1 + r)^t}
$$

Where:
- $FV$ = future value  
- $r$ = discount rate  
- $t$ = number of periods  

A central insight of present value analysis is that uncertainty and delay reduce economic value. As time increases, the present worth of a fixed future payment declines.

<br>

### Discount Factor

The discount factor is the multiplicative term that converts future cash flows into present value form. It provides a compact way to express time-based reduction in value.

$$
DF =
\frac{1}{(1+r)^t}
$$

Where:
- $r$ = discount rate  
- $t$ = number of periods  

Using this formulation, present value can be written more compactly as:

- Present Value = Future Value × Discount Factor

This representation is particularly useful in valuation models where multiple future cash flows must be aggregated into a single present value.


--- PAGE ---

## Investments

Investments are financial assets purchased with the expectation that they will generate future income, appreciate in value, or both. Individuals, corporations, and institutions invest capital in order to grow wealth, preserve purchasing power, or generate consistent cash flow over time.

Most investment decisions rely heavily on the concepts of time value of money, discounting, risk assessment, and expected return. Because future outcomes are uncertain, investors use mathematical models to estimate value and compare opportunities across different asset classes.

<br>

Common investment categories include:

| Investment Type | Description | Typical Risk Level |
|---|---|---|
| Stocks | Ownership shares in publicly traded companies | High |
| Bonds | Loans made to governments or corporations | Low–Medium |
| Mutual Funds | Professionally managed pooled investment funds | Medium |
| Exchange-Traded Funds (ETFs) | Funds traded like stocks that track indexes or sectors | Medium |
| Real Estate | Property investments that may generate rental income or appreciation | Medium–High |
| Certificates of Deposit (CDs) | Bank deposits with fixed interest and maturity dates | Low |
| Money Market Funds | Short-term, highly liquid investments | Low |
| Treasury Securities | Government-issued debt instruments | Very Low |
| Commodities | Physical goods such as gold, oil, or agricultural products | High |
| Options and Derivatives | Financial contracts based on underlying assets | Very High |
| Cryptocurrency | Digital decentralized assets such as Bitcoin or Ethereum | Very High |
| Index Funds | Funds designed to track market indexes | Medium |
| Retirement Accounts | Tax-advantaged long-term investment accounts | Varies |
| Private Equity | Investments in privately held companies | High |
| Hedge Funds | Aggressive pooled investment strategies | High–Very High |
| Venture Capital | Funding provided to startup companies | Very High |
| Annuities | Insurance-based investment contracts providing future payments | Low–Medium |
| Foreign Exchange (Forex) | Trading one currency against another | Very High |
| Collectibles and Alternative Assets | Art, antiques, rare items, and other nontraditional assets | Medium–High |
| Cash and Cash Equivalents | Highly liquid assets such as savings accounts and cash | Very Low |

<br>

Different investments offer different combinations of risk, return, liquidity, and growth potential.

<br>

### Future Value of an Annuity

An annuity is a sequence of equal recurring payments made over time. The future value of an annuity measures how much those payments will accumulate to after earning compound interest.

This model is commonly used in retirement planning, savings accounts, pensions, and recurring investment contributions.

$$
FV_{annuity}
=
PMT
\cdot
\frac{
(1+r)^n - 1
}{r}
$$

Where:
- $PMT$ = periodic payment  
- $r$ = interest rate per period  
- $n$ = number of periods  

<br>

### Future Value of a Growing Annuity

A growing annuity extends the standard annuity model by allowing payments to increase over time. This reflects many real-world financial situations, such as salaries, retirement contributions, or dividend reinvestment plans that gradually grow each year.

$$
FV_{growing}
=
PMT
\cdot
\frac{
(1+r)^n - (1+g)^n
}{
r-g
}
$$

Where:
- $PMT$ = initial payment  
- $r$ = interest rate  
- $g$ = growth rate  
- $n$ = number of periods  

<br>

### Perpetuity

A perpetuity represents an infinite stream of constant recurring cash flows. Because the payments never end, the valuation depends entirely on discounting future payments back to the present.

Perpetuity models are widely used in finance when valuing preferred stock, endowments, and stable long-term cash-producing assets.

$$
PV_{perpetuity}
=
\frac{C}{r}
$$

Where:
- $C$ = recurring cash flow  
- $r$ = discount rate  

<br>

### Growing Perpetuity

A growing perpetuity assumes that recurring payments continue forever while increasing at a constant rate.

This model is foundational in equity valuation and dividend discount models.

$$
PV_{growing}
=
\frac{
C_1
}{
r-g
}
$$

Where:
- $C_1$ = next cash flow  
- $r$ = discount rate  
- $g$ = growth rate  

<br>

### Bond Pricing

A bond is a fixed-income security that pays periodic coupon payments and returns its face value at maturity. The value of a bond equals the present value of all future cash flows generated by the bond.

$$
P =
\sum_{t=1}^{n}
\frac{C}{(1+r)^t}
+
\frac{F}{(1+r)^n}
$$

Where:
- $C$ = coupon payment  
- $F$ = face value  
- $r$ = discount rate  
- $n$ = maturity periods  

<br>

### Stocks

Stocks represent ownership shares in a corporation. Investors earn returns through price appreciation and dividends.

Stock returns are often highly volatile in the short term but historically have provided strong long-term growth.

- Stock Return:

$$
R = \frac{P_1 - P_0 + D}{P_0}
$$

Where:
- $P_0$ = initial stock price  
- $P_1$ = final stock price  
- $D$ = dividends received  

<br>

### Bonds

Bonds are debt securities issued by governments or corporations. Investors lend money in exchange for periodic interest payments and repayment of principal at maturity.

One of the most important bond concepts is yield to maturity (YTM), which estimates the total annualized return earned if the bond is held until maturity.

- Yield to Maturity (simplified concept):

$$
YTM \approx
\frac{
C + (F - P)/n
}{
(F + P)/2
}
$$

Where:
- $C$ = annual coupon payment  
- $F$ = face value  
- $P$ = current bond price  
- $n$ = years to maturity  


--- PAGE ---

## Loans

Loans are financial agreements in which a lender provides money to a borrower under the condition that the amount will be repaid over time, usually with interest. Loans are fundamental to modern finance because they allow individuals, businesses, and governments to access capital before they fully possess it.

Common uses of loans include:

- Purchasing homes
- Financing education
- Expanding businesses
- Buying vehicles
- Managing short-term liquidity needs

From a mathematical perspective, loans are applications of the time value of money. The lender gives up money today in exchange for a stream of future payments that compensate for time, inflation, and risk.

Different loan structures exist depending on how payments are organized, how interest is calculated, and how long repayment lasts.

<br>

### Mortgage Loans

A mortgage is a long-term loan used to finance real estate purchases. In a mortgage agreement, the property itself serves as collateral for the loan.

Most mortgages are amortizing loans, meaning each payment contains:

- An interest component
- A principal repayment component

At the beginning of the loan, a larger portion of each payment goes toward interest. Over time, the balance declines and more of each payment goes toward reducing principal.

Mortgage mathematics is heavily dependent on compound interest and annuity formulas because the borrower makes recurring fixed payments over many years.

The standard mortgage payment formula calculates the fixed periodic payment required to fully repay a loan over a specified number of periods.

$$
PMT =
\frac{
Pr
}{
1 - (1+r)^{-n}
}
$$

Where:
- $P$ = loan principal  
- $r$ = periodic interest rate  
- $n$ = total number of payments  

This formula is derived from the present value of an annuity, where the stream of future loan payments must equal the original amount borrowed.

Key observations:

- Higher interest rates increase required payments
- Longer loan terms reduce periodic payments but increase total interest paid
- Larger principal balances increase total repayment obligations

Because mortgage payments are fixed in many traditional loan structures, borrowers can predict their future payment obligations with relatively high precision.

<br>

### Amortization

Amortization refers to the gradual reduction of loan principal over time through scheduled payments.

Each payment can be decomposed into:

$$
\text{Payment} =
\text{Interest Portion}
+
\text{Principal Portion}
$$

The interest portion for a given period is:

$$
\text{Interest} =
\text{Remaining Balance}
\cdot r
$$

As the remaining balance declines, interest charges decrease, causing a progressively larger share of each payment to reduce principal.

This creates a nonlinear repayment structure:

- Early payments are interest-heavy
- Later payments are principal-heavy

Amortization schedules are widely used in banking, real estate finance, and consumer lending to track repayment progress over time.

<br>

### Interest Rates and Borrowing Costs

The total cost of a loan depends heavily on the interest rate applied to the borrowed amount.

Small differences in rates can produce large long-term effects because of compounding. For example:

- A lower interest rate reduces both monthly payments and total repayment cost
- A higher interest rate increases the amount ultimately paid to the lender

This relationship is especially important in long-term loans such as mortgages, where repayment may span 15 to 30 years.

In practice, lenders determine interest rates using factors such as:

- Creditworthiness
- Income stability
- Inflation expectations
- Central bank policy rates
- Market supply and demand for credit

<br>

### Fixed vs. Variable Rate Loans

Loans are commonly divided into two major interest-rate structures:

#### Fixed-Rate Loans
- Interest rate remains constant throughout the loan term
- Produces stable and predictable payments
- Protects borrowers from rising market rates

#### Variable-Rate Loans
- Interest rate changes over time based on market benchmarks
- Payments may increase or decrease
- Often begin with lower introductory rates but carry greater uncertainty

The choice between fixed and variable structures reflects a trade-off between predictability and potential cost savings.

<br>

### Credit Risk in Lending

Whenever a lender issues a loan, there is a possibility that the borrower may fail to repay the debt. This uncertainty is known as credit risk.

Financial institutions estimate credit risk using models that analyze factors such as:

- Credit history
- Debt-to-income ratio
- Employment stability
- Asset ownership
- Payment history

Higher perceived risk generally leads to:

- Higher interest rates
- Stricter borrowing requirements
- Lower approved loan amounts

In this way, loans combine mathematical valuation with probabilistic risk assessment.

<br>

### Loan Balance

The remaining balance on a loan after a certain number of payments can be calculated using the loan balance formula.

$$
B_k
=
P(1+r)^k
-
PMT
\left(
\frac{(1+r)^k - 1}{r}
\right)
$$

Where:
- $B_k$ = remaining balance after $k$ payments  
- $P$ = original loan principal  
- $r$ = periodic interest rate  
- $PMT$ = periodic payment  
- $k$ = number of payments made  

This formula is useful for determining:

- Remaining debt at a given point in time
- Refinancing calculations
- Early payoff analysis
- Equity accumulation in mortgages

It also demonstrates how compound interest and amortization interact over the life of the loan.

<br>

### Total Interest Paid

The total interest paid over the life of a fully amortizing loan can be estimated by subtracting the original principal from the total amount repaid.

$$
\text{Total Interest}
=
(PMT \cdot n) - P
$$

Where:
- $PMT$ = periodic payment  
- $n$ = total number of payments  
- $P$ = original loan principal  

This highlights an important property of long-term borrowing:

- Lower monthly payments often result in higher total interest costs because repayment occurs over a longer period.

<br>

### Effective Annual Rate (EAR)

The effective annual rate measures the true annual borrowing cost after accounting for compounding frequency.

$$
EAR
=
\left(
1 + \frac{r}{n}
\right)^n
- 1
$$

Where:
- $r$ = nominal annual interest rate  
- $n$ = number of compounding periods per year  

EAR allows borrowers and investors to compare loans with different compounding structures on an equal basis.

For example:

- Monthly compounding produces a higher effective rate than annual compounding at the same nominal rate.
- More frequent compounding increases total borrowing cost.

<br>

### Annual Percentage Rate (APR)

APR represents the standardized yearly cost of borrowing, including certain fees and financing costs in addition to interest.

Conceptually:

$$
APR
=
\text{Interest Rate}
+
\text{Loan Fees}
$$

APR is widely used in consumer finance because it provides a more complete measure of borrowing cost than the stated interest rate alone.

Lenders are often legally required to disclose APR so borrowers can compare competing loan offers more transparently.

<br>

### Debt-to-Income Ratio (DTI)

Lenders frequently evaluate a borrower’s debt burden using the debt-to-income ratio.

$$
DTI
=
\frac{
\text{Monthly Debt Payments}
}{
\text{Monthly Gross Income}
}
$$

Where:
- Monthly debt payments include mortgages, loans, and credit obligations
- Gross income is income before taxes

A lower DTI generally indicates:

- Greater repayment capacity
- Lower default risk
- Higher likelihood of loan approval

High DTI ratios may lead to:

- Higher interest rates
- Reduced borrowing limits
- Loan denial

<br>

### Loan-to-Value Ratio (LTV)

In mortgage lending, lenders evaluate collateral risk using the loan-to-value ratio.

$$
LTV
=
\frac{
\text{Loan Amount}
}{
\text{Property Value}
}
$$

Where:
- Loan Amount = amount borrowed
- Property Value = appraised market value of the property

Higher LTV ratios imply:

- Lower borrower equity
- Greater lender risk
- Increased probability of loss in foreclosure

Because of this, high-LTV loans often require:

- Mortgage insurance
- Larger interest rates
- Stricter underwriting standards


--- PAGE ---

## Markets

Financial markets are systems in which buyers and sellers exchange financial assets, commodities, currencies, and other instruments of value. These markets allow capital to flow between participants and play a central role in economic growth, investment, and risk management.

Markets serve several major economic functions:

- Allocating capital efficiently
- Determining prices through supply and demand
- Providing liquidity
- Facilitating investment and speculation
- Allowing participants to transfer and manage risk

Modern financial markets operate through highly interconnected global systems involving banks, governments, corporations, institutional investors, and individual traders.

<br>

### Types of Financial Markets

Financial markets are typically categorized based on the type of assets being traded.

Major categories include:

- Stock markets
- Bond markets
- Commodity markets
- Foreign exchange markets
- Derivatives markets
- Money markets

Each market has different risk structures, pricing mechanisms, and economic purposes.

<br>

### Stock Markets

Stock markets facilitate the buying and selling of ownership shares in publicly traded companies. When investors purchase stock, they acquire partial ownership in a corporation and may benefit from:

- Capital appreciation
- Dividend payments
- Voting rights

Stock prices fluctuate continuously based on:

- Company earnings
- Economic conditions
- Interest rates
- Investor expectations
- Market sentiment

One of the most basic measures of investment performance in stocks is total return.

#### Stock Return

$$
R =
\frac{
P_1 - P_0 + D
}{
P_0
}
$$

Where:
- $P_0$ = initial stock price  
- $P_1$ = final stock price  
- $D$ = dividends received  

Stock markets are often considered forward-looking systems because prices reflect collective expectations about future company performance.

<br>

### Bond Markets

Bond markets involve the trading of debt securities issued by governments, corporations, or other institutions. When investors purchase bonds, they are effectively lending money to the issuer in exchange for future interest payments and repayment of principal.

Bond prices are strongly influenced by:

- Interest rates
- Inflation expectations
- Credit risk
- Time to maturity

A bond’s value is determined by discounting its future cash flows into present value form.

#### Bond Price

$$
P =
\sum_{t=1}^{n}
\frac{C}{(1 + r)^t}
+
\frac{F}{(1 + r)^n}
$$

Where:
- $C$ = coupon payment  
- $F$ = face value  
- $r$ = discount rate  
- $n$ = maturity periods  

This formula demonstrates one of the core principles of finance: the value of an asset equals the present value of its expected future cash flows.

Bond markets are especially important for governments and corporations seeking long-term financing.

<br>

### Commodity Markets

Commodity markets facilitate the trading of raw materials and natural resources.

Examples include:

- Oil
- Gold
- Silver
- Wheat
- Corn
- Natural gas

Commodity prices are heavily influenced by:

- Supply and demand conditions
- Weather events
- Geopolitical conflict
- Transportation costs
- Global economic activity

Unlike stocks or bonds, commodities often derive value from physical scarcity and industrial usefulness.

Commodity markets are widely used for:

- Hedging price risk
- Speculation
- Inflation protection
- Industrial production planning

<br>

### Foreign Exchange Markets

Foreign exchange (forex) markets involve the trading of currencies between nations. These markets are among the largest and most liquid financial systems in the world.

Exchange rates determine how much one currency is worth relative to another.

#### Exchange Rate

$$
S =
\frac{
\text{Domestic Currency}
}{
\text{Foreign Currency}
}
$$

Exchange rates fluctuate due to factors such as:

- Interest rate differences
- Inflation
- Trade balances
- Political stability
- Central bank policies

Foreign exchange markets are essential for international trade, investment, and global financial integration.

<br>

### Market Efficiency

Financial economists often study whether markets accurately incorporate available information into asset prices. This idea is formalized through the Efficient Market Hypothesis (EMH).

The central claim of EMH is that prices rapidly adjust to new information, making it difficult to consistently outperform the market using publicly available data.

A simplified representation is:

#### Efficient Market Hypothesis (EMH)

$$
P_t =
E(P_{t+1} \mid \mathcal{I}_t)
$$

Where:
- $P_t$ = current price  
- $E(P_{t+1} \mid \mathcal{I}_t)$ = expected future price given current information set $\mathcal{I}_t$  

Under strong forms of market efficiency:

- Mispriced assets are quickly corrected
- Arbitrage opportunities disappear rapidly
- Predicting short-term price movements becomes extremely difficult

In practice, financial markets are not perfectly efficient, but the concept remains foundational in modern finance and investment theory.

<br>

### Liquidity and Market Activity

Liquidity refers to how easily an asset can be bought or sold without causing large price changes.

Highly liquid markets typically have:

- Large trading volume
- Narrow bid-ask spreads
- Rapid transaction execution

Examples of highly liquid assets include:

- Major stocks
- Government bonds
- Large currency pairs

Less liquid assets may experience:

- Higher volatility
- Larger spreads
- Greater difficulty finding buyers or sellers

Liquidity is critically important because it affects transaction costs, pricing stability, and overall market efficiency.

<br>

### Volatility and Market Risk

Financial markets are inherently uncertain. Prices fluctuate continuously as participants react to new information, economic changes, and investor psychology.

Volatility measures the degree of price variation over time and is often interpreted as a proxy for market risk.

Periods of elevated volatility may arise from:

- Economic recessions
- Financial crises
- Political instability
- Unexpected corporate news
- Changes in monetary policy

Understanding market volatility is essential for investment management, portfolio construction, and financial risk analysis.


--- PAGE ---

## Risk

Risk is an unavoidable component of investing and financial decision-making. In finance, risk refers to the possibility that actual outcomes will differ from expected outcomes. Investors generally seek higher returns as compensation for accepting greater uncertainty, which creates the fundamental trade-off between risk and reward.

Different forms of risk affect financial systems in different ways. Some risks originate from market-wide economic conditions, while others stem from individual borrowers, institutions, operational failures, or the inability to convert assets into cash efficiently.

Understanding risk is essential for portfolio construction, asset pricing, financial forecasting, and long-term investment planning.

<br>

### Types of Risk

Financial risk can be divided into several major categories:

- **Market Risk** — losses caused by changes in market prices
- **Credit Risk** — risk that a borrower fails to repay obligations
- **Liquidity Risk** — inability to buy or sell assets quickly without affecting price
- **Operational Risk** — failures arising from internal systems or processes
- **Inflation Risk** — reduction in purchasing power over time
- **Interest Rate Risk** — sensitivity of investments to changing interest rates
- **Currency Risk** — fluctuations in foreign exchange values
- **Systematic Risk** — market-wide risk that cannot be diversified away
- **Unsystematic Risk** — company-specific risk that can be reduced through diversification

In practice, financial institutions attempt to measure, model, and manage these risks simultaneously.

<br>

### Market Risk

Market risk refers to the possibility of losses caused by movements in financial markets. This includes changes in stock prices, bond prices, interest rates, exchange rates, and commodity prices.

Because financial markets are interconnected, market risk can spread rapidly across institutions and sectors.

One commonly used measurement is **Value at Risk (VaR)**, which estimates the maximum expected loss over a given time horizon under normal market conditions.

$$
VaR = z \cdot \sigma \cdot \sqrt{t}
$$

Where:
- $z$ = confidence interval z-score  
- $\sigma$ = portfolio volatility  
- $t$ = time horizon  

VaR is widely used by banks, hedge funds, and institutional investors for portfolio risk monitoring.

<br>

### Credit Risk

Credit risk is the possibility that a borrower or counterparty fails to meet financial obligations. This is especially important in lending, bond investing, and banking.

Examples include:
- A corporation defaulting on bonds
- A homeowner failing to repay a mortgage
- A bank counterparty failing during a transaction

A standard model for estimating expected credit losses is:

$$
EL = PD \times LGD \times EAD
$$

Where:
- $PD$ = probability of default  
- $LGD$ = loss given default  
- $EAD$ = exposure at default  

Credit rating agencies, banks, and institutional lenders use these models extensively when evaluating borrowers.

<br>

### Liquidity Risk

Liquidity risk occurs when an asset cannot be converted into cash quickly without significantly affecting its market price.

Highly liquid assets include:
- Major stocks
- Government bonds
- Money market instruments

Less liquid assets include:
- Real estate
- Private equity
- Rare collectibles
- Thinly traded securities

Liquidity problems often become severe during financial crises, when buyers disappear and market prices can fall rapidly.

Liquidity risk is especially important for hedge funds, banks, and institutions that may need rapid access to cash.

<br>

### Operational Risk

Operational risk refers to losses caused by failures in internal systems, processes, technology, or human behavior.

Examples include:
- Cybersecurity breaches
- Accounting fraud
- Trading errors
- System outages
- Regulatory failures
- Internal mismanagement

Unlike market or credit risk, operational risk often arises from organizational weaknesses rather than external market movements.

Modern financial firms invest heavily in:
- Compliance systems
- Internal controls
- Data security
- Risk monitoring infrastructure

<br>

### Risk Management Techniques

Risk management involves identifying, measuring, and reducing exposure to financial uncertainty.

Common techniques include:

- **Diversification**
  - Spreading investments across multiple assets to reduce concentration risk

- **Hedging**
  - Using derivatives or offsetting positions to reduce exposure

- **Asset Allocation**
  - Balancing portfolios between stocks, bonds, cash, and alternative assets

- **Insurance**
  - Transferring specific risks to another party

- **Stress Testing**
  - Simulating extreme market conditions to evaluate vulnerabilities

- **Position Limits**
  - Restricting exposure to individual investments or sectors

- **Risk-Adjusted Performance Metrics**
  - Evaluating returns relative to volatility or downside exposure

One widely used measure of risk-adjusted return is the **Sharpe Ratio**:

$$
S = \frac{R_p - R_f}{\sigma_p}
$$

Where:
- $R_p$ = portfolio return  
- $R_f$ = risk-free rate  
- $\sigma_p$ = portfolio volatility  

Effective risk management does not eliminate uncertainty entirely. Instead, it seeks to control exposure so that risks remain consistent with an investor’s objectives and tolerance for loss.


--- PAGE ---

## Taxes

Taxes play a major role in personal finance, investing, and business decision-making. In many cases, the profitability of an investment depends not only on the return generated, but also on how much of that return is retained after taxes are paid. Because taxes reduce net earnings, investors often evaluate investments on an after-tax basis rather than relying solely on raw returns. Tax systems vary between countries and jurisdictions, but most investment taxation falls into several major categories:

- Capital gains taxes
- Dividend taxes
- Interest income taxes
- Property taxes
- Corporate taxes

Understanding taxation is important because it directly affects:

- Investment strategy
- Portfolio construction
- Retirement planning
- Asset allocation
- Long-term wealth accumulation

<br>

### Taxation on Investments

Investment income is generally taxable in some form. Different types of investments may receive different tax treatment depending on:

- Holding period
- Type of asset
- Account structure
- Jurisdictional law

For example:

- Stocks may generate taxable capital gains and dividends
- Bonds may generate taxable interest income
- Real estate may involve property taxes and capital gains taxes
- Retirement accounts may defer taxation until withdrawal

Because taxes reduce realized profits, investors often seek strategies that improve after-tax performance rather than maximizing nominal returns alone.

<br>

### Capital Gains

A capital gain occurs when an asset is sold for more than its purchase price.

#### Capital Gains Formula

$$
\text{Gain} =
P_{sell} - P_{buy}
$$

Where:
- $P_{sell}$ = selling price  
- $P_{buy}$ = purchase price  

If the result is negative, the investment generates a capital loss rather than a gain.

Capital gains are commonly associated with:

- Stocks
- Real estate
- Cryptocurrencies
- Mutual funds
- Collectibles

Many tax systems distinguish between:

- **Short-term capital gains** — gains on assets held for shorter periods
- **Long-term capital gains** — gains on assets held for longer periods

Long-term gains are often taxed at lower rates in order to encourage long-term investing.

<br>

### Dividend and Interest Taxes

Many investments generate recurring income in addition to price appreciation.

Examples include:

- Stock dividends
- Bond coupon payments
- Savings account interest

These payments are often taxed as income when received.

Dividend taxation may vary depending on whether dividends are classified as:

- Qualified dividends
- Ordinary dividends

Interest income from bonds or savings accounts is generally taxed at ordinary income tax rates unless special exemptions apply.

<br>

### After-Tax Return

The after-tax return measures the actual return retained by an investor after taxes are deducted.

#### After-Tax Return Formula

$$
R_{after} =
R(1 - t)
$$

Where:
- $R$ = pre-tax return  
- $t$ = tax rate  

This calculation highlights an important financial principle:

- Two investments with identical pre-tax returns may produce very different after-tax outcomes.

As a result, investors frequently compare investments using after-tax performance metrics rather than nominal returns alone.

<br>

### Tax-Advantaged Accounts

Many financial systems provide specialized investment accounts that offer tax benefits in order to encourage saving and investing.

Examples may include:

- Retirement accounts
- Education savings accounts
- Health savings accounts

Common tax advantages include:

- Tax-deferred growth
- Tax-free withdrawals
- Reduced taxable income contributions

These accounts can significantly increase long-term investment growth because fewer funds are lost to annual taxation.

<br>

### Tax Planning Strategies

Tax planning involves structuring investments and financial decisions in ways that legally reduce tax liability.

Common strategies include:

- Holding investments long enough to qualify for lower long-term capital gains rates
- Using tax-advantaged accounts
- Offsetting gains with investment losses
- Diversifying across taxable and non-taxable assets
- Timing the sale of assets strategically

Effective tax planning can substantially improve long-term wealth accumulation because investment growth compounds more efficiently when fewer earnings are lost to taxation each year.

<br>

### Taxes and Economic Behavior

Taxes influence both individual and institutional decision-making throughout financial markets.

Changes in tax policy can affect:

- Consumer spending
- Corporate investment
- Housing markets
- Stock market activity
- International capital flows

Because taxes alter incentives, governments often use tax policy as a tool for influencing economic behavior and broader macroeconomic conditions.

<br>

### Capital Gains Tax Formula

The tax owed on a capital gain can be estimated using:

$$
\text{Capital Gains Tax}
=
(P_{sell} - P_{buy})
\cdot t
$$

Where:
- $P_{sell}$ = selling price  
- $P_{buy}$ = purchase price  
- $t$ = applicable capital gains tax rate  

This formula illustrates how taxation directly reduces realized investment profit.

<br>

### Net Investment Profit After Taxes

The net profit retained after taxes can be expressed as:

$$
\text{Net Profit}
=
(P_{sell} - P_{buy})
(1 - t)
$$

Where:
- $t$ = tax rate applied to the gain  

This calculation is useful when comparing investments with different tax treatments.

<br>

### Dividend After-Tax Income

The after-tax income generated from dividends can be calculated as:

$$
D_{after}
=
D(1 - t)
$$

Where:
- $D$ = dividend received  
- $t$ = dividend tax rate  

This demonstrates that dividend-producing investments may have different effective yields depending on taxation.

<br>

### Interest Income After Taxes

Interest-bearing investments are often evaluated on an after-tax basis.

$$
I_{after}
=
I(1 - t)
$$

Where:
- $I$ = interest income  
- $t$ = income tax rate  

This is particularly important when comparing taxable and tax-exempt bonds.

<br>

### Tax-Equivalent Yield

Tax-equivalent yield is commonly used to compare tax-free investments (such as certain municipal bonds) to taxable investments.

$$
TEY
=
\frac{
Y_{tax\text{-}free}
}{
1 - t
}
$$

Where:
- $Y_{tax\text{-}free}$ = yield on tax-free investment  
- $t$ = investor's marginal tax rate  

This formula estimates the taxable yield required to match the return of a tax-free investment.

<br>

### Effective Tax Rate

The effective tax rate measures the proportion of total income paid in taxes.

$$
\text{Effective Tax Rate}
=
\frac{
\text{Total Taxes Paid}
}{
\text{Total Income}
}
$$

This differs from marginal tax rates because it reflects the overall tax burden across all income levels.

<br>

### Marginal Tax Rate

The marginal tax rate is the tax rate applied to the next additional dollar of income earned.

Conceptually:

$$
\text{Marginal Tax Rate}
=
\frac{
\Delta \text{Taxes}
}{
\Delta \text{Income}
}
$$

Marginal rates are important because many financial decisions depend on how additional income will be taxed rather than average taxation overall.

<br>

### Real After-Tax Return

Inflation further reduces the purchasing power of investment returns. A simplified approximation of real after-tax return is:

$$
R_{real}
\approx
R(1 - t) - \pi
$$

Where:
- $R$ = nominal investment return  
- $t$ = tax rate  
- $\pi$ = inflation rate  

This formula highlights that investors must account for both taxes and inflation when evaluating true wealth growth.

<br>

### Property Tax Formula

Real estate ownership often involves recurring property taxes.

$$
\text{Property Tax}
=
\text{Property Value}
\cdot
\text{Tax Rate}
$$

Where:
- Property Value = assessed value of the property  
- Tax Rate = local property tax percentage  

Property taxes can significantly affect long-term real estate investment profitability.

<br>

### Corporate Tax Formula

Corporate profit taxation can be approximated as:

$$
\text{Corporate Tax}
=
\text{Taxable Income}
\cdot t
$$

Where:
- $t$ = corporate tax rate  

Corporate taxation affects business profitability, retained earnings, and shareholder returns.

<br>

### Tax Loss Harvesting

Investors may offset gains using realized losses.

$$
\text{Net Capital Gain}
=
\text{Capital Gains}
-
\text{Capital Losses}
$$

This strategy can reduce taxable investment income and improve after-tax portfolio efficiency.

<br>

### Required Pre-Tax Return

To achieve a desired after-tax return, investors may calculate the required pre-tax return:

$$
R_{pre}
=
\frac{
R_{after}
}{
1 - t
}
$$

Where:
- $R_{after}$ = desired after-tax return  
- $t$ = tax rate  

This formula is useful when comparing investments across different tax environments.