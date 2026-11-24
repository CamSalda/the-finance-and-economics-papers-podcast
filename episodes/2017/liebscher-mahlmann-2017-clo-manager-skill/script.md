# The Finance and Economics Papers Podcast: Where Skill Shows Up. Liebscher and Mählmann (2017) on Professional Investment Managers and Syndicated Loan Portfolios

> **Open-source educational project.** The Finance and Economics Papers Podcast is a free, open-source initiative
> whose only goal is education: to create and spread knowledge about research in finance and economics. This
> episode is an independent, unofficial explanation of the paper below, written in our own words for teaching
> purposes. It is not affiliated with or endorsed by the authors or the publisher. The paper is not reproduced
> here: read the original at the DOI link. Short quotes are attributed to the authors. Scripts and audio are
> released under CC BY 4.0; the paper remains the property of its authors and publisher.

- **Paper:** Liebscher, R., & Mählmann, T. (2017). Are professional investment managers skilled? Evidence from syndicated loan portfolios. *Management Science*, 63(6), 1892-1918.
- **Read the paper:** https://doi.org/10.1287/mnsc.2015.2412
- **Topics:** Asset management; manager skill; performance persistence; collateralized loan obligations; syndicated loans; market efficiency
- **Length:** 20 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Quick note before we start. This is an open-source, educational project. We explain published research in our own words, for learning only. We are not affiliated with the authors or the journal, and the best thing you can do after listening is read the original paper. The link is in the episode notes.

MEI: Today, a paper that goes looking for investment skill in the one place the textbooks say it should be easiest to find. Roberto Liebscher and Thomas Mählmann, "Are Professional Investment Managers Skilled? Evidence from Syndicated Loan Portfolios," Management Science, 2017. Twenty-seven pages.

MIGUEL: Twenty-seven pages. What's the hook?

MEI: Here's the hook. Fifty years of research on mutual funds says managers barely beat the market, if at all. But that evidence comes from the stock market, where prices are efficient and the payoff to being smart is small. What if you looked where prices are not efficient?

MIGUEL: Like where?

MEI: The market for leveraged loans: the bank loans that finance buyouts, bought in bulk by vehicles called CLOs. The authors assemble data on more than a thousand of these vehicles and find that the best managers beat the worst by twenty-two percent a year at the moment you rank them, and still by five percent a year three years later. Without taking more risk.

MIGUEL: That is not what my asset management professor told me.

MEI: Which is why we're here. Thomas Mählmann holds the chair of finance and banking at the Catholic University of Eichstätt-Ingolstadt, in Bavaria. He did his doctorate and habilitation in Cologne, on credit rating systems and default risk, and most of his work is about securitization: hedge funds and CDOs, arbitrage CDOs, leveraged loan funds. Roberto Liebscher was his doctoral student, and this paper is the first essay of Liebscher's dissertation, "Three Essays on Financial Intermediation," defended in 2017 with Mählmann as first examiner.

MIGUEL: A professor and his PhD student reading twenty-seven thousand trustee reports. I feel seen.

MEI: Two details from the first page. The paper was received in June 2014 and accepted in November 2015, after two rounds of revision, and it thanks the finance department editor, Wei Jiang. Let's start with the theory that motivates the whole thing.

## The problem

MEI: In 1980, Grossman and Stiglitz made a simple point. Gathering information costs money, so people only do it if they're paid for it in higher returns. In a market where prices already reflect everything, the payoff to being informed is tiny, so skilled and unskilled investors end up with nearly the same returns and you can't tell them apart.

MIGUEL: So the mutual fund result, "no skill," could just mean "no visible skill in stocks."

MEI: That's the authors' reading. And the flip side is a prediction: in markets with less informative prices, returns to skill should be larger and easier to see. There was already a hint of that in venture capital and private equity, where performance persists across funds of the same firm. And a 2014 paper had shown that the most skilled bond fund managers get assigned to high-yield bonds, where skill pays more.

MIGUEL: And the authors pick leveraged loans. Why are those inefficient?

MEI: Two reasons. The syndicated loan market runs on information asymmetry: between the bank that arranges a loan and the banks that join it, and between banks and the institutional investors who buy loans later. Because of that, it's essentially a rated market. Institutional investors want a rating from an agency before they buy. And ratings are ordinal, often stale, and slow to move.

