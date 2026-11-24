# The Finance Papers Podcast: Bonds Have Betas Too. Kelly, Palhares and Pruitt (2023) on Modeling Corporate Bond Returns

> **Open-source educational project.** The Finance Papers Podcast is a free, open-source initiative whose only
> goal is education: to create and spread knowledge about research in finance. This episode is an independent,
> unofficial explanation of the paper below, written in our own words for teaching purposes. It is not affiliated
> with or endorsed by the authors or the publisher. The paper is not reproduced here: read the original at the
> DOI link. Short quotes are attributed to the authors. Scripts and audio are released under CC BY 4.0; the paper
> remains the property of its authors and publisher.

- **Paper:** Kelly, B., Palhares, D., & Pruitt, S. (2023). Modeling corporate bond returns. *The Journal of Finance*, 78(4), 1967-2008.
- **Read the paper:** https://doi.org/10.1111/jofi.13233
- **Topics:** Corporate bonds and credit; factor models; asset pricing; market integration
- **Length:** 26 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance Papers Podcast, where we discuss the papers that shaped finance, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Quick note before we start. This is an open-source, educational project. We explain published research in our own words, for learning only. We are not affiliated with the authors or the journal, and the best thing you can do after listening is read the original paper. The link is in the episode notes.

MEI: Today we leave the stock market for a change. Bryan Kelly, Diogo Palhares and Seth Pruitt, "Modeling Corporate Bond Returns," Journal of Finance, 2023. Forty-two pages, with tables.

MIGUEL: Forty-two pages about bonds. I can already feel the excitement in the room.

MEI: Give it a chance, because the opening numbers are a slap in the face. In 2019, the world's bond markets were worth about 106 trillion dollars. Global stock markets, 95 trillion. In the United States, companies issued 1.4 trillion dollars of bonds that year, against 228 billion dollars of new stock.

MIGUEL: Wait. So companies raise six times more money with bonds than with stocks?

MEI: In 2019, yes. And yet, as the authors put it, our academic understanding of risk and return is "less developed in corporate bond markets than in equity markets." We have fifty years of factor models for stocks and a handful of young ones for bonds.

MIGUEL: So the paper is: let's finally give bonds a proper factor model.

MEI: With a twist in the method, and three findings. One, their model beats the existing bond models by a mile. Two, it implies that the reward for bearing credit risk is much bigger than we thought. Three, bond and stock markets are more connected than the literature believed.

MIGUEL: And who are the three authors?

MEI: Bryan Kelly is a professor of finance at Yale and, at the same time, head of machine learning at AQR, the quantitative investment firm. He did his PhD at NYU, where his committee was chaired by Robert Engle, and spent eight years at Chicago Booth before Yale. Seth Pruitt is at Arizona State. He did his PhD at UC San Diego with James Hamilton, then spent six years as an economist at the Federal Reserve Board. Diogo Palhares did his PhD at Chicago, worked at AQR, and was at Citadel when the paper came out.

MIGUEL: Two academics and two hedge funds. That explains the trading costs section.

MEI: Kelly and Pruitt have been co-authors since 2013. Their first joint paper won the very first AQR Insight Award, and the paper that introduced the method we'll discuss today won the Fama-DFA prize for the best paper in the Journal of Financial Economics. And one detail students will love: Pruitt maintains a free Python package for the method, and a replication archive for this very paper.

MIGUEL: So I can actually run this at home.

MEI: If you can get the data, yes. More on that later. Two more facts from the paper's first page. The editor was Stefan Nagel, who ran the Journal of Finance from 2016 to 2022. And the timeline: submitted in December 2020, accepted in October 2021. Ten months. For a top journal, that's fast.

## The problem

MIGUEL: Okay, start from zero. What is a factor model, and what's wrong with the bond ones?

MEI: A factor model says every asset's return is a bundle of exposures to a few common forces, the factors, plus noise that belongs to that asset alone. The exposure is the beta. If you know the betas, you know the asset's risk, and you can ask whether its average return is fair compensation for that risk.

MIGUEL: Like the market beta in the CAPM, but with several factors.

MEI: Exactly. In stocks, the standard recipe comes from Fama and French. You pick a characteristic you believe matters, like size or value, build a long-short portfolio sorted on it, and call that portfolio a factor. Then you regress each asset on the factors to get betas.

MIGUEL: And bond people copied that recipe?

