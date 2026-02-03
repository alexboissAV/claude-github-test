# Workshop Sequence Workflow

## Overview

This document outlines the workflow for a two-workshop sequence designed to analyze and improve Go-To-Market (GTM) strategies for SMB companies ($20-70M revenue):

1. **GTM Discovery Workshop** - Analyzes current state GTM architecture and identifies opportunities
2. **RFM+ Analysis** - Segments existing clients to extract Ideal Customer Profile (ICP) patterns

The output from Workshop 1 informs strategic priorities, while Workshop 2 validates and refines the ICP definition through historical client data.

---

## Workshop 1: GTM Discovery Workshop

### Purpose
Analyze transcripts from 90-minute GTM Discovery workshops to generate comprehensive revenue architecture assessments.

### Input Requirements

| Input Type | Description | Format |
|------------|-------------|--------|
| Workshop Transcript | Fireflies transcript of 90-minute Discovery session | Text/Transcript file |
| GTM Maturity CSV | Pre-workshop maturity assessment data | CSV |
| Question Bank | Reference document mapping Question IDs to pillars | Document |
| Project Library | Supporting documents and frameworks | Document collection |

### Workshop Structure (90 Minutes)

The workshop is divided into 5 frames:

| Frame | Focus Area | Duration | Key Objectives |
|-------|-----------|----------|----------------|
| Frame 1 | Business Context & Model | 15 min | Understand revenue model, growth trajectory, company stage |
| Frame 2 | Competitive Landscape | 20 min | Identify competitors, win/loss factors, positioning |
| Frame 3 | Pipeline Health & Economics | 30 min | Assess pipeline metrics, conversion rates, unit economics |
| Frame 4 | Budget & Investment | 15 min | Review GTM spend, attribution, ROI visibility |
| Frame 5 | Strategic Priorities | 10 min | Capture client's stated priorities and constraints |

### Analysis Workflow

#### Step 1: Transcript Extraction & Mapping (Foundation)

**Objective**: Extract all responses from transcript and map to the 5 frames

**Process**:
1. Read complete transcript
2. Identify responses for each frame's questions
3. Create extraction table with:
   - Question text
   - Extracted answer (direct quotes when possible)
   - Confidence level (HIGH/MEDIUM/LOW)
   - Notes for unclear/missing information

**Output Format**:
```
FRAME [X]: [FRAME NAME]
───────────────────────────────────
Q: [Question text]
A: [Extract from transcript] OR [NOT DISCUSSED] OR [INFERRED from: ...]
Confidence: [HIGH/MEDIUM/LOW]

[Repeat for all questions in frame]
```

**Critical Rules**:
- Quote directly from transcript when possible
- Mark missing information: `[NOT DISCUSSED]` or `[UNCLEAR - needs clarification]`
- Note inferences: `[INFERRED from: ...]`
- Capture numbers exactly as stated
- Track confidence for each data point

---

#### Step 2: GTM Maturity Assessment (Score 1-4 across 4 pillars)

**Objective**: Score the client's GTM maturity across 4 pillars on a 1-4 scale

**Scoring Framework**:

| Score Range | Maturity Level | Characteristics |
|-------------|----------------|-----------------|
| 1.0-1.5 | REACTIVE | Ad-hoc, founder-dependent, no systems |
| 1.5-2.0 | EARLY STRUCTURED | Some documentation, basic systems, inconsistent |
| 2.0-2.5 | STRUCTURED | Documented processes, actively used systems |
| 2.5-3.0 | EARLY PROACTIVE | Automated workflows, data-driven decisions |
| 3.0-4.0 | PROACTIVE/PRESCRIPTIVE | AI-assisted, self-optimizing, continuous improvement |

**The 4 Pillars**:

##### 🏗️ Infrastructure Pillar (Process & Systems Foundation)

**What to Assess**:
- Process documentation status
- CRM implementation and usage
- Pipeline stage definitions
- System integrations
- Workflow automation

**Scoring Indicators**:
- Score 1-1.5: "It's in people's heads", no CRM or minimal usage
- Score 1.5-2: "We're still building", basic CRM in place
- Score 2-2.5: "We have documented", CRM actively used
- Score 2.5-3: "We automate", integrated systems
- Score 3-4: Fully automated, self-optimizing

**Output Requirements**:
```
🏗️ INFRASTRUCTURE PILLAR: [X.XX] / 4.0

Evidence from transcript:
- "[Quote supporting score]"
- "[Quote supporting score]"
- "[Quote supporting score]"

Scoring rationale:
[Explain why you assigned this score]

Confidence level: [HIGH/MEDIUM/LOW]
Missing information: [What would improve confidence]
```

##### 🧠 Intelligence Pillar (Data Capture & Analysis)

**What to Assess**:
- Win-loss tracking systems
- Attribution model sophistication
- Customer intelligence capture
- Competitive intelligence processes
- Predictive analytics capabilities

**Scoring Indicators**:
- Score 1-1.5: "We don't really track why we win or lose"
- Score 1.5-2: "We ask but don't do anything with it"
- Score 2-2.5: "We have a system for capturing"
- Score 2.5-3: "Our dashboard shows us"
- Score 3-4: "We can predict"

**Output Requirements**: Same structure as Infrastructure Pillar

##### 🎯 Execution Pillar (Process Consistency & Adherence)

**What to Assess**:
- Sales process consistency
- Qualification frameworks (BANT, MEDDIC, etc.)
- Deal progression tracking
- Coaching and enablement
- Performance management

