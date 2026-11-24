# The Finance and Economics Papers Podcast: The Bounce in the Price. Bao, Pan and Wang (2011) on the Illiquidity of Corporate Bonds

> **Open-source educational project.** The Finance and Economics Papers Podcast is a free, open-source initiative
> whose only goal is education: to create and spread knowledge about research in finance and economics. This
> episode is an independent, unofficial explanation of the paper below, written in our own words for teaching
> purposes. It is not affiliated with or endorsed by the authors or the publisher. The paper is not reproduced
> here: read the original at the DOI link. Short quotes are attributed to the authors. Scripts and audio are
> released under CC BY 4.0; the paper remains the property of its authors and publisher.

- **Paper:** Bao, J., Pan, J., & Wang, J. (2011). The illiquidity of corporate bonds. *The Journal of Finance*, 66(3), 911-946.
- **Read the paper:** https://doi.org/10.1111/j.1540-6261.2011.01655.x
- **Topics:** Corporate bonds and credit; market liquidity; asset pricing; the 2008 financial crisis
- **Length:** 21 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Quick note before we start. This is an open-source, educational project. We explain published research in our own words, for learning only. We are not affiliated with the authors or the journal, and the best thing you can do after listening is read the original paper. The link is in the episode notes.

MEI: Today, a paper about something every bond trader knows and almost nobody could measure. Jack Bao, Jun Pan and Jiang Wang, "The Illiquidity of Corporate Bonds," Journal of Finance, 2011. Thirty-six pages.

MIGUEL: Illiquidity. So, bonds that are hard to sell.

MEI: Hard to sell without moving the price. Here's the hook. In the autumn of 2008, the yield spreads on corporate bonds exploded. Two stories were on the table. One: companies had become much riskier, so lenders demanded more. Two: nobody could trade, so prices fell for lack of buyers. Credit crisis, or liquidity crisis?

MIGUEL: And everybody had an opinion and nobody had a number.

MEI: That's the gap this paper fills. The authors build a simple measure of illiquidity for every bond, from the bounce a trade leaves in its price, and then ask how much of the spread it explains. The answer, for the safest bonds in the crisis, is: most of it.

MIGUEL: Who are the authors?

MEI: Jack Bao was at Ohio State when the paper came out and is now at the University of Delaware. He got his PhD at MIT in 2009, with a thesis on corporate bonds, and his advisor was the second author, Jun Pan. Pan was a professor at MIT Sloan and is now at the Shanghai Advanced Institute of Finance. She has two PhDs: physics at NYU, then finance at Stanford. Jiang Wang is the Mizuho Financial Group Professor at MIT Sloan. He also started in physics, with a physics PhD from Penn before a finance PhD from Wharton.

MIGUEL: Two physicists and their student, measuring bounces. That tracks.

MEI: And a story from the paper itself. It thanks the editor, Campbell Harvey, and Andrew Lo among others, and it exists only because regulators forced bond dealers to report their trades. More on that in a minute. Okay, let's start with the question.

## The problem

MEI: Everyone agreed that illiquidity matters for corporate bond prices. But the evidence was, in the authors' words, "mostly qualitative and indirect." The usual approach was to build a model of credit risk, see how much of the spread it explained, and call the rest illiquidity.

MIGUEL: The leftover approach. Whatever I can't explain must be the thing I didn't measure.

MEI: And the leftover was big. Earlier work had found that spreads were far too high to be explained by default risk alone, especially for safe bonds. But a leftover is not a measurement. You can't say how illiquidity moves over time, or which bonds suffer from it, if all you have is a residual.

MIGUEL: So they want a direct measure, bond by bond.

MEI: Bond by bond, month by month. And then two tests. In the time series: do changes in market-wide illiquidity explain changes in spreads? In the cross-section: do more illiquid bonds carry higher spreads, holding credit risk fixed?

## The measure: gamma

MIGUEL: So how do you measure something as vague as illiquidity?

MEI: With one idea. Think of a bond's log price as two pieces. One piece is the fundamental value, which follows a random walk: new information arrives and the price moves permanently. The other piece is transitory: a temporary push that comes from the frictions of trading, and that fades away.

MIGUEL: Like when a big seller shows up and the dealer lowers the price to take the bonds, and then the price drifts back.

MEI: Exactly that. The dealer needs to be compensated for holding inventory, so the trade pushes the price away from fundamental value, and later it comes back. Now, what does a temporary push look like in the data? A price change followed by a price change in the opposite direction. A bounce.

MIGUEL: Negative autocorrelation.

MEI: Negative autocovariance of consecutive price changes. And that's the measure. They call it gamma: minus the covariance between this price change and the next one. If the fundamental value is a random walk, its changes are uncorrelated and contribute nothing. So gamma depends only on the transitory piece, and it grows with the size of the bounces.

