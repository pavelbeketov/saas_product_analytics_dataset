# SaaS Product Analytics Lab — Synthetic Dataset

**All data are synthetic, generated for education. Not real company data.**

Period: 2025-01-01 through 2025-12-31. 50,000 users. All money in USD.

## Files and keys
- `users.csv`: one row per user (`user_id`).
- `events.csv`: one row per product event (`event_id`); links to users by `user_id`.
- `subscriptions.csv`: subscription records (`subscription_id`); links to users.
- `payments.csv`: paid invoices (`payment_id`); links to users and subscriptions.
- `experiment_assignments.csv`: one assignment per user for onboarding_v1.
- `marketing_spend.csv`: daily channel spending (no user-level attribution).

## Analysis challenges
1. Build a signup-to-onboarding-to-trial-to-purchase funnel.
2. Calculate signup cohorts, activity retention, paid conversion, ARPU, and revenue by month.
3. Investigate mobile conversion and acquisition channel quality.
4. Compare experiment variants for trial start; report effect size and confidence interval.
5. Build a Power BI dashboard with a date dimension and documented measures.

## Important caveats
- Event behavior and subscriptions are simplified, not a production event stream.
- `subscriptions.status` is a simulated status, not an as-of-date historical status.
- Experiment assignment is randomized, but the simulated treatment influences trial start only; it is not a real experiment.
- Synthetic marketing spend is not calibrated to customer acquisition costs.
- No causal claim should be made about observed non-experimental correlations.
