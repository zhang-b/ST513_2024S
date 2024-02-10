import pandas as pd

filename = r'WorldDevelopmentIndicators.xlsx'

data = pd.read_excel(filename, sheet_name='Data').pivot(
    index=['Country Name', 'Country Code', 'Year'],
    columns=['Indicator Name', 'Indicator Code'],
    values='Value'
).sort_index(axis='index').sort_index(axis='columns')
data.columns.to_frame().to_excel('WorldDevelopmentIndicators_indicator.xlsx', sheet_name='indicator')
data.droplevel(axis='columns', level=0).reset_index().to_excel(
    'worldDevelopmentIndicators_pivot.xlsx', sheet_name='pivot', index=False,
)
