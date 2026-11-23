# The Finance Papers Podcast: Six Percent Too Many. Mehra and Prescott (1985) and the Equity Premium Puzzle

> **Open-source educational project.** The Finance Papers Podcast is a free, open-source initiative whose only
> goal is education: to create and spread knowledge about research in finance. This episode is an independent,
> unofficial explanation of the paper below, written in our own words for teaching purposes. It is not affiliated
> with or endorsed by the authors or the publisher. The paper is not reproduced here: read the original at the
> DOI link. Short quotes are attributed to the authors. Scripts and audio are released under CC BY 4.0; the paper
> remains the property of its authors and publisher.

- **Paper:** Mehra, R., & Prescott, E. C. (1985). The equity premium: A puzzle. *Journal of Monetary Economics*, 15(2), 145-161.
- **Read the paper:** https://doi.org/10.1016/0304-3932(85)90061-3
- **Topics:** Asset pricing; equity premium puzzle; consumption-based asset pricing
- **Length:** 21 minutes
- **Hosts:** Mei (the guide) and Miguel (the student)

## Cold open

MEI: Welcome to The Finance Papers Podcast, where we discuss the papers that shaped finance, to make reading them easier and more fun. I'm Mei.

MIGUEL: And I'm Miguel, still asking the questions you're too embarrassed to ask in class.

MEI: Quick note before we start. This is an open-source, educational project. We explain published research in our own words, for learning only. We are not affiliated with the authors or the journal, and the best thing you can do after listening is read the original paper. The link is in the episode notes.

MEI: Today is a special one. Rajnish Mehra and Edward Prescott, "The equity premium: A puzzle," Journal of Monetary Economics, 1985. Seventeen pages.

MIGUEL: The equity premium puzzle. I've heard that name in every asset pricing class.

MEI: And this is where the name comes from. Mankiw in 1986, Constantinides and Duffie in 1996, and many other papers are attempts to solve the puzzle these two set.

MIGUEL: So it's the origin story. The first movie that every sequel copies.

MEI: And it's worth it. Here's the hook. Over ninety years, from 1889 to 1978, American stocks paid a real return of about seven percent a year. Safe short-term debt paid less than one percent. Mehra and Prescott ask a simple question: can a standard economic model explain that gap?

MIGUEL: And the answer is in the title. It's a puzzle.

MEI: The answer is "not even close." And the way they show it is a masterclass in how to use a model.

MIGUEL: Any fun facts before we dive in?

MEI: Plenty, starting with the first footnote. The research began at the University of Chicago, where Mehra was a visiting scholar at the business school and Prescott a visiting professor in economics. And early versions had a much more boring title: "A Test of the Intertemporal Asset Pricing Model."

MIGUEL: "The equity premium: A puzzle" is way catchier. Somebody had a marketing instinct.

MEI: It also needed patience. Mehra later wrote that the research dates from 1979, and that "it took us six more years to convince a skeptical profession" before it was published. The Minneapolis Fed put out the version with the old title as a staff report in 1982.

MIGUEL: Six years. I get impatient when a referee takes six weeks.

MEI: Then look at who they thank: George Constantinides, Eugene Fama, Merton Miller, Fischer Black, Stephen LeRoy and Charles Plosser.

MIGUEL: Fischer Black, as in Black-Scholes? He's like the Stan Lee of finance: he makes a cameo everywhere.

MEI: He even shows up in a second footnote, which we'll get to. And remember Constantinides in that list. He matters at the end.

MIGUEL: And who are the authors?

MEI: Edward Prescott was at the Federal Reserve Bank of Minneapolis and the University of Minnesota. He got his PhD at Carnegie Mellon in 1967. In 2004 he won the Nobel prize with Finn Kydland, for their work on dynamic macroeconomics: why policy promises are hard to keep, and what drives business cycles. He died in November 2022, at 81.

MIGUEL: And Mehra?

MEI: Rajnish Mehra was at Columbia. He did his PhD at Carnegie Mellon too, finishing in 1978, and his advisor was Prescott himself. Fun detail: Finn Kydland was also one of Prescott's PhD students.

MIGUEL: So Prescott wrote his most famous finance paper with one student and won the Nobel with another. Great mentor, or great at recruiting co-authors.

MEI: Both, probably. Mehra and Prescott had already worked together on a 1980 Econometrica paper about recursive competitive equilibrium, which this paper cites. Mehra later spent decades at UC Santa Barbara and is now at Arizona State.

## The data

MIGUEL: Let's start with the numbers. Where do they come from?

MEI: Five series from 1889 to 1978. Four of them come from Grossman and Shiller, who shared their data, and the authors thank them in a footnote. There's the Standard and Poor's stock index, its dividends, per capita consumption of nondurables and services, and a price index to turn everything into real terms, meaning adjusted for inflation.

