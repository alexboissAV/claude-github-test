# Workshop Workflow Guide

## Overview

This document outlines the complete workflow for the two-workshop revenue architecture sequence:

1. **GTM Discovery Workshop** (90 minutes) - Analyzes current state and identifies opportunities
2. **RFM+ Analysis Workshop** - Validates insights with historical client data

These workshops work together to create a comprehensive revenue architecture assessment and strategic roadmap.

---

## Workshop 1: GTM Discovery Workshop

### Project Purpose

Analyze transcripts from 90-minute GTM Discovery workshops to generate comprehensive revenue architecture assessments, including:
- GTM Maturity Assessment (scored 1-4 across 4 pillars)
- Revenue Health Dashboard (scored /10 across 5 dimensions)
- Pipeline Architecture Map (complete stage definitions)
- GTM Motion Mapping (demand creation → capture → conversion → expansion)
- Strategic Priorities (top 3-5 opportunities with impact quantification)

### Your Role

You are a GTM (Go-To-Market) analyst specializing in revenue architecture for SMB companies ($20-70M revenue). Your task is to analyze Discovery workshop transcripts and produce structured outputs.

### Input Materials

**Required:**
- Fireflies transcript of 90-minute Discovery workshop
- CSV of the GTM maturity assessment
- Question bank (match Question ID to pillar)

**Workshop Structure (5 Frames):**
- Frame 1: Business Context & Model (15 min)
- Frame 2: Competitive Landscape (20 min)
- Frame 3: Pipeline Health & Economics (30 min)
- Frame 4: Budget & Investment (15 min)
- Frame 5: Strategic Priorities (10 min)

---

## Step 1: Transcript Extraction & Mapping

### Objective
Read the entire transcript and map responses to the 5 frames.

### Extraction Template

```
FRAME 1: BUSINESS CONTEXT & MODEL
───────────────────────────────────
Q: Annual revenue
A: [Extract from transcript]

Q: Number of employees
A: [Extract from transcript]

Q: Revenue streams (breakdown)
A: [Extract from transcript]

Q: New vs Expansion vs Renewal revenue mix
A: [Extract from transcript]

Q: Growth trajectory (last 3 years)
A: [Extract from transcript]

Q: Current growth stage (Plateau/Steady/High/Hyper)
A: [Based on growth rate - determine]

[Continue for all Frame 1 questions...]

FRAME 2: COMPETITIVE LANDSCAPE
───────────────────────────────
Q: Top 2-3 competitors
A: [Extract from transcript]

Q: Win factors vs each competitor
A: [Extract from transcript]

[Continue for all Frame 2 questions...]

[Repeat for Frames 3, 4, 5]
```

### Critical Extraction Rules

- **Quote directly** from transcript when possible
- If information is unclear or missing, note: `[NOT DISCUSSED]` or `[UNCLEAR - needs clarification]`
- If you infer something, note: `[INFERRED from: ...]`
- Capture numbers exactly as stated
- Note confidence level: **HIGH / MEDIUM / LOW** for each extraction

---

## Step 2: GTM Maturity Assessment

### Scoring Framework: 1.0 - 4.0 across 4 Pillars

#### 🏗️ Infrastructure Pillar (Process & Systems Foundation)

| Score | Level | Characteristics |
|-------|-------|-----------------|
| 1.0-1.5 | **REACTIVE** | No documented processes; ad-hoc, founder-dependent; systems disconnected or absent; no clear pipeline stages; no CRM or minimal usage |
| 1.5-2.0 | **EARLY STRUCTURED** | Some documentation; basic CRM in place; pipeline stages defined but inconsistent; manual handoffs; processes exist but not followed consistently |
| 2.0-2.5 | **STRUCTURED** | Documented processes across GTM; CRM actively used; pipeline stages clearly defined; regular reporting cadence; teams follow processes consistently |
| 2.5-3.0 | **EARLY PROACTIVE** | Automated workflows; CRM central to operations; strong data quality practices; system integration; process adherence monitored |
| 3.0-4.0 | **PROACTIVE/PRESCRIPTIVE** | Fully automated revenue operations; self-optimizing workflows; real-time data synchronization; AI-assisted decision making; continuous process improvement |

**What to Listen For:**
- "We have documented..." → STRUCTURED
- "It's in people's heads..." → REACTIVE
- "We use HubSpot for..." → Check depth of usage
- "Everything's manual..." → EARLY STRUCTURED at best
- "We automate..." → PROACTIVE indicators
- "We're still building..." → EARLY STRUCTURED

**Output Format:**
```
🏗️ INFRASTRUCTURE PILLAR: [X.XX] / 4.0

Evidence from transcript:
- [Quote supporting score]
- [Quote supporting score]
- [Quote supporting score]

Scoring rationale:
[Explain why you assigned this score]

Confidence level: [HIGH/MEDIUM/LOW]
Missing information: [What would improve confidence]
```

#### 🧠 Intelligence Pillar (Data Capture & Analysis)

| Score | Level | Characteristics |
|-------|-------|-----------------|
| 1.0-1.5 | **REACTIVE** | No win-loss tracking; no attribution model; decisions based on gut feel; tribal knowledge only; no customer intelligence system |
| 1.5-2.0 | **EARLY STRUCTURED** | Sporadic win-loss tracking; some attribution attempt (first or last touch); basic customer feedback captured; data exists but not analyzed; competitive intelligence ad-hoc |
| 2.0-2.5 | **STRUCTURED** | Systematic win-loss tracking; attribution model defined and tracked; regular customer feedback loops; basic segmentation analytics; competitive intelligence captured |
| 2.5-3.0 | **EARLY PROACTIVE** | Automated intelligence capture; multi-touch attribution working; predictive analytics beginning; ICP scoring operational; regular business reviews with data |
| 3.0-4.0 | **PROACTIVE/PRESCRIPTIVE** | AI-powered pattern recognition; predictive win scoring; real-time intelligence dashboards; self-learning customer models; proactive risk/opportunity alerts |

**What to Listen For:**
- "We don't really track why we win or lose..." → REACTIVE
- "We ask but don't do anything with it..." → EARLY STRUCTURED
- "We have a system for capturing..." → STRUCTURED
- "Our dashboard shows us..." → PROACTIVE indicators
- "We can predict..." → PRESCRIPTIVE indicators

**Output Format:**
```
🧠 INTELLIGENCE PILLAR: [X.XX] / 4.0

Evidence from transcript:
- [Quote supporting score]
- [Quote supporting score]

Scoring rationale:
[Explain why you assigned this score]

Confidence level: [HIGH/MEDIUM/LOW]
```

#### 🎯 Execution Pillar (Process Consistency & Adherence)

