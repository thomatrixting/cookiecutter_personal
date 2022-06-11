import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def covid_time_series(df: pd.DataFrame):
    sns.lineplot(
    data=df,
    x="date",
    y="value",
    hue="country_region"
    )
    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");
# we make a function were is a product that we want to present 

def top_countries_df_gen(df:pd.DataFrame,countries_for_hue:list, number_top = 20):
    top_countries_df = (
    df #process covid df
    .select_columns(["country_region", "value"])
    .groupby(["country_region"])
    .aggregate("sum")
    .sort_values("value", ascending=False)
    .reset_index()
    .head(number_top)
    .transform_column(
        column_name="country_region",
        function=lambda x: "red" if x in countries_for_hue else "lightblue",
        dest_column_name="color"
        )
    )

    return top_countries_df

def genertate_bar_plot_top_countries(*args,**kargs):
    top_countries_df = top_countries_df_gen(*args,**kargs)
    
    sns.barplot(
    data=top_countries_df,
    x="value",
    y="country_region",
    palette=top_countries_df.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");