MIGUEL: And the safe asset?

MEI: A patchwork, because ninety-day Treasury bills didn't exist the whole time. They use Treasury bills from 1931, Treasury certificates in the 1920s, and short-term commercial paper before 1920.

MIGUEL: Commercial paper. Short-term loans to big companies, right?

MEI: Right. Close enough to riskless for this purpose. Now the headline numbers. The average real return on stocks was 6.98 percent a year. The average real return on the safe asset was 0.80 percent. So the equity premium, the extra return of stocks over safe debt, was 6.18 percent a year.

MIGUEL: Six percent, every year, for ninety years.

MEI: On average. And the paper has a lovely table that splits it by decade. The premium jumps around a lot. In 1949 to 1958, it was 18.3 percent a year. In the decade of the Great Depression, 1929 to 1938, it was almost zero, with a standard deviation above thirty percent.

MIGUEL: So in the Depression, stocks were a roller coaster that went nowhere.

MEI: And the safe asset had its own drama. In 1939 to 1948, with wartime inflation, the real return on safe debt was minus 5.8 percent a year. And in 1969 to 1978, the real return on stocks was basically zero, 0.03 percent.

MIGUEL: The seventies. Great music, terrible returns.

MEI: Nicely put. And one more number matters most: consumption. Per capita consumption grew 1.83 percent a year on average, with a standard deviation of 3.57 percent.

MIGUEL: So stocks are wild, and consumption is calm.

MEI: Keep that contrast in your head. It's the whole puzzle.

## The model

MIGUEL: Okay, so what model do they test?

MEI: A version of the Lucas tree. Robert Lucas, 1978, "Asset prices in an exchange economy." Lucas won the Nobel prize in 1995, so we start on solid ground.

MIGUEL: The Lucas tree. Explain it like I'm five.

MEI: Imagine an economy with one tree. Every year it drops fruit. The fruit can't be stored, so everyone eats it right away. The tree is the stock market: owning a share of it gives you a share of the fruit, which is the dividend. And since the fruit is all there is to eat, consumption equals dividends.

MIGUEL: So the stock pays exactly what the economy produces.

MEI: Exactly. Mehra and Prescott add a twist. In Lucas's model, the level of fruit follows a random process. But American consumption grew enormously between 1889 and 1978. So they make the growth rate random instead. Each year, the economy grows fast or slow, and which one you get depends on last year. The technical name is a two-state Markov chain.

MIGUEL: Markov chain. So tomorrow's state depends only on today's state, not on the whole history.

MEI: Right. A third number controls how sticky the states are: the probability of staying in the same state next year. If it's one half, each year is a fresh coin flip. Mehra and Prescott set it at 0.43, a bit below one half, so the economy tends to switch between fast and slow growth.

MIGUEL: Got it.

MEI: Now the people. There's one representative household, a stand-in for everybody. It has power utility, also called constant relative risk aversion, with two parameters. Alpha is the curvature of utility, which measures risk aversion. Beta is the subjective discount factor, which measures patience.

MIGUEL: Alpha for fear, beta for patience.

MEI: I'm stealing that. Then they price two assets. The equity share, which is a claim on the tree's fruit forever. And a one-period riskless bill, which pays one unit of fruit next year, no matter what.

MIGUEL: How do you price them, without reading equations to me?

MEI: The price of any asset is the expected value of its future payoffs, each one multiplied by a weight. The weight is the ratio of marginal utility in the future to marginal utility today, discounted by beta. Marginal utility is how much an extra unit of fruit is worth to you. When the economy does badly, fruit is scarce and precious, so those payoffs get a big weight.

MIGUEL: So the stock is risky because it pays little exactly when fruit is precious.

MEI: Yes. And one elegant detail: because of power utility, the stock price is always proportional to current consumption. That turns the whole pricing problem into two small linear equations, one per state. You could solve it by hand.

## Calibration: the rules of the game

MIGUEL: Now they have to pick numbers for the model.

MEI: In two steps, and this is the clever part. First the technology, meaning the consumption process. They pick three numbers so that the model's consumption growth matches the data: a mean of 1.8 percent, a standard deviation of 3.6 percent, and a serial correlation of minus 0.14.

MIGUEL: Serial correlation: how much this year's growth predicts next year's.

MEI: Right, and here it's slightly negative, so a good year is a bit more likely to be followed by a worse one. Step two: the preferences, alpha and beta. Here they don't estimate anything. They let alpha range from zero to ten, and beta from zero to one, and ask: is there any combination that matches both the average safe rate and the average premium?

MIGUEL: Why stop at ten?