MIGUEL: So a perfectly liquid bond has gamma zero, and the more the price bounces around, the bigger gamma.

MEI: Right. And there's a nice connection to a classic. In 1984, Richard Roll showed that if prices just bounce between the bid and the ask, the autocovariance equals minus the spread squared over four. So in that special case, two times the square root of gamma is the bid-ask spread.

MIGUEL: So gamma is a generalized bid-ask spread.

MEI: It captures bid-ask bounce and anything else that pushes prices temporarily: dealers' inventory, thin markets, slow buyers. And it does so without any pricing model of credit risk. That's the selling point.

MIGUEL: Any caveats?

MEI: Three, and the authors list them. Gamma mixes together how big the transitory push is and how fast it fades. It is only a partial measure. And it depends on the horizon over which you measure price changes. They mostly use trade-by-trade and daily prices, so gamma captures the high-frequency part of illiquidity.

## The data

MIGUEL: Where do you get trade-by-trade prices for corporate bonds? I thought that market was a black box.

MEI: It was, until TRACE. The Trade Reporting and Compliance Engine, run by FINRA. US regulators forced dealers to report their corporate bond trades, in phases. Phase one in July 2002 covered big investment-grade issues. Phase two, from April 2003, expanded coverage to about 4,650 bonds. Phase three, complete in February 2005, covered about ninety-nine percent of all public transactions.

MIGUEL: So this paper exists because of a regulation.

MEI: Entirely. The sample runs from April 2003 to June 2009, and the authors keep only the phase one and two bonds, so the set of bonds is comparable over time. Then they filter hard. A bond must trade on at least seventy-five percent of its business days, be in the data for at least a full year, and be investment grade.

MIGUEL: How many survive?

MEI: One thousand and thirty-five bonds. Big ones: the median issue is seven hundred and fifty million dollars. The median rating is A2, average maturity about six years, average age about four.

MIGUEL: And those filters bias the sample toward liquid bonds.

MEI: Very much so, and the authors say it. Their bonds turn over seven and a half percent a month, against under four percent for the whole TRACE universe. They trade two hundred and eight times a month, against thirty-three. The median trade is three hundred and twenty-four thousand dollars, against sixty-five thousand. So whatever illiquidity they find is a lower bound. If it shows up in the most liquid bonds, it's real.

## How illiquid are corporate bonds?

MIGUEL: Okay. Numbers. How big is gamma?

MEI: Using trade-by-trade prices, the average bond has a gamma of 0.63, with a t-statistic of nineteen. The median is 0.34. And here's the striking part: 99.81 percent of the bonds have a statistically significant gamma.

MIGUEL: So it's not a few terrible bonds dragging the average. It's everyone.

MEI: Everyone. With daily prices the numbers are bigger, an average of 1.18 and a median of 0.56, because the daily change accumulates several bounces. And now the comparison that makes the paper. Take each bond's quoted bid-ask spread from Bloomberg and compute the gamma that pure bid-ask bounce would generate. The median of that implied gamma is 0.026.

MIGUEL: Against an actual 0.56. That's twenty times bigger.

MEI: More than an order of magnitude. Flip it around with Roll's formula: the median gamma implies a bid-ask spread of one and a half percent. The median quoted spread is 0.29 percent.

MIGUEL: So the price bounces five times more than the quoted spread says it should.

MEI: And it's not just quoted spreads, which are indicative rather than binding. Another study, by Edwards, Harris and Piwowar, had estimated actual effective spreads from a richer version of the TRACE data. The gamma-implied spreads in this paper are fifty percent higher than those estimates for small trades, about double for trades of a hundred to two hundred thousand dollars, and more than four times higher for trades around a million.

MIGUEL: So bid-ask bounce is a small part of the story.

MEI: The authors' conclusion is that illiquidity in corporate bonds is "substantially beyond what the bid-ask spread captures."

MIGUEL: Hold on. If every bond bounces, does a portfolio of bonds bounce too?

MEI: Good question, and the answer is no. They compute gamma for equal-weighted and issuance-weighted portfolios of the same bonds, and it's essentially zero. The transitory pushes are idiosyncratic. They wash out when you average across bonds.

MIGUEL: So illiquidity is a bond-level thing.

MEI: At the level of the bounces, yes. But wait for the aggregate section, because the level of illiquidity moves together across bonds in a way that matters a lot.

## What makes a bond illiquid

MIGUEL: Before that: which bonds are the illiquid ones?

MEI: They regress each bond's yearly gamma on its characteristics. Older bonds are more illiquid: one more year of age adds 0.19 to gamma, which is more than fifteen percent of the average. That matters because traders have always used age as a proxy for illiquidity, and now it's confirmed by a direct measure.

MIGUEL: Why would age matter?