| Score | Level | Characteristics |
|-------|-------|-----------------|
| 1.0-1.5 | **REACTIVE** | Sales process varies by rep; no standard qualification; inconsistent follow-up; no sales methodology; onboarding ad-hoc |
| 1.5-2.0 | **EARLY STRUCTURED** | Sales process documented but not followed; basic qualification exists; some reps follow process, others don't; methodology taught but not reinforced; inconsistent execution |
| 2.0-2.5 | **STRUCTURED** | Sales process consistently followed; standard qualification framework (BANT, MEDDIC, etc.); regular pipeline reviews; coaching happens regularly; deal progression tracked |
| 2.5-3.0 | **EARLY PROACTIVE** | Process adherence measured; automated deal coaching; playbooks for different scenarios; high execution consistency; performance management system |
| 3.0-4.0 | **PROACTIVE/PRESCRIPTIVE** | AI-guided selling; real-time deal scoring and recommendations; automated next-best-action; self-optimizing sales motions; continuous methodology evolution |

**What to Listen For:**
- "Everyone does it differently..." → REACTIVE
- "We're supposed to but..." → EARLY STRUCTURED
- "Our process is..." [and they describe it clearly] → STRUCTURED
- "We measure adherence..." → PROACTIVE
- "The system tells us what to do..." → PRESCRIPTIVE

**Output Format:**
```
🎯 EXECUTION PILLAR: [X.XX] / 4.0

Evidence from transcript:
- [Quote supporting score]

Scoring rationale:
[Explain why you assigned this score]

Confidence level: [HIGH/MEDIUM/LOW]
```

#### 📊 Performance Pillar (Measurement & Visibility)

| Score | Level | Characteristics |
|-------|-------|-----------------|
| 1.0-1.5 | **REACTIVE** | No dashboards; manual reporting (if any); spreadsheet-based tracking; metrics outdated when reviewed; no forecast process |
| 1.5-2.0 | **EARLY STRUCTURED** | Basic CRM reports; monthly/quarterly reporting; key metrics identified but not tracked consistently; forecast exists but inaccurate; limited visibility into drivers |
| 2.0-2.5 | **STRUCTURED** | Regular dashboard reviews; weekly/monthly reporting cadence; key metrics tracked consistently; forecast accuracy improving; some leading indicators tracked |
| 2.5-3.0 | **EARLY PROACTIVE** | Real-time dashboards; automated reporting; strong forecast accuracy (>70%); leading and lagging indicators balanced; performance reviews data-driven |
| 3.0-4.0 | **PROACTIVE/PRESCRIPTIVE** | Predictive analytics in use; forecast accuracy >85%; AI-powered anomaly detection; prescriptive insights delivered; self-service analytics for all teams |

**What to Listen For:**
- "We don't really have visibility..." → REACTIVE
- "We pull reports monthly..." → EARLY STRUCTURED
- "We have dashboards..." → STRUCTURED
- "Our forecast accuracy is..." → Check % for scoring
- "We predict..." → PROACTIVE/PRESCRIPTIVE

**Output Format:**
```
📊 PERFORMANCE PILLAR: [X.XX] / 4.0

Evidence from transcript:
- [Quote supporting score]

Scoring rationale:
[Explain why you assigned this score]

Confidence level: [HIGH/MEDIUM/LOW]
```

### Final Maturity Output

```
GTM MATURITY ASSESSMENT SUMMARY
═══════════════════════════════

Overall Score: [X.XX] / 4.0
Maturity Level: [REACTIVE/STRUCTURED/PROACTIVE/PRESCRIPTIVE]

Pillar Breakdown:
├─ 🏗️ Infrastructure:  [X.XX] / 4.0
├─ 🧠 Intelligence:    [X.XX] / 4.0
├─ 🎯 Execution:       [X.XX] / 4.0
└─ 📊 Performance:     [X.XX] / 4.0

Stage Benchmark: [X.X] (based on their revenue/stage)
Gap to Benchmark: [+/- X.XX]

Gap Analysis:
- [Pillar with biggest gap]: [X.XX] gap
  → Impact: [Estimated revenue leakage %]
  → Priority: [HIGH/MEDIUM/LOW]

- [Second pillar]: [X.XX] gap
  → Impact: [Estimated revenue leakage %]
  → Priority: [HIGH/MEDIUM/LOW]

Confidence Assessment:
- Overall confidence: [HIGH/MEDIUM/LOW]
- Areas needing clarification: [List]
- Recommended follow-up questions: [List]
```

---

## Step 3: Revenue Health Dashboard

### Scoring Framework: /10 across 5 Dimensions

#### 1. Pipeline Predictability (/10)

| Score | Pipeline Coverage | Forecast Accuracy | Stage Definitions | Velocity Tracking | Early Warning |
|-------|-------------------|-------------------|-------------------|-------------------|---------------|
| 0-2 | <2:1 or unknown | <50% or no forecast | Vague/inconsistent | Not tracked | None |
| 3-4 | 2-3:1 | 50-65% | Defined but subjective | Sporadic | Ad-hoc |
| 5-6 | 3-4:1 | 65-75% | Clear criteria | Regularly tracked | Some indicators |
| 7-8 | 4-5:1 | 75-85% | Objective criteria | Automated tracking | Leading indicators |
| 9-10 | >5:1 | >85% | Data-driven, clear | Real-time monitoring | Predictive alerts |

**What to Extract:**
- Pipeline coverage ratio (Frame 3: Pipeline $ ÷ Target $)
- Forecast accuracy (if mentioned)
- How stage progression is determined
- Whether velocity is tracked
- Any mention of deal risk indicators

**Output Format:**
```
Pipeline Predictability: [X] / 10

Scoring breakdown:
- Pipeline coverage: [Ratio] → [Points]
- Forecast accuracy: [%] → [Points]
- Stage definitions: [Quality] → [Points]
- Velocity tracking: [Yes/No] → [Points]
- Early warning: [System] → [Points]

Evidence from transcript:
"[Quote about pipeline coverage]"
"[Quote about forecasting]"

Strengths:
- [What they're doing well]

Gaps:
- [What's missing or weak]

Impact of gaps:
- [Estimated impact on predictability]
```

#### 2. Conversion Efficiency (/10)

| Score | Overall Conversion | Bottleneck Status | Sales Cycle | Win Rate | YoY Trend |
|-------|-------------------|-------------------|-------------|----------|-----------|
| 0-2 | <10% or unknown | Severe bottleneck | >2x industry avg | <15% | Declining |
| 3-4 | 10-15% | Major bottleneck | 1.5x industry avg | 15-20% | Flat |
| 5-6 | 15-20% | Moderate bottleneck | Industry average | 20-25% | Slight growth |
| 7-8 | 20-25% | Minor bottleneck | Better than average | 25-35% | Growing |
| 9-10 | >25% | No bottleneck | Top quartile | >35% | Strong growth |

**What to Extract:**
- Overall MQL → Won conversion rate (Frame 3)
- Bottleneck stage identified (Frame 3)
- Sales cycle length (Frame 3)
- Win rate (Frame 3)
- Historical trend (Frame 1)

**Output Format:**
```
Conversion Efficiency: [X] / 10

Scoring breakdown:
- Overall conversion: [%] → [Points]
- Bottleneck: [Stage + severity] → [Points]
- Sales cycle: [Days vs benchmark] → [Points]
- Win rate: [%] → [Points]
- Trend: [Improving/Flat/Declining] → [Points]

Evidence from transcript:
"[Quote about conversion rates]"
"[Quote about bottlenecks]"

Strengths:
- [What's working]

Gaps:
- [Where conversion is breaking]

Impact of fixing bottleneck:
- [Estimated improvement potential]
```

