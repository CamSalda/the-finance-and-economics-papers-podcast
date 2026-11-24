# The Finance and Economics Papers Podcast: Who Pays for the Recession? Mankiw (1986) and the Equity Premium

> **Open-source educational project.** The Finance and Economics Papers Podcast is a free, open-source initiative whose only
> goal is education: to create and spread knowledge about research in finance and economics. This episode is an independent,
> unofficial explanation of the paper below, written in our own words for teaching purposes. It is not affiliated
> with or endorsed by the authors or the publisher. The paper is not reproduced here: read the original at the
> DOI link. Short quotes are attributed to the authors. Scripts and audio are released under CC BY 4.0; the paper
> remains the property of its authors and publisher.

- **Paper:** Mankiw, N. G. (1986). The equity premium and the concentration of aggregate shocks. *Journal of Financial Economics*, 17(1), 211-219.
- **Read the paper:** https://doi.org/10.1016/0304-405X(86)90012-7
- **Topics:** Asset pricing; equity premium puzzle; incomplete markets
- **Length:** 23 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance and Economics Papers Podcast, where we discuss the papers that shaped finance and economics, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel. I'm the one who asks the questions you're too embarrassed to ask in class.

MEI: Quick note before we start. This is an open-source, educational project. We explain published research in our own words, for learning only. We are not affiliated with the authors or the journal, and the best thing you can do after listening is read the original paper. The link is in the episode notes.

MEI: Today we're doing a classic. Gregory Mankiw, 1986, in the Journal of Financial Economics. The title is "The equity premium and the concentration of aggregate shocks." It's nine pages long.

MIGUEL: Nine pages? I've written longer emails to my landlord.

MEI: And this one has more ideas per page than your landlord emails. Fun fact to start: the referee on this paper was Fischer Black.

MIGUEL: Black, as in Black-Scholes?

MEI: That one. Mankiw thanks him in the very first footnote. So imagine sending in your paper, and the person checking your math has an option-pricing formula named after him.

MIGUEL: No pressure at all.

MEI: And a sad footnote to that. Black died in 1995. Two years later, Myron Scholes and Robert Merton won the Nobel prize for option pricing, and the Nobel is never awarded after death.

MIGUEL: Oof. Okay, and the author himself?

MEI: When this paper was submitted, in 1985, Mankiw was a 27-year-old assistant professor at Harvard. He had finished his PhD at MIT a year earlier, and his advisor was Stanley Fischer, who is also thanked in this paper.

MIGUEL: Thanking your PhD advisor. Smart career move.

MEI: And look at the rest of that list. Stanley Fischer later ran the Bank of Israel and became Vice Chair of the US Federal Reserve. Olivier Blanchard later became chief economist of the IMF. And David Romer was Mankiw's classmate at Princeton.

MIGUEL: So this nine-page paper has a better guest list than my wedding.

MEI: Here's the hook. Between 1929 and 1933, during the Great Depression, consumption per person in the United States fell by about twenty percent.

MIGUEL: Twenty percent is huge.

MEI: It is. But Mankiw asks a sneaky question. Did everyone consume twenty percent less? Or did most people carry on more or less as before, while some people lost almost everything?

MIGUEL: I'm guessing the second one.

MEI: And that question, who actually takes the hit, is the whole paper. By the end of this episode you'll see why it can make stocks much riskier than the averages suggest.

## The puzzle

MIGUEL: Okay, but first, what problem is he trying to solve?

MEI: The equity premium puzzle, from Mehra and Prescott in 1985. The equity premium is the extra return that stocks earn over safe assets like Treasury bills. In US data it's about six percent per year. Fun fact: Edward Prescott later won the Nobel prize, in 2004, though for his work on business cycles.

MIGUEL: Six percent extra, every year, just for holding stocks. Why doesn't everyone just buy stocks?

MEI: Exactly the right question. In theory, you get paid for bearing risk. So the premium should be roughly how risky stocks are, times how much people dislike risk. The puzzle is that when you plug in the numbers, people would need to dislike risk absurdly much.

