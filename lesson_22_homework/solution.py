import pandas as pd
from pandas import DataFrame


def show_missing_results(df):
    scores = df['score']
    na_scores = scores.isna()
    print(na_scores)
    print(df[na_scores])


def score_between(df):
    a, b = float(input('a')), float(input('b'))
    scores_in_between = df['score'].between(a, b)
    print(df[scores_in_between])


def sorted_by_scores_and_name(df):
    sorted_by_name = df.sort_values('name')
    sorted_by_scores = df.sort_values('score', ascending=False)
    print(sorted_by_name)
    print(sorted_by_scores)
    sorted_by_scores.to_excel('scores_sorted.xlsx')


def add_new_recods(df: DataFrame):
    name = input('Name')
    score = float(input('Score'))
    attempts = int(input('Attemps'))
    quali = input('Qualified')
    row = dict(
        name=name,
        score=score,
        attempts=attempts,
        qualify=quali
    )
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    print(df)


def remove_by_id(original_df):
    print(original_df.to_string())
    index = int(input('Index to remove: '))
    removed_df = original_df.drop(index)
    print(removed_df.to_string())
    return removed_df


def save_qualified(original_df):
    qualified = original_df[original_df['qualify'] == 'yes']
    names_and_scores_only = qualified[['name', 'score']]
    names_and_scores_only.to_excel('qualified_studs.xlsx')


if __name__ == '__main__':
    data_frame = pd.read_excel('homework.xlsx')
    # print(data_frame)
    # show_missing_results(data_frame)
    # sorted_by_scores_and_name(data_frame)
    # score_between(data_frame)
    # add_new_recods(data_frame)
    # remove_by_id(data_frame)
    save_qualified(data_frame)