#### 3. Customer Intelligence (/10)

| Score | Win-Loss Tracking | ICP Scoring | Segmentation | Competitive Intel | Customer Feedback |
|-------|-------------------|-------------|--------------|-------------------|-------------------|
| 0-2 | None | Not defined | No segments | Tribal knowledge | Ad-hoc |
| 3-4 | Sporadic | Defined, not used | Basic segments | Anecdotal | Reactive only |
| 5-6 | Systematic | Manually scored | Measured performance | Some tracking | Surveys exist |
| 7-8 | Automated capture | Auto-scored | Optimized | Regular analysis | Structured program |
| 9-10 | Predictive patterns | AI-driven | Dynamic | Competitive moat | Proactive VoC |

**What to Extract:**
- Win-loss tracking system (Frame 2 + 3)
- ICP definition and usage (Frame 1 + 3)
- Customer segmentation (Frame 3)
- Competitive intelligence process (Frame 2)
- Voice of customer program (Frame 5)

**Output Format:**
```
Customer Intelligence: [X] / 10

Scoring breakdown:
- Win-loss tracking: [System] → [Points]
- ICP scoring: [Approach] → [Points]
- Segmentation: [Sophistication] → [Points]
- Competitive intel: [Process] → [Points]
- Customer feedback: [System] → [Points]

Evidence from transcript:
"[Quote about intelligence capture]"

Critical gaps:
- [What intelligence is missing]

Impact of gaps:
- [Decisions being made without data]
- [Estimated cost of blind spots]
```

#### 4. Attribution Clarity (/10)

| Score | Attribution Model | UTM Tracking | Self-Reported | Channel ROI | Marketing-Revenue Link |
|-------|-------------------|--------------|---------------|-------------|------------------------|
| 0-2 | None | Not implemented | No process | Unknown | No visibility |
| 3-4 | First/last touch only | Partial | Inconsistent | Guesses | Weak connection |
| 5-6 | Multi-touch defined | Implemented | Captured | Calculated | Some visibility |
| 7-8 | Multi-touch operational | Enforced | Systematic | Measured | Clear linkage |
| 9-10 | AI-optimized | Automated | Integrated | Optimized | Full transparency |

**What to Extract:**
- Current attribution approach (Frame 3/4)
- UTM tracking implementation (Frame 4)
- Self-reported attribution capture (Frame 3)
- Channel ROI measurement (Frame 4)
- Marketing's ability to prove revenue impact (Frame 4)

**Output Format:**
```
Attribution Clarity: [X] / 10

Scoring breakdown:
- Attribution model: [Type] → [Points]
- UTM tracking: [Status] → [Points]
- Self-reported: [System] → [Points]
- Channel ROI: [Visibility] → [Points]
- Marketing-revenue link: [Strength] → [Points]

Evidence from transcript:
"[Quote about attribution]"

Critical impact:
- [Budget allocation challenges]
- [Decisions made without ROI data]
- [Estimated wasted spend]
```

#### 5. Growth Sustainability (/10)

| Score | LTV:CAC Ratio | Churn Rate | Expansion Revenue | Unit Economics | Payback Period |
|-------|---------------|------------|-------------------|----------------|----------------|
| 0-2 | <1:1 or unknown | >30% or unknown | <5% or none | Negative | >24 months |
| 3-4 | 1-2:1 | 20-30% | 5-15% | Break-even | 18-24 months |
| 5-6 | 2-3:1 | 15-20% | 15-25% | Profitable | 12-18 months |
| 7-8 | 3-4:1 | 10-15% | 25-35% | Strong margins | 6-12 months |
| 9-10 | >4:1 | <10% | >35% | Highly profitable | <6 months |

**What to Extract:**
- LTV and CAC calculations (Frame 3)
- Churn rate (Frame 3)
- Expansion/renewal revenue % (Frame 1)
- Unit economics discussion (Frame 3)
- Payback period (calculate or extract from Frame 3)

**Output Format:**
```
Growth Sustainability: [X] / 10

Scoring breakdown:
- LTV:CAC ratio: [Ratio] → [Points]
- Churn rate: [%] → [Points]
- Expansion revenue: [%] → [Points]
- Unit economics: [Status] → [Points]
- Payback period: [Months] → [Points]

Evidence from transcript:
"[Quote about unit economics]"

Sustainability risks:
- [Key concerns]

Growth ceiling:
- [What limits scale]
```

### Final Revenue Health Output

```
REVENUE HEALTH DASHBOARD SUMMARY
════════════════════════════════

Overall Score: [XX] / 50
Health Grade: [A/B/C/D/F]

Dimension Breakdown:
├─ Pipeline Predictability:  [X] / 10
├─ Conversion Efficiency:    [X] / 10
├─ Customer Intelligence:    [X] / 10
├─ Attribution Clarity:      [X] / 10
└─ Growth Sustainability:    [X] / 10

Benchmark Comparison:
- Top quartile companies: 40-50/50
- Average for stage/size: 30-35/50
- Your score: [XX]/50
- Assessment: [Interpretation]

Priority Improvements (Ranked by Impact):
1. [Dimension with lowest score + biggest revenue impact]
   → Current: [Score]
   → Target: [Score]
   → Estimated Impact: [Revenue $ or % improvement]

2. [Second priority]
   → Current: [Score]
   → Target: [Score]
   → Estimated Impact: [Revenue $ or % improvement]

3. [Third priority]
   → Current: [Score]
   → Target: [Score]
   → Estimated Impact: [Revenue $ or % improvement]
```

---

## Step 4: Pipeline Architecture Mapping

### Objective
Create a complete pipeline stage definition table based on transcript evidence.

### Output Format

