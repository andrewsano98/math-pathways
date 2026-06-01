<!--
title: "Math in Sports"
output: html_document
bibliography: rmarkdown.bib
-->


<div class="pathway-card">

  <img
    src="markdown/pathway_images/sports_photo_1.jpeg"
    alt="Placeholder Text"
    class="pathway-image"
  />

  <div class="pathway-title-overlay">
    <h1 class="pathway-title">
      Sports
    </h1>
  </div>

</div>

<br>

###  What can I do?
- Analyze strategies, formations, and movement patterns within team play  
- Calculate averages, percentages, and probabilities related to gameplay outcomes  
- Organize practice routines and performance goals for skill development  
- Study opponent tendencies and game situations to improve decision-making  
- Use technology and video analysis tools to review athletic performance  
- Analyze player performance, injury risk, and team efficiency using statistical software and tracking systems  
- Work with motion capture, wearable sensors, and biomechanics data to improve athletic performance  
- Use spreadsheets, SQL databases, and visualization tools to evaluate scouting and game strategy  
- Model probabilities and outcomes for drafting, scheduling, and sports analytics applications  
- Interpret real-time game data and video analysis software to support coaching decisions  
- Communicate performance metrics and analytical findings to athletes, coaches, and organizations  

<br>

###  What math concepts do I need to know?
- Statistics  
- Probability  
- Data Analysis  
- Ratios and Proportions  
- Algebra  
- Graphing and Trends  
- Geometry  
- Optimization  
- Performance Metrics  

--- PAGE ---

## American Football

Football techniques and plays are structured around creating spatial and timing advantages through coordinated movement, formation design, and situational decision-making. Offenses use a combination of passing routes, blocking schemes, motion, and play-action to manipulate defensive alignment and generate mismatches in coverage or gaps in the run defense. Defenses respond with layered coverage systems, pressure packages, and gap control strategies designed to disrupt timing, limit yardage, and force turnovers. At a strategic level, football is a continuous optimization problem where both sides attempt to control space, predict opponent behavior, and maximize expected value on each play.

<br>

### Offensive Techniques & Plays

Effective offensive football strategy focuses on creating and exploiting spatial mismatches before the defense can react. Offenses use motion, spacing, timing, deception, and route combinations to open passing lanes or running corridors. Short-passing systems emphasize consistency and controlled gains, while spread and vertical systems stretch defenses horizontally and vertically. Good play design forces conflicting defensive assignments and creates uncertainty through play-action and option concepts. Overall, offenses aim to maximize available pathways while minimizing defensive efficiency and reaction time.

<br>

| Techniques & Plays | When to Use | Advantages & Disadvantages |
|---|---|---|
| West Coast Offense | Against defenses that prevent deep passing or prioritize blitz containment | + High completion rate and controlled progression<br>- Limited explosive play potential |
| Spread Offense | When maximizing space and stressing defensive coverage horizontally | + Forces defensive stretching and creates mismatches<br>- Can struggle in short-yardage or physical conditions |
| Air Raid Offense | When relying on high-volume passing and quarterback efficiency | + Maximizes passing opportunities and tempo<br>- Can be vulnerable to strong pass rush |
| Zone Run Scheme (Inside/Outside Zone) | Against aggressive or over-pursuing defensive fronts | + Creates flexible running lanes and cutback options<br>- Requires strong timing and offensive line cohesion |
| Play-Action Passing | When the run game is effective and defenses are committed to stopping it | + Creates deep passing opportunities through deception<br>- Less effective if run threat is weak |
| RPO (Run-Pass Option) | Against reactive defenses with identifiable linebackers or coverage cues | + Forces defenders into conflict and delayed decisions<br>- Risk of negative plays if read incorrectly |
| Mesh Concept | Against man coverage or tight zone structures | + Creates natural rubs and separation opportunities<br>- Timing-dependent and requires precision |
| Flood Concept (3-Level Sideline Stretch) | Against zone defenses that struggle with sideline coverage | + Overloads one side of the field and stresses coverage depth<br>- Can be limited by strong boundary defenders |
| Motion-Based Offense | Before the snap to identify coverage and create mismatches | + Reveals defensive intentions and creates leverage advantages<br>- Can add complexity and timing issues if overused |

<br>

### Defensive Techniques & Plays

Effective defensive football strategy focuses on restricting space, limiting high-value lanes, and increasing pressure on offensive decision-making. Defenses maintain structure while balancing coverage, pursuit, and pass rush to prevent mismatches. Zone coverage emphasizes spatial control, while man coverage focuses on individual containment. Blitzes and disguised coverages reduce quarterback time and disrupt timing before plays develop. Strong defenses continuously adjust to motion and route combinations to limit offensive opportunities.

<br>

| Techniques or Plays | When to Use | Advantages & Disadvantages |
|---|---|---|
| Cover 2 Zone Defense | Against offenses that rely on deep passing or boundary shots | + Strong deep-field protection and prevents explosive plays<br>- Vulnerable to seams and short/intermediate completions |
| Cover 3 Zone Defense | Against balanced offenses or run-heavy schemes | + Good deep coverage with strong field balance<br>- Can be stressed in intermediate zones and flats |
| Cover 1 (Man-to-Man Coverage) | When matching up athletes individually or applying pressure schemes | + Tight coverage and strong man accountability<br>- Susceptible to mismatches and pick plays |
| Tampa 2 Defense | Against offenses using intermediate passing concepts | + Strong middle-field protection with adaptive linebacker support<br>- Can be vulnerable to deep seams behind linebackers |
| Blitz Packages | When forcing quick decisions or disrupting timing-based offenses | + Creates pressure and increases turnover potential<br>- Risk of leaving receivers open due to reduced coverage |
| Zone Blitz | Against quarterbacks who read coverage pre-snap or rely on protection schemes | + Generates pressure while disguising coverage<br>- Requires high coordination and can be risky if misread |
| Match Coverage (Pattern Matching Defense) | Against complex route combinations and motion-heavy offenses | + Adapts dynamically to offensive routes and reduces predictable gaps<br>- High cognitive and communication demands can lead to breakdowns |