MEI: Largely. The main bond model, by Bai, Bali and Wen in 2019, has four factors built this way: downside risk, credit risk, liquidity risk, and a bond market factor. Kelly, Palhares and Pruitt see two problems with the recipe.

MIGUEL: Problem one?

MEI: You prespecify the factors and treat them as if they were the true risk factors, observed without error. But they're portfolios someone chose by hand. Any measurement or specification error leaks into your conclusions. And when each researcher proposes their own favorite factors, you end up with what John Cochrane, in his 2011 presidential address, called "a zoo of new factors."

MIGUEL: A zoo. Hundreds of animals, no idea which ones matter.

MEI: Problem two: betas. The standard approach estimates them with rolling time-series regressions, say the last 36 months of returns. That gives you a static, stale and noisy number. But a bond's risk changes fast. A bond issued by a healthy firm in January can be a distressed bond by June.

MIGUEL: And a 36-month regression is still averaging over the healthy days.

MEI: That's the problem in one sentence.

## The method: IPCA

MIGUEL: So what's the twist?

MEI: A method called instrumented principal components analysis, or IPCA. Kelly and Pruitt had developed it a few years earlier, with Yinan Su, for stocks. This paper brings it to bonds. It has two moves. First, the factors are not chosen by hand. They are latent: the model estimates whatever factors best explain how bonds move together.

MIGUEL: Latent, meaning hidden. We don't see them, we infer them from the data.

MEI: Right. That's the principal components part: find the few common directions in a big panel of returns. Move two is the instrumented part, and it's the heart of the paper. Each bond's beta is not a fixed number. It's a linear function of the bond's observable characteristics at that moment: its credit spread, its duration, its rating, its volatility, the issuer's leverage, and so on.

MIGUEL: Hold on. So the beta changes every month because the characteristics change every month?

MEI: Exactly. The characteristics are the instruments. When a bond's spread blows out, the model knows immediately that its risk exposure went up. No need to wait three years of data.

MIGUEL: And how do characteristics turn into betas?

MEI: Through one matrix the authors call Gamma. Think of it as a translation table. Thirty characteristics go in, five factor exposures come out. Every bond uses the same table. That's the whole trick: instead of estimating a separate beta for each of 14,600 bonds, you estimate one small table that applies to all of them.

MIGUEL: How small?

MEI: Thirty characteristics times five factors: 150 numbers. Add the monthly factor realizations and the whole model has about 1,470 parameters. A traditional five-factor model with a separate beta per bond needs around 70,000. That's 98 percent fewer parameters.

MIGUEL: Fewer parameters, less overfitting.

MEI: And that will matter enormously out of sample. One more piece of intuition. IPCA is roughly the same as running ordinary principal components on a set of characteristic-managed portfolios: for each characteristic, a portfolio that holds each bond in proportion to that characteristic. Thirty portfolios instead of 14,600 bonds. Much of the idiosyncratic noise averages out.

MIGUEL: And where does the risk premium come in?

MEI: The model has an economic restriction built in. If a characteristic predicts returns, it must be because it predicts betas. No alpha. They test that restriction too, with a bootstrap. With five factors, they can't reject it at the one percent level, so characteristics earn returns through risk, not mispricing.

## The data

MIGUEL: Where does the bond data come from? I've heard bond data is a nightmare.

MEI: It is. Most academic papers use TRACE, the trade reporting system, through the WRDS platform. This paper uses data from the Intercontinental Exchange, ICE, which the authors call "the gold standard" used by banks and hedge funds. It starts earlier, in December 1999, and it runs through December 2020, so it includes the COVID crash.

MIGUEL: Why is ICE better?

MEI: Two reasons. You get a return every month, not only when a bond happens to trade near both ends of the month. And ICE computes the hard analytics for you: duration, option-adjusted spreads, and hedge returns that strip out the pure interest rate component.

MIGUEL: Why strip out interest rates?

MEI: Because they want credit returns. A corporate bond moves for two reasons: Treasury yields move, or the market's view of the company's credit moves. They hedge the first with a portfolio of Treasuries and keep the second. That's what the model prices.

MIGUEL: Fair. How big is the sample?

MEI: The bonds in the Bank of America investment-grade and high-yield indices. After cleaning: 14,600 bonds, 264 months, about 556,000 bond-months. Each bond comes with 29 characteristics, plus a constant, so 30 instruments. They're all ranked each month and squeezed between minus one half and plus one half, so a coefficient on spread is comparable to a coefficient on rating.

MIGUEL: And the characteristics are the usual suspects?