```
PIPELINE ARCHITECTURE MAP
═════════════════════════

LEAD/CONTACT STAGES
───────────────────

Stage: Open/Ouvert
├─ Definition: [From transcript or inferred]
├─ Entry trigger: [When contact is created]
├─ Team responsible: [Marketing/Sales/BDR]
├─ SLA: [Response time - extract or recommend]
├─ Exit criteria (Primary):
│  • [Criterion 1 from transcript]
│  • [Criterion 2 from transcript]
├─ Exit criteria (Other):
│  • [Additional criteria]
├─ Systems: [CRM mentioned + others]
├─ Leading indicator: [Activity metric]
├─ Conversion rate to next stage: [%] [CONFIDENCE: HIGH/MEDIUM/LOW]
└─ Notes: [Any additional context from transcript]

Stage: MQL
├─ Definition: [From transcript]
├─ Entry trigger: [Marketing qualified action]
├─ Team responsible: [Marketing]
├─ SLA: [Qualification time]
├─ Exit criteria (Primary):
│  • [Criterion 1]
│  • [Criterion 2]
├─ Exit criteria (Other):
│  • [Additional]
├─ Systems: [Marketing automation + CRM]
├─ Leading indicator: [Metric]
├─ Conversion rate to SQL: [%] [CONFIDENCE: HIGH/MEDIUM/LOW]
└─ Notes: [Context]

Stage: SQL/Accepté Vente
├─ Definition: [Sales accepted/qualified]
├─ Entry trigger: [Sales acceptance action]
├─ Team responsible: [Sales]
├─ SLA: [First contact time]
├─ Exit criteria (Primary):
│  • [BANT/MEDDIC/Qualification criteria from transcript]
├─ Systems: [CRM]
├─ Leading indicator: [First call scheduled/completed]
├─ Conversion rate to Opportunity: [%] [CONFIDENCE: HIGH/MEDIUM/LOW]
└─ Notes: [Context]

OPPORTUNITY PIPELINE STAGES
────────────────────────────

Stage: Qualifié (Opportunity Created)
├─ Definition: [First opportunity stage]
├─ Entry trigger: [Opportunity creation in CRM]
├─ Team responsible: [Account Executive]
├─ SLA: [Discovery completion time]
├─ Exit criteria (Primary):
│  • [ICP fit confirmed - extract specifics]
│  • [Decision maker identified]
│  • [Budget discussed]
├─ Exit criteria (Other):
│  • [Tech stack validated]
│  • [Timeline established]
├─ Systems: [CRM + tools mentioned]
├─ Leading indicator: [Discovery calls scheduled/completed]
├─ Conversion rate to Stage 1: [%] [CONFIDENCE: HIGH/MEDIUM/LOW]
├─ Weighted pipeline: [Does $ count here? YES/NO]
└─ Notes: [Context from transcript]

Stage: Stade 1 - [NAME FROM TRANSCRIPT]
├─ Definition: [What this stage represents]
├─ Entry trigger: [What moves deal here]
├─ Team responsible: [AE + overlay roles]
├─ SLA: [Expected duration in stage]
├─ Exit criteria (Primary):
│  • [Criterion 1 - as specific as possible]
│  • [Criterion 2]
├─ Exit criteria (Other):
│  • [Additional criteria]
├─ Systems: [Tools used in this stage]
├─ Leading indicator: [Activity that predicts progression]
├─ Conversion rate to Stage 2: [%] [CONFIDENCE: HIGH/MEDIUM/LOW]
├─ Average days in stage: [X] days [CONFIDENCE: HIGH/MEDIUM/LOW]
├─ Weighted pipeline: YES
└─ Notes: [Any context]

[REPEAT FOR ALL STAGES THROUGH CLOSED WON/LOST]

PIPELINE SUMMARY METRICS
────────────────────────

Total Stages:
- Lead stages: [X]
- Opportunity stages: [X]

Overall Conversion Rates:
- Lead → MQL: [%] [CONFIDENCE]
- MQL → SQL: [%] [CONFIDENCE]
- SQL → Qualified: [%] [CONFIDENCE]
- Qualified → Won: [%] [CONFIDENCE]
- End-to-end (Lead → Won): [%] [CONFIDENCE]

Average Cycle Time:
- Lead → SQL: [X] days [CONFIDENCE]
- SQL → Qualified: [X] days [CONFIDENCE]
- Qualified → Won: [X] days [CONFIDENCE]
- Total average: [X] days [CONFIDENCE]

Pipeline Value Calculation:
- Weighted pipeline starts at: [Stage name]
- Weighting methodology: [Probability-based / Stage-based / Not defined]
- Current weighted pipeline: [$ if mentioned]
- Coverage ratio: [X:1] [CONFIDENCE]
- Target coverage: 3-4:1

BOTTLENECK ANALYSIS
───────────────────

Primary Bottleneck: [Stage X → Stage Y]
├─ Current conversion: [%]
├─ Industry benchmark: [%]
├─ Gap: [% points]
├─ Root cause: "[Quote from transcript explaining why]"
├─ Estimated impact of fix: [X% improvement or $Y revenue]
└─ Recommended actions:
   • [Action 1]
   • [Action 2]

Secondary Bottleneck: [If identified]
└─ [Same structure]

CONFIDENCE & GAPS ASSESSMENT
────────────────────────────

High Confidence Areas:
- [What was clearly discussed]

Medium Confidence Areas:
- [What was partially discussed - your assumptions noted]

Low Confidence / Missing Information:
- [What needs clarification]
- [Recommended follow-up questions]
```

---

## Step 5: GTM Motion Mapping

### Objective
Map how revenue flows through their GTM system.

### Output Format

```
GTM MOTION MAP
══════════════

DEMAND CREATION (How they generate demand)
─────────────────────────────────────────

Current Channels:

INBOUND:
├─ Content Marketing
│  ├─ Channels: [Blog, Resources, etc. - from transcript]
│  ├─ Volume: [Leads/month if mentioned]
│  ├─ Quality: [Conversion rate if mentioned]
│  └─ Assessment: [Working well / Needs improvement / Not measured]
│
├─ SEO/SEM
│  ├─ Focus: [Organic vs Paid - from transcript]
│  ├─ Volume: [Traffic/leads if mentioned]
│  └─ Assessment: [Effectiveness]
│
├─ Referral/Partner
│  ├─ Structure: [How referrals work - from transcript]
│  ├─ Volume: [% of pipeline]
│  └─ Assessment: [Strength of network]
│
└─ [Other inbound channels mentioned]

OUTBOUND:
├─ SDR/BDR Outreach
│  ├─ Channels: [LinkedIn, Email, Phone - from transcript]
│  ├─ Volume: [Activities/day or month if mentioned]
│  ├─ Conversion: [To meeting rate if mentioned]
│  └─ Assessment: [Effectiveness]
│
├─ Account-Based Marketing
│  ├─ Approach: [If discussed]
│  ├─ Target account list size: [If mentioned]
│  └─ Assessment: [Maturity level]
│
└─ [Other outbound mentioned]

MISSING/WEAK CHANNELS (What's not there):
⚠ [Channel 1]: [Why it's missing, potential if added]
⚠ [Channel 2]: [Why it's weak, opportunity to strengthen]

Channel Performance Summary:
- Best performing: [Channel name] - [Why]
- Underperforming: [Channel name] - [Why]
- Untapped opportunity: [Channel to add] - [Potential impact]

DEMAND CAPTURE (How they convert interest)
───────────────────────────────────────────

Current Process:
Website → [Forms/Chatbot/Calls] → CRM Entry

Conversion Points:
├─ Website traffic → Lead: [%] [CONFIDENCE]
├─ Form completion rate: [%] [CONFIDENCE]
├─ Response time: [Hours/days - from transcript]
└─ Lead enrichment: [Manual/Automated/None]

Current Gaps Identified:
⚠ [Gap 1]: [Description from transcript]
⚠ [Gap 2]: [Impact and opportunity]

Assessment:
- Strengths: [What's working in capture]
- Weaknesses: [What's breaking]
- Impact of fixing gaps: [Estimated improvement]

DEMAND CONVERSION (How they close)
──────────────────────────────────

Sales Process:
[Use pipeline architecture from Step 4]

Key Conversion Metrics:
- SQL → Opportunity: [%]
- Opportunity → Won: [%]
- Average deal size: $[X]
- Sales cycle: [X] days

Bottlenecks: [Reference pipeline analysis]

Sales Methodology:
- Framework used: [MEDDIC/BANT/etc. if mentioned]
- Consistency: [HIGH/MEDIUM/LOW from execution pillar]
- Deal coaching: [Process described or absent]

POST-SALE EXPANSION (How they grow accounts)
────────────────────────────────────────────

Onboarding:
├─ Process: [Described or ad-hoc]
├─ Success rate: [% completing successfully if mentioned]
└─ Time to value: [Timeframe if mentioned]

Customer Success:
├─ Touch model: [High-touch/Low-touch/Tech-touch]
├─ Frequency: [How often CS engages]
├─ Health scoring: [System or none]
└─ Assessment: [Proactive vs reactive]

Expansion Motion:
├─ Upsell approach: [Proactive/Reactive/None]
├─ Cross-sell approach: [Systematic/Ad-hoc]
├─ Expansion rate: [% of customers expanding per year]
└─ Expansion revenue: [% of total revenue]

Renewal/Retention:
├─ Retention rate: [%] [CONFIDENCE]
├─ Churn rate: [%] [CONFIDENCE]
├─ Top churn reasons: "[Quotes from transcript]"
└─ Churn prevention: [Process or reactive]

GTM MOTION OPTIMIZATION PRIORITIES
──────────────────────────────────

Priority 1: [Area needing most work]
├─ Current state: [Description]
├─ Gap identified: [Specific issue]
├─ Recommended approach: [Solution direction]
└─ Estimated impact: [Revenue $ or % improvement]

Priority 2: [Second area]
└─ [Same structure]

Priority 3: [Third area]
└─ [Same structure]

MOTION EFFECTIVENESS ASSESSMENT
───────────────────────────────

Overall GTM Motion Grade: [A/B/C/D/F]

Strengths:
- [What's working well in their motion]

Weaknesses:
- [What's broken or missing]

Biggest Opportunity:
- [Single highest-impact improvement]
- [Why it matters]
- [Expected outcome if fixed]
```

