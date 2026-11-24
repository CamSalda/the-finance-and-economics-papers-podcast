# The Finance and Economics Papers Podcast: The Inequality Factor. Constantinides and Duffie (1996)

> **Open-source educational project.** The Finance and Economics Papers Podcast is a free, open-source initiative whose only
> goal is education: to create and spread knowledge about research in finance and economics. This episode is an independent,
> unofficial explanation of the paper below, written in our own words for teaching purposes. It is not affiliated
> with or endorsed by the authors or the publisher. The paper is not reproduced here: read the original at the
> DOI link. Short quotes are attributed to the authors. Scripts and audio are released under CC BY 4.0; the paper
> remains the property of its authors and publisher.

- **Paper:** Constantinides, G. M., and Duffie, D. (1996). Asset pricing with heterogeneous consumers. *Journal of Political Economy*, 104(2), 219-240.
- **Read the paper:** https://doi.org/10.1086/262023
- **Topics:** Asset pricing; equity premium puzzle; incomplete markets; heterogeneous agents
- **Length:** 29 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Quick note before we start. This is an open-source, educational project. We explain published research in our own words, for learning only. We are not affiliated with the authors or the journal, and the best thing you can do after listening is read the original paper. The link is in the episode notes.

MEI: Stay with me, because today's paper is worth it. George Constantinides and Darrell Duffie, "Asset Pricing with Heterogeneous Consumers," Journal of Political Economy, 1996. Twenty-two pages, with two appendices.

MIGUEL: I can feel my happiness leaving my body.

MEI: It's one of the most cited papers on why inequality matters for asset prices. Here's the starting point. In 1986, Gregory Mankiw suggested that recessions hit some people a lot instead of everyone a little. If people can't insure that risk, and marginal utility is convex, stocks look much riskier than aggregate data suggest. But Mankiw's model had two dates and one coin flip. A toy.

MIGUEL: And these two build the real thing?

MEI: A full dynamic economy, with many periods, many assets, and an equation you can actually take to the data.

MIGUEL: Who are these two?

MEI: George Constantinides is at the Chicago Booth School of Business. He was born in Cyprus and studied physics at Oxford before he turned to finance. Darrell Duffie has been at Stanford since finishing his PhD there in 1984. He wrote the textbook Dynamic Asset Pricing Theory, which this very paper cites.

MIGUEL: Citing your own textbook. Power move.

MEI: Both later served as president of the American Finance Association: Constantinides in 2001, Duffie in 2009. And the acknowledgments are fun. Lars Hansen "provided a correction and many helpful suggestions."

MIGUEL: Lars Hansen, the Nobel prize Lars Hansen? Corrected their math?

MEI: That one. He shared the 2013 Nobel with Eugene Fama and Robert Shiller. And Constantinides acknowledges funding from a gift by Dimensional Fund Advisors to the Chicago business school.

MIGUEL: So a fund company paid for research on why stocks pay so much. I'm sure that was completely neutral.

MEI: At least it's disclosed. And Constantinides later served as an independent director of Dimensional's funds for about four decades. Okay. On to the paper.

## Why the earlier fixes failed

MIGUEL: Okay, set the scene. What's wrong with the standard model?

MEI: The standard model is the representative-consumer model of Lucas, 1978. One imaginary consumer eats the whole economy's consumption, and asset prices must satisfy that consumer's Euler equation.

MIGUEL: Remind me what an Euler equation is.

MEI: It's the condition that says you're investing optimally. In words: if you give up one dollar of consumption today to buy an asset, the discounted, marginal-utility-weighted payoff tomorrow must be worth exactly one dollar today. If it were worth more, you'd buy more of the asset. If it were worth less, you'd sell.

MIGUEL: So it's the "no regrets" condition. You can't make yourself happier by moving a dollar between today and tomorrow.

MEI: Lovely way to say it. And the paper lists the problems with the representative version. Mehra and Prescott showed it predicts an equity premium that is too low and a risk-free interest rate that is too high, because aggregate consumption is so smooth.

