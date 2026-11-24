# The Finance and Economics Papers Podcast: Everywhere Means Everywhere. Asness, Moskowitz and Pedersen (2013) on Value and Momentum Everywhere

> **Open-source educational project.** The Finance and Economics Papers Podcast is a free, open-source initiative
> whose only goal is education: to create and spread knowledge about research in finance and economics. This
> episode is an independent, unofficial explanation of the paper below, written in our own words for teaching
> purposes. It is not affiliated with or endorsed by the authors or the publisher. The paper is not reproduced
> here: read the original at the DOI link. Short quotes are attributed to the authors. Scripts and audio are
> released under CC BY 4.0; the paper remains the property of its authors and publisher.

- **Paper:** Asness, C. S., Moskowitz, T. J., & Pedersen, L. H. (2013). Value and momentum everywhere. *The Journal of Finance*, 68(3), 929-985.
- **Read the paper:** https://doi.org/10.1111/jofi.12021
- **Topics:** Asset pricing; factor models; anomalies; value; momentum; liquidity risk
- **Length:** 23 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Quick note before we start. This is an open-source, educational project. We explain published research in our own words, for learning only. We are not affiliated with the authors or the journal, and the best thing you can do after listening is read the original paper. The link is in the episode notes.

MEI: Today, the two most famous anomalies in finance, tested everywhere at once. Clifford Asness, Tobias Moskowitz and Lasse Heje Pedersen, "Value and Momentum Everywhere," Journal of Finance, 2013. Fifty-seven pages.

MIGUEL: Fifty-seven. And "everywhere" means?

MEI: Eight markets. Stocks in the United States, the United Kingdom, Europe and Japan. Country stock indices. Currencies. Government bonds. Commodities. Here's the hook. Value, buying what's cheap, and momentum, buying what's been rising, had each been studied for decades, mostly in American stocks, and mostly one at a time. This paper asks: do they work in every market? Do they move together across markets? And what happens if you hold both?

MIGUEL: And the answer?

MEI: They work everywhere. Value strategies move together across markets, momentum strategies move together across markets, and value and momentum move against each other. So a half-and-half mix across all eight markets has a Sharpe ratio of 1.45. That's several times the Sharpe ratio of the US stock market.

MIGUEL: Okay, that's a big number. Who are the authors?

MEI: Cliff Asness co-founded AQR Capital Management in 1998, after running quantitative research at Goldman Sachs Asset Management. His Chicago PhD dissertation, in 1994, was on momentum, with Eugene Fama and Kenneth French as co-chairs. Toby Moskowitz was the Fama Family Professor at Chicago Booth when the paper came out and moved to Yale in 2016. He won the Fischer Black Prize in 2007, and he is a principal at AQR. Lasse Heje Pedersen was at NYU Stern and Copenhagen Business School, is a principal at AQR too, and won the 2011 Bernacer Prize for the best European economist under forty. He later wrote the book Efficiently Inefficient.

MIGUEL: So all three authors work with the firm that trades these strategies. Should I worry?

MEI: They disclose it in the first footnote: AQR invests in value and momentum strategies. And the paper's design answers that worry: simple, uniform signals, the most liquid assets, and results anyone can replicate. The editor was Campbell Harvey, and a first draft circulated in 2008. Let's start with why anyone needed this paper.

## The problem

MEI: By 2009, when this paper was first submitted, value and momentum were old news in US stocks. Value: stocks with a high ratio of book value to market value earn more. Momentum: stocks that rose over the past year keep rising for a while. Both had competing theories, behavioral and rational.

MIGUEL: So what was missing?

MEI: Three things. First, almost all the evidence came from individual stocks, which raises the worry of data mining: if you test enough things on one dataset, something works. Second, value and momentum were studied separately, so nobody knew how they related. Third, the theories were built for stocks: firms, investment, growth options, investor psychology about companies. If the same patterns show up in currencies and commodities, those theories have a problem.

MIGUEL: Because a barrel of oil doesn't have a management team to overreact to.

MEI: Exactly. And a government bond has no book value, no earnings announcements, no analysts to be slow. If value and momentum show up there, and move in step with value and momentum in stocks, then the explanation has to be about investors and markets in general, not about firms.

MIGUEL: Or about something all these markets share. Like who trades them.

MEI: Hold that thought, it's where the paper ends up. So the authors ask four questions. How much do the premiums vary across markets? How correlated are they? What drives the correlation? And what's a natural benchmark model for global portfolios?

## Eight markets, two signals

MIGUEL: Tell me about the data. Eight markets is a lot of plumbing.

MEI: For stocks, they take the United States, the United Kingdom, continental Europe and Japan, and they restrict each to the big liquid names: the stocks that make up ninety percent of market capitalization. In the US that's the largest seventeen percent of firms, 354 stocks at the start in 1972. So the results are for a universe you could actually trade.