MEI: Because they surveyed the evidence on risk aversion. Kenneth Arrow argued on theoretical grounds that it should be about one. Friend and Blume, looking at what people hold in their portfolios, found about two. Kydland and Prescott needed between one and two to match business cycles. A study of farmers found between one and two. Tobin and Dolde used 1.5 to fit life-cycle savings.

MIGUEL: So everybody's evidence says one or two, and they allow up to ten. That's generous.

MEI: Very generous. And they explain why there must be some cap: with a huge alpha, almost any pair of returns can be matched by tiny changes in the consumption process. A model that can match anything explains nothing.

MIGUEL: Fair. And this isn't estimation?

MEI: No, and they insist on it. They call it "a quantitative theoretical exercise designed to address a very particular question." Instead of asking "which parameters fit best," they ask "does any reasonable parameter fit at all."

MIGUEL: Like asking whether any key opens the door, instead of which key is shiniest.

MEI: Perfect.

## The result

MIGUEL: Okay, drumroll. Does any key open the door?

MEI: They map every combination of alpha and beta into a pair: the model's average safe rate and its average equity premium. That gives a region in a picture, figure four in the paper, which they call the admissible region. Then they look for the real-world point: a safe rate of 0.8 percent and a premium of about 6 percent.

MIGUEL: And?

MEI: The largest premium the model can produce, with a safe rate between zero and four percent, is 0.35 percent.

MIGUEL: Zero point three five. Against six.

MEI: The model misses by a factor of about seventeen. And notice how they reject it. Not with a p-value, not with a test statistic. They say the model's failure hinges on, quote, "its inability to generate average returns even close to those observed."

MIGUEL: So it's not "statistically rejected at five percent." It's "not even in the same building."

MEI: That's the style. And the intuition is simple. Consumption is too smooth. Stocks move with consumption, but consumption barely moves, so stocks don't look risky enough to deserve six percent. To get there, you need a crazy alpha.

## The other puzzle: the risk-free rate

MIGUEL: Can't we just accept a crazy alpha and move on?

MEI: Here's the beautiful twist, and it's in the conclusion. Raising alpha creates a second problem. The authors say the puzzle may not be why the equity return was so high, but why the risk-free rate was so low.

MIGUEL: Why would more risk aversion push the safe rate up?

MEI: Because in this model, alpha does two jobs. It measures fear of risk, and it also measures how much you want smooth consumption over time. Now think about a growing economy. Consumption grows about two percent a year, so you expect to be richer tomorrow. If you hate uneven consumption, you'd love to borrow from your richer future self and consume more today.

MIGUEL: Like borrowing from future me, who will definitely have his life together.

MEI: Exactly. But everybody wants to borrow, and nobody wants to lend. So the interest rate must rise until people are happy holding the bills. With alpha equal to two, the model's average safe rate is at least 3.7 percent. The data says 0.8, with a standard error of only 0.6.

MIGUEL: So turn alpha up, and you fix the premium but break the interest rate.

MEI: Turn it down, toward zero, and you wonder why anyone demands extra return on stocks at all. Either way, the model fails. In 1989, Philippe Weil gave this second problem its own name: the risk-free rate puzzle.

MIGUEL: Two puzzles for the price of one.

MEI: And they add a sneaky example of another asset with a "too low" return: cash. Treasury bills pay positive interest, yet people hold large amounts of currency, which pays nothing.

MIGUEL: My wallet is a monument to irrationality.

## Kicking the tires

MIGUEL: Okay, but maybe they just did something wrong. Did they check?

MEI: A lot. Here's the list. One: mismeasured inflation. If the price index is off, both the stock return and the safe return are off by the same amount, so the premium doesn't change.

MIGUEL: Clever. The error cancels.

MEI: They also think about taxes, since investors care about returns after tax. Tax rates were low in the early years, and in the later years the low safe rate and the big premium hold after tax for every income class.

MEI: Two: the time period. Maybe yearly data hides something. They let the model's period run from two years down to one hundred twenty-eighth of a year. The admissible region moves by hundredths of a percent.

MIGUEL: So it doesn't matter how often you look.

MEI: Three: the consumption process. They try average growth from 1.4 to 2.2 percent: no difference. They find the premium is roughly proportional to the variance of consumption growth, which is small. And they build a four-state version with more extreme moves, keeping the same mean and variance. The maximum premium goes from 0.35 to 0.39 percent.

MIGUEL: Wow. Big win. Point zero four.

MEI: And more persistence in growth rates makes the premium smaller, not bigger. So by assuming a stable, stationary world, they say they actually biased the test toward the model passing.

MIGUEL: So they gave the model every advantage, and it still lost.