--- PAGE ---

## Fantasy Football

Fantasy football is a data-driven game of projecting real-world player performance into scoring outcomes, where roster decisions are shaped by usage, efficiency, and situational context. Players are evaluated not only by raw talent but by opportunity—such as snap share, target volume, red zone role, and offensive scheme—and how those opportunities translate into consistent fantasy production. Successful fantasy strategy blends statistical modeling, matchup analysis, and risk management to balance high-ceiling players with stable weekly contributors. At its core, fantasy football is a probabilistic optimization problem, where managers aim to maximize expected points while accounting for variance, injuries, and game script volatility.

<br>

| Category | Key Fantasy Football Metrics |
|---|---|
| Usage / Opportunity | Snap counts, snap share, routes run, route participation rate, targets, target share, carries, carry share |
| Volume (Team Context) | Team pass attempts, team rush attempts, team plays per game (pace) |
| Efficiency | Yards per target, yards per carry, aDOT, YAC |
| Air Game Role | Air yards, air yards share |
| Scoring | Receptions, receiving yards, rushing yards, receiving TDs, rushing TDs, total touchdowns |
| Red Zone / High-Value Usage | Red zone targets, red zone carries, red zone touches, goal-line carries, red zone team efficiency |
| Game Environment | Game script indicators (score differential), opponent defensive ranking vs position |
| Player Availability | Injury status / availability |
| Team / Line Factors | Quarterback efficiency, offensive line metrics (pressure rate, run blocking) |
| Outcome Metrics | Fantasy points scored, expected fantasy points (xFP inputs) |

<br>

Using these metrics, we can calculate statistics that will give us an informed decision on who to start and who to sit for fantasy teams and for predicting winning teams.

<br>

### Snap Share

Measures the proportion of a team’s offensive plays in which a player is on the field, capturing overall usage and opportunity.

$$
\text{Snap Share} = \frac{\text{Player Snaps}}{\text{Team Offensive Snaps}}
$$

<br>

### Route Participation Rate

Measures how often a receiver is involved in passing plays by running routes.

$$
\text{Route Rate} = \frac{\text{Routes Run}}{\text{Team Pass Plays}}
$$ 

<br>

### Target Share

Measures a player’s share of passing targets within the offense. One of the strongest predictors of fantasy output.

$$
\text{Target Share} = \frac{\text{Player Targets}}{\text{Team Pass Attempts}}
$$  

<br>

### Carry Share

Measures a running back’s share of rushing workload. Defines RB workload dominance.

$$
\text{Carry Share} = \frac{\text{Player Carries}}{\text{Team Rush Attempts}}
$$

<br>

### Air Yards Share

Measures a player’s share of total intended passing depth. Captures deep-threat involvement and upside potential.

$$
\text{Air Yards Share} = \frac{\text{Player Air Yards}}{\text{Team Air Yards}}
$$  

<br>

### Red Zone Usage Rate

Measures how often a player is involved in plays inside the opponent’s 20-yard line. Strong TD predictor (high correlation with boom games).

$$
\text{RZ Usage} = \frac{\text{Player RZ Touches}}{\text{Team RZ Plays}}
$$ 

<br>

### Yards Per Target

Measures receiving efficiency per target.

$$
YPT = \frac{\text{Receiving Yards}}{\text{Targets}}
$$

<br>

### Yards Per Carry

Measures rushing efficiency per attempt. Important but high-variance (less stable than volume metrics).

$$
YPC = \frac{\text{Rushing Yards}}{\text{Carries}}
$$

<br>

### Explosive Play Rate

Measures the frequency of high-impact plays above a defined yardage threshold.

$$
\text{Explosive Rate} = \frac{\text{Plays ≥ Threshold}}{\text{Total Plays}}
$$ 

<br>

### Touchdown Rate

Measures scoring efficiency per touch. Used carefully due to randomness, but important for ceiling outcomes.

$$
\text{TD Rate} = \frac{\text{Touchdowns}}{\text{Touches}}
$$

<br>

### Expected Fantasy Points per Opportunity

Measures expected scoring efficiency per touch or target.

$$
\text{xFP/Opp} = \frac{\text{Expected Fantasy Points}}{\text{Touches + Targets}}
$$ 

<br>

### Implied Team Scoring

Estimates expected scoring environment based on Vegas totals. Proxy for scoring environment strength.

$$
\text{Implied Points} = \frac{\text{Vegas Total} + \text{Opponent Total}}{2}
$$

<br>

### Pass Rate Over Expectation (PROE)

Measures how pass-heavy an offense is relative to expectation. Indicates offensive aggressiveness.

$$
\text{PROE} = \text{Actual Pass Rate} - \text{Expected Pass Rate}
$$

<br>

### Air Yards per Target

Measures depth of target in the passing game. Distinguishes deep vs short-area roles.

$$
AYPT = \frac{\text{Air Yards}}{\text{Targets}}
$$

<br>

### Opportunity Score

Measures overall offensive role using weighted usage inputs.

$$
\text{Opportunity Score} = a(\text{Snap Share}) + b(\text{Target Share}) + c(\text{Carry Share})
$$

<br>

### Expected Fantasy Points (xFP)

Estimates expected scoring based on underlying opportunity.