MIGUEL: Define "dislike risk." Properly.

MEI: The technical term is the coefficient of relative risk aversion. Mankiw calls it A. It measures how much you'd give up to avoid a gamble, relative to your wealth. Values of one or two are usually considered reasonable. Ten already makes people look very, very nervous.

MIGUEL: And what does someone with a risk aversion of thirty look like?

MEI: Someone who refuses almost any bet, even very favourable ones, and pays a fortune to insure a scratch on their bike.

MIGUEL: I know that guy.

MEI: Now, how do we measure how risky a stock is? Here's the key move of consumption-based asset pricing. An asset is risky if it pays badly exactly when you're poor. And when are you poor? When your consumption is low. So the risk of an asset is how much its return moves together with consumption growth. The technical word is covariance.

MIGUEL: Covariance. So, how much the stock's return and consumption go up and down together.

MEI: Right. Mankiw starts from a relation derived by Grossman and Shiller in 1982, called the consumption-beta relation. It's a simple product. On one side you have the expected excess return of an asset. On the other side you have two ingredients multiplied together: risk aversion, and the covariance between the asset's return and the growth of aggregate consumption.

MIGUEL: Shiller, as in Robert Shiller?

MEI: The same. He shared the 2013 Nobel prize with Eugene Fama and Lars Hansen, and Hansen's tests of these consumption models are cited in this paper too.

MIGUEL: And aggregate consumption is just everybody's spending added up.

MEI: Per person, yes. Now the numbers. The equity premium is about six percent. The volatility of stock returns is about twenty percent. The volatility of consumption growth is about three percent. Consumption is boring. It barely moves.

MIGUEL: Boring consumption, wild stocks.

MEI: Here's the trick. The covariance can be at most the two volatilities multiplied together. That happens if stocks and consumption are perfectly correlated. Twenty percent times three percent is 0.006. To turn that into a premium of 0.06, risk aversion has to be at least ten.

MIGUEL: Already in nervous territory.

MEI: And in the data, the correlation between stocks and consumption is only about one third. So the covariance is a third of that upper bound, and risk aversion has to be about thirty.

MIGUEL: Thirty. So the model says the typical investor is basically a hamster in a bomb shelter.

MEI: Which, as Mankiw says very politely, is "generally considered implausible."

## The toy economy

MIGUEL: So where does the standard model go wrong?

MEI: Mankiw's suspicion is the word "aggregate." All of these calculations use a representative consumer.

MIGUEL: The one imaginary person who stands in for the whole economy.

MEI: Yes. The idea is that if you add everyone up, the economy behaves as if there were one person consuming the average. Mankiw wants to show that this can badly mislead you. And he builds the simplest possible model to show it.

MIGUEL: Simplest possible. I like this man already.

MEI: There are two dates. Today, you choose your portfolio. Tomorrow, nature flips a fair coin and everyone consumes. Heads is the good state: consumption per person is at its normal level, which he calls mu. Tails is the bad state: consumption per person falls by a fraction he calls phi. If phi is five percent, the economy is five percent poorer in the bad state.

MEI: Now the asset. Instead of stocks and bonds separately, he uses one portfolio: you borrow at the Treasury bill rate and buy equity. That's a long-short position. In the bad state it pays minus one, so you lose your dollar. In the good state it pays one plus pi, where pi is the premium, the reward for taking the risk.

MIGUEL: So it's a bet. Lose a dollar if things go badly, win a dollar plus a bonus if things go well.

MEI: Perfect. And the question is: how big must the bonus pi be for people to be willing to hold this bet?

MIGUEL: And where does the answer come from?

MEI: The first-order condition, the workhorse equation of asset pricing. In words, it says that the expected payoff of the bet, weighted by marginal utility, must equal zero.

MIGUEL: Translate "marginal utility."

MEI: Marginal utility is how much extra happiness the next dollar gives you. When you're rich, one more dollar barely matters. When you're poor, one more dollar is gold. So marginal utility is high in bad times and low in good times.