MEI: Bond ones: spread, duration, rating, age, coupon, face value, bond momentum, bond volatility, value-at-risk, VIX beta. Firm ones: leverage, profitability, book-to-price, distance to default, equity momentum. Twenty-nine in total, each borrowed from an earlier paper.

MIGUEL: One thing I don't get. A junk bond and a AAA bond have completely different volatility. Doesn't the junk bond dominate the estimation?

MEI: Great catch, and they handle it. They divide each return by the bond's duration times its spread, a standard forward-looking proxy for bond volatility. Low-risk bonds, about forty percent of them, are left essentially unchanged. Very risky bonds are scaled down so they don't hijack the least-squares fit. And they check that the results hold without this scaling.

## A first look: do characteristics matter?

MIGUEL: Before the big model, any warm-up evidence?

MEI: Two tables. First, the characteristic-managed portfolios themselves. Several earn serious Sharpe ratios. Equity momentum, 1.76. Value-at-risk, 1.25. Spread, 0.81.

MIGUEL: Quick reminder: Sharpe ratio is average excess return divided by volatility. Above one is already very good.

MEI: Yes. And one sign surprised me. Duration has a Sharpe ratio of minus 0.97.

MIGUEL: Negative? So long-duration bonds pay less than short ones, per unit of risk?

MEI: Buying short-duration and selling long-duration bonds was profitable. That's the low-risk anomaly, the same pattern Frazzini and Pedersen found: boring, low-risk assets do too well. Book-to-price, the value measure, also comes out negative, which the authors attribute to their sample: more than half of it is after 2010, a terrible decade for value everywhere.

MIGUEL: And the second table?

MEI: They ask whether today's characteristics predict a bond's beta on the bond market over the next twelve months. They do, with an R-squared of 17 percent. Given how noisy a beta estimated from twelve monthly returns is, that's a lot.

MIGUEL: So characteristics predict both returns and risk. The question is whether it's the same story.

MEI: And that's exactly what IPCA tests.

## The results

MIGUEL: Numbers. Give me the headline.

MEI: Out of sample, the five-factor IPCA model explains 50.7 percent of the variation in monthly returns of individual bonds. And 98.5 percent of the variation in the characteristic-managed portfolios.

MIGUEL: Define out of sample, because people throw it around.

MEI: Every estimate at a given month uses only data up to that month. Then the model is tested on the next month. So there's no peeking. The remarkable thing is that the out-of-sample numbers are almost identical to the in-sample ones. That's the small parameter count paying off.

MIGUEL: And the pricing errors?

MEI: They use a measure called relative pricing error: the squared alphas divided by the squared average returns. Zero means the model explains all differences in average returns. A hundred percent means it explains none. For the managed portfolios, IPCA gets 1.8 percent out of sample.

MIGUEL: One point eight. Basically nothing left to explain.

MEI: For individual bonds it's higher, 63 percent, because individual bonds are incredibly noisy. Now the comparison, on a common sample from 2004 to 2019. The competitors are a bond market model, the Bai, Bali and Wen four-factor model, and the Fama-French five-factor equity model.

MIGUEL: Let me guess. IPCA wins.

MEI: It's not a win, it's a knockout. Out-of-sample total R-squared on individual bonds: IPCA, 45 percent. The market model, 32. Fama-French, minus 3.5. Bai, Bali and Wen, minus 17.

MIGUEL: Negative R-squared? How is that even possible?

MEI: It means the model does worse than predicting zero for every bond. The betas estimated from the past 36 months don't match next month's betas, so the predictions add noise instead of removing it. That's the stale-beta problem, measured.

MIGUEL: And pricing errors?

MEI: On individual bonds, IPCA has 39 percent, the market model 68, Fama-French 76, and Bai, Bali and Wen 100, so the model explains nothing of the average returns out of sample. On managed portfolios: IPCA 2.9 percent, market model 26, Fama-French 38, Bai, Bali and Wen 106.

MIGUEL: But Bai, Bali and Wen published good results. How do the authors reconcile that?

MEI: Two reasons. In sample, their model does look fine, with a total R-squared around 27 percent on individual bonds, close to the original paper. The collapse happens out of sample. And second, a subtle point about testing. If your factors are traded portfolios, the cross-sectional slope on beta should be the factor's own return. If you re-estimate that slope freely, your mimicking portfolio can drift away from the factor, and the fit looks inflated. When Kelly, Palhares and Pruitt impose the restriction, the competing models' cross-sectional R-squareds turn negative.