MEI: The equity premium puzzle and the risk-free rate puzzle. And it gets worse. Formal tests by Hansen and Singleton and others rejected the Euler equations even when risk aversion was allowed to be anything at all.

MIGUEL: So even with a crazy risk aversion of a hundred, it still fails?

MEI: Still fails. So people tried to fix the preferences. The paper lists them: habit formation, where you get used to a standard of living and hate falling below it. One of those habit papers, from 1990, is by Constantinides himself, so this paper is his second attempt at curing the same disease. Recursive preferences, like Epstein and Zin, which separate risk aversion from the willingness to move consumption over time. Rare disasters, from Rietz in 1988. Transaction costs.

MIGUEL: And the option on today's menu: heterogeneous consumers with incomplete insurance.

MEI: Right. Now, why does heterogeneity even need insurance to be missing? Because with full consumption insurance, everyone equalizes their marginal rates of substitution state by state. And then, a classic result says, the economy prices assets exactly as if there were one representative consumer.

MIGUEL: So with perfect insurance, a crowd of different people behaves like one person.

MEI: Exactly. But the authors note that full insurance is suspect, because, quote, "certain types of insurance, such as unemployment insurance, are conspicuously nonexistent." Full unemployment insurance, I mean. And direct tests using household data, like Cochrane 1991 and Townsend's work on village India, reject full insurance.

MIGUEL: So, problem solved? Insurance is incomplete, heterogeneity matters, go home?

MEI: That's the twist of this paper's introduction. People had already tried this, and it didn't work. Telmer in 1993, Deborah Lucas in 1991, Heaton and Lucas. They built economies where people face uninsurable income risk and can only trade, say, one bond. And they found that people come close to full risk sharing anyway.

MIGUEL: How? If insurance doesn't exist?

MEI: Self-insurance. You build a buffer of savings. A bad year? Sell some bonds. A good year? Buy some back. If the income shocks are temporary, a buffer smooths them out really well.

MIGUEL: Like keeping an emergency fund for a broken laptop.

MEI: Exactly that. And when those authors added borrowing costs or transaction costs, people just kept a bigger inventory of bonds. The only way to make heterogeneity matter was to make the supply of bonds unrealistically small, so there wasn't enough buffer to go around.

MIGUEL: So the key problem is the shocks being temporary.

MEI: That's the diagnosis. In those models, each person's share of income is a stationary process with low persistence. Today's bad luck fades, and in the long run everyone's income share looks the same. The economic term is mean reversion.

MIGUEL: And Constantinides and Duffie say: what if bad luck doesn't fade?

MEI: That's the whole idea. Their shocks are persistent. In fact, permanent. If you lose your job and end up in a worse-paid one, that's not a broken laptop. That's for life. And you can't smooth a permanent shock with a savings buffer. You just have to consume less, forever.

MIGUEL: That's depressing, but I get it. A buffer works for a flat tire, not for losing the car.

MEI: Great analogy. The abstract summarizes the income shocks in three words: uninsurable, persistent, and heteroscedastic.

MEI: It means the variance changes over time. Here, how risky your personal income is depends on the state of the economy. That will turn out to be crucial.

## The economy

MIGUEL: Let's build the economy.

MEI: It's an exchange economy. That means nothing is produced by choice. Fruit falls from trees, so to speak. There is a single consumption good. There are n securities, think stocks and corporate bonds, and each pays a dividend every period. Each security is in fixed positive supply, normalized to one.

MIGUEL: Plus bonds?

MEI: Plus default-free discount bonds of many maturities. A discount bond pays one unit of the good at maturity and nothing before. These bonds are in zero net supply.

MIGUEL: Zero net supply, meaning what?

MEI: For every borrower there is a lender. If you add up everyone's bond holdings, you get zero. Bonds are just contracts between consumers.

MIGUEL: And the people?

MEI: An infinite number of consumers. They need infinitely many so that the law of large numbers works: individual shocks average out exactly in the aggregate. Each consumer receives a labour income and consumes. Aggregate consumption equals total labour income plus total dividends.

MIGUEL: So consumption equals wages plus dividends. Fruit plus salary.