MIGUEL: So if everyone is pricing off ratings, someone who actually reads the credit can beat them.

MEI: And the paper opens with a picture of that. Take loan portfolios with almost no defaults at the start of 2008, and plot their average spread against the share of loans in default eighteen months later. If spreads priced risk correctly, the two would line up. Instead there's a cloud: the R-squared is 0.14. Same spread, wildly different default outcomes.

MIGUEL: Which means either spreads are wrong, or some managers know which loans to pick at a given spread.

MEI: Or both. Understanding that cloud is the goal of the paper.

## What a CLO is

MIGUEL: Okay, I need the basics. What's a CLO?

MEI: A collateralized loan obligation. Think of it as a small bank in a box. A special purpose vehicle issues bonds in slices, called tranches, and uses the money to buy a portfolio of syndicated loans, typically to companies rated single B, originated to finance leveraged buyouts. The loan payments flow down a waterfall: the senior tranche is paid first, then the next, and so on. Whatever is left goes to the bottom slice, the equity tranche.

MIGUEL: So the equity tranche is the shock absorber.

MEI: It eats the first losses and keeps the leftovers. In the paper's illustrative deal, the top tranche is seventy percent of the structure, rated triple A, paying Libor plus 23 basis points, and the equity is eight percent, with no rating and no coupon, just the residual.

MIGUEL: And who runs it?

MEI: An asset manager, a firm. In the common type, called an arbitrage CLO, the manager actively trades the portfolio during a reinvestment period, six years on average before 2008 and four after, reinvesting repayments and selling a limited share of the loans each year at its discretion. The manager is paid three fees: a senior fee of fifteen to twenty basis points of assets, paid before anyone else; a subordinated fee of thirty to thirty-five basis points, paid only after all debt tranches got their coupons; and an incentive fee, usually twenty percent of what's left once the equity has earned a hurdle return, typically twelve percent.

MIGUEL: Twenty over twelve. That sounds like a hedge fund.

MEI: It's a structured hedge fund with a rulebook. Covenants force the manager to keep the portfolio's average rating above a floor and its diversification above a floor, and coverage tests divert cash from equity to debt if the collateral gets thin. Those rules matter later, because they limit how much a manager can juice equity returns by taking risk.

MIGUEL: And how big is this market?

MEI: Big and recovering fast when the paper was written. CLOs accounted for about fifty-five percent of the notional in the US primary leveraged loan market. US issuance was eighty-two billion dollars in 2013 and a hundred and twenty-four billion in 2014, a record.

## The data

MIGUEL: Where does the data come from? There's no ticker for a CLO.

MEI: This is a data collection paper as much as anything. The core is Creditflux's CLO-i database, which copies equity payments from trustee reports. The authors add Bloomberg, screen all the trustee and investor reports by hand for missing payments, and end up with 16,624 equity payments to 836 CLOs between May 1998 and December 2012. Adding deals from Moody's and S&P lists brings the sample to 1,042 CLOs.

MIGUEL: That's most of the market?

MEI: About seventy-two percent of global issuance volume. Then they download 27,590 monthly trustee reports and read them with text-mining code to extract the portfolio's risk measures, and hand-collect default rates. Deal structures and tranche coupons come from a Barclays platform, for 938 deals. And they find the prospectus for 624 deals and type in the fee structures by hand.

MIGUEL: Someone spent a long time in PDFs.

MEI: The authors say they believe it's the most comprehensive CLO data studied to date, and I see no reason to doubt it.

## Measuring performance

MIGUEL: How do you measure a manager's performance when the tranches don't trade?

MEI: Three ways. The main one is what the industry uses: the cash-on-cash return. Add up the cash paid to the equity tranche over a half year, divide by the face value of the equity, and annualize. The average deal pays about fifteen percent a year, so equity investors get their money back in roughly six and a half years.

MIGUEL: But a deal from 2007 and a deal from 2010 faced totally different markets.

MEI: So every return is adjusted by subtracting the return of the median deal from the same vintage year. That strips out market conditions, funding costs of the era, and typical deal structures, and leaves relative performance against peers who competed for the same loans at the same time.

MIGUEL: And the other two measures?

