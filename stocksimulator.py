from taipy import Gui

import pandas as pd

data = {
    "Date": pd.date_range("2023-12-16", periods=4, freq="D"),
    "Min": [222,419.7,662.7,323.5],
    "Max": [28.6,68.2,666.,173.5]
}

title = "STOCK SIMULATOR BY RIESHU"
path = "image1.jpg"   
company_name = "Tata"
company_minp = 340
company_maxp = 740


def demo(state):
    print("Hey Rieshu this Side!")
    print(state.company_minp)

    with open("data.txt", "w") as f:
        f.write(f"{state.company_name},{state.company_minp},{state.company_maxp}")

page = """
<|text-center|
<|{path}|image|>

<|{title}|hover_text=WELCOME TO STOCK SCREENER|>

Name of Stock : <|{company_name}|input|>
Min price : <|{company_minp}|input|>
Max Price : <|{company_maxp}|input|>

<|Run Simulation|button|on_action=demo|>

<|{title}|hover_text=Your Simulation|>

<|{data}|chart|mode=lines|x=Date|y[1]=Min|y[2]=Max|line[1]=dash|color[2]=blue|>

>
"""

if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)