MEI: Right. And here's a nice footnote. The authors cite Mankiw and Zeldes, 1991, and others, who found that only a small fraction of people hold any stocks at all. So they say: our consumers are the stockholders. The aggregate labour income in the model is the labour income of stockholders only.

MIGUEL: Mankiw again, five years after his concentration paper. The man is everywhere.

MEI: Now preferences. Everyone has the same utility function: power utility, also called constant relative risk aversion. Two parameters. Alpha is the risk aversion coefficient, and rho is the subjective discount rate, how impatient you are.

MIGUEL: Same preferences for everyone. So the heterogeneity is only in income.

MEI: Only in income. That's an important design choice. Nobody is a weird risk lover. People differ only because of what life throws at them.

## Reverse engineering

MIGUEL: So how do they solve this beast? A dynamic economy with infinitely many people and incomplete markets sounds impossible.

MEI: Usually it is. That's why the earlier papers used computer simulations. Constantinides and Duffie do something clever: they work backwards.

MIGUEL: Backwards how?

MEI: Normally, you specify incomes, solve for optimal behaviour, and get prices out. They do the opposite. They take the prices as given, the actual observed prices of stocks and bonds, and ask: is there some income process, consistent with aggregate data, that would make these prices an equilibrium?

MIGUEL: So instead of "what prices does this world produce," it's "what world could produce these prices."

MEI: Exactly. Reverse engineering. And their degree of freedom is how they split aggregate income among individuals.

MIGUEL: Where do they start?

MEI: With no arbitrage. An arbitrage is a free lunch: a trading strategy that costs nothing and might make money with no risk of losing any. If prices allow no arbitrage, a fundamental theorem of asset pricing says there exists a strictly positive pricing kernel. They call it M.

MIGUEL: Pricing kernel. Also called the stochastic discount factor, right?

MEI: Same thing. The functional form is simple: the price of any asset today equals the expected sum of its future dividends, each multiplied by the kernel in that future state, relative to the kernel today. The kernel is high in states where money is precious and low where money is cheap.

MIGUEL: So it's the "how much is a dollar worth in that world" multiplier.

MEI: Exactly. Bond prices too: a bond price is just the expected ratio of future to current kernel.

MIGUEL: And any assumptions on the kernel?

MEI: One substantive one. They call it the pricing kernel condition. It says: the growth of the true kernel, from one period to the next, must be at least as large as the representative consumer's marginal rate of substitution. That marginal rate is the discount factor times aggregate consumption growth raised to minus alpha.

MIGUEL: Translate, please.

MEI: The representative-agent model says "here is how much bad times hurt." The true kernel, from prices, says "here's how much bad times actually seem to hurt investors." The condition says the true pain is always at least as big as the representative-agent pain. Never smaller.

MIGUEL: And why is that a reasonable assumption?

MEI: Two reasons. First, intuition from Mankiw: heterogeneity with convex marginal utility only adds pain. Adding uninsurable risk can never make people less worried. Second, it's testable. It implies an Euler inequality: if you plug any asset return into the representative-agent Euler equation, the left side must be at most one, instead of exactly one.

MIGUEL: An inequality instead of an equality. Sounds weaker.

MEI: Much weaker, and that's the beauty. Remember, the representative-agent equality was rejected over and over. But the authors cite tests of the inequality, by Cochrane and Hansen, Luttmer, and He and Modest, and these tests failed to reject it with plausible risk aversion.

MIGUEL: So the data says "the representative agent doesn't feel enough pain." And this paper says "fine, the missing pain comes from inequality."

MEI: Miguel, you're becoming dangerous.

## Building the income shocks

MIGUEL: Now the fun part. How do they design incomes?

MEI: Each consumer's income is defined so that their consumption equals a personal share, call it delta, times aggregate consumption. Their income equals that share times aggregate consumption, minus aggregate dividends.

MIGUEL: Wait, why minus dividends?

MEI: Because each consumer also receives dividends from their stock holdings, and everyone starts with identical holdings. So income plus dividends gives exactly the personal share times aggregate consumption. That's chosen so that, in equilibrium, nobody needs to trade.