MEI: The internal rate of return of the equity tranche, for the deals with complete payment histories. And the clever one, which they call Alpha. From the trustee reports they run a regression, deal by deal, of the portfolio's average loan spread on the portfolio's expected loss, computed from ratings and recovery rates. The deal's fixed effect is Alpha: the spread the manager earns over and above what the risk of the portfolio would justify.

MIGUEL: So Alpha is: how much extra yield you collect per unit of risk you hold.

MEI: And it has two nice properties. It's before fees, and it only uses the asset side, so it doesn't depend on how much leverage the deal has or how cheap its funding was. Things the underwriter decides, not the manager.

## Persistence

MIGUEL: Okay. The main result.

MEI: Every half year, rank managers into quartiles by their adjusted cash-on-cash return. Then follow the quartiles for three years before and after. At the ranking date, the top quartile beats the bottom quartile by twenty-two percent a year, annualized. One year later, the gap is still about ten percent. Three years later, five point four percent a year.

MIGUEL: Some of that is mechanical, no? If I rank you on your return this half year, part of that persists because you're holding the same loans.

MEI: The authors worry about exactly that, so they do a second test across deals. Rank managers by the performance of their first CLO, then look at their second, third and fourth CLOs, different portfolios, different vintages. The first deal predicts the rest: managers who outperformed with their first deal beat the bottom quartile with their follow-on deals by three and a half to thirteen and a half percent a year.

MIGUEL: And this holds before fees?

MEI: It holds for the IRR and for Alpha too. On Alpha, top-quartile managers earn up to a hundred and twenty basis points more risk-adjusted spread on their loans than bottom-quartile managers. With the typical leverage of ten, that's most of the difference in equity returns right there.

MIGUEL: What about survivorship? Bad managers disappear.

MEI: They do, and faster than good ones: the bottom quartile shrinks quicker from deal to deal. That works against finding persistence, because the worst are dropping out of the comparison. The gaps survive anyway.

## Is it just risk?

MIGUEL: Here's my obvious objection. The equity tranche is a leveraged bet. Maybe the "skilled" managers just hold riskier loans.

MEI: That's the objection the paper spends the most effort on. They build a single summary of equity risk, the equity tranche expected loss, from five ingredients in the trustee reports: the portfolio's default probability, implied by its average rating; the recovery rate; the diversification, from Moody's diversity score; how much collateral cushion sits under the equity; and the leverage. It's the fraction of the equity you'd expect to lose over the next year if the deal were wound up.

MIGUEL: And the average?

MEI: Seventy-five percent. Equity tranches are often under water, with less collateral than debt outstanding, so expected losses are enormous. That's the nature of the slice.

MIGUEL: Fine. So do the top managers carry more of that risk?

MEI: Less. Top-quartile managers hold portfolios with a lower average rating factor, about two points less ten-year default probability. More diversified portfolios, by ten to twenty uncorrelated loans. A bigger collateral cushion under the equity. A lower expected loss around the ranking date. And lower realized default rates: three years after the ranking, their portfolios have one and a half percentage points fewer loans in default.

MIGUEL: So the better the equity returns, the safer the portfolio. That's backwards from a risk story.

MEI: And it's consistent with the covenants doing their job. A manager can't load up on junk without tripping the rating floor and diverting cash away from equity. The paper's phrase is that top managers "do good to equity tranche investors" and also "serve well debt note holders."

MIGUEL: Any natural experiment?

MEI: The 2009 default wave, when loan default rates went from two percent to over ten. Rank managers on pre-crisis performance and compare how their default rates moved through 2009 against the bottom quartile. The difference-in-differences estimate is 0.003 percent, with a standard error three hundred times larger. Nothing.

MIGUEL: Okay, I believe it's not risk. What else could it be?

MEI: Leverage and funding, which belong to the underwriter rather than the manager. So they run regressions of a deal's performance on the previous deal's performance, controlling for leverage, the cost of the debt tranches, deal size, and underwriter fixed effects. A one-standard-deviation better previous deal raises the next deal's return by 1.94 percentage points. Leverage helps too, 1.21 points per standard deviation, but less. And the deal before the previous one predicts as well.

MIGUEL: So the manager matters more than the structure.

MEI: In the authors' words, "the crucial part in the determination of returns seems to be played by the managers," above and beyond anything the underwriter does.

## Do skilled managers get paid?