MIGUEL: That's conservative. Anomalies are usually stronger in small stocks.

MEI: And they say so. A footnote even admits that an earlier version of the paper used a broader, less liquid universe and found much stronger returns. They deliberately give that up, for two reasons: the results should describe strategies a large institution could run, and they should be comparable with futures and currencies, which are liquid by construction. Then eighteen developed-country equity index futures from 1978, ten currencies from 1979, ten government bond markets from 1982, and twenty-seven commodity futures from 1972. Everything monthly, ending in July 2011.

MIGUEL: And how do you define "value" for a currency?

MEI: This is the clever part, and the authors insist on keeping it simple to avoid data mining. For stocks, value is the standard book-to-market ratio, with book value lagged six months. For everything else, they use long-run reversal: a cheap asset is one whose price has fallen over the past five years. For commodities, the five-year change in the spot price. For currencies, the five-year change in the real exchange rate, which is the purchasing power parity gap. For bonds, the five-year change in the ten-year yield. For country indices, the MSCI book-to-market.

MIGUEL: And they check that the five-year reversal is really "value"?

MEI: In US stocks, a value portfolio built on five-year past returns has a correlation of 0.83 with one built on book-to-market. Close enough.

MIGUEL: And momentum?

MEI: The same in every market: the return over the past twelve months, skipping the most recent month, the standard measure.

MIGUEL: Why skip the last month?

MEI: Because returns over one month tend to reverse, for reasons linked to liquidity and microstructure, so including it would mix two different effects. For futures and currencies the skip isn't needed, and the authors note momentum is in fact stronger there without it. They skip anyway, for uniformity. The whole paper is built on that principle: one recipe, applied the same way everywhere, so that nobody can say the results were tuned market by market.

MIGUEL: And the portfolios?

MEI: Within each market, sort assets into three groups by value, and three by momentum. That gives low, middle and high portfolios for two signals in eight markets: forty-eight test portfolios. Plus, for each market, a long-short factor that weights assets by their rank: buy the cheap, sell the expensive, dollar neutral. And a fifty-fifty combination of the value and momentum factors.

MIGUEL: Forty-eight portfolios nobody had looked at together.

MEI: In the authors' words, "48 new test assets" that any asset pricing model should seek to explain. One more design choice matters for everything that follows. Commodity strategies are about four times as volatile as bond strategies, so when the authors combine asset classes they weight each one by the inverse of its volatility. Every market then contributes roughly the same risk to the global portfolio, instead of commodities drowning out everything else.

## The results: it works everywhere

MIGUEL: So, does value work in Japan? Does momentum work in commodities?

MEI: Value has a significant premium in every stock market, strongest in Japan. Momentum is positive in every stock market, strongest in Europe, but not significant in Japan. Outside stocks, both premiums are positive in every asset class, including novelties: value and momentum in government bonds, value in currencies and commodities, none of which had been documented before.

MIGUEL: All significant?

MEI: Not all. Bonds are the weak spot. With the simple five-year yield-change measure, bond value has a Sharpe ratio of only 0.18. The authors show that better value measures, like the real bond yield or the term spread, give 0.74 and 0.55, and a composite gets above 0.9. But they stick to the simple measure on principle.

MIGUEL: Okay. And the Japan momentum thing. That's a famous puzzle.

MEI: And the paper reframes it. Momentum doesn't work in Japan, but value works spectacularly, and the correlation between the two in Japan is minus 0.64. So a fifty-fifty mix in Japan has a higher Sharpe ratio than value alone. The authors' line: rather than explain why momentum failed in Japan, "it would be nearly equally appropriate to ask why value did so well."

MIGUEL: Wait. Say more about that negative correlation. That seems to be the heart of it.

MEI: It is the heart of it. Within every stock market, value and momentum returns are negatively correlated, about minus 0.60 on average. In the non-stock asset classes, minus 0.49. Two strategies that both make money, and that lose money at different times. Combine them and the Sharpe ratio jumps. In every single market, the combination beats both value and momentum alone.

MIGUEL: And across everything?

MEI: Weight each asset class so it contributes equal volatility, combine value and momentum fifty-fifty, and the Sharpe ratio is 1.45. The authors note that asset pricing models already struggle to explain the US equity premium, whose Sharpe ratio is about a third of that.

MIGUEL: So the hurdle for theory just got several times higher.

MEI: That's their framing. And notice what the global numbers reveal. Value applied across the four stock markets has a Sharpe ratio not much higher than the average of the four individual ones. If the four value strategies were independent bets, diversifying across them would have raised the Sharpe ratio a lot. It doesn't, which already tells you they rise and fall together.

MIGUEL: The missing diversification benefit is itself evidence of a common factor.

MEI: Nicely put. That's the bridge to the next section.

## They move together