MIGUEL: Sneaky. Okay, and the personal share delta?

MEI: Here's the functional form, in words. Delta is an exponential of a running sum of shocks. Each period, you get a new shock: a standard normal random number, specific to you, times a scale y that's common to everyone, minus a correction of y squared over two.

MIGUEL: Why the minus y squared over two?

MEI: It's a lognormal correction. When you exponentiate a normal variable, the average gets pushed up by half the variance. Subtracting y squared over two cancels that, so the average share across people stays exactly one. That way the shares add up to total consumption. No money appears or disappears.

MIGUEL: Right, Jensen's inequality again. It's following us around.

MEI: It's the mascot of this podcast. Now, two features. First, the shocks add up over time, so log consumption share is a random walk. That's permanent. A bad shock today shifts your whole future. That's the persistence we needed.

MIGUEL: And the second?

MEI: The scale y, the size of everyone's idiosyncratic risk, changes over time. That's the heteroscedasticity. And here's the trick of the whole paper: they choose y exactly.

MIGUEL: Chosen how?

MEI: y squared equals a constant, two divided by alpha squared plus alpha, times a bracket. In the bracket: the log growth of the true kernel, plus rho, plus alpha times log aggregate consumption growth.

MIGUEL: In human words.

MEI: The bracket is the log of the gap between the true kernel and the representative-agent kernel. So the variance of idiosyncratic risk is set to exactly fill the gap. When the data says investors feel much more pain than the representative agent, idiosyncratic risk that period is large. When the two agree, idiosyncratic risk is zero.

MIGUEL: And that's why they need the pricing kernel condition! If the gap were negative, y squared would be negative.

MEI: And a variance can't be negative. Exactly. That's the role of the condition.

MIGUEL: I just felt something click. It was either my brain or my chair.

## Proposition 1 and the no-trade equilibrium

MEI: Now the main result. Proposition 1: under the pricing kernel condition, there exists an equilibrium with no trade that supports the given prices of securities and bonds.

MIGUEL: No trade? Nobody trades anything?

MEI: Nobody. Each person just eats their income plus dividends. And the claim is that, at the observed prices, nobody wants to trade.

MIGUEL: How do they show it?

MEI: Here's the gist. Take consumer i. Their marginal rate of substitution between today and tomorrow is the representative one, times an extra factor: the exponential of minus alpha times their personal shock tomorrow.

MIGUEL: So my personal pain is the average pain, adjusted for my personal luck.

MEI: Right. Now compute how much consumer i would pay for a security, their private valuation. You average over your own personal shock. And because the personal shock is normal and independent of everything else, that average has a closed form: the exponential of alpha times alpha plus one, over two, times y squared.

MIGUEL: And y squared was chosen to fill the kernel gap, right?

MEI: So that factor equals exactly the ratio of the true kernel to the representative kernel. Substitute, and consumer i's private valuation equals the market price. For every consumer, for every security.

MIGUEL: So everyone looks at the market and says, "that price is exactly what I think it's worth." No reason to buy or sell.

MEI: That's a no-trade equilibrium. Appendix A adds a technical check: nobody gains from some infinitely long trading strategy either.

MIGUEL: Appendix A, you have been acknowledged. Moving on.

MEI: Now, the authors are honest: no-trade is counterfactual. People do trade. They say the income processes were designed for a tractable equilibrium with a closed-form solution. And they suggest reading the individual consumption processes as "posttrade" allocations. In other words, think of the shocks as what is left after people have done whatever trading they do. The uninsurable part.

MIGUEL: So the trading happened offstage, and we only see the leftovers.

MEI: Nice.

## The new Euler equation

MEI: This is the heart of the paper. Section four. Because every consumer's Euler equation holds, they can aggregate and get a new Euler equation that uses only aggregate objects.

MIGUEL: Hold on. Mankiw said you can't aggregate.

MEI: Mankiw said you can't aggregate using only aggregate consumption. Here you need one extra aggregate variable: the cross-sectional variance of consumption growth.

MIGUEL: Okay, describe it.