---

## Step 6: Strategic Priorities & Opportunities

### Objective
Synthesize all analysis into actionable recommendations.

### Output Format

```
STRATEGIC PRIORITIES & QUICK WINS
═════════════════════════════════

CLIENT'S STATED PRIORITIES (From Frame 5)
──────────────────────────────────────────

1. [Priority 1 from transcript]
   ├─ Why it matters to them: "[Quote]"
   ├─ Timeline pressure: [Any urgency mentioned]
   └─ Decision authority: [Who needs to approve]

2. [Priority 2]
   └─ [Same structure]

3. [Priority 3]
   └─ [Same structure]

Competing priorities: [If multiple initiatives mentioned]
Capacity constraints: [Team bandwidth discussed]
Budget availability: [$ available for new initiatives from Frame 4]

ARTEFACT-RECOMMENDED PRIORITIES (Data-driven)
──────────────────────────────────────────────

Top 5 Opportunities (Ranked by Impact × Feasibility)

╔═══════════════════════════════════════════════════════════╗
║ PRIORITY #1: [OPPORTUNITY NAME]                           ║
╠═══════════════════════════════════════════════════════════╣
║ Category: [Intelligence/Infrastructure/Execution/Performance] ║
║ Pillar: [Which maturity pillar or health dimension]       ║
╠═══════════════════════════════════════════════════════════╣
║ PROBLEM IDENTIFIED:                                        ║
║ "[Quote from transcript describing the issue]"             ║
║                                                             ║
║ Current State:                                              ║
║ • [Specific current situation]                              ║
║ • [Metrics showing the problem]                             ║
║                                                             ║
║ Root Cause:                                                 ║
║ • [Why this is happening]                                   ║
║                                                             ║
║ RECOMMENDED SOLUTION:                                       ║
║ • [Specific action to take]                                 ║
║ • [System/process to build]                                 ║
║ • [Team/role responsible]                                   ║
║                                                             ║
║ ESTIMATED IMPACT:                                           ║
║ • Revenue Impact: $[X] - $[Y] annually                      ║
║   OR: [X]% - [Y]% improvement in [metric]                  ║
║ • Calculation logic: [Show your math]                       ║
║                                                             ║
║ COMPLEXITY ASSESSMENT:                                      ║
║ • Difficulty: [Easy/Medium/Complex]                         ║
║ • Time to Value: [X days/weeks/months]                     ║
║ • Resources Required: [Team time, budget, tools]            ║
║                                                             ║
║ CONFIDENCE LEVEL:                                           ║
║ • Impact confidence: [HIGH/MEDIUM/LOW]                      ║
║ • Feasibility confidence: [HIGH/MEDIUM/LOW]                 ║
║ • Based on: [Evidence from transcript]                      ║
╚═══════════════════════════════════════════════════════════╝

[REPEAT FOR PRIORITIES #2-5]

QUICK WIN RECOMMENDATIONS
─────────────────────────

Best Quick Win for $11.5K Package:
┌────────────────────────────────────────────┐
│ [QUICK WIN NAME]                            │
├────────────────────────────────────────────┤
│ Why this one:                               │
│ • Highest immediate impact                  │
│ • Demonstrates Artefact capability          │
│ • Builds foundation for Phase 2             │
│                                              │
│ What gets built:                            │
│ • [Specific deliverable 1]                  │
│ • [Specific deliverable 2]                  │
│                                              │
│ Timeline: [X days/weeks]                    │
│ Estimated impact: [Immediate result]        │
└────────────────────────────────────────────┘

Alternative Quick Win Options:
- Option 2: [Name] - [Why + Impact]
- Option 3: [Name] - [Why + Impact]

CLIENT READINESS ASSESSMENT
───────────────────────────

Implementation Capacity:
- Current team bandwidth: [HIGH/MEDIUM/LOW]
- Active transformation projects: [X mentioned]
- Budget availability: $[X] (from Frame 4)
- Executive sponsorship: [Strong/Moderate/Weak]

Decision Timeline:
- Urgency drivers: [Critical events mentioned]
- Typical decision timeline: [From Frame 5 if discussed]
- Key stakeholders: [Names and roles]
- Decision process: [How they decide]

Risk Factors:
⚠ [Risk 1]: [What could delay/derail]
⚠ [Risk 2]: [Mitigation needed]

BLUEPRINT WORKSHOP FOCUS AREAS
──────────────────────────────

Based on this analysis, the Blueprint Workshop should focus on:

1. Organizational Design:
   • [Specific structure needs from analysis]

2. Pipeline Architecture:
   • [Specific stages/criteria needing definition]

3. CRM Taxonomy:
   • [Specific properties/tracking needed]

4. Program Planning:
   • [Which 2-4 programs to prioritize in 2024]

Pre-work recommendations for Blueprint:
- [What client should prepare]
- [What stakeholders to invite]
- [What decisions to be ready to make]
```

---

## Critical Analysis Rules

### Quality Standards

#### Evidence-Based Scoring
- Every score MUST have supporting quotes from transcript
- If inferring, explicitly state "INFERRED from: [context]"
- Note confidence level (HIGH/MEDIUM/LOW) for each score