$$
xFP = \sum P_i V_i
$$

Examples include touchdowns, receptions, and yardage outcomes.

<br>

### Touchdown Probability

Estimates likelihood of scoring based on usage context.

$$
P(TD) = \frac{\text{Red Zone Opportunities}}{\text{Total Opportunities}}
$$ 

<br>

### Traits Correlated with Boom Games

- High snap share
- High route participation
- High air yards share
- Strong red zone usage
- Participation in high-total games
- Fast-paced offenses
- Big-play ability
- QB aggressiveness
- Weak opposing secondary or soft coverage matchups
- Players with low efficiency but high volume upside
- Clear “alpha” roles
- Positive game script

<br>

### Traits Correlated with Bust Games

- Low or inconsistent snap share
- Low target share or unclear pecking order
- Dependence on low volume + efficiency only
- No red zone role
- Run-heavy offenses
- Slow-paced offenses
- Heavy reliance on deep TDs only
- Strong opposing defense
- Negative game script without receiving role
- Highly volatile efficiency metrics
- Crowded target distribution
- Injury-limited or “managed snap” players
- QB instability or low passing efficiency ceiling


--- PAGE ---

## Baseball Plays & Strategies

Baseball strategy is built around the interaction between pitching, hitting, defense, and base running, where each decision is shaped by situational context and probability. Plays are designed to either maximize run creation or minimize opponent scoring by exploiting matchups, timing, and defensive positioning. Because outcomes are highly variable and constrained by limited opportunities, teams rely on structured tactical choices such as bunts, steals, shifts, and pitch sequencing to tilt expected value over time. At its core, baseball strategy is a system of controlled risk-taking, where small situational advantages compound across innings to determine overall game outcome.

<br>

### Offensive Strategies and Plays

Effective offensive baseball strategy focuses on creating scoring opportunities by manipulating defensive positioning, pitcher behavior, timing, and base-runner pressure. Offenses use tools like bunts, steals, hit-and-runs, sacrifice plays, and disciplined plate appearances to force defensive reactions under uncertainty. Some systems emphasize power and extra-base hits, while others rely on small ball to steadily advance runners through incremental gains. Overall, offense aims to maximize run production and runner advancement while minimizing outs.

<br>

| Play or Technique | When to Use | Advantages & Disadvantages |
|---|---|---|
| Bunting | When a runner needs to advance or the defense is positioned deep | + Advances runners and pressures defense<br>- Gives up power potential and risks easy outs |
| Sacrifice bunt | Early or close games with runners on base | + Improves scoring position<br>- Costs an out |
| Squeeze play | Runner on third with less than two outs | + Can guarantee a run<br>- High risk if bunt fails |
| Hit-and-run | Runner on first during contact-oriented at-bats | + Opens holes in defense and advances runner<br>- Risks double plays or strike-em-out throw-em-out |
| Stealing bases | Against slow pitchers or weak catchers | + Creates scoring chances<br>- Risk of being thrown out |
| Delayed steal | When defense relaxes after pitch | + Catches defense off guard<br>- Timing-sensitive |
| Double steal | Multiple runners on base with pressure opportunities | + Distracts defense and advances runners<br>- Can lead to multiple outs |
| Tagging up | Fly ball with runner on base | + Advances runners after catches<br>- Risk of strong defensive throws |
| Sacrifice fly | Runner on third with less than two outs | + Scores a run without a hit<br>- Produces an out |
| Suicide squeeze | Runner breaks for home before bunt contact | + Extremely aggressive scoring tactic<br>- Very risky if missed |
| Safety squeeze | Runner waits for bunt contact before running home | + Safer than suicide squeeze<br>- Easier for defense to react |
| Small ball | Low-scoring or close games | + Manufactures runs consistently<br>- Less explosive offense |
| Power hitting | Need for extra-base hits or quick scoring | + High scoring potential<br>- More strikeouts |
| Contact hitting | Situations requiring runners to advance | + Consistent ball-in-play pressure<br>- Less home run potential |
| Working the count | Against pitchers with control issues | + Tires pitchers and earns walks<br>- Can lead to strikeouts looking |
| Drawing walks | Patient offensive approach | + Free baserunners<br>- Relies on pitcher mistakes |
| Pinch hitting | Weak hitter in key moment | + Better offensive matchup<br>- Uses bench resources |
| Pinch running | Slow runner on base late in game | + Improves speed and steal threat<br>- Removes original player |
| Calling for steals | Aggressive offensive pressure | + Forces defensive mistakes<br>- Can erase baserunners |
| Baserunner decoys | Distracting defenders | + Creates confusion<br>- Requires coordination |
| Fake bunt slash | Showing bunt before swinging | + Surprises defense<br>- Hard to execute consistently |
| Situational hitting | Specific scoring scenarios | + Improves team efficiency<br>- Requires disciplined hitters |
| Advancing runners | Productive outs or contact situations | + Moves runners into scoring position<br>- May sacrifice offensive potential |
| Manufacturing runs | Tight games against strong pitching | + Produces steady scoring opportunities<br>- Requires precise execution |

<br>

### Defensive Strategies and Plays

Effective defensive baseball strategy focuses on limiting offensive efficiency by controlling space, reducing scoring chances, and disrupting hitter expectations. Defenses adjust positioning, pitch sequencing, and matchups based on batter tendencies, game state, and statistical patterns. Pitchers and catchers vary pitch speed, location, and movement to distort timing, while fielders optimize coverage to suppress hits. Defensive strategy also emphasizes risk management through bullpen usage, pitch counts, cutoff plays, and double-play positioning, with the goal of minimizing successful offensive outcomes and limiting base advancement.

<br>