MEI: The new Euler equation looks like the representative one, with one extra multiplier. Inside the expectation: the asset's return, times the usual representative kernel, discount factor times consumption growth to the minus alpha. Times a new term: the exponential of alpha times alpha plus one, over two, times y squared. And the whole expectation must equal one.

MIGUEL: So the pricing kernel is the old kernel times an inequality booster.

MEI: "Inequality booster" is going on a T-shirt. And the booster is always at least one, because y squared is non-negative and alpha is positive. Higher dispersion means a higher kernel, so periods of high dispersion count as bad times.

MIGUEL: And what is y squared, in the data?

MEI: That's the key interpretation. y squared is the cross-sectional variance of the log of individual consumption growth, relative to aggregate consumption growth. Take everyone in the economy, compute how fast their consumption grew this year compared with the average, take logs, and compute the variance across people.

MIGUEL: So in a year when everyone's consumption grows at roughly the same rate, y squared is small. In a year when some people do great and others crash, y squared is big.

MEI: Exactly. And it can be measured from panel data on consumption, which is data that follows the same households over time. That's why the authors stress that the model is testable.

MEI: Now special cases. First: if consumers are homogeneous, y squared is zero, the booster equals one, and you're back to the textbook representative Euler equation.

MIGUEL: Good. The new model nests the old one.

MEI: Second case: suppose y squared is a linear function of log aggregate consumption growth. A constant a plus a slope b times consumption growth.

MIGUEL: So dispersion moves with the business cycle in a simple way.

MEI: Then something magical happens. The new Euler equation looks exactly like a representative-agent Euler equation, but with a different discount rate and a different risk aversion. The modified discount rate is rho minus alpha times alpha plus one, over two, times a. The modified risk aversion is alpha minus the same factor times b.

MIGUEL: So an economist who ignores heterogeneity would estimate the "wrong" rho and alpha, and think they're the right ones.

MEI: Exactly. Now the punchline. Suppose dispersion increases in recessions. That's what Mankiw would expect. Then b is negative: when consumption growth is low, dispersion is high. And so the modified risk aversion is bigger than the true one.

MIGUEL: So the economist overestimates risk aversion. That's Mankiw's result, in a dynamic model!

MEI: Precisely. But the authors add an important caveat. This linear case is of limited economic interest, because representative-agent Euler equations are rejected by the data even when you let the discount rate and risk aversion be anything. So the interesting case is when dispersion is not just a linear function of consumption growth.

MIGUEL: So the inequality factor has to bring new information, not just repackage consumption growth.

MEI: Very well put. Now the general case. They write the expected excess return of any asset over the risk-free rate. The functional form: minus the covariance between the asset's return and the new kernel, divided by the expected value of the kernel.

MIGUEL: That's the standard formula. Assets that pay badly when the kernel is high earn a premium.

MEI: Same structure as always. The novelty is what's inside the kernel. Now the kernel includes the inequality booster. So an asset whose return is low when dispersion is high earns a positive premium. An asset that pays well when dispersion is high is a hedge and earns a negative premium.

MIGUEL: Does that mean ignoring heterogeneity always understates the premium?

MEI: No, and this is a fun moment. Weil, in 1992, had a proposition saying that with power utility, an economist unaware of uninsurable risk would unambiguously understate the equity premium. Constantinides and Duffie say: this finding contradicts Weil. It can go either way, depending on the sign of the covariance between returns and the booster.

MEI: Then the extreme example. Suppose aggregate consumption growth is a constant. Totally flat. In the representative model, the kernel is constant, so all assets earn the same expected return. No equity premium at all.

MIGUEL: Because nothing covaries with a constant.

MEI: Right. But in the heterogeneous model, a security still has a positive risk premium if its return covaries negatively with the cross-sectional variance. So inequality alone can generate a premium, even with no aggregate risk.

MIGUEL: That's wild. An equity premium in an economy where the average person's consumption never changes.

MEI: The authors call it "a potential source of the equity premium, a source that is assumed away in a representative-consumer economy."

## Persistence and dynasties

MIGUEL: Okay, now I have a worry. If everyone's share is a random walk, doesn't inequality explode over time?