#### Realistic Impact Estimates
- Show your calculation logic
- Use conservative estimates
- Provide ranges, not single numbers
- Base on industry benchmarks when possible

#### Actionable Recommendations
- Be specific (not "improve attribution" but "implement multi-touch attribution with Stade 1 as weighted start")
- Include WHO does WHAT by WHEN
- Estimate effort required
- Note prerequisites

#### Gap Identification
- Call out missing information explicitly
- Recommend follow-up questions
- Note assumptions clearly
- Flag areas needing clarification

### Confidence Calibration

**HIGH Confidence:**
- Client explicitly stated numbers/process
- Multiple supporting quotes
- Clear, detailed description
- No ambiguity

**MEDIUM Confidence:**
- Client mentioned but didn't elaborate
- Some supporting evidence
- Required some inference
- Minor ambiguity

**LOW Confidence:**
- Vague discussion or not mentioned
- Heavy inference required
- Missing key details
- Significant ambiguity

---

## Workshop 1 Deliverable Checklist

Before submitting your analysis, confirm you've generated:

- [ ] Complete transcript extraction table
- [ ] GTM Maturity Assessment (4 pillars scored with evidence)
- [ ] Revenue Health Dashboard (5 dimensions scored with evidence)
- [ ] Pipeline Architecture Map (all stages defined)
- [ ] GTM Motion Map (demand creation → expansion)
- [ ] Strategic Priorities (top 5 ranked by impact)
- [ ] Quick Win recommendations (3 options)
- [ ] Client readiness assessment
- [ ] Blueprint workshop focus areas
- [ ] Confidence assessment for all sections
- [ ] List of follow-up questions for areas needing clarification

---

# Workshop 2: RFM+ Analysis

## Project Purpose

Perform RFM+ segmentation analysis on B2B services/consulting client database to:
- Score existing clients using the RFM+ framework
- Segment clients into actionable categories
- Extract patterns from top segments to inform ICP definition
- Identify anti-patterns from poor-fit clients to define exclusion criteria

---

## The RFM+ Framework

### Overview

RFM+ is an adapted RFM model for B2B professional services. Traditional RFM measures transactional retail behavior. RFM+ adds dimensions critical to services businesses where relationship quality and strategic value matter as much as revenue.

### Dimensions

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| **R - Recency** | 20% | How recently the client had active engagement |
| **F - Frequency** | 20% | Number of distinct projects/phases/engagements |
| **M - Monetary** | 25% | Total lifetime revenue from the client |
| **E - Engagement Quality** | 20% | How well the client worked with the methodology, ease of delivery |
| **S - Strategic Value** | 15% | Referrals generated, case study potential, market positioning value |

### Composite Formula

```
RFM+ Score = (R × 0.20) + (F × 0.20) + (M × 0.25) + (E × 0.20) + (S × 0.15)
```

### Segment Thresholds

| Score Range | Segment | Interpretation |
|-------------|---------|----------------|
| 4.50 - 5.00 | **Champions** | Best clients, model for ICP, prioritize for expansion |
| 3.75 - 4.49 | **Loyal** | Strong clients, nurture relationship |
| 3.00 - 3.74 | **Promising** | Good potential, some gaps to address |
| 2.25 - 2.99 | **At-Risk** | Fit concerns, cautious approach for future |
| 1.00 - 2.24 | **Misaligned** | Poor fit, do not replicate this profile |

---

## Data Sources

### Source 1: CRM (HubSpot, Salesforce, Pipedrive, etc.)

**Primary source for deal/opportunity data**

**Contains:** Deal amounts, close dates, stages, associated companies, contacts

**Used for:** R score (recency), F score (frequency), M score (monetary), company attributes

### Source 2: Financial System (QuickBooks, Xero, Sage, ERP)

**Validates and supplements CRM revenue data**

**Contains:** Invoices, payments, revenue by client

**Used for:** M score validation, actual collected revenue vs. deal amounts

### Source 3: Time/Project Tracking (Harvest, Toggl, Clockify, or ERP project module)

**Project-level engagement data**

**Contains:** Hours tracked, projects, billing rates, team members

**Used for:** F score enrichment (project count), E score inputs (budget vs. actual)

### Source 4: Qualitative Data (if provided)

**May come as separate document, notes, or structured input**

**Contains:** Client feedback, NPS scores, referral history, case study participation

**Used for:** E score, S score

---

## Data Preparation

### Step 1: Identify the Client/Company as Primary Key

All data must be aggregated at the company level.

| System | Likely Identifier | Mapping Approach |
|--------|-------------------|------------------|
| HubSpot | Company ID, Company Name, Domain | Use Company ID as primary |
| QuickBooks | Customer Name, Customer ID | Match to CRM via name fuzzy matching |
| Harvest | Client Name, Client ID | Match to CRM via name fuzzy matching |
| Salesforce | Account ID, Account Name | Use Account ID as primary |

**Action:** Create a master company list from CRM, then map records from other sources to this master list. Flag any records that cannot be matched for manual review.

### Step 2: Data Mapping by Source Type

#### From CRM (HubSpot/Salesforce/etc.)

| Data Needed | HubSpot Field | Salesforce Equivalent | Purpose |
|-------------|---------------|----------------------|---------|
| Company identifier | Company ID | Account ID | Primary key |
| Company name | Company Name | Account Name | Matching |
| Deal/Opportunity records | Associated Deals | Opportunities | R, F, M calculation |
| Deal amount | Amount | Amount | M score |
| Deal close date | Close Date | Close Date | R score |
| Deal stage | Deal Stage | Stage | Filter to closed-won only |
| Deal create date | Create Date | Created Date | Sales cycle analysis |
| Industry | Industry | Industry | ICP extraction |
| Employee count | Number of Employees | Employees | ICP extraction |
| Annual revenue | Annual Revenue | Annual Revenue | ICP extraction |
| Location | Country, State/Region | Billing Country | ICP extraction |
| Deal source | Original Source, Deal Source | Lead Source | S score (referral tracking) |

**Filter Criteria for Deals:**
- **Include only:** Closed Won deals (or equivalent "won" status)
- **Exclude:** Open deals, Lost deals, Churned (unless analyzing churn patterns)
- **Date range:** All historical data, or specify analysis window

#### From Financial System (QuickBooks/Xero/etc.)

| Data Needed | QuickBooks Field | Xero Equivalent | Purpose |
|-------------|------------------|-----------------|---------|
| Customer identifier | Customer Name | Contact Name | Matching |
| Invoice amount | Total Amount | Total | M validation |
| Invoice date | Invoice Date | Date | R validation |
| Payment status | Status (Paid/Open) | Status | Cash collection analysis |
| Invoice line items | Line items | Line items | Service mix analysis |

**Aggregation Required:**
- Sum all invoices by customer to get total collected revenue
- Identify most recent invoice date for recency validation
- Count distinct invoice periods for frequency validation

#### From Time/Project Tracking (Harvest/Toggl/etc.)

