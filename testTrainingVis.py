import re
from matplotlib import pyplot as plt

stringData = """Iteration 1, loss = 0.00404616
Validation score: -23.911000
Iteration 2, loss = 0.00332035
Validation score: -19.486160
Iteration 3, loss = 0.00264434
Validation score: -15.037179
Iteration 4, loss = 0.00197704
Validation score: -10.786674
Iteration 5, loss = 0.00139033
Validation score: -7.328613
Iteration 6, loss = 0.00096236
Validation score: -5.031758
Iteration 7, loss = 0.00070156
Validation score: -3.761234
Iteration 8, loss = 0.00055784
Validation score: -3.133629
Iteration 9, loss = 0.00047693
Validation score: -2.819465
Iteration 10, loss = 0.00042630
Validation score: -2.635524
Iteration 11, loss = 0.00039003
Validation score: -2.519268
Iteration 12, loss = 0.00036179
Validation score: -2.430000
Iteration 13, loss = 0.00033873
Validation score: -2.354532
Iteration 14, loss = 0.00031967
Validation score: -2.290541
Iteration 15, loss = 0.00030344
Validation score: -2.238099
Iteration 16, loss = 0.00028953
Validation score: -2.182786
Iteration 17, loss = 0.00027753
Validation score: -2.136609
Iteration 18, loss = 0.00026698
Validation score: -2.091803
Iteration 19, loss = 0.00025780
Validation score: -2.049750
Iteration 20, loss = 0.00024956
Validation score: -2.008545
Iteration 21, loss = 0.00024230
Validation score: -1.974337
Iteration 22, loss = 0.00023577
Validation score: -1.938528
Iteration 23, loss = 0.00022991
Validation score: -1.906918
Iteration 24, loss = 0.00022461
Validation score: -1.876872
Iteration 25, loss = 0.00021980
Validation score: -1.848587
Iteration 26, loss = 0.00021540
Validation score: -1.821129
Iteration 27, loss = 0.00021138
Validation score: -1.795574
Iteration 28, loss = 0.00020770
Validation score: -1.773685
Iteration 29, loss = 0.00020428
Validation score: -1.750706
Iteration 30, loss = 0.00020113
Validation score: -1.730777
Iteration 31, loss = 0.00019820
Validation score: -1.710274
Iteration 32, loss = 0.00019549
Validation score: -1.692867
Iteration 33, loss = 0.00019297
Validation score: -1.674981
Iteration 34, loss = 0.00019061
Validation score: -1.658233
Iteration 35, loss = 0.00018841
Validation score: -1.643150
Iteration 36, loss = 0.00018634
Validation score: -1.628576
Iteration 37, loss = 0.00018438
Validation score: -1.614361
Iteration 38, loss = 0.00018257
Validation score: -1.601631
Iteration 39, loss = 0.00018084
Validation score: -1.589760
Iteration 40, loss = 0.00017922
Validation score: -1.578332
Iteration 41, loss = 0.00017768
Validation score: -1.567178
Iteration 42, loss = 0.00017623
Validation score: -1.557311
Iteration 43, loss = 0.00017487
Validation score: -1.548077
Iteration 44, loss = 0.00017357
Validation score: -1.538491
Iteration 45, loss = 0.00017233
Validation score: -1.529337
Iteration 46, loss = 0.00017115
Validation score: -1.521909
Iteration 47, loss = 0.00017004
Validation score: -1.514312
Iteration 48, loss = 0.00016898
Validation score: -1.507955
Iteration 49, loss = 0.00016796
Validation score: -1.501114
Iteration 50, loss = 0.00016701
Validation score: -1.495030
Iteration 51, loss = 0.00016608
Validation score: -1.488674
Iteration 52, loss = 0.00016521
Validation score: -1.482605
Iteration 53, loss = 0.00016436
Validation score: -1.477484
Iteration 54, loss = 0.00016355
Validation score: -1.473116
Iteration 55, loss = 0.00016279
Validation score: -1.468651
Iteration 56, loss = 0.00016204
Validation score: -1.464291
Iteration 57, loss = 0.00016133
Validation score: -1.460456
Iteration 58, loss = 0.00016066
Validation score: -1.457159
Iteration 59, loss = 0.00016000
Validation score: -1.453468
Iteration 60, loss = 0.00015937
Validation score: -1.449429
Iteration 61, loss = 0.00015877
Validation score: -1.446639
Iteration 62, loss = 0.00015819
Validation score: -1.444827
Iteration 63, loss = 0.00015763
Validation score: -1.441833
Iteration 64, loss = 0.00015710
Validation score: -1.439110
Iteration 65, loss = 0.00015658
Validation score: -1.437578
Iteration 66, loss = 0.00015607
Validation score: -1.435292
Iteration 67, loss = 0.00015559
Validation score: -1.433866
Iteration 68, loss = 0.00015512
Validation score: -1.431735
Iteration 69, loss = 0.00015467
Validation score: -1.430183
Iteration 70, loss = 0.00015423
Validation score: -1.428683
Iteration 71, loss = 0.00015381
Validation score: -1.427718
Iteration 72, loss = 0.00015340
Validation score: -1.425752
Iteration 73, loss = 0.00015300
Validation score: -1.425067
Iteration 74, loss = 0.00015262
Validation score: -1.424393
Iteration 75, loss = 0.00015224
Validation score: -1.423864
Iteration 76, loss = 0.00015189
Validation score: -1.422895
Iteration 77, loss = 0.00015154
Validation score: -1.422292
Iteration 78, loss = 0.00015121
Validation score: -1.422146
Iteration 79, loss = 0.00015087
Validation score: -1.421498
Iteration 80, loss = 0.00015055
Validation score: -1.421213
Iteration 81, loss = 0.00015023
Validation score: -1.420927
Iteration 82, loss = 0.00014994
Validation score: -1.420709
Iteration 83, loss = 0.00014965
Validation score: -1.421164
Iteration 84, loss = 0.00014935
Validation score: -1.420696
Iteration 85, loss = 0.00014908
Validation score: -1.421018
Iteration 86, loss = 0.00014881
Validation score: -1.420743
Iteration 87, loss = 0.00014855
Validation score: -1.420968
Iteration 88, loss = 0.00014829
Validation score: -1.421532
Iteration 89, loss = 0.00014804
Validation score: -1.421700
Iteration 90, loss = 0.00014780
Validation score: -1.421972
Iteration 91, loss = 0.00014757
Validation score: -1.422324
Iteration 92, loss = 0.00014734
Validation score: -1.423009
Iteration 93, loss = 0.00014712
Validation score: -1.423075"""




# Initialize lists
loss_values = []
validation_scores = []

# Find all loss values and validation scores
loss_values_str = re.findall(r'loss = (\d+\.\d+)', stringData)
validation_scores_str = re.findall(r'Validation score: (-?\d+\.\d+)', stringData)

# Convert strings to floats and append to lists
loss_values = [float(value) for value in loss_values_str]
validation_scores = [float(score) for score in validation_scores_str]


# plot the data
plt.plot(loss_values, label='loss')
plt.plot(validation_scores, label='validation score')
plt.legend()
plt.show()