MEI: New bonds are actively traded by the investors who bought the issue. Over time they get locked into buy-and-hold portfolios, like insurers' and pension funds', and float dries up. Smaller issues are more illiquid too, and so are longer maturities. Credit rating doesn't matter much, but remember the sample is investment grade only.

MIGUEL: And trading activity?

MEI: This is the result I like most. Bonds with smaller average trade sizes are more illiquid. And bonds with more trades are more illiquid, not less. In the authors' words, "more trades do not imply more liquidity, especially if these trades are of small sizes."

MIGUEL: So a bond that trades a lot in tiny pieces is a bond retail investors are getting bounced around in.

MEI: That's one reading. And one more: within the bonds that have credit default swaps traded on their issuer, higher CDS spreads go with higher gamma. Credit risk and illiquidity are connected even at the level of a single firm.

## The crisis, month by month

MEI: Now the aggregate. Each month, they compute gamma for every bond and take the median across bonds. That's market-wide illiquidity. And its time series is the story of the crisis.

MIGUEL: Give me the numbers.

MEI: Before August 2007, aggregate gamma sat around 0.30, with a standard deviation of 0.10. In August 2007, when the credit problem first broke out, it doubled to 0.60. In March 2008, when Bear Stearns collapsed, it tripled the pre-crisis average, at 0.90, an all-time high at the time.

MIGUEL: And then September.

MEI: September 2008, Lehman defaults, AIG is bailed out: gamma reaches 1.59. Over twelve standard deviations from its pre-crisis level. And it kept getting worse. The peak is October 2008, at 3.37.

MIGUEL: Eleven times the normal level. A month after Lehman.

MEI: After which it declined slowly, as the Federal Reserve injected liquidity and markets calmed down. There's also an earlier bump in May 2005, when Ford and GM were downgraded to junk.

MIGUEL: So illiquidity isn't just a bond-level nuisance. It spikes for the whole market at once.

MEI: And it spikes with everything else. Regress monthly changes in aggregate gamma on changes in the VIX, the stock market's fear gauge, and you get an R-squared of sixty-seven percent. Exclude 2008 and 2009, and the relation is still there, with an R-squared of thirty-three percent.

MIGUEL: That's remarkable. One number comes from bond trades, the other from S&P 500 options.

MEI: The authors call it "a rather intriguing result." Shocks to market liquidity and shocks to market risk, or risk appetite, seem to interact. And once the VIX is in the regression, other market variables, like a CDS index or lagged returns, add little.

## Illiquidity and spreads

MIGUEL: Okay, the main event. Does illiquidity explain spreads?

MEI: Take the Barclays corporate bond indices by rating, and regress monthly changes in their yield spreads on monthly changes in aggregate gamma. For bonds rated A and above, illiquidity alone explains fifty-one percent of the variation for AAA, forty-seven percent for AA, and close to sixty percent for A.

MIGUEL: Half of the movement in safe-bond spreads is illiquidity.

MEI: Then add the CDS index as the measure of credit risk. It helps, raising the R-squared by thirteen to thirty points, but illiquidity remains the dominant force for high-rated bonds. And the VIX, despite its tight correlation with gamma, adds nothing once gamma is in.

MIGUEL: So gamma is not just a proxy for fear.

MEI: It carries information about bond spreads that the VIX does not. Now the subtle part. Split the sample. Before 2008, illiquidity and credit risk are about equally important: roughly twenty percent R-squared each, around forty percent combined. Include 2008 and 2009, and illiquidity takes over.

MIGUEL: How much?

MEI: For AAA bonds, the link to credit risk stops being significant, and the univariate R-squared of illiquidity doubles, from twenty-five to fifty-two percent. In money: before the crisis, a one-standard-deviation monthly jump in aggregate gamma moved AAA spreads by three and a half basis points. With the crisis included, it moves them by twenty-four.

MIGUEL: So for the safest bonds, 2008 was a liquidity crisis.

MEI: That's their conclusion, carefully worded: "as far as high-rated corporate bonds are concerned, the sudden increase in illiquidity was the dominating factor in driving up the yield spreads." For junk bonds it's different. Credit risk matters more there, which is consistent with what structural models had long said: default risk explains a lot of junk spreads and very little of AAA spreads.

## Bond by bond

MIGUEL: And in the cross-section?

MEI: Every month, regress each bond's yield spread over Treasuries on its gamma, with controls. The method is Fama-MacBeth with Newey-West errors, for those keeping score. A baseline first: controlling for callability, the average spread of Aaa and Aa bonds is a hundred and twenty-nine basis points, A bonds are sixty-one higher, and Baa bonds a hundred and seventy-six higher.

MIGUEL: And gamma?

MEI: The coefficient is 0.17, with a t-statistic of 9.6. Meaning: two bonds in the same rating category, one with a gamma higher by one unit, differ in spread by seventeen basis points. And the cross-sectional standard deviation of gamma is 3.84.

