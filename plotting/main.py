import numpy as np
import matplotlib.pylab as plt
from matplotlib.pyplot import figure as fig
import pandas as pd
import seaborn as sns
import openpyxl

# Set graph save path
from matplotlib.ticker import MaxNLocator

save_path = r'C:\Users\Emil Riis Hansen\Dropbox\Apps\Overleaf\Node Initialization HeDAI\figures'

# Read Data
sheet_names = [f'L{x} With' for x in range(1, 6)] + [f'L{x} Without' for x in range(1, 6)] + [f'L{x} Graphlet' for x in range(1, 6)]
df = pd.read_excel(io='data/results.xlsx', sheet_name=sheet_names)

# Get L1 data
l1_with = df['L1 With']['test-Micro_f1'].values
l1_without = df['L1 Without']['test-Micro_f1'].values
l1_graphlet = df['L1 Graphlet']['test-Micro_f1'].values

# Get L2 data
l2_with = df['L2 With']['test-Micro_f1'].values
l2_without = df['L2 Without']['test-Micro_f1'].values
l2_graphlet = df['L2 Graphlet']['test-Micro_f1'].values

# Get L3 data
l3_with = df['L3 With']['test-Micro_f1'].values
l3_without = df['L3 Without']['test-Micro_f1'].values
l3_graphlet = df['L3 Graphlet']['test-Micro_f1'].values

# Get L4 data
l4_with = df['L4 With']['test-Micro_f1'].values
l4_without = df['L4 Without']['test-Micro_f1'].values
l4_graphlet = df['L4 Graphlet']['test-Micro_f1'].values

# Get L5 data
l5_with = df['L5 With']['test-Micro_f1'].values
l5_without = df['L5 Without']['test-Micro_f1'].values
l5_graphlet = df['L5 Graphlet']['test-Micro_f1'].values

l1_data = [l1_graphlet, l1_without, l1_with]
l2_data = [l2_graphlet, l2_without, l2_with]
l3_data = [l3_graphlet, l3_without, l3_with]
l4_data = [l4_graphlet, l4_without, l4_with]
l5_data = [l5_graphlet, l5_without, l5_with]
all_data = [l1_data, l2_data, l3_data, l4_data, l5_data]
labels = ['Graphlet', 'Rand', 'FeatInit']

figure, axes = plt.subplots(1, 5, figsize=(10, 5))

hatches = ['//', '\\\\', 'o']
for i, data in enumerate(all_data):
    df = pd.DataFrame(data={labels[0]: data[0], labels[1]: data[1], labels[2]: data[2]})
    box = sns.boxplot(data=df, ax=axes[i], showfliers=False, palette="Set2")
    for hatch, patch in zip(hatches, box.patches):
        patch.set_hatch(hatch)


# set the spacing between subplots
plt.subplots_adjust(left=0.1,
                    right=0.9,
                    wspace=0.4,
                    hspace=0.4,
                    bottom=0.2)

for i, ax in enumerate(axes, 1):
    ax.tick_params(labelrotation=45)
    ax.set_title(f'L{i}', size=16)
    ax.tick_params(axis='both', which='major', labelsize=13)
    ax.set_ylim(ymin=24, ymax=78)

axes[0].set_ylabel('F1 Score', fontsize=16)  # Y label


plt.savefig(f'{save_path}/boxplot.pdf')
plt.show()