MEI: Now the second big finding, comovement. Take the value strategy in one stock market and the average value strategy in the other three. Correlation: 0.68. Momentum with momentum elsewhere: 0.65. Stock momentum with momentum in bonds, currencies and commodities: 0.37.

MIGUEL: So value in Japan knows what value in Europe is doing.

MEI: And it cuts the other way too. Value in one stock market against momentum in the other stock markets: minus 0.53. Stock value against non-stock momentum: minus 0.26. The pattern is the same everywhere: value with value positive, momentum with momentum positive, value with momentum negative.

MIGUEL: Couldn't that just be the markets themselves moving together?

MEI: No, because these are long-short, market-neutral strategies. And the authors point out that they are more correlated across asset classes than the asset classes themselves are. Something ties value strategies together that is not the market.

MIGUEL: Is there a way to see all of this at once?

MEI: A principal component analysis. The first principal component loads with one sign on every value strategy and the opposite sign on every momentum strategy. It is essentially "long momentum, short value, everywhere," and it explains fifty-four percent of the covariance among the stock strategies and twenty-three percent across all asset classes.

MIGUEL: So there's a global value-versus-momentum factor hiding in there.

MEI: Which raises the question: what is it?

## What drives it: funding liquidity

MIGUEL: My first guess would be the business cycle.

MEI: They try. Growth, consumption, recessions, default risk. Only modest links. The variable that works is liquidity, and specifically funding liquidity: how easy it is for leveraged investors to borrow. They measure it with shocks to the TED spread and similar spreads, following Brunnermeier and Pedersen's theory of funding liquidity.

MIGUEL: And what do they find?

MEI: Funding liquidity shocks hurt value and help momentum. When borrowing gets easier, momentum does well and value does badly, and the other way round when funding dries up. So part of the negative correlation between the two comes from opposite exposures to the same risk.

MIGUEL: Why would momentum like easy money?

MEI: The authors offer an intuition, carefully labelled as a story. Momentum holds the most popular, crowded trades: the assets everyone has been piling into. Value is the contrarian side. When a liquidity shock forces investors to sell, they dump the crowded trades first, so momentum gets hit and value, less crowded, is spared.

MIGUEL: Is the effect strong?

MEI: Here's a methodological lesson worth remembering. If you look at one market at a time, you'd miss it. The average t-statistic of the liquidity exposure across the individual strategies is minus 0.95 for value and 1.81 for momentum. Not convincing. But regress the average value and momentum return across all markets on the liquidity shocks, and the t-statistics become minus 3.25 and 4.43. Averaging across markets washes out the noise and lets the common factor show.

MIGUEL: The power of everywhere.

MEI: That's literally the subsection title: "The Power of Averaging Across Markets." And liquidity risk is priced: in a cross-sectional regression on the forty-eight portfolios, the liquidity beta carries a premium of twenty-four basis points a month. Funding liquidity is priced, market liquidity is not.

MIGUEL: So does liquidity explain the premiums?

MEI: Only partly, and here's the twist. Momentum loads positively on liquidity risk, so part of its premium can be compensation for that risk. But value loads negatively, which makes the value premium an even deeper puzzle. And the fifty-fifty combination has essentially zero exposure to liquidity shocks, yet earns huge returns. The authors' conclusion: liquidity risk "cannot explain why a combination of value and momentum is so profitable."

MIGUEL: And this seems to have changed over time?

MEI: Markedly. Split the sample at August 1998, the peak of the funding crisis around Long-Term Capital Management. Before 1998, funding shocks barely matter. After 1998, value has a Sharpe ratio of 0.85 when liquidity is worsening and only 0.28 when it is improving. Momentum is the mirror image: 0.19 when liquidity worsens, 0.99 when it improves.

MIGUEL: So once leveraged arbitrageurs got big in these trades, funding became the thing.

MEI: That's the interpretation they suggest, with appropriate caution. They also check that the liquidity shocks they built are sensible: the global series spikes at the 1987 crash, September 2001, the quant meltdown of August 2007, Bear Stearns and Lehman. A dozen of the best-known liquidity events of the last twenty-five years show up on their own.

## A three-factor model for the world

MIGUEL: Okay. The benchmark model.

MEI: Two tests. The first is a comovement test with no overlap: explain value and momentum portfolios in one market using value and momentum factors built only from the other markets. The cross-sectional R-squared is 0.55, with average pricing errors of about twenty-three basis points a month. US stock value portfolios are explained, in part, by value in currencies and commodities.

MIGUEL: And the formal model?

MEI: Three factors: a global market index, the MSCI World, plus a "value everywhere" factor and a "momentum everywhere" factor, each an equal-volatility average across all eight markets. On the forty-eight test portfolios, the cross-sectional R-squared is 0.71 and the average absolute alpha is eighteen basis points a month.