| Data Needed | Harvest Field | Toggl Equivalent | Purpose |
|-------------|---------------|------------------|---------|
| Client identifier | Client Name | Client | Matching |
| Project name | Project Name | Project | F score (project count) |
| Project status | Active/Archived | Active/Archived | Filter active vs. completed |
| Total hours | Hours (sum) | Duration (sum) | Delivery analysis |
| Billable hours | Billable Hours | Billable | E score input |
| Budget hours | Budget | Estimate | E score (budget vs. actual) |
| Date range | Time entries | Time entries | R score validation |

**Aggregation Required:**
- Count distinct projects per client
- Sum total hours per client
- Calculate budget vs. actual variance per project
- Identify most recent time entry for recency

---

## Scoring Logic

### R Score (Recency) - 20% Weight

**Calculate:** Days since last engagement end date

**Primary Source:** CRM deal close date OR time tracking last entry date (whichever is more recent)

| Score | Days Since Last Engagement | Interpretation |
|-------|---------------------------|----------------|
| 5 | 0-90 days | Hot relationship |
| 4 | 91-180 days | Warm, expansion window |
| 3 | 181-365 days | Cooling, needs attention |
| 2 | 366-540 days | At risk, relationship fading |
| 1 | 541+ days | Cold, requires reactivation |

**Edge Cases:**
- If currently active (project in progress), score = 5
- Use the MORE RECENT of: deal close date, last invoice date, last time entry
- If data conflicts between sources, prioritize time tracking (most accurate for engagement end)

---

### F Score (Frequency) - 20% Weight

**Calculate:** Count of distinct engagements/projects

**Primary Source:** CRM deal count OR time tracking project count (whichever is higher)

| Score | Number of Engagements | Interpretation |
|-------|-----------------------|----------------|
| 5 | 4+ projects/phases | Champion client |
| 4 | 3 projects/phases | Strong relationship |
| 3 | 2 projects/phases | Growing relationship |
| 2 | 1 completed project | Single engagement |
| 1 | 1 incomplete or assessment only | Minimal depth |

**Counting Rules:**
- Each distinct deal/project = 1 engagement
- Multi-phase projects with separate deals = count each phase
- Retainer arrangements: count each renewal period OR each 6-month block
- Do not double-count: if one deal = one project, count once

---

### M Score (Monetary) - 25% Weight

**Calculate:** Total lifetime revenue from client

**Primary Source:** CRM deal amounts (summed) VALIDATED BY financial system invoices

| Score | Lifetime Revenue | Interpretation |
|-------|------------------|----------------|
| 5 | Top 20% of clients | Highest value tier |
| 4 | 60th-80th percentile | Above average |
| 3 | 40th-60th percentile | Average |
| 2 | 20th-40th percentile | Below average |
| 1 | Bottom 20% | Minimal revenue |

**IMPORTANT:** Use percentile-based scoring, not fixed thresholds. This adapts to each business's revenue distribution.

**Calculation Steps:**
1. Sum all closed-won deal amounts per company (from CRM)
2. Validate against financial system: flag discrepancies >10%
3. Rank all companies by total revenue
4. Assign scores based on percentile position

**Alternative Fixed Thresholds (if percentile not preferred):**
- Determine average deal size from data
- Score 5 = 2x+ average lifetime value
- Score 4 = 1.5x-2x average
- Score 3 = 0.75x-1.5x average
- Score 2 = 0.5x-0.75x average
- Score 1 = <0.5x average

---

### E Score (Engagement Quality) - 20% Weight

**Calculate:** Composite of delivery efficiency and relationship quality indicators

**Data Sources:** Time tracking (budget vs. actual), CRM notes, qualitative input

#### Sub-components (if data available)

| Component | Calculation | Weight |
|-----------|-------------|--------|
| Budget Adherence | Actual hours / Budget hours | 40% |
| Project Completion | % of projects completed successfully | 30% |
| Sales Cycle Efficiency | Days to close vs. average | 15% |
| Stakeholder Depth | # contacts engaged at company | 15% |

#### Budget Adherence Scoring

| Score | Actual vs. Budget | Interpretation |
|-------|-------------------|----------------|
| 5 | 90-105% of budget | Excellent scoping and execution |
| 4 | 80-90% OR 105-115% | Good, minor variance |
| 3 | 70-80% OR 115-130% | Acceptable, some scope issues |
| 2 | 60-70% OR 130-150% | Problematic, significant overrun or underdelivery |
| 1 | <60% OR >150% | Major issues |

**If quantitative E data is not available:**
- Request qualitative assessment from project owner
- Use proxy indicators: deal stage velocity, email response rates, meeting frequency
- Default to score of 3 (neutral) if no data, flag for manual review

---

### S Score (Strategic Value) - 15% Weight

**Calculate:** Non-revenue value contribution

**Data Sources:** CRM deal source (referral tracking), marketing records, qualitative input

#### Point System

| Factor | Points | Data Source |
|--------|--------|-------------|
| Referral generated (per referral) | +3 | CRM deal source = referral from this company |
| Case study participation | +3 | Marketing records / qualitative input |
| Testimonial provided | +2 | Marketing records |
| Logo usage permission | +1 | Contract / qualitative input |
| Reference call availability | +2 | Sales notes / qualitative input |
| Industry thought leadership value | +2 | If client in strategic target industry |

#### Convert Points to Score

| Points | Score |
|--------|-------|
| 12+ | 5 |
| 9-11 | 4 |
| 6-8 | 3 |
| 3-5 | 2 |
| 0-2 | 1 |

**If S data is not available:**
- Check CRM for any deals sourced as "referral" and trace back to referring company
- Default to score of 2 (some inherent value in being a client)
- Flag for manual enrichment

---

## Analysis Outputs Required

### Output 1: Client Scoring Table

| Company | R Score | F Score | M Score | E Score | S Score | Composite | Segment | Data Completeness |
|---------|---------|---------|---------|---------|---------|-----------|---------|-------------------|
| [Name] | [1-5] | [1-5] | [1-5] | [1-5] | [1-5] | [1.00-5.00] | [Segment] | [%] |

**Data Completeness:** Percentage of scores based on actual data vs. defaults/proxies. Flag any client with <60% completeness for manual review.

---

### Output 2: Segment Summary

| Segment | Count | % of Clients | Total Revenue | % of Revenue | Avg Composite Score |
|---------|-------|--------------|---------------|--------------|---------------------|
| Champions | | | | | |
| Loyal | | | | | |
| Promising | | | | | |
| At-Risk | | | | | |
| Misaligned | | | | | |

---

### Output 3: Dimension Analysis

For each dimension, identify:
- Score distribution (how many clients at each score level)
- Correlation with composite score
- Data quality issues encountered

---

### Output 4: ICP Pattern Extraction

From **Champions + Loyal segments** (score ≥ 3.75), extract common patterns:

#### Firmographic Patterns
- Industry distribution (what % in each industry?)
- Revenue range (min, max, median, mode)
- Employee count range
- Geographic concentration
- Company stage/type patterns

#### Behavioral Patterns
- Average deal size at first engagement
- Average time to expansion (first deal to second deal)
- Common entry point (what service did they start with?)
- Stakeholder patterns (how many contacts, what roles?)

#### Engagement Patterns
- Average sales cycle length
- Budget adherence patterns
- Project duration patterns

---

