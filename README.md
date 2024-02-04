# Long Term Stock Prediction
This in an experiment to see how accurate long term Predictions can get from an NN which gets basic information about stock charts.

## Plans
Currently the NN gets information about the chart of one stock.
The last x data points are fed as context and it must predict the next x data points.
This results in a long term prediction, instead of just the next day, hour or minute.

The plans are bigger though. I want this NN to get the context frame of many stocks at the same time,
so it can have a meaningful understanding of the market.

## Examples
I've accidentally deleted the entire README.md that I wrote a few minutes ago, so I'm going to keep this short :(
Also these results are not cherrypicked, I'm not going through that hassle for some github folks.

#### AAPL Prediction
Blue is Context, Green is Actual, Red is Predicted.
It got 1000 days context and has to predict the next 100 days.
The NN was trained on AAPL so its no wonder it actually performs quite reasonable.
One noteable thing: It has never seen this partion of the data, because of the Train-Test-Split.

![image](https://github.com/FelixCodesTech/Long-Term-Stock-Prediction/assets/66774630/c46568cd-2135-4b9c-8c98-708c40a763e4)

#### GOOG Prediction
Same setup as above, except for the fact that this still is the AAPL Trained model and has never seen any Google charts.
The NN can definitely get the direction the stock is heading, but details etc. are not really there.

![image](https://github.com/FelixCodesTech/Long-Term-Stock-Prediction/assets/66774630/7a7ab119-04b7-4b5b-8857-ea1fe6f6f46f)

#### MSFT
Same setup as above.
Here you can see that the outcome is a bit misleading on this chart.
The actual end result is about a 40% gain, while the NN predicted about 25%.
This would have been a great deal, but if you imagine this going the other way around,
something like an end result of -40%, whilt the NN predicts +25%, that would be a big loss.

![image](https://github.com/FelixCodesTech/Long-Term-Stock-Prediction/assets/66774630/3244eb66-f161-4bdd-a7ce-6a6f54e6a685)

## Statistics
#### Chart V2
This is a chart showing how good the NN performs on certain combinations of Context and Solution Window.
Red (1.0) is really bad, while Blue (0.0) is "good" (compared to the other really terrible predictions. Probably as good as the examples above.)
You can see that the smaller the Ratio SolutionWindow/ContextWindow becomes, the better (more blue) the point gets.
This chart contains way less points gives therefor a better overview.

![image](https://github.com/FelixCodesTech/Long-Term-Stock-Prediction/assets/66774630/887e5dc8-ea88-4ae2-8606-d995aa8b2b34)

#### Chart V1
Why is this only until 300 Context Window? Because I haven't run the statistics notebook for long enough yet.

![image](https://github.com/FelixCodesTech/Long-Term-Stock-Prediction/assets/66774630/a7402382-75e0-4a58-ad25-2162a2a2ee61)