| Play or Technique | When to Use | Advantages & Disadvantages |
|---|---|---|
| Pickoff attempt | When runners take large leads | + Prevents steals and pressures runners<br>- Bad throws can advance runners |
| Intentional walk | Dangerous hitter at the plate | + Avoids strong batter<br>- Adds free baserunner |
| Pitchout | Suspected steal attempt | + Improves chance to catch runner<br>- Wastes a pitch if guess is wrong |
| Infield shift | Pull-heavy hitters at bat | + Cuts off likely hit zones<br>- Leaves open field space elsewhere |
| Defensive positioning | Adjusting to hitter tendencies or game situation | + Improves defensive efficiency<br>- Can fail if hitter adapts |
| Double play | Runner on first with less than two outs | + Quickly ends threats<br>- Requires precise execution |
| Relay throw | Deep outfield hits | + Limits extra bases<br>- Mistakes can allow more advancement |
| Cutoff play | Outfield throws heading to infield | + Controls runner advancement<br>- Miscommunication can hurt defense |
| Rundown (pickle) | Runner trapped between bases | + Can secure outs<br>- Errors may let runners escape |
| Pitch framing | Catcher receiving borderline pitches | + Can earn extra strikes<br>- Depends on umpire perception |
| Pitch sequencing | Setting up hitters with changing pitch types | + Keeps batters guessing<br>- Predictable patterns can backfire |
| Bullpen management | Late innings or pitching fatigue | + Keeps pitchers fresh<br>- Overuse weakens bullpen depth |
| Starting pitcher rotation | Across long seasons | + Maintains pitcher health<br>- Injuries disrupt planning |
| Lefty-righty matchup strategy | Favorable batter-pitcher handedness | + Creates statistical advantages<br>- Can limit flexibility |
| Defensive substitution | Protecting a lead late | + Stronger fielding<br>- May weaken offense |
| Playing the corners in | Preventing bunt advances | + Stops small ball tactics<br>- Opens larger gaps down lines |
| Guarding the lines | Preventing extra-base hits late in games | + Limits doubles<br>- Creates middle-field openings |
| Outfield shading | Adjusting to hitter spray tendencies | + Better defensive coverage<br>- Vulnerable if hitter changes approach |
| Managing pitch counts | Preventing pitcher fatigue | + Reduces injury risk<br>- May remove effective pitchers early |
| Wheel play | Defending expected sacrifice bunts | + Aggressive anti-bunt defense<br>- Leaves defensive vulnerabilities |
| Hidden ball trick | Catching unaware baserunners | + Surprise out opportunity<br>- Rarely works repeatedly |
| Quick pitch | Catching hitter unprepared | + Disrupts timing<br>- Risk of illegal pitch call |
| Backdoor breaking pitch | Fooling hitters expecting outside ball | + Freezes hitters<br>- Difficult pitch location |
| High fastball strategy | Against uppercut swings | + Generates swings and misses<br>- Mistakes get hit hard |
| Ground-ball pitching | With runners on base | + Creates double-play chances<br>- Grounders can sneak through |
| Fly-ball pitching | In large ballparks or weak power lineups | + Easier outs in spacious fields<br>- Vulnerable to home runs |


--- PAGE ---

## Baseball Analytics

Baseball analytics is a quantitative approach to understanding and predicting player and team performance using statistical models, data tracking systems, and machine learning methods. Modern analysis moves beyond traditional box-score statistics to evaluate underlying processes such as pitch quality, batted-ball data, plate discipline, defensive positioning, and run expectancy. By integrating large-scale datasets with contextual game information, analysts aim to isolate skill from variance and better estimate true talent levels over time. At its core, baseball analytics treats the game as a probabilistic system, where outcomes emerge from measurable inputs shaped by strategy, environment, and randomness.

<br>

| Category | Key Baseball Analytics Metrics |
|---|---|
| Batting Opportunity / Usage | Plate appearances (PA), at-bats (AB), batting order position |
| Contact Volume | Hits, singles, doubles, triples, home runs, total bases |
| Plate Discipline | Walk rate (BB%), strikeout rate (K%), chase rate, swing rate |
| Power / Exit Profile | Exit velocity, launch angle, hard hit rate, barrel rate |
| Advanced Hitting Value | wOBA, OPS, ISO (isolated power), wRC+ |
| Run Production | Runs, RBIs, runs created, clutch hits |
| Baserunning | Stolen bases, caught stealing, sprint speed, base running runs |
| Pitching Volume | Innings pitched (IP), batters faced (BF), pitch count |
| Pitching Outcomes | Strikeouts (K), walks (BB), hits allowed, home runs allowed |
| Pitch Quality | Velocity, spin rate, pitch movement, release point |
| Run Prevention | ERA, FIP, xFIP, SIERA |
| Batted Ball Profile | Ground ball %, fly ball %, line drive %, pull/oppo %
| Defensive Metrics | Defensive runs saved (DRS), UZR, outs above average (OAA) |
| Game Context | Opposing pitcher quality, park factors, weather conditions |
| Outcome Metrics | WAR, fantasy points, win probability added (WPA) |

<br>

Using these metrics, we can calculate statistics that will give us an informed decision on who to start and who to sit for fantasy teams and for predicting winning teams.

<br>

### Batting Average (AVG)

Measures hitting efficiency per at-bat and is most useful as a basic contact success indicator, though it does not capture walks or power.

$$
AVG = \frac{\text{Hits}}{\text{At Bats}}
$$

<br>

### On-Base Percentage (OBP)

Measures how frequently a player reaches base and is a primary indicator of offensive opportunity creation.

