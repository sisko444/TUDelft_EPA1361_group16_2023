# Imports used in visualization and calculation for visualization
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from ema_workbench.analysis import feature_scoring
from ema_workbench import Scenario

# Function to visuaize epsilon progress
def visualize_epsilon_progress(convergence, name):
    fig, ax1 = plt.subplots(ncols=1, sharex=True, figsize=(8, 4))
    ax1.plot(convergence.nfe, convergence.epsilon_progress)
    ax1.set_ylabel('$\epsilon$-progress')

    ax1.set_xlabel('number of function evaluations')
    ax1.set_title(name)
    plt.show()
    return plt

# Function to calculate all relevant outcomes
def calc_all_outcomes(df):
    df['total_expected_cost_them'] = df['A.1 Total Costs'] + \
                                     df['A.2 Total Costs'] + \
                                     df['A.3 Total Costs']

    df['total_expected_deaths_them'] = df['A.1_Expected Number of Deaths'] + \
                                       df['A.2_Expected Number of Deaths'] + \
                                       df['A.3_Expected Number of Deaths']

    df['total_expected_cost_us'] = df['A.4 Total Costs'] + \
                                   df['A.5 Total Costs']

    df['total_expected_deaths_us'] = df['A.4_Expected Number of Deaths'] + \
                                     df['A.5_Expected Number of Deaths']

    df['total_expected_cost'] = df['A.1 Total Costs'] + \
                                df['A.2 Total Costs'] + \
                                df['A.3 Total Costs'] + \
                                df['A.4 Total Costs'] + \
                                df['A.5 Total Costs']

    df['total_expected_deaths'] = df['A.1_Expected Number of Deaths'] + \
                                  df['A.2_Expected Number of Deaths'] + \
                                  df['A.3_Expected Number of Deaths'] + \
                                  df['A.4_Expected Number of Deaths'] + \
                                  df['A.5_Expected Number of Deaths']

    # df = df.drop(['EWS_DaysToThreat', 'RfR Total Costs', 'Unnamed: 0',
    #               'Expected Evacuation Costs']
    #              , axis=1)
    return df

# Function to construct the scenarios
def make_scenario(name, Bmax = 175, Brate = 1.5, pfails = [0.5, 0.5, 0.5, 0.5, 0.5], \
                  discount_rate = 3.5, ID_flood_wave_shape = 4):

    dic = {'discount rate 0': discount_rate, 'A.0_ID flood wave shape': ID_flood_wave_shape,
     'A.1_Bmax': Bmax, 'A.1_pfail': pfails[0], 'A.1_Brate': Brate, 'A.2_Bmax': Bmax, 'A.2_pfail': pfails[1],
     'A.2_Brate': Brate, 'A.3_Bmax': Bmax, 'A.3_pfail': pfails[2], 'A.3_Brate': Brate, 'A.4_Bmax': Bmax,
    'A.4_pfail': pfails[3], 'A.4_Brate': Brate, 'A.5_Bmax': Bmax, 'A.5_pfail': pfails[4],
     'A.5_Brate': Brate}
    #setting so that the reference scenario
    return Scenario(name, **dic)

# Function to calculate outcomes in a province versus province view without totals
def outcomes_to_df_them_vs_us_only(outcomes):
    df = pd.DataFrame(outcomes)

    df['total_expected_cost_them'] = df['A.1 Total Costs'] + \
                                df['A.2 Total Costs'] + \
                                df['A.3 Total Costs']

    df['total_expected_deaths_them'] = df['A.1_Expected Number of Deaths'] + \
                                  df['A.2_Expected Number of Deaths'] + \
                                  df['A.3_Expected Number of Deaths']

    df['total_expected_cost_us'] = df['A.4 Total Costs'] + \
                                df['A.5 Total Costs']

    df['total_expected_deaths_us'] = df['A.4_Expected Number of Deaths'] + \
                                  df['A.5_Expected Number of Deaths']

    df = df.drop(['A.1 Total Costs', 'A.2 Total Costs', 'A.3 Total Costs',
             'A.4 Total Costs', 'A.5 Total Costs', 'A.1_Expected Number of Deaths',
             'A.2_Expected Number of Deaths', 'A.3_Expected Number of Deaths',
             'A.4_Expected Number of Deaths', 'A.5_Expected Number of Deaths',
            'RfR Total Costs', 'Expected Evacuation Costs'], axis=1)
    return df