MEI: Four: leverage. Real stocks are riskier than the whole economy, because firms pay wages and debt first, and shareholders get what's left. So they make the stock a claim on output after ninety percent of expected output is promised to others, since profits are about ten percent of output. The premium rises by less than a tenth of a percent.

MIGUEL: Why so little? That sounds like a big change.

MEI: Because in this economy, financial arrangements don't change what people consume. Slicing the same fruit differently doesn't change how scarce fruit is in bad times.

MIGUEL: And five?

MEI: Production. Adding investment and capital can't help, because it doesn't expand the set of consumption and price patterns the model can produce. They even admit they expected the simple model to pass, and had planned to add production afterwards.

MIGUEL: So they built a test they thought was easy, and it blew up in their faces.

MEI: That's what makes it a classic. And a fun footnote: Fischer Black, in a private communication, built an example in Merton's continuous-time model that matched the data. It needed a curvature parameter of 55.

MIGUEL: Fifty-five. That's not a person. That's a hamster in a bomb shelter inside another bomb shelter.

## Where the answer might be

MIGUEL: Do they say where the answer might be?

MEI: They speculate, and this is where it gets fun for us. Their main suspect is in the abstract: most likely, the right model "is not an Arrow-Debreu economy."

MIGUEL: Arrow-Debreu. That's the dream world where you can buy insurance against everything, right?

MEI: Right. An Arrow-Debreu economy has complete markets: for every possible future state of the world, there is a contract that pays in that state. People can trade away any risk and share it perfectly. That is why one representative household can stand in for everybody.

MIGUEL: So the problem might be the dream world itself.

MEI: That's their bet. First, they doubt that heterogeneity alone will fix it. They write: "We doubt whether heterogeneity, per se, of the agents will alter the conclusion." And they cite a 1982 paper by George Constantinides.

MIGUEL: Wait. Constantinides? As in Constantinides and Duffie, who solved it with heterogeneous consumers?

MEI: The same. Eleven years later, Constantinides and Duffie showed that heterogeneity can matter a lot, when income shocks are uninsurable and persistent.

MIGUEL: Plot twist. The author they cite to doubt heterogeneity later co-wrote the paper that rescued it.

MEI: But read the next sentences, because Mehra and Prescott point to the right road. They suggest that some trades between people may be impossible. In that case, individual consumption can vary a lot while aggregate consumption barely moves. They mention contracts that can't be enforced, and the fact that you can't sign contracts with generations not yet born.

MIGUEL: That's Mankiw's missing insurance markets!

MEI: Exactly. And the last line of the conclusion says that testing such theories would probably require consumption data by income or age groups.

MIGUEL: Which is exactly the household data Constantinides and Duffie asked for.

MEI: So in seventeen pages, they set the problem, and sketched where the answers would come from.

MIGUEL: And did the puzzle stay famous?

MEI: Very. The paper has thousands of citations, and it's one of the most cited papers in finance and macroeconomics. Mehra kept working on it for decades. His 2003 article "The Equity Premium: Why Is It a Puzzle?" won a Graham and Dodd award for financial writing, and in 2008 he edited a whole Handbook of the Equity Risk Premium.

MIGUEL: A whole handbook. The puzzle became a career.

## Wrap-up: the recap

MIGUEL: Okay, quick recap before we go. Give me the whole paper in one minute.

MEI: Deal. The question: can a standard model, with no frictions and reasonable risk aversion, explain why American stocks earned about six percent a year more than safe debt between 1889 and 1978?

MIGUEL: And the method?

MEI: A Lucas tree economy with one representative household and power utility. The growth rate of consumption follows a two-state Markov chain, calibrated to match the mean, volatility and serial correlation of US consumption growth. Then they search over all risk aversion values up to ten and all discount factors, to see if any combination matches the average safe rate and premium. It's a quantitative theoretical exercise, not an estimation.

MIGUEL: Main takeaways?

MEI: One: the model's largest premium is 0.35 percent, against 6.18 percent in the data. Two: raising risk aversion to fix the premium pushes the safe rate far too high, at least 3.7 percent with alpha of two against 0.8 in the data. So there are really two puzzles. Three: the result survives every check they throw at it: inflation errors, the time period, the consumption process, leverage, and production.

MIGUEL: And the conclusion?

MEI: Most likely, the model that explains the equity premium is not a frictionless Arrow-Debreu economy. Missing markets and contracts that can't be enforced are the suspects. That set the agenda for the next decade of research, from Mankiw in 1986 to Constantinides and Duffie in 1996.

MIGUEL: And my takeaway: six percent is a lot. If your model can only give me 0.35, check your model, not the data.

MEI: Thanks for listening to The Finance Papers Podcast.

MIGUEL: See you next time. And remember: six percent is not a rounding error.