$$
OBP = \frac{\text{Hits} + \text{Walks} + \text{Hit By Pitch}}{\text{At Bats} + \text{Walks} + \text{Hit By Pitch} + \text{Sacrifice Flies}}
$$

<br>

### Slugging Percentage (SLG)

Measures power output per at-bat by weighting extra-base hits more heavily, making it a key proxy for scoring upside.

$$
SLG = \frac{\text{Total Bases}}{\text{At Bats}}
$$

<br>

### On-Base Plus Slugging (OPS)

Combines on-base ability and power to estimate overall offensive production in a simplified composite metric.

$$
OPS = \text{On Base Percentage} + \text{Slugging Percentage}
$$

<br>

### Weighted On-Base Average (wOBA)

Measures overall offensive value by assigning run-based weights to each offensive outcome, making it one of the strongest single-number hitting metrics.

<br>

$$
wOBA = \frac{
w_1 \cdot \text{Walks} +
w_2 \cdot \text{Hit By Pitch} +
w_3 \cdot \text{Singles} +
w_4 \cdot \text{Doubles} +
w_5 \cdot \text{Triples} +
w_6 \cdot \text{Home Runs}
}{
\text{Plate Appearances}
}
$$

<br>

### Earned Run Average (ERA)

Measures runs allowed per nine innings and is a traditional outcome-based pitching performance metric.

$$
ERA = \frac{\text{Earned Runs} \cdot 9}{\text{Innings Pitched}}
$$

<br>

### Fielding Independent Pitching (FIP)

Measures pitcher performance based only on outcomes they directly control, making it a better “skill estimate” than ERA.

$$
FIP = \frac{
13 \cdot \text{Home Runs Allowed} +
3 \cdot \text{Walks Allowed} -
2 \cdot \text{Strikeouts}
}{
\text{Innings Pitched}
} + \text{League Constant}
$$

<br>

### Strikeout Rate (K%)

Measures pitching dominance by quantifying how often a pitcher generates strikeouts per batter faced.

$$
K\% = \frac{\text{Strikeouts}}{\text{Batters Faced}}
$$

<br>

### Walk Rate (BB%)

Measures pitching control by quantifying how often a pitcher issues free passes.

$$
BB\% = \frac{\text{Walks Allowed}}{\text{Batters Faced}}
$$

<br>

### Walks & Hits per Inning Pitched (WHIP)

Measures baserunner suppression by tracking how many walks and hits a pitcher allows per inning.

$$
WHIP = \frac{\text{Walks Allowed} + \text{Hits Allowed}}{\text{Innings Pitched}}
$$

<br>

### Defensive Runs Saved (DRS)

Measures defensive value by estimating how many runs a player saves compared to an average defender.

$$
DRS = \sum (\text{Plays Made} - \text{Expected Plays}) \cdot \text{Run Value}
$$

<br>

### Ultimate Zone Rating (UZR)

Measures defensive value by breaking performance into range, errors, arm strength, and double plays.

$$
UZR = R_{range} + R_{error} + R_{arm} + R_{double\ play} - R_{misc}
$$

<br>

### Batting Average on Balls at Play (BABIP)

Measures how often balls in play become hits, used to separate skill from luck and evaluate regression potential.

$$
BABIP = \frac{\text{Hits} - \text{Home Runs}}{\text{At Bats} - \text{Strikeouts} - \text{Home Runs} + \text{Sacrifice Flies}}
$$

<br>

### Hard Hit Rate

Measures frequency of high-quality contact above a velocity threshold (typically 95+ mph), used as a proxy for power consistency.

$$
\text{Hard Hit Rate} = \frac{\text{Hard Hit Balls}}{\text{Total Batted Balls}}
$$

<br>

### Traits Correlated with Boom Games

- High plate appearance volume
- Strong batting order position
- High hard-hit rate
- High barrel rate
- Strong isolated power profiles
- Favorable ballpark factors
- Weak opposing starting pitcher matchup
- High fly-ball rate
- High stolen base opportunity
- Lineup strength behind hitter
- Positive run environment
- Batters facing high pitch count pitchers
- Strong left/right platoon advantage
- Players with multi-hit + extra-base hit potential

<br>

### Traits Correlated with Bust Games

- Low plate appearances
- Heavy platoon disadvantage
- High strikeout rate
- Low walk rate / on-base ability
- Weak contact quality metrics
- Ground-ball heavy hitters
- Facing elite starting pitchers
- Cold or pitcher-friendly ballparks
- Low implied team totals
- Lineup instability
- Dependence on HR-or-bust profiles
- Low stolen base opportunity
- Teams with weak lineup protection
- Poor recent form combined with skill regression signals


--- PAGE ---

## Basketball Plays & Techniques

Basketball techniques and plays are structured around creating efficient scoring opportunities through spacing, movement, and rapid decision-making under defensive pressure. Offenses use sets such as pick-and-rolls, isolations, cuts, and off-ball screens to generate mismatches, open shots, or driving lanes, while continuously adapting to defensive coverage schemes. Defensive strategies focus on limiting shot quality and controlling space through man-to-man assignments, zone structures, help defense, and switching concepts designed to disrupt offensive rhythm. At a strategic level, basketball is a fluid, possession-based system where teams aim to maximize shot value while minimizing defensive breakdowns through coordinated movement and timing.

<br>

### Offensive Techniques

Effective offensive basketball strategy focuses on creating high-quality scoring opportunities by manipulating spacing, defensive positioning, and timing through coordinated movement and ball handling. Offenses use actions such as pick-and-rolls, drives, kick-outs, off-ball screens, and cuts to force defensive rotations and generate mismatches or open shots. Some systems emphasize perimeter shooting and pace to stretch defenses horizontally, while others rely on post play and half-court execution to create efficient interior scoring. Overall, offense aims to maximize shot quality and scoring efficiency while minimizing turnovers and low-value possessions.