**Scoring Indicators**:
- Score 1-1.5: "Everyone does it differently"
- Score 1.5-2: "We're supposed to but..."
- Score 2-2.5: Clear process consistently followed
- Score 2.5-3: "We measure adherence"
- Score 3-4: "The system tells us what to do"

**Output Requirements**: Same structure as Infrastructure Pillar

##### 📊 Performance Pillar (Measurement & Visibility)

**What to Assess**:
- Dashboard availability and usage
- Reporting cadence and accuracy
- Forecast accuracy
- Metric tracking consistency
- Leading vs. lagging indicators

**Scoring Indicators**:
- Score 1-1.5: "We don't really have visibility"
- Score 1.5-2: "We pull reports monthly"
- Score 2-2.5: "We have dashboards"
- Score 2.5-3: Forecast accuracy >70%
- Score 3-4: "We predict", forecast accuracy >85%

**Output Requirements**: Same structure as Infrastructure Pillar

**Final Maturity Output**:
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

Confidence Assessment:
- Overall confidence: [HIGH/MEDIUM/LOW]
- Areas needing clarification: [List]
- Recommended follow-up questions: [List]
```

---

#### Step 3: Revenue Health Dashboard (Score /10 across 5 dimensions)

**Objective**: Assess current revenue health across 5 key dimensions

**The 5 Dimensions**:

##### 1. Pipeline Predictability (/10)

**Scoring Components**:

| Score | Pipeline Coverage | Forecast Accuracy | Stage Definitions | Velocity Tracking | Early Warning |
|-------|------------------|-------------------|-------------------|-------------------|---------------|
| 0-2 | <2:1 or unknown | <50% or no forecast | Vague/inconsistent | Not tracked | None |
| 3-4 | 2-3:1 | 50-65% | Defined but subjective | Sporadic | Ad-hoc |
| 5-6 | 3-4:1 | 65-75% | Clear criteria | Regularly tracked | Some indicators |
| 7-8 | 4-5:1 | 75-85% | Objective criteria | Automated tracking | Leading indicators |
| 9-10 | >5:1 | >85% | Data-driven, clear | Real-time monitoring | Predictive alerts |

**Data Sources**: Frame 3 (Pipeline $ ÷ Target $, forecast accuracy, stage progression, velocity tracking)

**Output Format**:
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

Strengths: [What they're doing well]
Gaps: [What's missing or weak]
Impact of gaps: [Estimated impact on predictability]
```

##### 2. Conversion Efficiency (/10)

**Scoring Components**:

| Score | Overall Conversion | Bottleneck Status | Sales Cycle | Win Rate | YoY Trend |
|-------|-------------------|-------------------|-------------|----------|-----------|
| 0-2 | <10% or unknown | Severe bottleneck | >2x industry avg | <15% | Declining |
| 3-4 | 10-15% | Major bottleneck | 1.5x industry avg | 15-20% | Flat |
| 5-6 | 15-20% | Moderate bottleneck | Industry average | 20-25% | Slight growth |
| 7-8 | 20-25% | Minor bottleneck | Better than average | 25-35% | Growing |
| 9-10 | >25% | No bottleneck | Top quartile | >35% | Strong growth |

**Data Sources**: Frame 3 (MQL→Won conversion, bottleneck stage, sales cycle, win rate), Frame 1 (trend)

##### 3. Customer Intelligence (/10)

**Scoring Components**:

| Score | Win-Loss Tracking | ICP Scoring | Segmentation | Competitive Intel | Customer Feedback |
|-------|------------------|-------------|--------------|-------------------|-------------------|
| 0-2 | None | Not defined | No segments | Tribal knowledge | Ad-hoc |
| 3-4 | Sporadic | Defined, not used | Basic segments | Anecdotal | Reactive only |
| 5-6 | Systematic | Manually scored | Measured performance | Some tracking | Surveys exist |
| 7-8 | Automated capture | Auto-scored | Optimized | Regular analysis | Structured program |
| 9-10 | Predictive patterns | AI-driven | Dynamic | Competitive moat | Proactive VoC |

**Data Sources**: Frames 2 & 3 (win-loss, ICP, segmentation, competitive intel), Frame 5 (VoC program)

##### 4. Attribution Clarity (/10)

**Scoring Components**:

| Score | Attribution Model | UTM Tracking | Self-Reported | Channel ROI | Marketing-Revenue Link |
|-------|------------------|--------------|---------------|-------------|----------------------|
| 0-2 | None | Not implemented | No process | Unknown | No visibility |
| 3-4 | First/last touch only | Partial | Inconsistent | Guesses | Weak connection |
| 5-6 | Multi-touch defined | Implemented | Captured | Calculated | Some visibility |
| 7-8 | Multi-touch operational | Enforced | Systematic | Measured | Clear linkage |
| 9-10 | AI-optimized | Automated | Integrated | Optimized | Full transparency |

**Data Sources**: Frames 3 & 4 (attribution model, UTM tracking, self-reported data, channel ROI)

##### 5. Growth Sustainability (/10)

**Scoring Components**:

| Score | LTV:CAC Ratio | Churn Rate | Expansion Revenue | Unit Economics | Payback Period |
|-------|---------------|------------|-------------------|----------------|----------------|
| 0-2 | <1:1 or unknown | >30% or unknown | <5% or none | Negative | >24 months |
| 3-4 | 1-2:1 | 20-30% | 5-15% | Break-even | 18-24 months |
| 5-6 | 2-3:1 | 15-20% | 15-25% | Profitable | 12-18 months |
| 7-8 | 3-4:1 | 10-15% | 25-35% | Strong margins | 6-12 months |
| 9-10 | >4:1 | <10% | >35% | Highly profitable | <6 months |