MIGUEL: So weighting by marginal utility means dollars in bad times count for more.

MEI: Exactly. In equilibrium, once each state's payoff is weighted that way, the bet is neither attractive nor unattractive. Otherwise people would keep buying or selling it.

MIGUEL: So pi has to be big enough that the bonus in good times, when dollars matter little, makes up for the loss in bad times, when dollars matter a lot.

MEI: You just derived the equation. The formula for the premium is a ratio. On top, you have the gap between marginal utility in the bad state and marginal utility in the good state. On the bottom, you have marginal utility in the good state. The more painful bad times feel relative to good times, the bigger the premium.

MIGUEL: And if the shock is small?

MEI: Then it simplifies beautifully. The premium is approximately risk aversion times the size of the shock.

MIGUEL: So with a five percent shock and a risk aversion of two, the premium is about ten percent.

MEI: Right. And this is exactly how an economist would back out risk aversion from the data: take the premium, take the size of the aggregate shock, and divide one by the other. That's the trap Mankiw is about to spring.

## The twist

MIGUEL: Okay. Where's the trap?

MEI: Now there are many people, infinitely many in fact, and they're all identical before the coin flip. Mankiw's key phrase is that they are identical ex ante but different ex post.

MIGUEL: Latin. Help.

MEI: Ex ante means "before": before the coin lands, everybody faces the same odds. Ex post means "after": after the coin lands, some people turn out lucky and some don't.

MIGUEL: Like a lottery. Before the draw, everyone holds the same ticket.

MEI: A rather grim lottery. In the good state, everyone consumes mu. But in the bad state, the aggregate loss isn't shared. It falls on a fraction lambda of the population.

MIGUEL: So if lambda is one?

MEI: Then everyone shares the loss equally, and we're back to the representative consumer. As lambda gets smaller, the same total loss gets piled onto fewer and fewer people.

MIGUEL: How much does each unlucky person lose?

MEI: The aggregate loss divided by lambda. Take Mankiw's own example. The aggregate shock is five percent, and lambda is twenty percent, so one person in five bears the whole shock. Each of them loses five percent divided by one fifth, which is twenty-five percent of their consumption.

MIGUEL: Ouch. So the newspaper says "the economy shrank five percent," but for the unlucky ones it's twenty-five.

MEI: And the other eighty percent lose nothing at all.

MIGUEL: Wait. Why don't people just insure each other? Like, "if I get hit, you pay me, and if you get hit, I pay you."

MEI: That's the crucial assumption. Mankiw assumes those markets don't exist. The technical term is missing contingent-claims markets. A contingent claim is a contract that pays only if a specific event happens, in this case, only if you personally are among the unlucky. Think unemployment insurance, but complete and perfect. In his model you can trade the portfolio, but you can't trade a contract on "I'm in the unlucky group." Economists call this situation incomplete markets.

MIGUEL: Why wouldn't such a contract exist? Sounds like a great product.

MEI: He answers that in the conclusion: moral hazard and adverse selection. Moral hazard means that if you're fully insured against losing your job, you might try a little less hard to keep it. Adverse selection means the people most eager to buy the insurance are exactly the ones who know they're likely to need it.

MIGUEL: So the insurer goes broke and the market vanishes.

MEI: Pretty much. In the math, the bad state now has two branches: you're fine with probability one minus lambda, and hammered with probability lambda. The premium becomes lambda, times the extra marginal utility when you're hammered, relative to your normal marginal utility.

MIGUEL: In human words, please.

MEI: The premium equals the probability of being hit, times how much more a dollar is worth to you when you're hit, compared with normal times. A small chance, but a huge pain.

MIGUEL: So the premium depends on two things now: the size of the shock, and how it's spread.

MEI: And that's the whole point. Same aggregate data, different premium.

## Three propositions

MEI: Mankiw states three propositions, and each one has a nice punchline.

MIGUEL: Proposition one. Go.

