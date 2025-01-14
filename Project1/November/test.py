import pandas as pd
file1_path = './ee.xlsx'
file2_path = './ee2.xlsx'
data1 = pd.read_excel(file1_path, sheet_name='Sheet1')
data2 = pd.read_excel(file2_path, sheet_name='Sheet1')
data1.rename(columns={"Reg. No.": "Reg.No"}, inplace=True)
data1_filtered = data1[data1['Reg.No'].str.len() == 10]
data2_filtered = data2[data2['Reg.No'].str.len() == 10]
intersection_data = pd.merge(data1_filtered, data2_filtered, on="Reg.No")
columns_to_drop = ["S. No._y","Name","Superset ID", "Interview Status"]
intersection_data = intersection_data.drop(columns=[col for col in columns_to_drop if col in intersection_data.columns])

print("\nIntersection of both files based on 'Reg.No' with 10 characters:")
print(intersection_data)

output_file = '/Users/arvindgarg/Downloads/tcs_result.xlsx'
intersection_data.to_excel(output_file, index=False)

print(f"\nUnion data saved successfully to {output_file}.")