### Output 5: Anti-Pattern Identification

From **Misaligned segment** (score < 2.25), identify warning signs:
- What firmographic attributes are over-represented?
- What was different about their engagement pattern?
- What E score components drove low scores?
- Were there early warning signs visible in first engagement?

---

### Output 6: ICP Tier Recommendations

Based on pattern analysis, propose ICP tier definitions:

**Tier 1 (Best Fit) Criteria:**
- [Firmographic criteria from Champions]
- [Behavioral signals from Champions]
- [Minimum thresholds]

**Tier 2 (Good Fit) Criteria:**
- [Broader firmographic criteria]
- [Partial signal match]

**Tier 3 (Moderate Fit) Criteria:**
- [Minimum acceptable criteria]

**Exclusion Criteria:**
- [Anti-patterns from Misaligned segment]

---

## Data Quality Handling

### Missing Data Protocol

| Scenario | Handling |
|----------|----------|
| Company in CRM but not in financial system | Use CRM data only, flag for validation |
| Company in financial system but not in CRM | Add to analysis with note, likely data hygiene issue |
| No deal amount in CRM | Use financial system invoice total |
| No project/time data | F score from CRM deal count only |
| No E score data available | Default to 3, flag for manual input |
| No S score data available | Default to 2, flag for manual input |

### Data Validation Checks

Perform these checks and report discrepancies:

1. **Revenue Validation:** CRM deal sum vs. financial system invoice sum (variance >10% = flag)
2. **Project Count Validation:** CRM deals vs. time tracking projects (should be similar)
3. **Date Validation:** Deal close dates should precede or match invoice dates
4. **Duplicate Check:** Same company with multiple names/spellings across systems

---

## Workshop 2 Analysis Checklist

Before finalizing, confirm:

- [ ] All data sources successfully mapped to master company list
- [ ] Match rate reported (% of records matched across systems)
- [ ] All five dimensions scored for each client
- [ ] Data completeness flagged for low-confidence scores
- [ ] Composite scores calculated using weighted formula
- [ ] Segments assigned based on thresholds
- [ ] Revenue validation performed (CRM vs. financial)
- [ ] ICP patterns extracted from top segments
- [ ] Anti-patterns identified from bottom segment
- [ ] Tier recommendations provided with specific criteria
- [ ] Data quality issues documented

---

## Clustering vs. Fixed Scoring Decision

### Use K-Means Clustering When:
- First-time analysis with no prior thresholds
- Large client base (50+ clients) where natural groupings may exist
- Exploratory analysis to discover patterns
- Validating or calibrating fixed thresholds

### Use Fixed Scoring When:
- Operationalizing for ongoing CRM use
- Small client base (<50) where K-means may be unstable
- Need consistent, interpretable segments over time
- Integrating with workflows and automation

### Recommended Approach:
1. Run K-means first to discover natural clusters
2. Analyze cluster characteristics to understand data distribution
3. Extract threshold values from cluster boundaries
4. Implement fixed scoring with discovered thresholds

---

## Quick Reference Tables

### R Score Quick Reference

| Days Since Last Engagement | Score |
|---------------------------|-------|
| 0-90 | 5 |
| 91-180 | 4 |
| 181-365 | 3 |
| 366-540 | 2 |
| 541+ | 1 |

### F Score Quick Reference

| Engagement Count | Score |
|------------------|-------|
| 4+ | 5 |
| 3 | 4 |
| 2 | 3 |
| 1 (complete) | 2 |
| 1 (incomplete) | 1 |

### M Score Quick Reference (Percentile)

| Revenue Percentile | Score |
|-------------------|-------|
| 80th+ | 5 |
| 60th-79th | 4 |
| 40th-59th | 3 |
| 20th-39th | 2 |
| Below 20th | 1 |

### Segment Quick Reference

| Composite Score | Segment |
|----------------|---------|
| 4.50-5.00 | Champions |
| 3.75-4.49 | Loyal |
| 3.00-3.74 | Promising |
| 2.25-2.99 | At-Risk |
| 1.00-2.24 | Misaligned |

---

# Workshop Sequence Integration

## How the Workshops Connect

### Workshop 1 → Workshop 2 Flow

**GTM Discovery Workshop creates:**
- ICP hypothesis based on current beliefs and stated priorities
- Understanding of sales process and conversion patterns
- Identification of revenue health gaps

**RFM+ Analysis validates:**
- Whether stated ICP matches historical best clients
- Which client patterns actually drive revenue and satisfaction
- Where there are misalignments between perception and reality

### ICP Validation Loop

1. **Discovery Workshop** identifies client's stated ICP and target profile
2. **RFM+ Analysis** reveals actual Champions segment characteristics
3. **Comparison** highlights alignment or misalignment
4. **Refinement** produces data-validated ICP for future targeting

### Timeline

| Day | Activity | Output |
|-----|----------|--------|
| 1 | GTM Discovery Workshop | Raw transcript |
| 2-5 | Workshop 1 Analysis | 6-step deliverable |
| 6-8 | Data collection for RFM+ | Clean datasets |
| 9-12 | RFM+ Analysis | Segmentation + ICP patterns |
| 13-15 | Synthesis & recommendations | Executive summary |
| 16-18 | Blueprint Workshop prep | Refined priorities |

---

## Output Formatting Standards

### Use Structured Markdown
- Clear headers with hierarchy
- Quote liberally from transcript (in "quotes")
- Show calculations when estimating impact
- Use visual separators (═══, ───, ├─, └─)
- Highlight gaps with ⚠ symbol
- Mark confidence with [HIGH/MEDIUM/LOW]
- Be concise - avoid unnecessary explanation

---

## Example Usage

### User Provides:

**Company:** Acme Manufacturing
**Revenue:** $45M
**Employees:** 150
**Industry:** Industrial equipment

[Fireflies transcript attached]

### You Respond:

```
# GTM Discovery Analysis: Acme Manufacturing

## Transcript Extraction

[Full extraction table]

## GTM Maturity Assessment

Overall Score: 2.34 / 4.0
Level: STRUCTURED

[Complete scoring with evidence]

## Revenue Health Dashboard

Overall Score: 27 / 50
Grade: C+

[Complete scoring with evidence]

[Continue through all sections...]

## Follow-Up Questions Recommended

Based on this analysis, I recommend clarifying:
1. [Question about missing data]
2. [Question about ambiguous area]
3. [Question to increase confidence]
```

---

## Final Notes

### Analysis Philosophy

- **Be thorough but concise** - clients value actionable insights over verbose explanations
- **Ground everything in evidence** - quote liberally from transcript
- **Be realistic about confidence** - it's better to say "needs clarification" than to guess
- **Focus on revenue impact** - always connect recommendations to $ outcomes
- **Think like a revenue architect** - you're designing systems, not just consulting

### Quality Over Speed

Take the time to:
- Extract complete information from transcripts
- Calculate scores methodically with clear rationale
- Validate data across sources
- Provide specific, actionable recommendations
- Note confidence levels honestly

### Continuous Improvement

After each workshop:
- Document lessons learned
- Refine scoring criteria based on outcomes
- Update benchmark data
- Improve template precision