MIGUEL: How does that compare with the usual suspects?

MEI: The global CAPM does badly. The Fama-French model with the US momentum factor, and a six-factor version with bond factors, do a little better than the CAPM but produce about twice the pricing errors of the global three-factor model. Local US factors don't price the world.

MIGUEL: And the other direction? Can global factors price US stocks?

MEI: Nearly as well as US factors can. On the Fama-French twenty-five size-value and twenty-five size-momentum portfolios, the global model gets an R-squared of 0.64 and the same eighteen basis points of error. It has no size factor, so it struggles with the smallest stocks, but drop the two smallest size quintiles and it does as well as the Fama-French model itself.

MIGUEL: Factors built from currencies and commodities pricing American small caps. That's wild.

MEI: They also take it to thirteen hedge fund indices, from the Dow Jones Credit Suisse family, and explain a good part of their returns. Which tells you something about what many hedge funds are doing: value and momentum, across asset classes, with leverage.

MIGUEL: So a lot of expensive alpha is cheap beta to these two factors.

MEI: That's the uncomfortable reading, yes. The formal test of zero pricing errors is still rejected, as it is for almost every model, but the fit is far better than the alternatives.

## Time, costs and caveats

MIGUEL: Has all this been arbitraged away?

MEI: Partly, and in an interesting way. Compare 1972 to 1991 with 1992 to 2011. The Sharpe ratios of value and momentum fell a little, from 0.78 and 0.90 to 0.68 and 0.71. The correlations across markets rose a lot: among value strategies from 0.31 to 0.71, among momentum strategies from 0.46 to 0.77. But the correlation between value and momentum got more negative, from minus 0.44 to minus 0.63. So the combination's Sharpe ratio barely moved: 1.40 to 1.43.

MIGUEL: Everyone's doing the same trades, so they move together more. But the mix still works.

MEI: And the rise in correlations lines up with 1998 rather than a smooth trend, consistent with arbitrageurs crowding in.

MIGUEL: What about trading costs? These are gross returns.

MEI: Gross, and the authors say so. They argue the universe is large and liquid, half the markets trade through futures, and live trading data from a companion paper suggests costs far below what calibrated models assumed. They also show the results hold with decile sorts, with different weightings, and that long-only versions still work. And there's a disclosure in the first footnote: AQR, where the authors work or consult, invests in value and momentum strategies.

MIGUEL: And what would you push back on?

MEI: The value measures outside stocks are proxies, chosen for uniformity, and the bond results are weak with the simple measure. The liquidity story explains only a fraction of the premiums and nothing of the combination. The theory question is left open: the paper challenges both behavioral and rational models and offers no model of its own. And "everywhere" is still the developed world after 1972.

## Legacy

MIGUEL: Why does this paper matter so much?

MEI: Three reasons. It moved anomalies research out of US stocks and made cross-asset evidence the standard: time-series momentum, betting against beta, carry, all followed the same template. It made the negative correlation between value and momentum, and the case for holding both, common knowledge. And it supplied a global benchmark model when finance was becoming global. When John Cochrane surveyed macro-finance in 2017, he pointed to this paper when asking why value and momentum are so pervasive and so correlated with each other, a question he left to future theory.

MIGUEL: So it's one of the few factors that survived the zoo.

MEI: Two of them, and they come as a pair.

## Wrap-up: the recap

MIGUEL: Okay, recap time. The whole paper in one minute.

MEI: The question: do value and momentum, the two most studied anomalies in US stocks, exist in other markets, how do they relate to each other, and what drives them?

MIGUEL: The method?

MEI: Simple, uniform value and momentum signals in eight markets, stocks in four regions, country indices, currencies, government bonds and commodities, from the 1970s to 2011, restricted to large liquid assets. Forty-eight sorted portfolios and long-short factors, correlations, principal components, regressions on macro and liquidity shocks, and a global three-factor model.

MIGUEL: Main takeaways?

MEI: One: value and momentum premiums exist in every market studied. Two: value strategies move together across markets, momentum strategies move together, and value and momentum move against each other, so the half-and-half combination across all markets has a Sharpe ratio of 1.45. Three: funding liquidity risk explains part of the structure, hurting value and helping momentum, especially after 1998, but not the premiums themselves. Four: a three-factor model with a global market, value everywhere and momentum everywhere prices the global portfolios and does nearly as well as US factors on US stocks.

MIGUEL: And the conclusion?

MEI: Theories built for US stocks can't be the whole story, because the same correlated effects appear in assets with no firms and no analysts. And any future theory must explain not value or momentum alone, but their combination, which is where the real puzzle lives.

MIGUEL: My takeaway: cheap and rising are two different bets, they lose on different days, and together they beat everything. Also, test your anomaly on pork bellies before you write the theory.

MEI: Read the paper. Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you next time.