MIGUEL: So part of the earlier success was a generous test.

MEI: That's their reading. And the gap between the two versions of the test is itself a sign of misspecification.

## The investment punchline

MIGUEL: Now the part my friends in trading care about. Can you make money with this?

MEI: The model implies two strategies. The spread strategy: each month, rank bonds by the model's expected return, buy the top fifth, short the bottom fifth. And the tangency portfolio: the best combination of the five factors, which in theory is the maximum Sharpe ratio portfolio of the whole bond market.

MIGUEL: And the Sharpe ratios?

MEI: Out of sample, before costs: 3.5 for the spread strategy and 6.2 for the tangency portfolio.

MIGUEL: Six point two?! The whole bond market earns, what?

MEI: An equal-weighted portfolio of all their bonds earns 0.26. A strategy from an earlier paper by Palhares himself, with Israel and Richardson, combining defensive, momentum, carry and value signals, earns 2.2. And the same IPCA method applied to US stocks earns 3.9.

MIGUEL: Okay, but bonds are expensive to trade. Please tell me they include costs.

MEI: They do. They assume 19 basis points one way, a conservative estimate from the literature, and they measure turnover: about 70 percent of the portfolio changes every month. Net of costs, the Sharpe ratios fall to 1.4 for the spread strategy and 2.5 for the tangency portfolio.

MIGUEL: Still enormous.

MEI: And the model was never told about costs. So they try slowing it down: each month, move only part of the way toward the new weights. With the right amount of smoothing, turnover drops by a quarter and the net Sharpe ratio rises to 2.9 for the tangency portfolio.

MIGUEL: So this is why they say the credit risk premium is bigger than we thought?

MEI: Yes. Remember the model forces zero alpha. So these returns are, by construction, compensation for exposure to systematic risk. If the efficient portfolio of credit risk earns a Sharpe ratio of two and a half after costs, the price of bearing credit risk is a lot higher than the 0.26 of the bond index suggests.

## What are the factors, really?

MIGUEL: Latent factors sound like black boxes. Do we know what they are?

MEI: You read the translation table, Gamma. Which characteristics move betas the most? Four stand out: the credit spread, duration, bond volatility, and the constant, which is just the market. Then spread divided by distance to default, which works like a value measure for bonds, and equity momentum. Fifteen of the thirty characteristics are statistically significant.

MIGUEL: And factor by factor?

MEI: The first factor is essentially a spread factor, with 12.7 percent volatility and a Sharpe ratio of 1.6. The second is a duration factor, Sharpe ratio 2.5. The third is driven by bond volatility. The fourth and fifth mix in equity momentum and the value measure.

MIGUEL: So could you skip the fancy method and just build five portfolios on those characteristics?

MEI: They try exactly that, and it's a nice lesson. With old-fashioned rolling betas, the five observable factors beat the earlier bond models but fall well short of IPCA. With instrumented betas, where betas depend on characteristics, the observable model gets close: a spread strategy Sharpe ratio of about 3 versus 3.5.

MIGUEL: So the magic is less in the latent factors and more in the moving betas.

MEI: Both matter, but yes, the dynamic betas do a lot of the work.

## Are bonds and stocks one market?

MIGUEL: Last big part. Bonds and stocks. Why would they be disconnected at all?

MEI: In theory they can't be. A bond and a stock are two claims on the same firm. Merton's model gives an exact hedge ratio: how much a bond should move when the stock moves. Schaefer and Strebulaev tested it in 2008. The slope was right, close to one. But the R-squared was low.

MIGUEL: So the direction is right, but stocks explain little of bond returns.

MEI: About 9 percent in this paper's matching sample. The question is where the disconnect lives. Two camps. One says it's about market segmentation: different investors in each market, so even the common risk factors are disconnected. The other says it's limits to arbitrage and frictions: slow information, illiquidity, corporate events that transfer wealth between bondholders and shareholders. That camp predicts the breakdown shows up in the idiosyncratic part of returns.

MIGUEL: And IPCA can split returns into systematic and idiosyncratic pieces, for both markets.

MEI: Exactly. They regress the systematic part of bond returns on the systematic part of equity returns, hedged with Merton. The R-squared doubles to 18 percent, and the sensitivity is about 2.3. Then they regress idiosyncratic bond returns on idiosyncratic equity returns: R-squared 4 percent. And idiosyncratic bond returns don't respond to systematic equity returns at all.

MIGUEL: So the common risks are shared, and the firm-specific noise is not.