MEI: Excellent worry, and the authors share it. Because shocks are permanent and independent across people, the cross-sectional distribution of income and consumption keeps spreading out. The variance grows, the Gini coefficient grows, forever.

MEI: And in the real world, inequality doesn't go to infinity. So in Section five and Appendix B, they fix it.

MIGUEL: How?

MEI: Random lifetimes. Each period, a consumer survives with a fixed probability q, the same for everyone and independent across people and time. When a consumer dies, an heir replaces them, and the heir's personal shock history restarts at zero.

MIGUEL: So death resets the random walk. Dark, but effective.

MEI: There's a key assumption: newborns don't inherit their parents' stock holdings. When someone dies, their holdings are redistributed equally among all newborns.

MIGUEL: A hundred percent inheritance tax, redistributed to babies. Very progressive.

MEI: It keeps the math tractable. And with that, a slightly modified version of Proposition 1 still holds. The Euler equation keeps the same form. The only change is that the discount rate picks up the survival probability: the effective rate is rho minus the log of q.

MIGUEL: Makes sense. If you might die, you discount the future more.

MEI: Exactly. And because dynasties restart, the cross-sectional distribution of consumption settles into a stationary distribution, with finite variance under plausible conditions.

## Conclusion and legacy

MIGUEL: How do the authors close?

MEI: Modestly. They chose power utility because it's homothetic: scaling everyone's consumption doesn't change their choices. That's what made the closed form possible. And they point out that convex marginal utility is what makes the pricing kernel condition necessary.

MIGUEL: Convex marginal utility again. That's Mankiw's third derivative.

MEI: Exactly. And they say it remains a challenge to build tractable heterogeneous economies that don't rely on convex marginal utility.

MIGUEL: And did the idea work in the data?

MEI: The model handed researchers a clear test: measure the cross-sectional variance of consumption growth in household data and see if it prices assets. One follow-up is Cogley, 2002, which uses the Consumer Expenditure Survey to do this. The answer there was more sobering: measured dispersion helps, but it moves only weakly with stock returns. So at moderate risk aversion it goes only part of the way toward explaining the equity premium.

MIGUEL: So the inequality booster is real, but it doesn't solve everything.

MEI: That's a fair summary. But the framework became the standard way to think about idiosyncratic risk and asset prices.

MEI: And Duffie took his career toward the plumbing of markets. He sat on the board of Moody's, the credit rating agency, from 2008 to 2018, and chaired a Financial Stability Board group on reforming LIBOR, the benchmark interest rate.

MIGUEL: From pricing kernels to fixing the world's most famous interest rate. Not bad.

## Wrap-up: the recap

MIGUEL: Okay, quick recap before we go. Give me the whole paper in one minute.

MEI: Deal. The question: can uninsurable income risk explain the equity premium and the risk-free rate puzzles, when earlier incomplete-markets models said it barely matters?

MIGUEL: And the method?

MEI: Reverse engineering. They take observed asset prices as given, together with a pricing kernel that is at least as large as the representative agent's. Then they construct individual income processes with permanent shocks whose variance moves with the state of the economy. They prove that the observed prices are a no-trade equilibrium and derive a new Euler equation. Appendix B adds random lifetimes so that inequality stays finite.

MIGUEL: Main takeaways?

MEI: One: the shocks have to be persistent. Temporary shocks get smoothed away with savings. Two: the pricing kernel is the representative-agent kernel times an exponential term in the cross-sectional variance of consumption growth. Three: assets that do badly when that dispersion is high earn a premium, even if aggregate consumption never moves. And if dispersion rises in recessions, an economist who ignores it overestimates risk aversion.

MIGUEL: And the conclusion?

MEI: With uninsurable, persistent and heteroscedastic income shocks, heterogeneity can support the asset prices we observe. The model gives a testable prediction: measure the cross-sectional variance of consumption growth in household panel data and check whether it prices assets. Its main limit is that it relies on convex marginal utility.

MIGUEL: And my takeaway: savings handle flat tires, not lost cars. And Jensen's inequality will find you, wherever you hide.

MEI: Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you next time. And thanks, Appendix A. You were technically there.