# Function to calculate agregate cost and deaths from province to province
def outcomes_to_df_them_vs_us(outcomes):
    df = pd.DataFrame(outcomes)

    df['total_expected_cost_them'] = df['A.1 Total Costs'] + \
                                df['A.2 Total Costs'] + \
                                df['A.3 Total Costs']

    df['total_expected_deaths_them'] = df['A.1_Expected Number of Deaths'] + \
                                  df['A.2_Expected Number of Deaths'] + \
                                  df['A.3_Expected Number of Deaths']

    df['total_expected_cost_us'] = df['A.4 Total Costs'] + \
                                df['A.5 Total Costs']

    df['total_expected_deaths_us'] = df['A.4_Expected Number of Deaths'] + \
                                  df['A.5_Expected Number of Deaths']

    df['total_expected_cost'] = df['A.1 Total Costs'] + \
                                df['A.2 Total Costs'] + \
                                df['A.3 Total Costs'] + \
                                df['A.4 Total Costs'] + \
                                df['A.5 Total Costs']

    df['total_expected_deaths'] = df['A.1_Expected Number of Deaths'] + \
                                  df['A.2_Expected Number of Deaths'] + \
                                  df['A.3_Expected Number of Deaths'] + \
                                  df['A.4_Expected Number of Deaths'] + \
                                  df['A.5_Expected Number of Deaths']

    df = df.drop(['A.1 Total Costs', 'A.2 Total Costs', 'A.3 Total Costs',
             'A.4 Total Costs', 'A.5 Total Costs', 'A.1_Expected Number of Deaths',
             'A.2_Expected Number of Deaths', 'A.3_Expected Number of Deaths',
             'A.4_Expected Number of Deaths', 'A.5_Expected Number of Deaths',
            'RfR Total Costs', 'Expected Evacuation Costs'], axis=1)
    return df

# Function to visualize the sensitivity of uncertainties on results in a heatmap
def visualize_featurescoring_heatmap(experiments, model, results):
    cleaned_experiments = experiments.drop(columns=[l.name for l in model.levers])

    for policy in experiments.policy.unique():
        logical = experiments.policy == policy
        subset_results = {k: v[logical] for k, v in results.items()}
        scores = feature_scoring.get_feature_scores_all(cleaned_experiments[logical],
                                                        subset_results)
        sns.heatmap(scores, annot=True, cmap='viridis')
        plt.show()

def outcomes_to_df(outcomes):
    df = pd.DataFrame(outcomes)

    df['total_expected_cost'] = df['A.1 Total Costs'] + \
                                df['A.2 Total Costs'] + \
                                df['A.3 Total Costs'] + \
                                df['A.4 Total Costs'] + \
                                df['A.5 Total Costs']

    df['total_expected_deaths'] = df['A.1_Expected Number of Deaths'] + \
                                  df['A.2_Expected Number of Deaths'] + \
                                  df['A.3_Expected Number of Deaths'] + \
                                  df['A.4_Expected Number of Deaths'] + \
                                  df['A.5_Expected Number of Deaths']
    return df

# Function to visualize the sensitivity of uncertainties for results in a bar plot
def visualize_bar_plot(Si, problem):
    Si_filter = {k: Si[k] for k in ['ST', 'ST_conf', 'S1', 'S1_conf']}
    Si_df = pd.DataFrame(Si_filter, index=problem['names'])

    sns.set_style('white')
    fig, ax = plt.subplots(1)

    indices = Si_df[['S1', 'ST']]
    err = Si_df[['S1_conf', 'ST_conf']]

    indices.plot.bar(yerr=err.values.T, ax=ax)
    fig.set_size_inches(8, 6)
    fig.subplots_adjust(bottom=0.3)
    plt.show()

# Function to visualize scenario and policy exploration results
def visualize_scatter(df, x, y):
    x_label = x
    x = df[x]
    y_label = y
    y = df[y]
    # Start with a square Figure.
    fig = plt.figure(figsize=(6, 6))
    # Add a gridspec with two rows and two columns and a ratio of 1 to 4 between
    # the size of the marginal axes and the main axes in both directions.
    # Also adjust the subplot parameters for a square plot.
    gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4),
                          left=0.1, right=0.9, bottom=0.1, top=0.9,
                          wspace=0.05, hspace=0.05)
    # Create the Axes.
    ax = fig.add_subplot(gs[1, 0])
    ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
    ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax / binwidth) + 1) * binwidth

    bins = 10
    ax.set(xlabel=x_label, ylabel=y_label)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')

