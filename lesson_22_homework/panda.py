import pandas as pd

def missing(df):
    print()
    print("Rows where the score is missing")
    print(df[df['score'].isnull()])
    
def between(df):
    print()
    print("Rows the score is between a and b")
    a = float(input("Enter lower bound: "))
    b = float(input("Enter upper bound: "))
    print(df[(df['score'] >= a) & (df['score'] <= b)])

def byscore(df):
    print()
    print("Rows sorted by score")
    print(df.sort_values(by='score',ascending=False))

def byname(df):
    print()
    print("Rows sorted by name")
    print(df.sort_values(by='name'))

def newelement(df):
    print()
    print("Add new element (result) to the dataframe")
    
    new_result = {'name'    : input("Enter student name: "), 
                  'score'   : float(input("Enter score: ")), 
                  'attempts': int(input("Enter number of attempts: ")), 
                  'qualify' : input("Did they qualify (yes/no)? ")}
    new_result = pd.DataFrame([new_result])
    df = pd.concat([df, new_result], ignore_index=True)
    df.to_excel('homework.xlsx', index=False)

def remres(df):    
    print()
    print("Remove results from the dataframe")
    index = int(input("Enter index of result to remove: "))
    df = df.drop(index)
    df.to_excel('homework.xlsx', index=False)

def qualified(df):    
    print()
    print("Save a list of all students that qualified to qualified_students.xlsx")
    qualified_students = df[df['qualify'] == 'yes']
    qualified_students.to_excel('qualified_students.xlsx', index=False, columns=['name', 'score'])
    
    print()

if __name__ == '__main__':
    df = pd.read_excel('homework.xlsx')
    #missing(df)
    #between(df)
    #byscore(df)
    #byname(df)
    newelement(df)
    #remres(df)
    #qualified(df)
    