<br>

| Techniques & Plays | When to Use | Advantages & Disadvantages |
|---|---|---|
| Motion Offense | Against disciplined defenses that rely on man coverage and switching | + Creates constant defensive confusion and open looks<br>- Requires high stamina and coordination |
| Pick-and-Roll | When exploiting mismatches or targeting slow or indecisive defenders | + Forces defensive decision-making and creates advantages<br>- Can be predictable if overused |
| Four-Out One-In Spacing | When aiming to open driving lanes and maximize spacing | + Expands driving lanes and improves offensive spacing<br>- Can limit interior presence if not balanced |
| Drive-and-Kick | When perimeter shooters are available and defenses collapse on drives | + Creates high-quality perimeter shots<br>- Relies heavily on shooting consistency |
| Isolation (Iso) | Late-clock situations or when a strong mismatch is identified | + Maximizes advantage for elite scorers<br>- Can stagnate offense and reduce ball movement |
| Transition Offense | After turnovers, rebounds, or fast defensive stops | + Generates high-efficiency scoring before defense sets<br>- Higher turnover risk due to pace |
| Shot Selection | Throughout all offensive possessions as a guiding principle | + Improves overall efficiency and scoring value<br>- Requires discipline and good decision-making |
| Three-Point Spacing | When building offenses around perimeter shooting efficiency | + Increases scoring variance in offensive favor<br>- Vulnerable to cold shooting stretches |
| Ball Movement | Against set defenses that are difficult to break down individually | + Increases defensive breakdowns and open shots<br>- Can lead to turnovers if rushed |
| Assist Chains | When offenses rely on teamwork and layered passing reads | + Produces high-quality, assisted shot opportunities<br>- Requires cohesion and strong passing skill |

<br>

### Defensive Techniques

Effective defensive basketball strategy focuses on limiting offensive efficiency by controlling space, disrupting timing, and reducing shot quality through coordinated team coverage. Defenses use man-to-man schemes, zone structures, switching, help defense, and ball pressure to force difficult shots and break offensive rhythm. Strong defensive systems prioritize protecting the paint, contesting perimeter attempts, and preventing easy mismatches through communication and rotation. Overall, defense aims to minimize opponent scoring opportunities while increasing forced errors, low-value shots, and inefficient possessions.

<br>

| Techniques & Plays | When to Use | Advantages & Disadvantages |
|---|---|---|
| Man-to-Man Defense | When defenders can match up well individually or against structured offenses | + Strong accountability and pressure on ball handlers<br>- Vulnerable to mismatches and screens |
| Zone Defense | Against poor outside shooting teams or to protect fatigued defenders | + Protects paint and conserves energy<br>- Can be exploited by good perimeter shooting and ball movement |
| Help Defense | When protecting against drives and breakdowns in primary coverage | + Reduces easy baskets and drives<br>- Can lead to open perimeter shots if rotations are slow |
| Switching Defense | Against heavy screening actions and pick-and-roll offenses | + Neutralizes screens and reduces mismatches<br>- Can create size/speed mismatches if poorly executed |
| Drop Coverage | Against pick-and-roll offenses with limited pull-up shooting threats | + Protects rim and forces jump shots<br>- Allows space for mid-range or pull-up shooters |
| Hedge Defense | Against skilled ball handlers in pick-and-roll situations | + Disrupts timing and forces reset<br>- Can overextend defenders and open passing lanes |
| Trap / Double Team | To force turnovers or disrupt elite ball handlers | + Creates pressure and steals opportunities<br>- Leaves offensive players open elsewhere |
| Full-Court Press | Late game or to disrupt inbounding and rhythm | + Forces turnovers and wastes clock<br>- High energy cost and vulnerable to breakouts |
| Weak-Side Rotation | When ball is moved quickly across the court | + Maintains defensive balance and coverage<br>- Requires high communication and timing |
| Rim Protection | Against teams that attack the basket heavily | + Reduces high-percentage shots near the rim<br>- Can leave perimeter shooters more open |


--- PAGE ---

## Data Analytics in Basketball

Basketball analytics is a data-driven approach to evaluating player and team performance through shot quality, spacing, pace, and lineup efficiency. Modern models extend beyond traditional box-score metrics to capture possession-level value, shot selection, defensive impact, and on/off court differentials. By integrating tracking data such as player movement, shot location, and lineup combinations, analysts can better understand how actions translate into points over the course of a game. At its core, basketball analytics treats the game as a continuous sequence of probabilistic possessions, where optimizing shot value and limiting opponent efficiency drives overall success.

<br>

Using these metrics, we can calculate statistics that will give us an informed decision on who to start and who to sit for fantasy teams and for predicting winning teams.

<br>

| Category | Key Basketball Analytics Metrics |
|---|---|
| Playing Time / Opportunity | Minutes played, games played, usage rate (USG%), usage share |
| Offensive Volume | Field goal attempts (FGA), free throw attempts (FTA), touches |
| Scoring Output | Points, points per game (PPG), total points, clutch points |
| Shooting Efficiency | Field goal %, 3-point %, free throw %, true shooting % (TS%) |
| Shot Profile | Shot location distribution, shot attempts by zone, mid-range vs 3PT rate |
| Playmaking | Assists, assist rate (AST%), potential assists |
| Turnovers | Turnovers (TOV), turnover rate (TOV%), assist-to-turnover ratio |
| Rebounding | Offensive rebounds, defensive rebounds, total rebounds, rebound % |
| Defensive Activity | Steals, blocks, defensive rating (DRtg), deflections |
| Lineup Impact | On/off net rating, plus-minus, lineup efficiency |
| Advanced Value Metrics | PER, BPM (Box Plus-Minus), VORP, win shares (WS) |
| Game Context | Pace, opponent defensive rating, matchup difficulty |
| Clutch Performance | Clutch TS%, clutch usage, clutch net rating |
| Outcome Metrics | Fantasy points, expected fantasy points (xFP), win probability added (WPA) |