**Data Sources**: Frame 3 (LTV, CAC, churn, unit economics), Frame 1 (expansion/renewal revenue %)

**Final Revenue Health Output**:
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
   → Current: [Score] → Target: [Score]
   → Estimated Impact: [Revenue $ or % improvement]
```

---

#### Step 4: Pipeline Architecture Mapping

**Objective**: Create complete pipeline stage definitions based on transcript evidence

**Structure**:

**LEAD/CONTACT STAGES**:
- Open/Ouvert
- MQL (Marketing Qualified Lead)
- SQL/Accepté Vente (Sales Qualified Lead)

**OPPORTUNITY PIPELINE STAGES**:
- Qualifié (Opportunity Created)
- Stage 1 through Closed Won/Lost

**For Each Stage, Document**:
```
Stage: [Stage Name]
├─ Definition: [From transcript or inferred]
├─ Entry trigger: [What moves deal here]
├─ Team responsible: [Marketing/Sales/BDR/AE]
├─ SLA: [Expected duration/response time]
├─ Exit criteria (Primary):
│  • [Criterion 1 from transcript]
│  • [Criterion 2 from transcript]
├─ Exit criteria (Other):
│  • [Additional criteria]
├─ Systems: [CRM + tools mentioned]
├─ Leading indicator: [Activity metric]
├─ Conversion rate to next stage: [%] [CONFIDENCE: HIGH/MEDIUM/LOW]
├─ Average days in stage: [X] days [CONFIDENCE: HIGH/MEDIUM/LOW]
├─ Weighted pipeline: [YES/NO]
└─ Notes: [Additional context from transcript]
```

**Pipeline Summary Metrics**:
```
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
- Lead → SQL: [X] days
- SQL → Qualified: [X] days
- Qualified → Won: [X] days
- Total average: [X] days

Pipeline Value Calculation:
- Weighted pipeline starts at: [Stage name]
- Weighting methodology: [Probability/Stage-based/Not defined]
- Current weighted pipeline: [$]
- Coverage ratio: [X:1]
- Target coverage: 3-4:1
```

**Bottleneck Analysis**:
```
BOTTLENECK ANALYSIS
───────────────────

Primary Bottleneck: [Stage X → Stage Y]
├─ Current conversion: [%]
├─ Industry benchmark: [%]
├─ Gap: [% points]
├─ Root cause: "[Quote from transcript]"
├─ Estimated impact of fix: [X% improvement or $Y revenue]
└─ Recommended actions:
   • [Action 1]
   • [Action 2]
```

---

#### Step 5: GTM Motion Mapping

**Objective**: Map how revenue flows through the GTM system from demand creation to expansion

**4 Motion Stages**:

##### DEMAND CREATION (How they generate demand)

**Inbound Channels**:
- Content Marketing (channels, volume, quality)
- SEO/SEM (focus, volume, effectiveness)
- Referral/Partner (structure, volume, network strength)
- Other channels mentioned

**Outbound Channels**:
- SDR/BDR Outreach (channels, volume, conversion)
- Account-Based Marketing (approach, target list size)
- Other outbound tactics

**Assessment**:
```
Channel Performance Summary:
- Best performing: [Channel] - [Why]
- Underperforming: [Channel] - [Why]
- Untapped opportunity: [Channel] - [Potential impact]

MISSING/WEAK CHANNELS:
⚠ [Channel 1]: [Why missing, potential if added]
⚠ [Channel 2]: [Why weak, opportunity to strengthen]
```

##### DEMAND CAPTURE (How they convert interest)

**Process Flow**: Website → Forms/Chatbot/Calls → CRM Entry

**Metrics**:
- Website traffic → Lead: [%]
- Form completion rate: [%]
- Response time: [Hours/days]
- Lead enrichment: [Manual/Automated/None]

**Assessment**:
```
Current Gaps:
⚠ [Gap 1]: [Description + Impact]
⚠ [Gap 2]: [Description + Impact]

Impact of fixing gaps: [Estimated improvement]
```

##### DEMAND CONVERSION (How they close)

**Reference**: Use Pipeline Architecture from Step 4

**Key Metrics**:
- SQL → Opportunity: [%]
- Opportunity → Won: [%]
- Average deal size: $[X]
- Sales cycle: [X] days

**Sales Methodology**:
- Framework: [MEDDIC/BANT/etc.]
- Consistency: [HIGH/MEDIUM/LOW]
- Deal coaching: [Process or absent]

##### POST-SALE EXPANSION (How they grow accounts)

**Onboarding**:
- Process: [Described or ad-hoc]
- Success rate: [%]
- Time to value: [Timeframe]

**Customer Success**:
- Touch model: [High-touch/Low-touch/Tech-touch]
- Engagement frequency: [How often]
- Health scoring: [System or none]
- Assessment: [Proactive vs reactive]

**Expansion Motion**:
- Upsell approach: [Proactive/Reactive/None]
- Cross-sell approach: [Systematic/Ad-hoc]
- Expansion rate: [% of customers/year]
- Expansion revenue: [% of total]

**Renewal/Retention**:
- Retention rate: [%]
- Churn rate: [%]
- Top churn reasons: "[Quotes]"
- Churn prevention: [Process or reactive]

**Motion Effectiveness Assessment**:
```
Overall GTM Motion Grade: [A/B/C/D/F]