MEI: If utility is quadratic, concentration doesn't matter at all. The premium doesn't depend on lambda.

MIGUEL: Why quadratic?

MEI: With quadratic utility, marginal utility is a straight line. Every lost dollar raises marginal utility by the same amount. So losing twenty-five percent with probability one fifth costs you, on average, exactly as much as losing five percent for sure. Spreading or concentrating the loss doesn't change average marginal utility.

MIGUEL: Straight-line marginal utility, so averages work, so the representative agent is fine.

MEI: Right. But quadratic utility is weird. It implies people become more risk averse as they get richer, and past some point, more money actually makes you less happy.

MIGUEL: Ah, the "I'm too rich, please make it stop" utility.

MEI: Proposition two. If the third derivative of the utility function is positive, then more concentration raises the premium.

MIGUEL: The third derivative. I barely trust the second one.

MEI: Let's build it up. The first derivative is marginal utility, and it's positive: more is better. The second derivative is negative: marginal utility falls as you get richer. That's risk aversion. A positive third derivative means marginal utility is convex. It falls steeply at first and then flattens out. Read it the other way: as you get poorer, your marginal utility shoots up faster and faster.

MIGUEL: So when you're already starving, every slice of pizza you lose hurts more than the one before.

MEI: Great analogy. The technical name is prudence. It's what drives precautionary saving: putting extra money aside when the future is uncertain. And it's very plausible. Mankiw points out it's an even weaker condition than decreasing absolute risk aversion, which almost everyone accepts. The standard power utility function satisfies it.

MIGUEL: So with convex marginal utility, one person losing twenty-five percent hurts way more than five people losing five percent each.

MEI: Exactly. Averages lie. The average of everyone's marginal utilities is higher than the marginal utility of average consumption. That's Jensen's inequality, if you remember it from statistics class.

MIGUEL: I remember the name. Vaguely. With fear.

MEI: The proof is short: the derivative of the premium with respect to lambda is negative whenever the third derivative is positive. More spreading, lower premium. More concentration, higher premium.

MIGUEL: And the implication?

MEI: An economist using the representative consumer model gets risk aversion right only if lambda equals one. If the shock is concentrated, the economist sees a big premium, blames it all on risk aversion, and overestimates risk aversion.

MIGUEL: So the hamster in the bomb shelter might just be a normal person who's scared of being one of the unlucky ones.

MEI: That's the paper in one sentence. One caveat Mankiw flags: the direction depends on the concentrated shock being bad. If a few people instead got a concentrated windfall, more concentration would shrink the premium.

MIGUEL: Okay, proposition three. What does it say?

MEI: Suppose marginal utility goes to infinity as consumption goes to zero. That's called the Inada condition. In plain words: having nothing at all is infinitely bad.

MIGUEL: Reasonable.

MEI: Then, as lambda goes to zero, so as the shock lands on fewer and fewer people, the premium goes to infinity.

MIGUEL: Infinity. Whoa.

MEI: Think about it. A tiny group loses almost everything. Each person faces a small chance of ruin, and ruin is infinitely bad. So you'd demand an enormous reward for holding the risky asset.

MIGUEL: So the size of the aggregate shock puts no ceiling on the premium.

MEI: Right. And flipping it around: from the premium and the aggregate shock alone, you can't put a floor under risk aversion. A modest risk aversion can be consistent with a six percent premium, if shocks are concentrated enough.

## The numbers

MIGUEL: Give me numbers. I need numbers.

MEI: Table one. The aggregate shock is fixed at five percent. He reports the ratio of the true premium to the premium that a representative-consumer economist would expect.

MIGUEL: So a ratio of one means no mistake.

MEI: Exactly. Start with twenty percent of people hit, so each unlucky person loses twenty-five percent. With log utility, which is a risk aversion of one, the ratio is 1.3. The true premium is thirty percent higher than expected. With risk aversion three, the ratio is 1.6. With risk aversion six, it's 2.6.

MIGUEL: So more than double.