<br>

### Field Goal Percentage (FG%)

Measures overall shooting accuracy from the field and is most useful for evaluating general scoring efficiency, though it does not separate shot difficulty or shot type.

$$
FG\% = \frac{\text{Field Goals Made}}{\text{Field Goals Attempted}}
$$

<br>

### Three-Point Percentage (3P%)

Measures shooting efficiency specifically from three-point range and is most useful for evaluating spacing and perimeter scoring ability.

$$
3P\% = \frac{\text{Three-Point Field Goals Made}}{\text{Three-Point Field Goals Attempted}}
$$

<br>

### Free Throw Percentage (FT%)

Measures free-throw shooting accuracy and is most useful as a stable indicator of shooting skill under low defensive pressure.

$$
FT\% = \frac{\text{Free Throws Made}}{\text{Free Throws Attempted}}
$$

<br>

### True Shooting Percentage (TS%)

Measures overall scoring efficiency by incorporating field goals, three-pointers, and free throws into a single possession-adjusted metric.

$$
TS\% = \frac{\text{Total Points Scored}}{2(\text{Field Goals Attempted} + 0.44 \cdot \text{Free Throws Attempted})}
$$

<br>

### Usage Rate (USG%)

Measures how frequently a player is directly involved in ending possessions via shots, free throws, or turnovers, and is most useful for identifying primary offensive creators.

$$
USG\% \approx \frac{\text{Field Goals Attempted} + 0.44 \cdot (\text{Free Throws Attempted} + \text{Turnovers})}{\text{Total Team Possessions}}
$$

<br>

### Points Per Game (PPG)

Measures average scoring output per game and is most useful as a raw volume scoring indicator.

$$
PPG = \frac{\text{Total Points Scored}}{\text{Games Played}}
$$

<br>

### Assists Per Game (APG)

Measures average passing production per game and is most useful for evaluating playmaking volume.

$$
APG = \frac{\text{Total Assists}}{\text{Games Played}}
$$

<br>

### Assist Percentage (AST%)

Measures how often a player assists teammate field goals while on the court and is most useful for isolating playmaking responsibility.

$$
AST\% = \frac{\text{Player Assists}}{\text{Team Field Goals Made While On Court}}
$$

<br>

### Turnover Rate (TOV%)

Measures how frequently a player commits turnovers per possession used and is most useful for evaluating decision-making efficiency.

$$
TOV\% = \frac{\text{Turnovers}}{\text{Field Goals Attempted} + 0.44 \cdot (\text{Free Throws Attempted} + \text{Turnovers})}
$$

<br>

### Rebounds Per Game (RPG)

Measures average rebounding production per game and is most useful as a raw volume indicator of board control.

$$
RPG = \frac{\text{Total Rebounds}}{\text{Games Played}}
$$

<br>

### Rebound Percentage (REB%)

Estimates the share of available rebounds secured by a player and is most useful for isolating rebounding impact independent of pace.

$$
REB\% = \frac{\text{Player Rebounds}}{\text{Total Available Rebounds}}
$$

<br>

### Steals and Blocks Per Game (STL, BLK)

Measure average defensive disruption per game and are most useful as volume indicators of defensive playmaking.

$$
STL = \frac{\text{Total Steals}}{\text{Games Played}}
$$

$$
BLK = \frac{\text{Total Blocks}}{\text{Games Played}}
$$

<br>

### Defensive Rating (DR)

Estimates points allowed per 100 possessions while a player is on the court and is most useful for evaluating individual defensive impact in team context.

$$
DR = \text{Points Allowed per 100 Possessions While On Court}
$$

<br>

### Defensive Win Shares (DWS)

Estimates defensive contribution to team wins using playing time and team defensive performance.

$$
DWS = \frac{\text{Minutes Played}}{\text{Team Minutes Played}} \times \text{Team Defensive Wins} \times \text{Defensive Impact Factor}
$$

<br>

### Player Efficiency Rating (PER)

Measures overall per-minute productivity adjusted for pace.

$$
PER = \frac{1}{MP} \sum \left(\text{Positive Stats} - \text{Negative Stats}\right) \times \text{Pace Adjustment}
$$

Where:
- $MP$ = minutes played

<br>

### Clutch Performance Metrics

Measures player efficiency and involvement during high-pressure game situations.

<br>

$$
\text{Clutch TS} = \frac{\text{Points Scored}}{2 \times (\text{FGA} + 0.44 \times \text{FTA})}
$$

<br>

$$
\text{Clutch Usage} =
\frac{\text{Clutch FGA} + 0.44 \times \text{Clutch FTA} + \text{Clutch TO}}
{\text{Clutch Possessions}}
$$

<br>

Where:
- $TS$ = true shooting
- $FGA$ = field goal attempts
- $FTA$ = free throw attempts
- $TO$ = turnovers

<br>

### Traits Correlated with Boom Games

- High usage rate with increasing offensive role
- Strong minutes volatility upward
- High assist + scoring involvement
- Injury return or lineup changes that increase offensive responsibility
- Fast-paced team environment
- High free-throw rate
- Multi-category stat contribution
- Favorable defensive matchup
- Positive shooting variance trends

<br>

### Traits Correlated with Bust Games