Strengths: [What's working well]
Weaknesses: [What's broken or missing]

Biggest Opportunity:
- [Single highest-impact improvement]
- [Why it matters]
- [Expected outcome if fixed]
```

---

#### Step 6: Strategic Priorities & Opportunities

**Objective**: Synthesize all analysis into actionable recommendations

##### CLIENT'S STATED PRIORITIES (From Frame 5)

```
1. [Priority 1 from transcript]
   ├─ Why it matters: "[Quote]"
   ├─ Timeline pressure: [Urgency]
   └─ Decision authority: [Who approves]

2. [Priority 2]
3. [Priority 3]

Competing priorities: [Multiple initiatives]
Capacity constraints: [Team bandwidth]
Budget availability: $[X] (from Frame 4)
```

##### ARTEFACT-RECOMMENDED PRIORITIES (Data-driven)

**Top 5 Opportunities (Ranked by Impact × Feasibility)**:

For each priority:
```
╔═══════════════════════════════════════════════════════════╗
║ PRIORITY #X: [OPPORTUNITY NAME]                           ║
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
║ Root Cause: [Why this is happening]                        ║
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
```

##### QUICK WIN RECOMMENDATIONS

```
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
```

##### CLIENT READINESS ASSESSMENT

```
Implementation Capacity:
- Current team bandwidth: [HIGH/MEDIUM/LOW]
- Active transformation projects: [X]
- Budget availability: $[X]
- Executive sponsorship: [Strong/Moderate/Weak]

Decision Timeline:
- Urgency drivers: [Critical events]
- Typical decision timeline: [Timeframe]
- Key stakeholders: [Names and roles]
- Decision process: [How they decide]

Risk Factors:
⚠ [Risk 1]: [What could delay/derail]
⚠ [Risk 2]: [Mitigation needed]
```

##### BLUEPRINT WORKSHOP FOCUS AREAS

```
Based on analysis, Blueprint Workshop should focus on:

1. Organizational Design:
   • [Specific structure needs from analysis]

2. Pipeline Architecture:
   • [Specific stages/criteria needing definition]

3. CRM Taxonomy:
   • [Specific properties/tracking needed]

4. Program Planning:
   • [Which 2-4 programs to prioritize in 2024]

Pre-work recommendations:
- [What client should prepare]
- [What stakeholders to invite]
- [What decisions to be ready to make]
```

---

### Quality Standards & Critical Rules

#### Evidence-Based Scoring
- Every score MUST have supporting quotes from transcript
- Explicitly state when inferring: `[INFERRED from: context]`
- Note confidence level (HIGH/MEDIUM/LOW) for each score
- Mark missing information clearly

#### Realistic Impact Estimates
- Show calculation logic
- Use conservative estimates
- Provide ranges, not single numbers
- Base on industry benchmarks when possible

#### Actionable Recommendations
- Be specific (not "improve attribution" but "implement multi-touch attribution with Stage 1 as weighted start")
- Include WHO does WHAT by WHEN
- Estimate effort required
- Note prerequisites

#### Confidence Calibration

**HIGH Confidence**:
- Client explicitly stated numbers/process
- Multiple supporting quotes
- Clear, detailed description
- No ambiguity

**MEDIUM Confidence**:
- Client mentioned but didn't elaborate
- Some supporting evidence
- Required some inference
- Minor ambiguity

**LOW Confidence**:
- Vague discussion or not mentioned
- Heavy inference required
- Missing key details
- Significant ambiguity

---

### Deliverable Checklist

Before finalizing analysis, confirm:

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

## Workshop 2: RFM+ Analysis

### Purpose
Perform RFM+ segmentation analysis on existing B2B client database to extract ICP patterns and inform strategic targeting.

### Connection to Workshop 1
- **Workshop 1 Output**: Strategic priorities and initial ICP hypothesis based on desired customer characteristics
- **Workshop 2 Input**: Validates ICP through analysis of actual best-fit clients
- **Workshop 2 Output**: Data-driven ICP tiers and anti-patterns to refine targeting

### The RFM+ Framework

**RFM+ Score = (R × 0.20) + (F × 0.20) + (M × 0.25) + (E × 0.20) + (S × 0.15)**

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| **R** - Recency | 20% | How recently the client had active engagement |
| **F** - Frequency | 20% | Number of distinct projects/phases/engagements |
| **M** - Monetary | 25% | Total lifetime revenue from the client |
| **E** - Engagement Quality | 20% | How well client worked with methodology, ease of delivery |
| **S** - Strategic Value | 15% | Referrals generated, case study potential, market positioning value |

### Segment Thresholds

| Score Range | Segment | Interpretation |
|-------------|---------|----------------|
| 4.50 - 5.00 | **Champions** | Best clients, model for ICP, prioritize for expansion |
| 3.75 - 4.49 | **Loyal** | Strong clients, nurture relationship |
| 3.00 - 3.74 | **Promising** | Good potential, some gaps to address |
| 2.25 - 2.99 | **At-Risk** | Fit concerns, cautious approach for future |
| 1.00 - 2.24 | **Misaligned** | Poor fit, do not replicate this profile |

---

### Input Requirements

#### Data Sources

| Source | Purpose | Key Data Elements |
|--------|---------|-------------------|
| **CRM** (HubSpot/Salesforce/etc.) | Primary deal/opportunity data | Deal amounts, close dates, stages, companies, contacts, industries, company attributes |
| **Financial System** (QuickBooks/Xero/etc.) | Revenue validation | Invoices, payments, actual collected revenue |
| **Time/Project Tracking** (Harvest/Toggl/etc.) | Project engagement data | Hours tracked, projects, budget vs. actual, team members |
| **Qualitative Data** (optional) | Client feedback and strategic value | NPS scores, referrals, case studies, testimonials |

---

### Analysis Workflow

#### Phase 1: Data Preparation

##### Step 1.1: Identify Client/Company as Primary Key

**Objective**: Create master company list and map all data sources to it

**Process**:
1. Extract all companies from CRM (primary source)
2. Use Company ID as primary key
3. Map records from other systems via name matching
4. Flag unmatched records for manual review

**System Identifier Mapping**:

| System | Identifier | Mapping Approach |
|--------|-----------|------------------|
| HubSpot | Company ID, Company Name, Domain | Use Company ID as primary |
| Salesforce | Account ID, Account Name | Use Account ID as primary |
| QuickBooks | Customer Name, Customer ID | Fuzzy match to CRM via name |
| Harvest | Client Name, Client ID | Fuzzy match to CRM via name |

##### Step 1.2: Data Mapping by Source

**From CRM**:

| Data Needed | HubSpot Field | Salesforce Equivalent | Purpose |
|-------------|---------------|----------------------|---------|
| Company identifier | Company ID | Account ID | Primary key |
| Company name | Company Name | Account Name | Matching |
| Deal/Opportunity records | Associated Deals | Opportunities | R, F, M calculation |
| Deal amount | Amount | Amount | M score |
| Deal close date | Close Date | Close Date | R score |
| Deal stage | Deal Stage | Stage | Filter to closed-won |
| Deal create date | Create Date | Created Date | Sales cycle |
| Industry | Industry | Industry | ICP extraction |
| Employee count | Number of Employees | Employees | ICP extraction |
| Annual revenue | Annual Revenue | Annual Revenue | ICP extraction |
| Location | Country, State/Region | Billing Country | ICP extraction |
| Deal source | Original Source, Deal Source | Lead Source | S score (referrals) |

**Filter Criteria**:
- **Include**: Closed Won deals only
- **Exclude**: Open deals, Lost deals, Churned (unless analyzing churn)
- **Date range**: All historical data (or specify analysis window)

**From Financial System**:

| Data Needed | QuickBooks Field | Xero Equivalent | Purpose |
|-------------|------------------|-----------------|---------|
| Customer identifier | Customer Name | Contact Name | Matching |
| Invoice amount | Total Amount | Total | M validation |
| Invoice date | Invoice Date | Date | R validation |
| Payment status | Status (Paid/Open) | Status | Cash collection |
| Invoice line items | Line items | Line items | Service mix |

**Aggregation Required**:
- Sum all invoices by customer → total collected revenue
- Identify most recent invoice date → recency validation
- Count distinct invoice periods → frequency validation

**From Time/Project Tracking**:

| Data Needed | Harvest Field | Toggl Equivalent | Purpose |
|-------------|---------------|------------------|---------|
| Client identifier | Client Name | Client | Matching |
| Project name | Project Name | Project | F score (project count) |
| Project status | Active/Archived | Active/Archived | Filter |
| Total hours | Hours (sum) | Duration (sum) | Delivery analysis |
| Billable hours | Billable Hours | Billable | E score input |
| Budget hours | Budget | Estimate | E score (budget vs actual) |
| Date range | Time entries | Time entries | R score validation |

**Aggregation Required**:
- Count distinct projects per client
- Sum total hours per client
- Calculate budget vs. actual variance per project
- Identify most recent time entry for recency

---

#### Phase 2: Scoring Logic

##### R Score (Recency) - 20% Weight

**Calculate**: Days since last engagement end date

**Primary Source**: CRM deal close date OR time tracking last entry date (whichever is more recent)

| Score | Days Since Last Engagement | Interpretation |
|-------|---------------------------|----------------|
| 5 | 0-90 days (active or just completed) | Hot relationship |
| 4 | 91-180 days | Warm, expansion window |
| 3 | 181-365 days | Cooling, needs attention |
| 2 | 366-540 days | At risk, relationship fading |
| 1 | 541+ days | Cold, requires reactivation |

**Edge Cases**:
- If currently active (project in progress) → score = 5
- Use MORE RECENT of: deal close date, last invoice date, last time entry
- If data conflicts → prioritize time tracking (most accurate for engagement end)

##### F Score (Frequency) - 20% Weight

**Calculate**: Count of distinct engagements/projects

**Primary Source**: CRM deal count OR time tracking project count (whichever is higher)

| Score | Number of Engagements | Interpretation |
|-------|-----------------------|----------------|
| 5 | 4+ projects/phases | Champion client |
| 4 | 3 projects/phases | Strong relationship |
| 3 | 2 projects/phases | Growing relationship |
| 2 | 1 completed project | Single engagement |
| 1 | 1 incomplete or assessment only | Minimal depth |

**Counting Rules**:
- Each distinct deal/project = 1 engagement
- Multi-phase projects with separate deals = count each phase
- Retainer arrangements: count each renewal period OR each 6-month block
- Do not double-count: if one deal = one project, count once

##### M Score (Monetary) - 25% Weight

**Calculate**: Total lifetime revenue from client

**Primary Source**: CRM deal amounts (summed) VALIDATED BY financial system invoices

**Percentile-Based Scoring** (Recommended):

| Score | Lifetime Revenue | Interpretation |
|-------|------------------|----------------|
| 5 | Top 20% of clients | Highest value tier |
| 4 | 60th-80th percentile | Above average |
| 3 | 40th-60th percentile | Average |
| 2 | 20th-40th percentile | Below average |
| 1 | Bottom 20% | Minimal revenue |

**Calculation Steps**:
1. Sum all closed-won deal amounts per company (from CRM)
2. Validate against financial system: flag discrepancies >10%
3. Rank all companies by total revenue
4. Assign scores based on percentile position

**Alternative Fixed Thresholds**:
- Determine average deal size from data
- Score 5 = 2x+ average lifetime value
- Score 4 = 1.5x-2x average
- Score 3 = 0.75x-1.5x average
- Score 2 = 0.5x-0.75x average
- Score 1 = <0.5x average

##### E Score (Engagement Quality) - 20% Weight

**Calculate**: Composite of delivery efficiency and relationship quality

**Data Sources**: Time tracking (budget vs. actual), CRM notes, qualitative input

**Sub-components** (if data available):

| Component | Calculation | Weight |
|-----------|-------------|--------|
| Budget Adherence | Actual hours / Budget hours | 40% |
| Project Completion | % of projects completed successfully | 30% |
| Sales Cycle Efficiency | Days to close vs. average | 15% |
| Stakeholder Depth | # contacts engaged at company | 15% |

**Budget Adherence Scoring**:

| Score | Actual vs. Budget | Interpretation |
|-------|------------------|----------------|
| 5 | 90-105% of budget | Excellent scoping and execution |
| 4 | 80-90% OR 105-115% | Good, minor variance |
| 3 | 70-80% OR 115-130% | Acceptable, some scope issues |
| 2 | 60-70% OR 130-150% | Problematic, significant overrun |
| 1 | <60% OR >150% | Major issues |

**If quantitative E data not available**:
- Request qualitative assessment from project owner
- Use proxy indicators: deal stage velocity, email response rates, meeting frequency
- Default to score of 3 (neutral), flag for manual review

##### S Score (Strategic Value) - 15% Weight

**Calculate**: Non-revenue value contribution

**Data Sources**: CRM deal source (referral tracking), marketing records, qualitative input

**Point System**:

| Factor | Points | Data Source |
|--------|--------|-------------|
| Referral generated (per referral) | +3 | CRM deal source = referral from this company |
| Case study participation | +3 | Marketing records / qualitative |
| Testimonial provided | +2 | Marketing records |
| Logo usage permission | +1 | Contract / qualitative |
| Reference call availability | +2 | Sales notes / qualitative |
| Industry thought leadership value | +2 | If client in strategic target industry |

**Convert Points to Score**:

| Points | Score |
|--------|-------|
| 12+ | 5 |
| 9-11 | 4 |
| 6-8 | 3 |
| 3-5 | 2 |
| 0-2 | 1 |

**If S data not available**:
- Check CRM for deals sourced as "referral" and trace back to referring company
- Default to score of 2 (some inherent value)
- Flag for manual enrichment

---

#### Phase 3: Analysis Outputs

##### Output 1: Client Scoring Table

| Company | R Score | F Score | M Score | E Score | S Score | Composite | Segment | Data Completeness |
|---------|---------|---------|---------|---------|---------|-----------|---------|-------------------|
| [Name] | [1-5] | [1-5] | [1-5] | [1-5] | [1-5] | [1.00-5.00] | [Segment] | [%] |

**Data Completeness**: % of scores based on actual data vs. defaults/proxies. Flag clients with <60% completeness for manual review.

##### Output 2: Segment Summary

| Segment | Count | % of Clients | Total Revenue | % of Revenue | Avg Composite Score |
|---------|-------|--------------|---------------|--------------|---------------------|
| Champions | | | | | |
| Loyal | | | | | |
| Promising | | | | | |
| At-Risk | | | | | |
| Misaligned | | | | | |

##### Output 3: Dimension Analysis

For each dimension (R, F, M, E, S):
- Score distribution (count at each score level)
- Correlation with composite score
- Data quality issues encountered

##### Output 4: ICP Pattern Extraction

**From Champions + Loyal segments (score ≥ 3.75)**, extract:

**Firmographic Patterns**:
- Industry distribution (% in each industry)
- Revenue range (min, max, median, mode)
- Employee count range
- Geographic concentration
- Company stage/type patterns

**Behavioral Patterns**:
- Average deal size at first engagement
- Average time to expansion (first deal → second deal)
- Common entry point (what service did they start with)
- Stakeholder patterns (how many contacts, what roles)

**Engagement Patterns**:
- Average sales cycle length
- Budget adherence patterns
- Project duration patterns

##### Output 5: Anti-Pattern Identification

**From Misaligned segment (score < 2.25)**, identify:
- What firmographic attributes are over-represented?
- What was different about their engagement pattern?
- What E score components drove low scores?
- Were there early warning signs in first engagement?

##### Output 6: ICP Tier Recommendations

```
Tier 1 (Best Fit) Criteria:
- [Firmographic criteria from Champions]
- [Behavioral signals from Champions]
- [Minimum thresholds]

Tier 2 (Good Fit) Criteria:
- [Broader firmographic criteria]
- [Partial signal match]

Tier 3 (Moderate Fit) Criteria:
- [Minimum acceptable criteria]

Exclusion Criteria:
- [Anti-patterns from Misaligned segment]
```

---

### Data Quality Handling

#### Missing Data Protocol

| Scenario | Handling |
|----------|----------|
| Company in CRM but not in financial system | Use CRM data only, flag for validation |
| Company in financial system but not in CRM | Add to analysis with note (data hygiene issue) |
| No deal amount in CRM | Use financial system invoice total |
| No project/time data | F score from CRM deal count only |
| No E score data available | Default to 3, flag for manual input |
| No S score data available | Default to 2, flag for manual input |

#### Data Validation Checks

Perform and report discrepancies:

1. **Revenue Validation**: CRM deal sum vs. financial system invoice sum (variance >10% = flag)
2. **Project Count Validation**: CRM deals vs. time tracking projects (should be similar)
3. **Date Validation**: Deal close dates should precede or match invoice dates
4. **Duplicate Check**: Same company with multiple names/spellings across systems

---

### Analysis Checklist

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

### Clustering vs. Fixed Scoring Decision

**Use K-Means Clustering When**:
- First-time analysis with no prior thresholds
- Large client base (50+ clients) where natural groupings may exist
- Exploratory analysis to discover patterns
- Validating or calibrating fixed thresholds

**Use Fixed Scoring When**:
- Operationalizing for ongoing CRM use
- Small client base (<50) where K-means may be unstable
- Need consistent, interpretable segments over time
- Integrating with workflows and automation

**Recommended Approach**:
1. Run K-means first to discover natural clusters
2. Analyze cluster characteristics
3. Extract threshold values from cluster boundaries
4. Implement fixed scoring with discovered thresholds

---

## Workshop Sequence Integration

### How Workshops Connect

```
┌─────────────────────────────────────────────────────────────────┐
│                     WORKSHOP SEQUENCE FLOW                       │
└─────────────────────────────────────────────────────────────────┘

WORKSHOP 1: GTM DISCOVERY
├─ Input: Current state discovery (transcript, CRM data, maturity assessment)
├─ Process: 6-step analysis framework
├─ Output:
│  ├─ GTM Maturity Score (1-4 across 4 pillars)
│  ├─ Revenue Health Score (/50 across 5 dimensions)
│  ├─ Pipeline Architecture Map
│  ├─ GTM Motion Map
│  ├─ Strategic Priorities (top 5 opportunities)
│  └─ Initial ICP hypothesis (based on desired customer characteristics)
│
└─> FEEDS INTO Workshop 2

WORKSHOP 2: RFM+ ANALYSIS
├─ Input:
│  ├─ Initial ICP hypothesis from Workshop 1
│  ├─ CRM data (deals, companies, contacts)
│  ├─ Financial data (invoices, revenue)
│  ├─ Project tracking data (hours, projects)
│  └─ Qualitative data (referrals, case studies)
├─ Process:
│  ├─ Data preparation & mapping
│  ├─ RFM+ scoring (5 dimensions)
│  ├─ Client segmentation
│  ├─ Pattern extraction from Champions/Loyal
│  └─ Anti-pattern identification from Misaligned
├─ Output:
│  ├─ Client scoring table (all clients scored)
│  ├─ Segment summary (distribution & revenue)
│  ├─ ICP patterns (firmographic, behavioral, engagement)
│  ├─ Anti-patterns (exclusion criteria)
│  └─ ICP tier recommendations (Tier 1/2/3 + exclusions)
│
└─> VALIDATES & REFINES Workshop 1 ICP hypothesis

SYNTHESIS: BLUEPRINT WORKSHOP
├─ Input: Outputs from both workshops
├─ Process:
│  ├─ Organizational design
│  ├─ Pipeline architecture finalization
│  ├─ CRM taxonomy design
│  └─ Program planning (2-4 priority programs)
└─ Output: Implementation roadmap
```

### Key Integration Points

1. **ICP Validation Loop**:
   - Workshop 1 creates ICP hypothesis based on: competitive positioning, target customer characteristics, strategic priorities
   - Workshop 2 validates this hypothesis against actual historical client data
   - Discrepancies inform refinement: "We think we want X customers, but Y customers are actually our Champions"

2. **Maturity → Data Quality**:
   - Workshop 1 Infrastructure Pillar score predicts data quality issues in Workshop 2
   - Low Infrastructure scores (1-2) → expect missing CRM data, poor attribution
   - Plan Workshop 2 data preparation accordingly

3. **Strategic Priorities → ICP Tiers**:
   - Workshop 1 identifies growth priorities (e.g., "expand into enterprise")
   - Workshop 2 ICP tiers should align with these priorities
   - If priorities misalign with Champion patterns → strategic decision required

4. **Quick Wins**:
   - Workshop 1 identifies immediate opportunities (e.g., "fix pipeline stage definitions")
   - Workshop 2 may reveal additional quick wins (e.g., "Champions share common entry point")
   - Combine for comprehensive quick win recommendations

### Deliverable Timeline

| Milestone | Timeline | Deliverable |
|-----------|----------|-------------|
| **Workshop 1 Execution** | Day 1 | 90-minute Discovery workshop conducted |
| **Workshop 1 Analysis** | Days 2-5 | Complete 6-step analysis framework |
| **Workshop 1 Delivery** | Day 6 | Present findings and recommendations |
| **Workshop 2 Data Prep** | Days 7-10 | Gather and map data from all sources |
| **Workshop 2 Analysis** | Days 11-14 | Complete RFM+ scoring and pattern extraction |
| **Workshop 2 Delivery** | Day 15 | Present ICP tiers and recommendations |
| **Synthesis** | Days 16-17 | Integrate findings from both workshops |
| **Blueprint Workshop** | Day 18 | Facilitate decision-making on priorities and roadmap |

---

## Templates & Tools

### Template 1: Transcript Extraction Table

```markdown
# GTM Discovery Transcript Extraction
**Company**: [Name]
**Date**: [Date]
**Participants**: [Names and roles]
**Analyst**: [Your name]

## FRAME 1: BUSINESS CONTEXT & MODEL (15 min)

| Question | Answer | Confidence | Notes |
|----------|--------|------------|-------|
| Annual revenue | [Extract] | HIGH/MED/LOW | [Notes] |
| Number of employees | [Extract] | HIGH/MED/LOW | [Notes] |
| Revenue streams | [Extract] | HIGH/MED/LOW | [Notes] |
| New vs Expansion vs Renewal mix | [Extract] | HIGH/MED/LOW | [Notes] |
| Growth trajectory (3 years) | [Extract] | HIGH/MED/LOW | [Notes] |
| Growth stage | [Plateau/Steady/High/Hyper] | HIGH/MED/LOW | [Notes] |

[Repeat for all frames...]
```

### Template 2: RFM+ Scoring Spreadsheet Structure

**Sheets**:
1. **Master Client List** - Primary key with all client identifiers
2. **R Score** - Recency calculations and scoring
3. **F Score** - Frequency calculations and scoring
4. **M Score** - Monetary calculations and scoring
5. **E Score** - Engagement quality calculations and scoring
6. **S Score** - Strategic value calculations and scoring
7. **Composite Scores** - Final RFM+ scores and segments
8. **Segment Summary** - Aggregated segment analysis
9. **ICP Patterns** - Pattern extraction from top segments
10. **Anti-Patterns** - Warning signs from bottom segments
11. **Data Quality** - Completeness and validation flags

### Template 3: Executive Summary Structure

```markdown
# [Company Name] GTM Assessment
**Executive Summary**

## Current State
- **GTM Maturity**: [Score] / 4.0 - [Level]
- **Revenue Health**: [Score] / 50 - Grade [X]
- **Primary Bottleneck**: [Stage transition]
- **Biggest Gap**: [Pillar/Dimension]

## Top 3 Opportunities
1. **[Opportunity Name]** - Estimated impact: [$ or %]
2. **[Opportunity Name]** - Estimated impact: [$ or %]
3. **[Opportunity Name]** - Estimated impact: [$ or %]

## Recommended Quick Win
**[Quick Win Name]** - [Timeline] - [Immediate impact]

## ICP Validation
- **Champions Profile**: [Key characteristics]
- **Misaligned Profile**: [Avoid these characteristics]
- **Strategic Alignment**: [How Champion profile aligns with growth goals]

## Next Steps
1. [Action item with owner]
2. [Action item with owner]
3. [Action item with owner]
```

---

## Best Practices & Tips

### For GTM Discovery Analysis

1. **Quote Liberally**: Use direct quotes from transcript to support every score and finding
2. **Show Your Math**: When estimating impact, show calculation logic
3. **Be Conservative**: Better to underestimate impact than over-promise
4. **Flag Gaps**: Call out missing information explicitly and recommend follow-up questions
5. **Think Systems**: Connect findings across pillars (e.g., low Infrastructure score → poor Intelligence capture)

### For RFM+ Analysis

1. **Data Quality First**: Invest time in data preparation and validation upfront
2. **Percentile over Fixed**: Use percentile-based M score for more adaptable analysis
3. **Manual Review Champions**: Manually review Champion segment scores to ensure they pass "smell test"
4. **Enrich S Score**: Actively seek qualitative data for Strategic Value - it's often the most insightful
5. **Visualize Segments**: Create visual representations of segment distributions for stakeholder communication

### For Both Workshops

1. **Confidence Calibration**: Be honest about confidence levels - "LOW" is better than wrong
2. **Actionability**: Every recommendation should include WHO does WHAT by WHEN
3. **Revenue Impact**: Always connect findings to revenue outcomes ($ or %)
4. **Quick Wins**: Identify 1-2 quick wins that demonstrate value immediately
5. **Follow-up Questions**: End every analysis with clarifying questions for next conversation

---

## Appendix: Reference Tables

### GTM Maturity Benchmarks by Company Stage

| Revenue Stage | Expected Overall Score | Top Quartile Score |
|---------------|------------------------|-------------------|
| $5-20M | 1.5-2.0 (Early Structured) | 2.0-2.5 |
| $20-50M | 2.0-2.5 (Structured) | 2.5-3.0 |
| $50-100M | 2.5-3.0 (Early Proactive) | 3.0-3.5 |
| $100M+ | 3.0+ (Proactive) | 3.5-4.0 |

### Industry Benchmark: Sales Cycle & Win Rate

| Industry | Avg Sales Cycle | Avg Win Rate | Avg Deal Size |
|----------|----------------|--------------|---------------|
| SaaS (SMB) | 30-60 days | 20-25% | $10-50K |
| SaaS (Enterprise) | 120-180 days | 15-20% | $100-500K |
| Professional Services | 45-90 days | 25-30% | $25-150K |
| Manufacturing | 90-180 days | 20-25% | $50-500K |

### RFM+ Score Distribution Guidelines

For a healthy B2B services client base:

| Segment | Expected % of Clients | Expected % of Revenue |
|---------|----------------------|----------------------|
| Champions | 10-15% | 30-40% |
| Loyal | 20-25% | 30-35% |
| Promising | 30-35% | 20-25% |
| At-Risk | 20-25% | 8-12% |
| Misaligned | 10-15% | 3-5% |

---

## Contact & Support

For questions about this workflow:
- Review the detailed instructions in each workshop section
- Refer to templates and examples provided
- Check reference tables for benchmarks
- Ensure all deliverable checklist items are completed before finalization