MEI: Now the economics gets interesting. Berk and Green's model of mutual funds says that if skill exists, money should flow to the skilled until their advantage is competed away, either through bigger funds or higher fees. So the authors ask: do skilled CLO managers get more assets, and do they charge more?

MIGUEL: Start with assets.

MEI: Three findings. Skilled managers keep their deals longer: a ten percent better return lowers the chance of losing the mandate, through a call or a replacement, by seven and a half percent in the simplest model and far more with controls. They are more likely to be given a new deal: a ten percent better track record raises the probability by about five and a half percent, though that fades once you control for assets under management, which already embed past performance. And their new deals are bigger, by one to seven percent for a ten percent better record, worth an extra twenty-seven to a hundred and eighty-eight thousand dollars of fees a year.

MIGUEL: So capital chases performance. And fees?

MEI: Flat. The senior and subordinated fees don't respond to past performance at all. The market standard is a twenty basis point senior fee plus a thirty basis point subordinated fee, and almost nobody deviates. The incentive fee is a bit higher for skilled managers, but the result rests on a handful of deals that pay twenty-five percent instead of the usual twenty, so the authors don't lean on it.

MIGUEL: Why wouldn't a manager with a track record charge more?

MEI: They offer a few reasons. Managers may have little bargaining power, because they need an underwriter to build and sell the deal, unlike a mutual fund. Fee levels may be a convention nobody breaks. Or managers may prefer to invest in the equity tranche themselves and collect the upside that way, which the data can't see.

## The puzzle and the caveats

MIGUEL: So where does that leave the theory?

MEI: With a puzzle, which is how the paper ends. Skill exists, performance persists, and capital flows to skill, exactly as Berk and Green predict. But the persistence doesn't fade. Bigger assets don't erode the edge, and fees don't absorb it. Three candidate explanations: returns to information in loans may not diminish with scale, perhaps because trading loans has little price impact; fees may be sticky because insiders who see the trustee reports would read a fee increase badly, as in a model by Hochberg and co-authors from venture capital; or investors may simply be unable to put as much money with the skilled managers as they'd like, because deals can't be scaled up.

MIGUEL: And what would you push back on?

MEI: Reporting is voluntary, so there could be a bias if managers hide bad deals, though the authors argue investors have no reason to hide and discuss it in an appendix. The risk measures depend on rating agencies' inputs, which is why they also look at realized defaults. The sample is dominated by the pre-crisis boom and the crisis itself. And the manager's own equity stake, which could be the real channel for capturing skill, is unobserved.

MIGUEL: And the lesson for someone who studies mutual funds?

MEI: That "no evidence of skill" and "no skill" are different statements. In the authors' framing, skill is a return to information, and you'll only see it where information pays.

## Wrap-up: the recap

MIGUEL: Okay, recap time. The whole paper in one minute.

MEI: The question: are professional investment managers skilled, and does the answer depend on how efficient the market is? Following Grossman and Stiglitz, skill should be most visible where prices are least informative, so the authors look at leveraged loan portfolios run by CLO managers.

MIGUEL: The method?

MEI: Hand-built data on more than a thousand CLOs from 1998 to 2012, with equity cash returns, internal rates of return and a before-fee Alpha from trustee reports. Persistence tests across time and across deals, an extensive set of risk controls including a summary measure of equity expected loss, a difference-in-differences test around the 2009 default wave, and regressions of mandates, deal sizes and fees on past performance.

MIGUEL: Main takeaways?

MEI: One: performance persists. Top-quartile managers beat the bottom by twenty-two percent a year at the ranking date and by five percent three years later, and a manager's first deal predicts the next ones. Two: it's not risk. Top managers hold better-rated, more diversified portfolios with bigger cushions and fewer defaults. Three: skill pays through assets, not fees. Skilled managers keep mandates longer and get bigger new deals, but charge the same standard fees as everyone else.

MIGUEL: And the conclusion?

MEI: The syndicated loan market is not informationally efficient, some managers exploit that, and the CLO market doesn't fully arbitrage the skill away. Which is a result for the Grossman and Stiglitz view of markets, and a puzzle for the Berk and Green view of fund management.

MIGUEL: My takeaway: if you want to find skill, don't look where everyone is already looking. And read the trustee reports. Twenty-seven thousand of them.

MEI: Read the paper first. Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you next time.