- Decreasing or unstable usage rate
- Minutes uncertainty
- Heavy reliance on scoring efficiency rather than volume
- Strong opposing defensive matchup
- Back-to-back games or high fatigue load
- Low assist involvement
- Injury management or “minutes restriction” status
- High dependency on three-point shooting
- Recent unsustainable shooting surge
- Team offensive congestion


--- PAGE ---

## Machine Learning and Predictive Modeling

Advanced sports analytics increasingly treats performance prediction as a machine learning problem, where outcomes are estimated from patterns in historical and contextual data rather than intuition alone. The focus is on building models that generalize across games and conditions, producing probabilistic forecasts of player and team performance under uncertainty.

Common approaches include regression models, random forests, neural networks, and clustering methods. These are trained on features such as snap counts, target share, air yards, weather conditions, and historical matchup data. The goal is to improve predictive accuracy while explicitly modeling the randomness and variability inherent in sports outcomes.

<br>

### Z-Score

Used to standardize a player's performance relative to a population, especially for comparing players across different weeks, seasons, or roles.

$$
z = \frac{x - \mu}{\sigma}
$$

Where:
- $x$ = observed player value  
- $\mu$ = population mean  
- $\sigma$ = standard deviation  

<br>

### Variance

Used to measure how volatile or inconsistent a player or prediction set is over time.

$$
\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2
$$

Where:
- $x_i$ = individual observations  
- $\mu$ = mean of the dataset  
- $N$ = number of observations  

<br>

### Expected Fantasy Points

Used to estimate a player's projected fantasy output based on the probability and value of underlying game events such as targets, carries, and touchdowns.

$$
E(FP) = \sum_i P_i \cdot V_i
$$

Where:
- $E(FP)$ = expected fantasy points  
- $P_i$ = probability of event i (target, carry, touchdown, etc.)  
- $V_i$ = fantasy value of event i  

<br>

### Correlation

Used to measure how strongly two players, stats, or variables move together, commonly applied in stacking decisions and game environment modeling.

$$
\rho_{XY} =
\frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}
$$

Where:
- $\rho_{XY}$ = correlation between variables X and Y  
- $\text{Cov}(X,Y)$ = covariance between X and Y  
- $\sigma_X$ = standard deviation of X  
- $\sigma_Y$ = standard deviation of Y  

<br>

### Elo Ratings in Practice

Used to model team strength dynamically over time, especially for predicting match outcomes based on historical performance and expected win probabilities.

The basic update rule is:

$$
R_{new} = R_{old} + K (S - E)
$$

Where:
- $R_{old}$ = current team rating  
- $R_{new}$ = updated team rating  
- $K$ = sensitivity constant (controls update speed)  
- $S$ = actual result (1 = win, 0 = loss, 0.5 = draw)  
- $E$ = expected win probability  

<br>

The expected outcome is usually computed using:

$$
E = \frac{1}{1 + 10^{-(R_A - R_B)/400}}
$$

Where:
- $E$ = expected probability of Team A winning  
- $R_A$ = rating of Team A  
- $R_B$ = rating of Team B  

<br>

### Linear Projection

Used as a baseline predictive model for estimating fantasy points or statistical output from weighted combinations of player features.

$$
\hat{y} = \beta_0 + \sum_{i=1}^{n} \beta_i x_i
$$

Where:
- $\hat{y}$ = predicted fantasy points  
- $\beta_0$ = intercept (baseline prediction)  
- $\beta_i$ = learned feature weights  
- $x_i$ = input features (targets, snaps, air yards, etc.)  
- $n$ = number of features  

<br>

### Ridge Regression

Used when predicting player outcomes with many correlated features, helping stabilize coefficients and reduce overfitting.

$$
\min_{\beta} \; ||y - X\beta||^2 + \lambda ||\beta||^2
$$

Where:
- $y$ = actual outcomes  
- $X$ = feature matrix  
- $\beta$ = model coefficients  
- $\lambda$ = regularization strength (penalty term)  

<br>

### Lasso Regression

Used for feature selection in predictive modeling, especially when trying to isolate the most impactful stats among many correlated variables.

$$
\min_{\beta} \; ||y - X\beta||^2 + \lambda ||\beta||_1
$$

Where:
- $y$ = actual outcomes  
- $X$ = feature matrix  
- $\beta$ = model coefficients  
- $\lambda$ = regularization strength  

<br>

### Logistic Model

Used for binary classification problems such as touchdown likelihood, boom/bust probability, or other yes/no event outcomes.

$$
P(y=1 \mid x) = \frac{1}{1 + e^{-(\beta_0 + \sum \beta_i x_i)}}
$$

Where:
- $P(y=1 \mid x)$ = probability of event occurring  
- $\beta_0$ = intercept term  
- $\beta_i$ = feature weights  
- $x_i$ = input features  

<br>

### Poisson Model

Used to model count-based events such as touchdowns, receptions, or targets over a fixed game window.

$$
P(k \text{ events}) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

Where:
- $k$ = number of events occurring  
- $\lambda$ = expected event rate  
- $e$ = Euler’s constant (~2.718)  

<br>

### Monte Carlo Simulation

Used to estimate expected outcomes by simulating thousands of possible game scenarios and averaging results. This is especially powerful in sports modeling because it captures uncertainty, nonlinear interactions between players, and rare game states that simpler point-estimate models cannot represent. It is commonly used for range-of-outcomes projections, lineup optimization, and probability distributions of player outcomes (floor, median, ceiling outcomes).

<br>

$$
E(X) = \frac{1}{N} \sum_{i=1}^{N} X_i
$$

Where:
- $E(X)$ = expected value of outcome  
- $X_i$ = outcome of simulation i  
- $N$ = total number of simulations  