MEI: Which favors the limits-to-arbitrage story. Then the second test: can equity factors price bonds? The five equity IPCA factors explain only about 11 percent of realized bond return variation. But when it comes to expected returns, they do nearly as well as the bond factors. The pricing errors on individual bonds are 45 percent with equity factors, versus 46 with bond factors.

MIGUEL: Wait. Equity factors are bad at explaining bond ups and downs but good at explaining bond risk premia?

MEI: That's the finding. And the clearest number: the expected bond returns from the equity model and from the bond model have a correlation of 83 percent. Choi and Kim had written in 2018 that they found it "difficult to reconcile the magnitudes of bond return premia with those of equity return premia." This paper reaches, in their words, "a more positive view regarding market integration."

## Limits and caveats

MIGUEL: Time for the skeptic's corner. What should I worry about?

MEI: A few things, most of which the authors flag themselves. First, the data. ICE data is proprietary, and the authors got it through their connection to AQR, the investment firm. They disclose it, and note anyone can buy it. They also mention a companion paper redoing the analysis with public TRACE data, with the same conclusions.

MIGUEL: Still, hard to replicate on a student budget.

MEI: True. Second, costs. A Sharpe ratio of 2.5 net assumes 19 basis points per trade. In a crisis, bond trading costs explode. Third, the model has no bond-specific fixed effects, by choice, because with thousands of bonds it overfits. Fourth, scaling returns by duration times spread helps the fit, and the unscaled results, while still strong, are weaker.

MIGUEL: And the competitor that collapsed out of sample, Bai, Bali and Wen. Any news there?

MEI: Big news, after this paper was published. In late 2023, the Journal of Financial Economics retracted the Bai, Bali and Wen paper. Another team, Dickerson, Mueller and Robotti, had found that some of its factor data were misaligned in time, and the journal's notice says the original results rested on that error. Kelly, Palhares and Pruitt used the factor data Bai, Bali and Wen had posted, so the collapse out of sample in this paper may partly reflect that problem.

MIGUEL: So the benchmark they beat was already wounded.

MEI: Which makes the comparison with the market model and Fama-French the more meaningful one. And IPCA beats those too.

MIGUEL: And the sample?

MEI: Twenty-one years, with 2020 in it. They show that excluding 2020 reduces pricing errors for every model. And the sample choice explains some surprising signs, like negative value returns.

MIGUEL: One more. If a model earns a Sharpe ratio of six, shouldn't the market have arbitraged it away?

MEI: The authors would say it's risk compensation, not free money, and that costs and the illiquidity of bonds keep it from being competed away. Whether a Sharpe ratio of six is risk compensation or a sign that something about the exercise is too easy is a fair question to keep in mind.

## Wrap-up: the recap

MIGUEL: Okay, quick recap before we go. Give me the whole paper in one minute.

MEI: Deal. The question: can we build a factor model that describes the risks and returns of corporate bonds as well as we do for stocks, and what does it say about credit risk and the link between bonds and stocks?

MIGUEL: And the method?

MEI: Instrumented principal components analysis. Five latent factors, and betas that are linear functions of 30 bond and firm characteristics through one shared matrix. Estimated on ICE data from 1999 to 2020, 14,600 bonds, with credit returns hedged for interest rates. Everything evaluated out of sample and compared with the market model, Bai, Bali and Wen, and Fama-French.

MIGUEL: Main takeaways?

MEI: One: the model explains about half of individual bond return variation out of sample, with pricing errors near 2 percent on portfolios, while the earlier bond models have negative out-of-sample R-squareds. Two: the implied strategies earn out-of-sample Sharpe ratios of 3.5 and 6.2 before costs, about 1.4 and 2.5 after, so the credit risk premium is far larger than the bond index suggests. Three: the systematic parts of bond and stock returns are about twice as integrated as total returns, and equity factors recover bond risk premia with a correlation above 80 percent.

MIGUEL: And the conclusion?

MEI: Characteristics predict bond returns because they predict bond betas. Dynamic, instrumented betas, more than hand-picked factors, are what was missing. The main caveats are proprietary data and the assumption that trading costs stay at 19 basis points.

MIGUEL: And my takeaway: next time someone says bonds are boring, tell them the bond market is bigger than the stock market, and apparently had a Sharpe ratio of six hiding in it.

MEI: Thanks for listening to The Finance Papers Podcast.

MIGUEL: See you next time. And remember: your beta is not a constant. Neither is mine.