MEI: Now concentrate it more: only ten percent of people are hit, and each loses half their consumption. With log utility the ratio is 1.9. With risk aversion three it's 4.2. And with risk aversion six, it's 17.5.

MIGUEL: Seventeen and a half times! That's not a rounding error.

MEI: But Mankiw is honest about it. He says the model is "too stylized to draw firm empirical conclusions." The table just shows that the effect can be large.

## The intuition section

MIGUEL: There's a section three, right? The "intuitive" one?

MEI: Yes. He goes general. He approximates each person's marginal utility around average consumption with a second-order Taylor expansion, a straight line plus a little bend, and adds up across everybody. The expected excess return splits into three terms.

MIGUEL: Walk me through them, quickly.

MEI: First, the covariance of the return with average consumption, scaled by risk aversion. That's the textbook consumption CAPM. Second, from the third derivative, how the return moves with big swings in average consumption, a kind of coskewness. Third, the new one, also from the third derivative: how the return moves with the dispersion of individual consumption around the average. If an asset pays badly when consumption is very spread out, it must earn more.

MIGUEL: And in the toy model, dispersion is high exactly in the bad state.

MEI: Right, so that term pushes the premium up. With quadratic utility the last two terms vanish, which is proposition one again. In general, Mankiw adds, uninsurable risk could push the premium either way, depending on when dispersion is high.

## What Mankiw concedes

MIGUEL: So should we throw representative agents in the bin?

MEI: Mankiw doesn't go that far. He says it's probably impossible to justify them rigorously once markets are incomplete. But they may still be a useful approximation where the missing markets don't matter much. And you can use what he calls a "surrogate" consumer, with a made-up utility function, as long as you don't pretend its risk aversion describes real people.

MIGUEL: So the representative agent is a stunt double. Great for action scenes, but don't ask about his feelings.

MEI: And he leaves a research agenda: figure out when the approximation works and when it fails. Ten years later, Constantinides and Duffie, in 1996, build a full dynamic model on this idea, where the cross-sectional variance of consumption growth enters the pricing kernel directly.

MEI: And Mankiw didn't drop the topic. In 1991, with Stephen Zeldes, he showed that only about a quarter of American families owned any stock at all.

MIGUEL: And what happened to Mankiw himself?

MEI: He wrote the textbook Principles of Economics, first published in 1997, with a record advance from the publisher of 1.4 million dollars. And from 2003 to 2005 he chaired the Council of Economic Advisers for President George W. Bush.

MIGUEL: So the man behind my first-year textbook also wrote about who pays for recessions. I feel personally seen.

## Wrap-up: the recap

MIGUEL: Okay, quick recap before we go. Give me the whole paper in one minute.

MEI: Deal. The question: can a reasonable risk aversion explain a six percent equity premium? With aggregate consumption alone, the answer is no. You need a risk aversion around thirty.

MIGUEL: And the method?

MEI: A deliberately tiny model: two dates, a fair coin, and a long-short portfolio of stocks against Treasury bills. In the bad state, the loss falls on a fraction lambda of identical consumers who cannot insure it. He compares their first-order conditions with the representative consumer's, proves three propositions, and puts numbers on the gap.

MIGUEL: Main takeaways?

MEI: One: with quadratic utility, concentration doesn't matter. Two: with a positive third derivative, which is prudence, a more concentrated shock means a higher premium, with no change in risk aversion. Three: as the shock lands on fewer and fewer people, the premium can grow without limit. In the table, the true premium is between 1.3 and 17.5 times what the representative model predicts.

MIGUEL: And the conclusion?

MEI: You cannot infer risk aversion from aggregate data alone, because averages hide who pays. Representative consumers can still be useful surrogates, but their risk aversion shouldn't be read as that of real people.

MIGUEL: And my takeaway: in a recession, try very hard not to be in lambda.

MEI: Thanks for listening to The Finance and Economics Papers Podcast.

MIGUEL: See you next time. And remember: nine pages can be enough to keep a whole literature busy.