MIGUEL: So one standard deviation of illiquidity is worth about sixty-five basis points of spread.

MEI: Sixty-five basis points, among investment-grade bonds, where the whole spread is a couple of hundred. That's the headline number of the paper.

MIGUEL: Does it survive controls for credit risk?

MEI: They add the issuer's equity volatility, which captures asset risk and leverage: a ten-point increase in equity volatility adds twenty basis points. Gamma is unchanged. Then, for the bonds with CDS, they add the CDS spread, which is a very strong control, with a coefficient of 0.69. Gamma survives, with a smaller effect: twelve basis points per unit. Then bond age, issue size, and the trading variables. Still there.

MIGUEL: And the old proxies?

MEI: This is the part that stings for earlier work. Quoted bid-ask spreads are insignificant in explaining spreads once gamma is in. The percentage of days a bond trades comes in significant but with the wrong sign. The direct measure beats the proxies.

## Three more facts about the bounce

MEI: The last section digs into the dynamics, and three results are worth knowing. First, the bounce doesn't finish in one trade. The covariance between a price change and the change two trades later is still 0.12, significant for seventy-two percent of bonds. After three trades it's almost gone.

MIGUEL: So it takes a couple of trades for the price to recover.

MEI: Second, the bounce is asymmetric. Reversals are stronger after a price drop than after a price rise. That matches a theory by Huang and Wang, where liquidity comes from costly market participation: when a seller needs out, buyers are slow to arrive, so the price overshoots downward more.

MIGUEL: Which is exactly when you'd want liquidity.

MEI: Third, trade size. Within bonds of similar overall liquidity, gamma falls as trades get bigger, monotonically. For the least liquid quintile, it goes from 2.46 for trades under five thousand dollars to 1.07 for trades above half a million. For the most liquid quintile, from 0.21 to 0.02.

MIGUEL: So small trades get bounced the most. That's the retail investor paying for the privilege.

MEI: Possibly, but the authors warn against reading it as "large trades face less illiquidity." Trade size and price are both chosen by the traders. Big players negotiate, small ones take what the dealer quotes. It's an equilibrium outcome, not a mechanical rule.

## Limits and legacy

MIGUEL: What would you push back on?

MEI: Four things, most of which the authors raise themselves. The sample is the most liquid thousand bonds, so the levels are lower bounds and the cross-section is truncated. The horizon matters: gamma at daily frequency captures fast reversals, and there may be slower ones they can't see with six years of data. The separation between fundamental and transitory assumes no high-frequency variation in risk premiums. And the comparison with estimated bid-ask spreads is across different samples, so it's a comparison of magnitudes, not a formal test.

MIGUEL: And the legacy?

MEI: The measure became a standard. When people talk about the Bao-Pan-Wang illiquidity measure, this is it: minus the autocovariance of price changes, computed from TRACE. It gave the field a way to put a number on liquidity in an over-the-counter market without quotes. And it settled, for high-grade bonds at least, the question the paper opened with. The authors end with questions of their own: why is illiquidity so much higher in bonds than in stocks, what drives its common movement, and whether it signals an inefficiency that policy should address.

MIGUEL: Those are still open.

MEI: Some of them, yes.

## Wrap-up: the recap

MIGUEL: Okay, recap time. The whole paper in one minute.

MEI: The question: how illiquid are corporate bonds, and how much of their yield spreads is illiquidity rather than credit risk, especially in the 2008 crisis?

MIGUEL: The method?

MEI: A direct measure, gamma, minus the autocovariance of consecutive price changes, computed bond by bond from TRACE transaction data for about a thousand liquid investment-grade bonds from 2003 to 2009. Then regressions of spread changes on aggregate gamma over time, and of individual spreads on bond-level gamma across bonds, with credit controls.

MIGUEL: Main takeaways?

MEI: One: illiquidity is large and universal. The median gamma implies a spread of one and a half percent, five times the quoted bid-ask spread, and virtually every bond shows it. Two: it moves together across bonds and with the market: it rose from 0.30 before the crisis to 3.37 in October 2008, and tracks the VIX. Three: it prices. Illiquidity explains about half of the monthly changes in high-grade spreads, more than credit risk in the crisis, and one standard deviation of bond-level illiquidity is worth sixty-five basis points of spread, after controlling for credit risk.

MIGUEL: And the conclusion?

MEI: For high-rated corporate bonds, the spike in spreads in 2008 was mostly a liquidity event, not a credit event. And illiquidity is a first-order determinant of corporate bond prices, not a residual.

MIGUEL: My takeaway: the bounce in the price is the price of getting out. And the quoted spread is the brochure, not the bill.

MEI: Read the paper. Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you next time.
